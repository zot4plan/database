from request_websites import request_websites
from json import load, dump
from collections import defaultdict

f = open('../../other/courseIDs.json')   
Data = {elem for elem in load(f)}
f.close()

def get_uci_samples():
    """
    get_uci_samples searches for schedule tables of each
    major requirement and call create_tables to collect information
    """
    open_urls = open('../../store/program_urls.json')
    all_urls = load(open_urls)

    for major, website in all_urls.items():
        soup = request_websites(website)
        tables = soup.find_all('table', class_='sc_plangrid')
        if tables:
            print(major)
            all_schedules = []
            for table in tables:
                schedule = create_tables(table)
                get_schedule_header_info(schedule, major, table)
                all_schedules.append(schedule)
            write_sample(major, all_schedules)


def create_tables(table):
    """
    create_tables takes in a sample schedule and stores it in a dictionary 
    :param table: UCI table schedule stored in BeautifulSoup object
    :return: a dictionary schedule with format -> {year:{Fall: [], Winter: [], Spring: []}} 
    """
    quarters = ['Fall', 'Winter', 'Spring']
    
    schedule = defaultdict(lambda:defaultdict(list))

    year = ''
    for elem in table.find_all('tr'):
        tag_class = elem.get('class')
        if tag_class and 'plangridyear' in tag_class:
            year = elem.find('th').text
            continue
        elif not tag_class:
            row = extract_courses(elem.find_all('td'))
            for x in range(len(row)):
                if row[x] != ' ':
                    schedule[year][quarters[x]].append(row[x])
    
    return schedule


def extract_courses(row):
    """
    extract_courses takes in a row of information and store them
    according to its type: course object and text
    :param row: BeautifulSoup object that contains a row of schedule
    :return: a list of organized course information
    """
    courses = []

    for line in row:
        clean_string = ''
        for course in line:
            if course.name and course.name == 'a':
                clean_string += course['title'].replace('\xa0', ' ')
            else:
                clean_string += course.text.replace('\xa0', ' ')
        courses.append(clean_string)
    return courses


def get_schedule_header_info(schedule, major, table):
    """
    get_schedule_header_info searches previous tags 
    for schedule's header or any provided notes
    :param schedule: cleaned schedule (dictionary)
    :param major: a string that denotes the major name of the schedule
    :param table: raw table collected from UCI website
    """
    previous = table.find_previous_sibling()

    if previous and previous.name in ['h4', 'h5', 'h6']:
        schedule['title'] = previous.text
    elif previous and previous.name == 'p':
        find_title = previous.find_previous_sibling()
        if find_title.name in ['h4', 'h5', 'h6']:
            schedule['title'] = find_title.text
        else:
            schedule['title'] = major
        schedule['text'] = previous.text
    else:
        schedule['title'] = major


def write_sample(major, tables):
    """
    write_sample writes out the cleaned schedule in a json file
    :param major: string contains the major's name
    :param tables: a list of sample schedules of the provided major
    """
    if "Criminology" in major:
        major = major.replace(' ', '_').replace('/', '-')
    else:
        major = major.replace(' ', '_').replace('/', '-').replace(',', '')
    if "Minor" in major:
        major += '.'

    with open('../../samples/' + major + 'json', 'w') as f:
        dump(tables, f, indent=4)


if __name__ == "__main__":
    get_uci_samples()
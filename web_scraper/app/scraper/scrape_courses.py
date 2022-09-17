import requests

from scraper.request_websites import request_websites, get_courses_websites
from models.Course import Course
import json

TERMS = {}

def get_terms() -> None:
    """
    send an API request to PeterPortal API and retrieve all information
    regarding UCI courses and save past terms that offered the course
    """
    
    try:
        response = requests.get("https://api.peterportal.org/rest/v0/courses/all")
        all_info = response.json()

        for course in all_info:
            TERMS[course['id']] = course['terms']
            
    except:
        print("Failed to attain API Request")


def get_courses(url: str) -> dict:
    """
    scrape all courses provided in the url
    (course id, course name, units, description, restriction, and prereq).
    """

    course_dict = {}
    soup = request_websites(url)
    for elem in soup.find_all('div', class_='courseblock'):
        header = elem.find('p', class_='courseblocktitle')
        section = elem.find('div', class_='courseblockdesc')
        get_info = section.find_all('p')
        course = Course()
        course.set_header_info(header.text)

        for x in range(len(get_info)):
            info = get_info[x].text
            ge = get_info[x].find('strong')

            if x == 0:
                course.set_description(info)
            elif 'Repeatability:' in info and 'Restriction:' not in info:
                course.set_repeatability(info)
            else:
                course.set_information(info)
                
            if ge:
                course.set_ge(ge.text)

            course.set_terms(TERMS[course.course_id.replace(' ', '')])

        course_dict[course.course_id] = course
    return course_dict


def save_courses() -> None:
    """
    write_courses calls get_courses_websites to collect all current UCI courses from UCI General Catalogue.
    Using those collected websites, get_courses will be called to scrape all of the courses offered at UCI by departments.
    """

    websites = get_courses_websites()
    course_names = []
    courses = {}

    for each_url in websites:
        uci_course = get_courses(each_url)
        for key, value in uci_course.items():
            print(key)
            course_names.append(key)
            courses[key] = value.__dict__

    with open('../../store/course_ids.json', 'w') as f: 
        json.dump(course_names, f, indent=4)

    with open('../../store/courses.json', 'w') as f:
        json.dump(courses, f, indent=4)


def scrape_courses():
    get_terms()
    save_courses()

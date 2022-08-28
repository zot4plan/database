from Course import Course
import json 
from pathlib import Path
import sys
from scrape_courses import write_course_helper

NAME_REQ_OUT = '../data/programs.sql'
REQ_TYPES = ['Minor', 'B.S.', 'B.A.', 'B.F.A.']
NO_COURSE_WARNING = "Course information cannot be found. This course may no longer be offered. If you believe there is an error or require more information, please contact the course department."

def get_paths():
    """
    get paths attains all of the path addresses of files that store information of 
    major/minor requirements
    """

    all_paths = {}
    path_name = Path(sys.argv[1])
    for addie in path_name.iterdir():
        find_name = ''
        addie_string = str(addie)
        if "Minor" in addie_string:
            find_name = addie_string.split('/')[-1].replace('.json', '').split('_')
        else:
            find_name = addie_string.split('/')[-1].replace('json', '').split('_')
        name = " ".join(find_name[:-1]) + ", " + find_name[-1]
        if find_name[-1] in REQ_TYPES:
            all_paths[name] = addie
    return all_paths


def check_course_exist(course_id):
    """
    check_course_exist determines if a course is in the database based on course ID. If not, it will create a new Course
    object for that course ID with a warning message as description.
    """

    all_courses = []
    with open('../other/courseIDs.json', "r") as course_file:
        all_courses = [elem for elem in json.load(course_file)]
    
    if course_id in all_courses:
        course_file.close()
        return
    
    new_course = Course()
    new_course.course_key, new_course.description = course_id, NO_COURSE_WARNING
    
    f = open("../data/courses.sql", "a")
    f.write(write_course_helper(course_id, new_course))
    f.close()

    all_courses.append(course_id)
    with open('../other/courseIDs.json', "w") as course_file:
        json.dump(all_courses, course_file, indent=4)


def write_required_depts(info):
    """
    write_required_depts collects all unique departmental courses of a 
    particular major and return the information in a list
    """
    all_depts = set()
    for header in info:
        for section in header['child']:
            for course in section['child']:    
                if type(course) == str:
                    check_course_exist(course)
                    all_depts.add(get_dept(course))
                else:
                    for elem in course:
                        check_course_exist(elem)
                        all_depts.add(get_dept(elem))
    
    return list(all_depts)


def get_dept(course):
    """
    get_dept takes in course id as a parameter and extract the course id number and
    return the department name
    """
    for x in range(len(course)-1, -1, -1):
        if course[x] != ' ':
            continue 
        else:
            return course[:x]


def write_requirements(file_names, out_file):
    """
    write requirements access the information of major/minor requirements of
    given file paths and write them into a given outfile.
    """
    
    open_urls = open('../other/program_Urls.json')
    all_urls = json.load(open_urls)
    write_majors = open(out_file, 'w')
    sorted_files = sorted(file_names)

    for name in sorted_files: 
        with open(file_names[name], 'r') as f:
            all_info = json.load(f)
            requirement = str(all_info).replace("'", '"')
            is_major = 1 
            if "Minor" in name:
                is_major = 0
            all_depts = write_required_depts(all_info)
            write_majors.write("INSERT INTO programs (name, is_major, requirement, departments, url) VALUES (" + 
                                "'" + name + "', " 
                                + "'" + str(is_major) + "', " 
                                + "'" + requirement + "', " 
                                + "ARRAY " + str(all_depts) + "::text[], '" 
                                + all_urls[name.replace('-', '/')] + '#requirementstext' + "');" + "\n")

    open_urls.close()
    write_majors.close()

if __name__ == "__main__":
    
    file_paths = get_paths()
    write_requirements(file_paths, NAME_REQ_OUT)
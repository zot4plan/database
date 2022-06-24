from gzip import READ
import json 
from pathlib import Path
import sys

NAME_REQ_OUT = '../database/requirements.sql'
REQ_TYPES = ['Minor', 'B.S.', 'B.A.', 'B.F.A.']

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


def write_required_courses(info, index):
    
    out_file = open("../database/courses_in_programs.sql", "a")
    for header in info:
        for section in header['child']:
            for course in section['child']:    
                if type(course) == str:
                    out_file.write("INSERT INTO courses_in_programs (courseId, programId) VALUES (" +
                                    "'" + course + "', " + "'" + str(index) + "');" + "\n")
                else:
                    for elem in course:
                        out_file.write("INSERT INTO courses_in_programs (courseId, programId) VALUES (" +
                                    "'" + elem + "', " + "'" + str(index) + "');" + "\n")
    out_file.close

def write_requirements(file_names, out_file):
    """
    write requirements access the information of major/minor requirements of
    given file paths and write them into a given outfile.
    """
    
    open_urls = open('../database/program_Urls.json')
    all_urls = json.load(open_urls)
    write_majors = open(out_file, 'w')
    sorted_files = sorted(file_names)

    for index, name in enumerate(sorted_files, 1): 
        with open(file_names[name], 'r') as f:
            all_info = json.load(f)
            requirement = str(all_info).replace("'", '"')
            is_major = 1 
            if "Minor" in name:
                is_major = 0
            write_majors.write("INSERT INTO programs (name, isMajor, requirement, url) VALUES (" + 
                                "'" + name + "', " + "'" + str(is_major) + "', " + "'" + requirement + "', '" + 
                                all_urls[name.replace('-', '/')] + '#requirementstext' + "');" + "\n")
            write_required_courses(all_info, index)

    open_urls.close()
    write_majors.close()


if __name__ == "__main__":
    
    file_paths = get_paths()
    write_requirements(file_paths, NAME_REQ_OUT)
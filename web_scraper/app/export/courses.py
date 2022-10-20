import common

def insert_course_string(course_id: str, course: dict) -> str:
    fields = [
        "name", 
        "department", 
        "units", 
        "units_text", 
        "description", 
        "prerequisite", 
        "prerequisite_tree", 
        "prerequisite_for",
        "corequisite", 
        "corequisite_tree",
        "prerequisite_or_corequisite",
        "prerequisite_or_corequisite_tree",
        "restriction", 
        "same_as", 
        "overlaps_with", 
        "concurrent_with",
        "repeatability", 
        "ge_string"]
    sql_string = []
    sql_string.append('INSERT INTO courses VALUES (\'' + course_id + '\'')

    for field in fields:
        value = course[field]
        if value:
            if type(value) == list:
                sql_string.append(', ARRAY ' + str(value))
                if field == 'prerequisite_for':
                    sql_string.append('::text[]')
            elif type(value) == int:
                sql_string.append(', ' + str(value))
            elif type(value) == dict:
                sql_string.append(',\'' + str(value).replace('\'','"') + '\'')
            else:
                sql_string.append(',\'' + value + '\'')
        else:
            sql_string.append(', ' + 'null')
    
    if course['terms']:
        sql_string.append(',\'' + course['terms'] + '\');' + '\n')
    else:
        sql_string.append(',' + 'null' + ');' + '\n')

    return "".join(sql_string)

def export_courses(file_path: str):
    with open(file_path, 'w') as f:
        for key, value in common.courses.items():
            f.write(insert_course_string(key, value))
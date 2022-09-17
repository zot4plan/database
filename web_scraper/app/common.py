import json

root_path = '../../store/'

def get_data(file_path: str) -> (dict or list):
    file = open(file_path)
    data = json.load(file)
    file.close()
    return data

course_ids = set(get_data(root_path + 'course_ids.json'))
courses = get_data(root_path + 'courses.json')
manually_changes = get_data(root_path + 'manually_changes.json')



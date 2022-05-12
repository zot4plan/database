import json 
file_names = ["../data/Criminology_Law_and_Society_B.A.json"]
for elem in file_names: 
    with open(elem, 'r') as f: 
        data = json.load(f)
        print(data)
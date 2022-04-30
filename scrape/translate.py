import json 
file_names = ["../data/Quantitative_Economics_B.A.json"]
for elem in file_names: 
    with open(elem, 'r') as f: 
        data = json.load(f)
        print(data)
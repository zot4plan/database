import json 




file_names = ["../data/Biological_Sciences_B.S.json"]
for elem in file_names: 
    with open(elem, 'r') as f: 
        data = json.load(f)
        print(data)

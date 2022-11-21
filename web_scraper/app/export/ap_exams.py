import csv

def export_ap_exam(file_path: str):
    ap_exam = []
    with open('../../store/ap_exam.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            ap_exam.append({
                'name': row[0], 
                'score': int(row[1]), 
                'credit': int(row[2]),
                'equivalent_courses': [w for w in row[3].split(' - ') if w]
            })
    
    with open(file_path, 'w') as f:
        for exam in ap_exam:
            f.write('INSERT INTO ap_exam (name, score, credit, equivalent_courses) VALUES (\'' 
                    + exam['name'] + '\', '
                    + str(exam['score']) +', '
                    + str(exam['credit']) + ', '
                    + ('NULL' if not exam['equivalent_courses'] else ('ARRAY ' + str(exam['equivalent_courses'])))
                    + ');\n')

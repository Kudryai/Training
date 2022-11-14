import csv


def condense_csv(filename, id_name) -> csv: #condensed.csv
    with open(f'./beginnerPRO/{filename}', 'r', encoding='utf-8') as file:
        data = csv.reader(file)
        head = [i for i in data]
        columns = [id_name]
        for i in range(len(head)):
            if head[i][1] not in columns:
                columns.append(head[i][1])
    with open('./beginnerPRO/condensed.csv', 'w', encoding='utf-8') as file_o:
        writer = csv.writer(file_o)
        writer.writerow(columns)
        result = [head[0][0]]
        for db in head:
            if db[0] in result:
                result.append(*db[2:])
            else:
                writer.writerow(result)
                result = [db[0], *db[2:]]
        writer.writerow(result)
                
        

condense_csv('data.csv', id_name='ID')

# with open('condensed.csv', encoding='utf-8') as file:
#     print(file.read().strip())
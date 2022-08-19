# Напишите программу, которая группирует данные файлы по расширению, 
# определяя общий объем файлов каждой группы, и выводит полученные группы файлов, 
# указывая для каждой ее общий объем. Группы должны быть расположены в лексикографическом порядке 
# названий расширений, файлы в группах — в лексикографическом порядке их имен.

with open('files.txt','r',encoding = 'utf-8') as file, open ('output.txt', 'w',encoding = 'utf-8') as output:
    data = list(map(str.strip,file.readlines()))
    res = [] # cписок файлов и их вес
    files_type = set() # расширения в файле
    end_result = []
    for i in range(len(data)):
        res.append(data[i].split(' '))
        type = res[i][0].split('.')
        files_type.add(type[1])
    files_type = list(sorted(files_type))
    for j in range(len(files_type)):
        bufer = []
        sum = {}
        res = sorted(res)
        for k in range(len(res)):
            if res[k][0].endswith(files_type[j]):
                bufer.append(res[k][0])
                sum[res[k][-1]] = sum.get(res[k][-1], 0) + int(res[k][1])
        bufer.append(sum)
        end_result.append(bufer)
    for o in range(len(end_result)):
        rest = 0 
        for key,values in end_result[o][-1].items():
            if key == 'B':
                rest += values
            elif key == 'KB':
                rest += values*1024
            elif key == 'MB':
                rest += values*1024**2
            elif key == 'GB':
                rest += values*1024**3
        type = {1 : 'KB', 0 : 'B', 2 : 'MB', 3 : 'GB'}
        for i in range(5):
            if rest > 1024:
                rest = round(rest/1024)
            else:
                end_result[o][-1].clear()
                end_result[o][-1][type[i]] = end_result[o][-1].get(type[i],rest)
                break
    for g in range(len(end_result)):
        end_result[g].insert(-1,'----------')
        print(*end_result[g][:-1],sep = '\n', file=output)
        for key, values in end_result[g][-1].items():
            print(f'Summary: {values} {key}',file=output)
        print(file=output)
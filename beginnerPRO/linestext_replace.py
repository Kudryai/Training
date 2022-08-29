from datetime import date,datetime, time
date_dict = {}
with open('/mnt/c/Users/user/Desktop/python/Training-1/Training/beginnerPRO/diary.txt', 'r+', encoding = 'utf-8') as file:
    data = list(map(str, file.readlines()))
    for text in data:
        try:
            if type(datetime.strptime(text, '%d.%m.%Y; %H:%M\n')) == datetime:
                sam = datetime.strptime(text, '%d.%m.%Y; %H:%M\n')
                date_dict[sam] = date_dict.get(sam, '') + text
        except:
            date_dict[sam] = date_dict.get(sam, '') + text
kak = sorted(date_dict.keys())
for keys in kak:
    print(f'{date_dict[keys]}'.rstrip()+'\n')
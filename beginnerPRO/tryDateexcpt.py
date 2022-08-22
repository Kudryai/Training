from datetime import date
cnt = 0
def is_correct(dat,cnt):
    dat = date(int(dat[2]), int(dat[1]), int(dat[0]))
    print('Корректная')
key = [0]
while key[0] != 'end':
    try:
        key = input().split('.')
        is_correct(key,cnt)
        cnt += 1
    except:
        if key[0] != 'end':
            print('Некорректная')
        else:
            print(cnt)
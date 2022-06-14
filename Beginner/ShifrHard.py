

txt = 'Day, mice. "Year" is a mistake!'
txt2 = ''
for slov in txt:
    if slov.isalpha() == True:
        txt2 += slov
    if slov.isalpha() == False:
        txt2 += ' '
n = txt2.split()
z = 0
o = 0
ready_txt = ''
for i in range(len(txt)):
    if 65 > ord(txt[i]) and 122 > ord(txt[i]):
        o -= 1
    if len(n[z]) == o:
        o = 0
        z += 1
    if 65 <= ord(txt[i]) <= 90:
        o += 1
        b = ord(txt[i]) + len(n[z])
        if b < 65:
            b += 26
        if b > 90:
            b -= 26
        ready_txt += chr(b)
        continue
    if 97 <= ord(txt[i]) <= 122:
        o += 1
        b = ord(txt[i]) + len(n[z])
        if b < 97:
            b += 26
        if b > 122:
            b -= 26
        ready_txt += chr(b)
        continue
    else:
        o += 1
        ready_txt += txt[i]
print(ready_txt)
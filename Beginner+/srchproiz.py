num = input()
lst = []
de = []
flag = False
for i in range(int(num)):
   lst.append(input())
mur = int(input())
if mur != 0:
    for j in range(len(lst)):
        if mur % int(lst[j])  == 0:
            odn = int(mur/int(lst[j]))
            lst[j] = "*"
            for k in range(len(lst)):
                if str(odn) == str(lst[k]):
                    flag = True
                    break
if mur == 0 or flag == True:
  print('ДА')
else:
  print('НЕТ')
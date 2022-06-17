n = int(input())
def pasca(spisok):
  list2 = [1]
  for i in range(1,len(spisok)):
    result = spisok[i]+spisok[i-1]
    list2.append(result)
  list2.append(1)
  if len(list2)-1 == n:
    return print(*list2)
  else:
    print(*list2)
    pasca(list2)
if n != 0 and n != 1 and n != 2:
    n -= 1
    print(*[1])
    print(*[1,1])
    pasca([1,1])
else:
    if n == 1:
        print(*[1])
    elif n == 2:
        print(*[1])
        print(*[1,1])
    else:
        print(*[1])
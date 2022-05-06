total = 0
for x in range (1,33):
    for y in range (1,33):
        for z in range (1,33):
            for d in range (1,33):
                if x != y and y != z and z != d and d != x and d != y and z != x:
                    if x**3 + y**3 == z**3 + d**3:
                        print(x**3 + y**3)
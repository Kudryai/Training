people = [i for i in range(1,int(input())+1)]
over = int(input())
new = []
while len(people) != 1:
    z = 0
    while z != over-1:
        z += 1
        people.append(people[0])
        del people[0]
    del people[0]
print(*people)
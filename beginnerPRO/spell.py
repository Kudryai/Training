def spell(*args):
    res = {}
    for num in args:
        try:
            if len(num) > res[num[0].lower()]:
                res[num[0].lower()] = res.get(num,len(num))
        except KeyError as error_msg:
            res[num[0].lower()] = res.get(num,len(num))
    return res





print(spell('Математика', 'История', 'химия', 'биология', 'Информатика'))
print(spell())
words = ['fruit', 'football', 'February', 'forest', 'Family']
print(spell(*words))
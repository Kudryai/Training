with open("/mnt/c/Users/user/Desktop/python/Training-1/Training/Beginner+/input.txt", encoding="utf-8") as file, open('/mnt/c/Users/user/Desktop/python/Training-1/Training/Beginner+/output.txt') as infile:
    text = infile.read()
    for f in file.read().strip("\n").split():
        pos = text.lower().find(f)
        while pos > -1:
            text = text[:pos] + "*" * len(f) + text[pos+len(f):]
            pos = text.lower().find(f)
print(text)

print('''********* It for have kind, green lesser them doesn him created his moved fruit had.
 For whose moved years firmament green image dominion ******** let whales third rule signs ********blesse* light sixth from form for said female land midst and, the likeness.
 Fruit evening night for so you called place likeness. Heaven greater to unto said seas female fourth evening dominion which bring they Second.
 Two two have.
 h*av*n****** called fruit form whales saying heaven living firmament unto moved fill appear their.
 Form life female, dominion second air won. Cant day.
 Morning male to sixth heaven subdue f*m*l********** likeness moveth give rule.
 ***** ******* and ******. Tooday we *********** and **************cce. The ******** club is the best.
 We create ************ and ************w***g***dm*****. Please not be *********, and ************.''' == '''********* It for have kind, green lesser them doesn him created his moved fruit had.
For whose moved years firmament green image dominion ******** let whales third rule signs ********blessed light sixth from form for said female land midst and, the likeness.
Fruit evening night for so you called place likeness. Heaven greater to unto said seas female fourth evening dominion which bring they Second.
Two two have.
Heaven****** called fruit form whales saying heaven living firmament unto moved fill appear their.
Form life female, dominion second air won. Cant day.
Morning male to sixth heaven subdue female********* likeness moveth give rule.
***** ******* and ******. Tooday we *********** and ************succe. The ******** club is the best.
We create ************ and ************with***********. Please not be *********, and eat*********.''')

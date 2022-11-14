class RenderList:
    def __init__(self, type_list):
        print(type_list)
        if type_list != 'ul' and type_list != 'ol':
            self.type_list = 'ul'
        else:
            self.type_list = type_list

    def __call__(self, lst, *args, **kwds):
        return f'''<{self.type_list}>
<li>{lst[0]}</li>
<li>{lst[1]}</li>
<li>{lst[2]}</li>
</{self.type_list}>'''


lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("ol")
html = render(lst)
print(html)
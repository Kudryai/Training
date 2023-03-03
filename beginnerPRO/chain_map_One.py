from collections import ChainMap


def deep_update(chainmap, key, value):
    res = []
    flag = True
    for dct in chainmap.maps:
        try:
            if dct[key]:
                flag = True
                dct[key] = value
                res.append(dct)
        except:
            flag = False
            continue
    if flag:
        chainmap = ChainMap(res)
    else:
        chainmap.maps[0][key] = value

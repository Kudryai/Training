from collections import ChainMap


def get_value(chainmap, key, from_left=True):
    if from_left:
        for name in chainmap.maps:
            try:
                return name[key]
            except:
                continue

    else:
        for name in chainmap.maps[::-1]:
            try:
                return name[key]
            except:
                continue


chainmap = ChainMap({"name": "Arthur"}, {"name": "Timur"})

print(get_value(chainmap, "name"))

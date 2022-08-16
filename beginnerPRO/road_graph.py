# Напишите программу, которая вычисляет минимальное расстояние, которое потребуется пройти Тимуру,
# чтобы посетить оба магазина и вернуться домой. Тимур всегда стартует из дома. 
# Он должен посетить оба магазина, перемещаясь только по имеющимся трём дорожкам,
# и вернуться назад домой. При этом его совершенно не смутит,
# если ему придётся посетить один и тот же магазин или пройти по одной и
# той же дорожке более одного раза. Единственная его задача — 
# минимизировать суммарное пройденное расстояние.


road_shop_1, road_shop_2, road_all = int(input()), int(input()), int(input())
result = []
result.append(road_shop_1*2)
result.append(road_shop_2*2)
result.append(road_all*2)
minimum = sorted(result)
res = minimum[0] + minimum[1]
sumator = road_shop_1 + road_shop_2 + road_all
if res > sumator:
    print(sumator)
else:
     print(res)

# Лучшее решение от Тимура Гуева:
# d1, d2, d3 = [int(input()) for _ in range(3)]
# print(min(d1 + d2 + d3, 2*(d1 + d2), 2*(d2 + d3), 2*(d1 + d3)))
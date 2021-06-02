'''scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a, *valid_score, b = scores
print(valid_score)'''

ice_cream = {"메로나": 1000, "폴라포": 1200, "빵빠레": 1800}
ice_cream["죠스바"] = 1200
ice_cream["월드콘"] = 1500
print(ice_cream)

inventory = {"메로나": [300, 20], "비비빅": [400, 3], "죠스바": [250, 100]}
print(inventory)
print(inventory["메로나"][0], "원")
print(inventory["메로나"][1], "개")

inventory["월드콘"] = [500, 7]
print(inventory)

icecream = {"탱크보이": 1200, "폴라포": 1800, "빵빠레": 1800, "월드콘": 1500, "메로나": 1000}
ice = list(icecream.keys())
ice_value = list(icecream.values())
print(ice)
print(ice_value)
print(sum(ice_value))

new_product = {'팥빙수': 2700, '아맛나': 1000}
icecream.update(new_product)
print(icecream)

keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
result = dict(zip(keys, vals))
print(result)
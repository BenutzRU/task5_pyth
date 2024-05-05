import random

def geg(my_list):
    return random.choices(my_list, k=2)

list_el = [100, 400, 500, 10, 50, "Банан", "Клубника", "Камень", "Морковь", "Огурец", "Пицца"]
result = geg(list_el)
print("Два случайных элемента из списка:", result)

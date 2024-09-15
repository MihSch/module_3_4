# def test_func(*params):
#     print("Тип:", type(params))
#     print("Аргумент:", params)
#
#
# test_func(1, 2, 3, 4)



# def summator(txt, *values, type="sum"):
#     s = 0
#     for i in values:
#         s += i               # сумма чисел
#     return f'{txt}{s} {type}'
#
#
# print(summator("Сумма чисел: ", 2, 3, 4, type="summator"))



# def info(value, *types, names_author="Den", **values):
#     print("Тип:", type(values))
#     print("Аргумент:", values)
#     for key, value in values.items():
#         print(key, value)
#     print(types)
# #
# #
# info("Пример использования параметров всех типов", 2, 3, 4, names_author="Denis", name="Den", course="Python")


# def my_sum(n, *args, txt="Сумма чисел"):
#     s = 0
#     for i in range(len(args)):
#         s += args[i] ** n  #s += args[i] - сумма чисел args   ** - возведение в степень
#     print(txt + ":", s)
#
#
# my_sum(1, 1, 2, 3, 4, 5)
# my_sum(2, 2, 3, 4, 5, txt="Сумма квадратов")



def single_root_words (root_word, *other_words):

    same_worlds = []
    root_lower = root_word.lower()
    for i in other_words:
        other_lower = i.lower()
        if root_lower in other_lower or other_lower in root_lower:
            same_worlds.append(i)
    return same_worlds

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)











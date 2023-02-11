# Задача 1. В каждой группе учится от 20 до 30 студентов. По итогам экзамена все оценки заносятся в таблицу. 
# Каждой группе отведена своя строка. Определите группу с наилучшим средним баллом.
import random

# groups = random.randint(2,6)
# print(groups)
# mas = [[0] * random.randint(20,30) for i in range(groups)]
# for i in range(groups):
#     for j in range(len(mas[i])):
#         mas[i][j] = random.randint(64, 100)
# for i in range(groups):
#     print(mas[i])
# max = 0
# for i in range(groups):
#     current_max = 0
#     for j in range(len(mas[i])):
#         current_max += mas[i][j]
#     current_max = current_max / len(mas[i])
#     if current_max > max:
#         max = round(current_max, 2)
#         best_group = i

# print(f"Лучший балл {max} у группы {best_group+1}")
        


# Задача 2. Дана квадратная матрица, заполненная случайными числами. 
# Определите, сумма элементов каких строк превосходит сумму главной диагонали матрицы.

# size = random.randint(3,6)
# mas = [[0] * size for i in range(size)]
# for i in range(size):
#     for j in range(len(mas[i])):
#         mas[i][j] = random.randint(0,99)
# for i in range(size):
#     print(mas[i])
# sum_diagonal = 0
# for i in range(size):
#     sum_diagonal += mas[i][i]
# print(sum_diagonal)
# count = 0
# for i in range(size):
#     sum_str = 0
#     for j in range(len(mas[i])):
#         sum_str += mas[i][j]
#     if sum_str > sum_diagonal:
#         print(f"Сумма элементов в строке {i} больше суммы элементов в диагонали")
#         count += 1
# if count == 0:
#     print('Нет строк, в которых сумма элементов превышает сумму элементов в диагонали')

# Задача 3. В двумерном массиве хранятся средние дневные температуры с мая по сентябрь за прошлый год. 
# Каждому месяцу соответствует своя строка.
# Определите самый жаркий и самый холодный 7-дневный промежуток каждого месяца. Выведите их даты.

mas = [ [0] * 31,
        [0] * 30,
        [0] * 31,
        [0] * 31,
        [0] * 30 ]
for i in range(len(mas)):
    for j in range(len(mas[i])):
        mas[i][j] = random.randint(15,35)
for i in range(len(mas)):
     print(mas[i])

def max_and_min(text, mas, index_month):
    temp = []
    for j in range(len(mas[index_month])-6):
        temp.append(sum(mas[index_month][j:j+7]))
    # print(temp)
    index_max = temp.index(max(temp))
    # print(index_max)
    index_min = temp.index(min(temp))
    # print(index_min)
    print(f"В месяце {text} самый жаркий 7-дневный период был с {index_max+1} по {index_max+7}")
    print(f"В месяце {text} самый холодный 7-дневный период был с {index_min+1} по {index_min+7}\n")
    
max_and_min("Май", mas, 0)
max_and_min("Июнь", mas, 1)
max_and_min("Июль", mas, 2)
max_and_min("Август", mas, 3)
max_and_min("Сентябрь", mas, 4)


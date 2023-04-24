#Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5. Используйте для решения лямбда-функцию.
import random
def task1():
    n = random.randint(1, 10)
    nums = [random.randint(1, 10) for n in range(10)]
    print(nums)
    nums = list(filter(lambda x: x > 5, nums))
    print(nums)
task1()

#Дан список случайных чисел. Создайте список, в который попадают числа, описывающие случайную возрастающую последовательность. Порядок элементов менять нельзя.
import random
def task2():
    n = random.randint(1, 10)
    numbers = [random.randint(1, 10) for _ in range(n)]
    print(numbers)
    length = len(numbers)     
    i = 0
    while i < length:
        result = []  
        min = numbers[i]
        result.append(min)
        j = i + 1
        flag1 = True
        while flag1:
            if result[len(result)-1] < min:
                result.append(min)
            if j == length:
                flag1 = False
                continue
            flag = True
            while flag:
                if min < numbers[j]:
                    min = numbers[j]
                    j += 1
                    flag = False
                else:
                    j += 1
                    flag = False
        if len(result) > 1:
            print(result)
        i += 1
task2()

#Задайте список случайных чисел от 1 до 10. Посчитайте, сколько всего совпадающих элементов есть в списке. Удалите все повторяющиеся элементы.
import random
def array():
    nums = [random.randint(0, 10) for _ in range(10)]
    print(nums)    
    unique = list(set(nums))
    repeat_sum = 0
    len_unique = len(unique)   
    for i in range(len_unique):
        repeat = 0
        repeat = nums.count(unique[i]) 
        if repeat > 1:
            repeat_sum += repeat    
        print(f'{unique[i]} - {repeat}')     
    print(f'{repeat_sum} элементов совпадают')
    print(f'Список уникальных элементов: ', unique)
array()
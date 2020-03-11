# 3.30 nested loop

# listA = list(range(4))
# listB = list(range(4))
# product =[]
# for a in listA:         # klasyczna petla
#     for b in listB:
#         product.append((a,b))
# print(product)
#
# product = [(a,b) for a in listA for b in listB]
# print(product)
#
# product = [(a,b) for a in listA for b in listB if a%2 == 0 and b%2 == 1]    # % podzielne przez
# print(product)


# 3.31 zadanie

# ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
#          'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']
#
# flights = [(a,b) for a in ports for b in ports]
# print(flights)
# flights_unique = [(a,b) for a in ports for b in ports if a!=b]
# print(flights_unique)
# # usuwam duplikaty A-B B-A szukajac pozycji A i B na liscie i porownujac
# # zamiast index zadziala tez prostsze a<b
# flights_1way = [(a,b) for a in ports for b in ports if a!=b and ports.index(a)<ports.index(b)]
# print(flights_1way)


# 3.33 generator

# listA = list(range(4))
# listB = list(range(4))
# product =[]
#
# product = [(a,b) for a in listA for b in listB if a%2 == 0 and b%2 == 1]    # % podzielne przez
# print(product)
#
# generatorek =  ((a,b) for a in listA for b in listB if a%2 == 0 and b%2 == 1)
# print(next(generatorek))
# print('-----')
# for g in generatorek:
#     print(g)            # generator przechowuje 'temp' dane. 1 pare pobralem recznie, 3 pobrala petla
#
# # druga opcja z while
# print('-----')
# generatorek =  ((a,b) for a in listA for b in listB if a%2 == 0 and b%2 == 1)
# while True:
#     try:
#         print(next(generatorek))
#     except StopIteration:
#         print('wszystko')
#         break


# 3.34 zadanie

# ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
#          'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']
#
# flights_gen = ((a,b) for a in ports for b in ports)
# flights_unique = ((a,b) for a in ports for b in ports if a!=b)
# for item in flights_unique:
#     print(item)
# # usuwam duplikaty A-B B-A szukajac pozycji A i B na liscie i porownujac
# # zamiast index zadziala tez prostsze a<b
# flights_1way = [(a,b) for a in ports for b in ports if a!=b and ports.index(a)<ports.index(b)]
# print(flights_1way)


# 3.36 eval

# var_x = 10
# password = 'secret password'
# source = 'password'
# result = eval(source)   # eval uruchamia kod przechowywany pod zmienna
# print(result)
#
# print(globals())    # globals pokazuje wszystkie zmienne w srodowisku
# globals_copy = globals().copy()


# 3.37 zadanie - cos tu nie dziala

import math
# arg = [a /10 for a in range(0, 101)]
# print(arg)
#
# funkcja = input('podaj wzor f: ')
# for x in arg:
#     exec(funkcja)
#     print(y)


# 3.39 exec()

# var_x = 10
# source = 'var_x = 4'
# result = exec(source)   # exec uruchamia kod przechowywany pod zmienna lub w pliku, nie zwraca wartosci
# print(result)             # w exec mozna wykonac >1 linie kodu, moze zmieniac wartosci
# print(var_x)


# 3.40 zadanie exec

# import os
# paths = [r'C:\Users\MD\PycharmProjects\udemy_py_sred_zaaw',r'3.40 zadanie A.py',
#          r'C:\Users\MD\PycharmProjects\udemy_py_sred_zaaw',r'3.40 zadanie B.py']
# path_join = [os.path.join(paths[0], paths[1]), os.path.join(paths[2], paths[3])]
#
# for file in path_join:
#     with open(file) as f:       # otworz plik i wczytaj kod
#         print(os.path.basename(file))
#         source = f.read()
#         result = exec(source)
#         print(result)


# 3.42 compile

# import time
#
# reportline = 0
# source = 'reportline += 1'
# start = time.time()
# for i in range(10000):
#     exec(source)
#     # print(reportline)       # zwraca zmienna po wykonaniu kodu w source
# stop = time.time()
# time_not_compiled = stop-start
#
# start = time.time()
# compiled = compile(source, 'pobrano ze zmiennej', 'exec')
# for i in range(10000):
#     exec(compiled)      # do exec trzeba podac prekompilowany kod do wykonania
# stop = time.time()
# time_compiled = stop-start
#
# # skompilowany kod jest 20x szybszy. Przy duzej ilosci danych dobrze skompilowac fragment kodu uzywajac exec
# # i podawac go w zmiennej do wykonania
#
# print(time_not_compiled, time_compiled, time_not_compiled/time_compiled)
#

# 3.43 zadanie compile


# import time, math
# formulas_list = [
#     "abs(x**3 - x**0.5)",
#     "abs(math.sin(x) * x**2)"
# ]
#
# args = []
# for i in range(100000):
#     args.append(i/10)
#
# for formula in formulas_list:
#     results = []
#     start = time.time()
#     print(formula)
#
#     for x in args:
#         result = eval(formula)  # eval zwraca wartosc kodu, exec nie
#         results.append(result)
#     stop = time.time()
#     print('min: {}, max: {}, time: {}'.format(min(results), max(results), stop-start))
#
#
# for formula in formulas_list:
#     compiled_formula = compile(formula, 'ze zmiennej', 'eval')  # kompilacji podlega tylko string
#     results = []
#     start = time.time()
#     print(formula)
#     for x in args:
#         result = eval(compiled_formula)  # eval zwraca wartosc kodu, exec nie.
#         results.append(result)
#     stop = time.time()
#     print('min: {}, max: {}, time: {}'.format(min(results), max(results), stop-start))
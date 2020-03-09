# 4.46 funkcje zadanie
#
# def show_progress(how_many, character='*'):
#     line = character * how_many
#     print(line)
#
#
# show_progress(10)
# show_progress(15)
# show_progress(30)
#
# show_progress(10, '-')  # mozna podmienic domyslny arg wywolujac funkcje
# show_progress(15, '+')


# 4.48 args kwargs

# def funkcja1(x = 'A', y = 'B', *args):
#     print(x,y)
#     print(args)
#
# funkcja1('a', 'b', 'c', 'd')    # przez args zwraca tuple z elementami spod args
#
# print('-----------')
#
# def funkcja2(x = 'A', y = 'B', *args, **kwargs):
#     print(x,y)
#     print(args)                     # args zwraca tuple
#     print(kwargs)                   # kwargs zwraca dict
#
# products = ['l1','l2','l3']
# params = {'k1':'v1', 'k2':'v2'}
#
# funkcja2('a', 'b', *products, **params)


# 4.49 zadanie args kwargs

# def calc_paint(efficiency, *args):
#     area = sum(args)
#     paint_quantity = area * efficiency
#     print(paint_quantity)
#
# rooms = [3,4,5]
# calc_paint(2, *rooms)
# calc_paint(2,3,4,5)

# def log_it(*args):
#     path1 = r'C:\Users\MD\PycharmProjects\udemy_py_sred_zaaw\zadanie_4_49.txt'
#     with open(path1,'a+') as f:    # a+ tworzy plik jesli go nie ma - append
#         for i in args:
#             f.writelines(i+'\n')        # dopisuje w nastepnej linii
#         f.writelines('-----')
#
# log_it('dupa','1','2')


# 4.52 zadanie - funkcja jako zmienna

# def double(x):
#     return 2 * x
#
#
# def root(x):
#     return x ** 2
#
#
# def negative(x):
#     return -x
#
#
# def div2(x):
#     return x / 2
#
# number = 8
# trans = [double, root, div2, negative]  # mozna zdefiniowac liste funkcji
# temp = number
#
# for t in trans:     # wywolac f z listy petla
#     result = t(temp)    # podstawic funkcje pod iterator
#     temp = temp + result
#     print(temp)

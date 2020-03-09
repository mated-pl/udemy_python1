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


# 4.54   funkcja w funkcji      #TODO powtarzac odtad

# def Bake(what):
#     print('Baking {}'.format(what))
#
# def Add(what):
#     print('Adding {}'.format(what))
#
# def Mix(what):
#     print('mixing {}'.format(what))
#
# # tworze list tupli (funkcja, arg)
# cookbook = [(Bake,'coockies'),(Add,'milk'), (Mix, 'ingredniens')]
#
# # tworze funkcje gdzie 1. arg - funkcja
# def Cook(activity, item):
#     activity(item)
#
# # petla wywoluje tuple i wsadza do funkcji Cook
# for activity, item in cookbook:
#     Cook(activity,item)


# 4.55 zadanie

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
# inputlist = [1,2,3]
# x_table = [2,3,4]
# outputlist = []
#
# def generate_values (fun, list):
#     for item in list:
#         outputlist.append(fun(item))
#     print(outputlist)
#
# generate_values(negative,inputlist)
# print(generate_values(double, x_table))
# print(generate_values(root, x_table))
# print(generate_values(negative, x_table))
# print(generate_values(div2, x_table))
#


# 4.57 generowanie funkcji przez funkcje

# def CreateFunction (kind):
# # tworzymy wewnetrzna funkcje jako str.
#     source = '''
# def dynamic_function(*args):
#     result = 0
#     for item in args:
#         result {}= item
#     return result
# '''.format(kind)    # pod {} wstawiamy argument kind
# # wykonuje txt kod w zmiennej
#     exec(source,globals())
# # zwracam nowa funkcje
#     return dynamic_function
#
# new_f_add = CreateFunction('+')
# print(new_f_add(5,6,7))


# 4.59 zadanie

# from datetime import datetime
#
# start = datetime(2020, 1, 1, 0, 0, 0)
# end = datetime.now()
#
# # f ma pokazac roznice czasu w wybranej jednostce (span)
# def Create_function(span):
#     if span == 'm':
#         sec = 60
#     elif span == 'h':
#         sec = 3600
#     elif span == 'd':
#         sec = 86400
#
# # funkcja ktora ma liczyc roznice w zaleznosci od span
#     generic_code = '''
# def generic_func(start, end):
#     diff = end-start
#     duration_in_s = diff.total_seconds()
#     return divmod(duration_in_s, {})[0]
# '''.format(sec)
#
# # wykonanie generycznej funkcji i zwrocenie jej wartosci
#     exec(generic_code, globals())
#     return generic_func
#
# # tworze custom funkcje dla span = h. Generator kodu
# new_func_h = Create_function('h')
# # wywoluje  custom funkcje dla argumentow podanych w generic
# print(new_func_h(start,end))


# 4.60
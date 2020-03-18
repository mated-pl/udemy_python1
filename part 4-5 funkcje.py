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


# 4.54   funkcja w funkcji

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


# 4.60 wrapper

# import functools    # musze zaimportowac zeby dzialal wraper
#
# def Create_F_wrapper(func):     # tworze f ktora dolozy wraper do func
#     def F_with_wrapper(*args, **kwargs):    # ma przyjac wszystkie mozliwe arg
#         print('start f')
#         result = func(*args, **kwargs)  # wsadzam funkcje z argumentu jako zmienna
#         print('stop f')
#     return F_with_wrapper       # zwracam nowa fukcje juz z wraperem
#
# @Create_F_wrapper     # dekoruje nowa funkcje tak, zeby trigerowala wraper
# def ChangeSal(name,value,is_Bonus = False):
#     print('Salary changed for {} to {}. Bonus - {}'.format(name,value,is_Bonus))
#
# print(ChangeSal('jas', 13, True))


# 4.61 wrapper zadanie

# from datetime import datetime
# import functools    # musze zaimportowac zeby dzialal wraper
#
# def duration_wrap(func):
#     def duration_func(*args, **kwargs):
#         start = datetime.now()
#         result = func(*args, **kwargs)
#         stop = datetime.now()
#         duration = stop - start
#         print(duration)
#         return result
#     return duration_func
#
# @duration_wrap
# def get_sequence(n):
#     if n <= 0:
#         return 1
#     else:
#         v = 0
#         for i in range(n):
#             v += 1 + (get_sequence(i - 1) + get_sequence(i)) / 2
#         return v
#
# get_sequence(1)
#
#
# # wersja z wraperem 'na piechote'

# import time
#
# def duration_wrap(func):
#     def duration_func(*args, **kwargs):
#         time_start = time.time()
#         result = func(*args, **kwargs)
#         time_stop = time.time()
#         print(">>>>>Function {} executed in {}".format(func.__name__, time_stop - time_start))
#         return result
#     return duration_func
#
# def get_sequence(n):
#     if n <= 0:
#         return 1
#     else:
#         v = 0
#         for i in range(n):
#             v += 1 + (get_sequence(i - 1) + get_sequence(i)) / 2
#         return v
#
# print(get_sequence(5))
# wrapper_get_sequence = duration_wrap(get_sequence)
# print(wrapper_get_sequence(7))


# 4.63 wrapper z parametrem

import datetime

# wraper zapisze log do pliku. Plik podajemy jako arg osobno dla kazdej funkcji
# def Create_F_wrapper_log(file_path):
#     def Create_F_wrapper(func):     # tworze f ktora dolozy wraper do func
#         def F_with_wrapper(*args, **kwargs):    # ma przyjac wszystkie mozliwe arg
#             with open(file_path,'a+') as file:
                    # func.__name__ zwraca nazwe funkcji
#                 file.write('Function {} started at {}\n'.format(func.__name__, datetime.datetime.now()))
#                 file.write('arguments were used: ')
#                 file.write(' '.join('{}'.format(x) for x in args)) # laczy iterowane elementy z args
#                 file.write('\n')
#                 file.write(' '.join('{}: {}'.format(k,v) for (k,v) in kwargs.items()))    # as above
#                 file.write('\n')
#                 result = func(*args, **kwargs)  # wsadzam funkcje z argumentu jako zmienna
#                 file.write('Function returned: {}\n'.format(result))
#             return result
#         return F_with_wrapper       # zwracam nowa fukcje juz z wraperem
#     return Create_F_wrapper
#
# @Create_F_wrapper_log(r'C:\Users\MD\PycharmProjects\udemy_py_sred_zaaw\zadanie_4_63.txt')     # dekoruje nowa funkcje tak, zeby trigerowala wraper
# def ChangeSal(name,value,is_Bonus = False):
#     print('Salary changed for {} to {}. Bonus - {}'.format(name,value,is_Bonus))
#
# print(ChangeSal('jas', 13, True))
# print(ChangeSal('jas', 13, is_Bonus=True))


# 4.64 zadanie wrapper

# import datetime, os, functools
#
# path = r'C:\Users\MD\PycharmProjects\udemy_py_sred_zaaw\zadanie_4_64_test_file.txt'
# path_log = r'C:\Users\MD\PycharmProjects\udemy_py_sred_zaaw\zadanie_4_64_log.txt'
#
# def log_wrapper(operation, path_log):
#     def f_wrapped_B(func):
#         def f_wrapping_C(*args,**kwargs):
#             with open(path_log, 'w') as file:
#                 file.write('Action {} executed on {} on {}\n'.format(operation, path, datetime.datetime.now()))
#             result = func(*args, **kwargs)
#             return result
#         return f_wrapping_C
#     return f_wrapped_B
#
# @log_wrapper('Create', path_log)    # dwa parametry
# def create_file(path):
#     f = open(path, "a")
#     f.close()
#
# @log_wrapper('Delete', path_log)
# def delete_file(path):
#     os.remove(path)
#
# create_file(path)


# 4.66 email

# import smtplib
# mailFrom = "python kurs"    # te zmienne musza byc tak sformatowane zeby smtplib je przelknal
# mailTo = ['dupa1@dupa.pl', 'elmatte@gmail.com']
# mailSubject = 'temat'
# mailBody = '''helo
# this is email
# test'''
#
# # wrzucamy zmienne do tekstu formatujac odpowiednio
# message = '''From: {}
# Subject: {}
#
# {}
# '''.format(mailFrom,mailSubject,mailBody)
#
# user = 'testowyadres@gmail.com'
# password = 'jakies_haslo'
#
# try:
#     server = smtplib.SMTP_SSL('smtp.gmail.com',465)
#     server.ehlo()
#     server.login(user,password) # wymagane parametry
#     server.sendmail(user, mailTo, message) # wymagane parametry
#     server.close()
#     print('main sent')
# except:
#     print('error')


# 4.69 partial

# import smtplib, functools
# # definiujemy funkcje normalnie
# def send_email(account, passw, sender, reciever, subject, body)
#     message = '''From: {}
#     Subject: {}
#
#     {}
#     '''.format(reciever,subject,body)
#
#     try:
#         server = smtplib.SMTP_SSL('smtp.gmail.com',465)
#         server.ehlo()
#         server.login(account,passw) # wymagane parametry
#         server.sendmail(account, sender, message) # wymagane parametry
#         server.close()
#         print('main sent')
#         return True # zeby latwo sprawdzic czy sie udalo
#     except:
#         print('error')
#         return False
#
# # wprowadzam customowe dane
# user = 'testowyadres@gmail.com'
# password = 'jakies_haslo'
# mailFrom = "python kurs"    # te zmienne musza byc tak sformatowane zeby smtplib je przelknal
# mailTo = ['dupa1@dupa.pl', 'elmatte@gmail.com']
# mailSubject = 'temat'
# mailBody = '''helo
# this is email
# test'''
#
# # tworze funkcje partial. Najlepiej podac arg po nazwie
# send_from_custom_account_partial = functools.partial(send_email, account=user,passw=password)
# # podaje tylko customowe paramentry
# send_from_custom_account_partial(sender = mailFrom, reciever=mailTo, subject=mailSubject, body=mailBody)


# 4.70 partial zadanie

# import requests
# import os
#
#
# def save_url_file(url, dir, file, msg):
#     print(msg.format(file))
#
#     r = requests.get(url, stream=True)
#     file_path = os.path.join(dir, file)
#
#     with open(file_path, "wb") as f:
#         f.write(r.content)
#
# msg = "Please wait - the file {} will be downloaded"
#
# # url = 'http://mobilo24.eu/spis'
# # dir = r'C:\Users\MD\PycharmProjects\udemy_py_sred_zaaw'
# # file = 'spis.html'
# # save_url_file(url, dir, file, msg)
#
# url = 'https://www.mobilo24.eu/wp-content/uploads/2015/11/Mobilo_logo_kolko_512-565b1626v1_site_icon.png'
# dir = r'C:\Users\MD\PycharmProjects\udemy_py_sred_zaaw'
# file = 'logo.png'
# # save_url_file(url, dir, file, msg)
#
# save_url_part = functools.partial(save_url_file, file=file, msg = msg)
# save_url_part(url=url, dir=dir)


# 4.72 cache

# import functools
# import time
#
# @functools.lru_cache()  # wraper wbudowany cachowanie
# def factorial(n):
#     time.sleep(0.1) # opoznienie specjalnie
#     if n ==1:
#         return 1
#     else:
#         return n*factorial(n-1)
#
# start = time.time()
# for i in range(1,10):
#     print('{}! = {}'.format(i,factorial(i)))
# stop = time.time()
# print('exec time', stop-start)
# print(factorial.cache_info())   # wyswietla paramentry cachowania


# 4.73 cache zadanie

# import functools, time
#
# @functools.lru_cache()
# def fib(n):
#     if n <= 2:
#         result = n
#     else:
#         result = fib(n - 1) + fib(n - 2)
#
#     return result
#
# start = time.time()
# for i in range(30):
#     fib(i)
# stop = time.time()
# print('exec time', stop-start)


# 4.75 lambda

# x = 10
# f = lambda x: x*2
# print(f(x))
#
# g = lambda x,y: x*y
# print(g(2,3))
#
#
# lista = [1,2,3,4,5,6,7,8,9]
#
# def is_odd(x):
#     return x % 2 != 0   # dzielenie bez reszty rozne od 0
#
# # funkcja filter odfiltruje elementy z listy ktore w funkcji is_odd daja wynik False
# filtered_list = list(filter(is_odd,lista))  # is_odd podaje bez ().
# print(filtered_list)
#
# # zamiast definiowac fukncje is odd
# filtered_list = list(filter(lambda x: x % 2 != 0 ,lista))
# print(filtered_list)


# 4.76 lambda zadanie

text_list = ['x','xxx','xxxxx','xxxxxxx','']

f = lambda x: len(x)
print(f('asd'))

# funkcja map uruchamia funkcje f na kazdym elemencie listy text_list
mapa = map(f,text_list)
print(list(mapa))
# drugi sposob
print(list(map(lambda x: len(x),text_list)))
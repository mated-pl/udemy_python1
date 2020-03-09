# 2.2

# myvar = "text"
# myvar2 = myvar
# print(type(myvar), type(myvar2))
# print('is value equal?', myvar==myvar2)
# print('is variable the same?', myvar is myvar2)
# print(id(myvar), id(myvar2))    # obie zmienne odnosza sie do tego samego obszaru w pamieci
# #
# myvar = "text"
# myvar2 = myvar+"ABC"            # myvar 2 przestaje odnosic sie do tego samego obszaru w pamieci
# print(type(myvar), type(myvar2))
# print('is value equal?', myvar==myvar2)
# print('is variable the same?', myvar is myvar2)
# print(id(myvar), id(myvar2))    # obie zmienne NIE odnosza sie do tego samego obszaru w pamieci
#
# myvar2 = myvar2[:-3]
# print('is value equal?', myvar==myvar2)
# print('is variable the same?', myvar is myvar2)
# print(id(myvar), id(myvar2))    # obie zmienne NIE odnosza sie do tego samego obszaru w pamieci


# 2.4 zadanie

# a = b = c = 10
# print(a, id(a),"\n", b, id(b),"\n", c, id(c))
# print('')
# a = 20
# print(a, id(a),"\n", b, id(b),"\n", c, id(c))
# print('')
# a = b = c = [1,2,3]
# print(a, id(a),"\n", b, id(b),"\n", c, id(c))
# print('')
# a = a+[4]
# # modyfikacja zmiennej przez podstawienie pod stara zmienna zwraca none 'a = a+[4] a = a.append(4)'
# # append doda 4 tez do b i c, a+[4] zmieni tylko a.
# # https://stackoverflow.com/questions/11205254/why-dont-list-operations-return-the-resulting-list
# print(a, id(a),"\n", b, id(b),"\n", c, id(c))
# print('')
#
# x=10+1-1
# y=10
# print(id(x), id(y))


# 2.6 Mutable\Immutable

# n = 10
# print(n, id(n))
# n +=2
# print(n, id(n))     # powstala nowa zmienna. Int\str immutable
#
# lst1 = [1,2,3]
# print(lst1, id(lst1))
# lst1.append(4)
# print(lst1, id(lst1))   # list - mutable
#
# lst2 = lst1
# lst2.append(5)
# print(lst1, id(lst1))
# print(lst2, id(lst2))   # list - mutable
#
# lst3 = lst1.copy()
# print(lst1, id(lst1))
# print(lst3, id(lst3))   # kopia - osobne zmienne
#
# lst3.append(6)
# print(lst1, id(lst1))
# print(lst3, id(lst3))


# # 2.7 LAB
#
# days = ['mon','tue','wed','thu','fri','sat','sun']
# workdays = days.copy()
# print(id(workdays), id(days))
# workdays = workdays[:len(workdays)-2]
# print(workdays)
# print(days)


# 2.8 bool konwersja

# var1 = "dupa"
# if str:
#     print('str to text a i tak bool = True')


# 2.9 zadanie

# options = ['load data', 'export data', 'analyze & predict']
# choice = 'x'
#
# def DisplayOptions(x):
#     for i in range(len(x)):
#         print(i + 1, " - ", x[i])
#     answer1 = input('Select option above or press enter to exit: ')
#     result = x[int(answer1)-1]
#     print(result)
#     return result
#
# while choice:   # dopoki choice ma wart logiczna True
#     try:        # try this code
#         choice = DisplayOptions(options)
#     except ValueError:  # if occures ValueError than do...
#         print("input is empty or text")
#     except:             # if occures other error do...
#         print("value out of range")
#     else:
#         break


# 2.11 Operacje na plikach w wyrażeniach logicznych
# 2.13 zadanie

# import os
# path = r'C:\Users\MD\PycharmProjects\udemy_py_sred_zaaw\part1_1.txt'
# def count_words(path_to_file):
#     with open(path_to_file) as file:
#         file_content = file.read()
#         words_list = file_content.split()
#         print("words count = ", len(words_list))
#
# # os.remove(path)                 # usuniecie pliku
# if os.path.isfile(path):
#     print('plik %s istnieje' % path)
#     count_words(path)
# else:
#     print('plik nie istnieje, tworzenie pliku')
#     open(path, 'x').close()     # tworzenie pliku
#     print('plik gotowy')


# 2.16  zadanie skladnia IF i PASS

# import datetime, calendar
# from datetime import date
# today = datetime.datetime.today()
# print(today)
# today_weekday = calendar.day_name[today.weekday()]
# print(today_weekday)
#
# if today_weekday == 'sob':
#     pass
# elif today_weekday == 'asda':
#     print("wtorek")
# else:
#     print('nic')


# 2.19 zadanie

# import os, urllib.request
# url_dir = r'C:\Users\MD\PycharmProjects\udemy_py_sred_zaaw\2.19'
# pages = [
#     { 'name': 'mobilo',      'url': 'http://www.mobilo24.eu/'},
#     { 'name': 'onexistent', 'url': 'http://abc.cde.fgh.ijk.pl/' }]

# for page in pages:
#     # os.path.join laczy elementy sciezki zeby nie bylo bledow z \
#     try:
#         url_file = os.path.join(url_dir,page['name']+'.html')
#         print(url_file)
#         print(page['url'])
#         urllib.request.urlretrieve(page['url'], url_file)
#     except:
#         print('error')
#         break
# else:
#     print('ok')

# # to samo przez while
# i=0
# while i < len(pages):
#     # os.path.join laczy elementy sciezki zeby nie bylo bledow z \
#     try:
#         url_file = os.path.join(url_dir, pages[i]['name'] + '.html')
#         print(url_file)
#         print(pages[i]['url'])
#         urllib.request.urlretrieve(pages[i]['url'], url_file)
#         i = i + 1
#     except:
#         print('error while processing ' + pages[i]['url'])
#         break
# else:
#     print('ok')


# 2.21 list

# dupa = range(10)
# print(type(dupa))   # range jest osobna klasa
# dupa_list = list(dupa)  # zamiana na liste
# print(type(dupa_list))
#
# dupa_list2 = dupa_list.copy()   # lista jest immutable, zeby stworzyc kopie trzeba uzyc .copy
# dupa_list3 = dupa_list[:]       # drugi sposob zamiast .copy. Od 0 do 0
# print(dupa_list3)
# print(id(dupa_list))
# print(id(dupa_list2))
# print(id(dupa_list3))


# 2.22 list zadanie

# colours = ["red", "orange", "green", "violet", "blue", "yellow"]
#
# def select_colours(colours_list):
#     n = input("Podaj liczbe kolorow")
#     n = int(n)
#     new_colours_list = colours_list[:n]
#     print(new_colours_list)
#
# #select_colours(colours)
#
#
# def colours_combinations(colours_list):
#     temp_col_lst = colours_list.copy()
#     for i in range(len(colours_list)):
#         for item in colours_list[i+1:]:
#             print(colours_list[i]," - ", item)
#
# colours_combinations(colours)


# 2.23 enumerate i zip

# workdays = [10,20,30,40]
# en_workdays = list(enumerate(workdays))
# print(en_workdays)
#
# for pos, val in en_workdays:
#     print('pos', pos, 'val', val)
#
# months = ['I','II','III', 'IV']
# workdays_months = zip(months,workdays)
# workdays_months_list = list(workdays_months)
# print(type(workdays_months))
# print(workdays_months_list)

# for m,d in workdays_months_list:
#     print('month', m, 'days', d)
#
# for pos, (m,d) in enumerate(zip(months,workdays)):  # for po 3 zmiennych
#     print(pos, m, d)


# 2.25 zadanie enumerate i zip

# projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
# leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']
# pro_lead = zip(projects,leaders)
#
# # for p, l in pro_lead:
# #     print('projekt', p, 'lider', l)
#
# dates = ['2016-06-23', '2016-08-29', '1994-01-01']
# pro_lead_dates = zip(dates,pro_lead)
#
# # for d, (p,l) in zip(dates,pro_lead):
# #     print(d, 'data', p, 'projekt', l, 'leader')
#
# for n, (d,(p,l)) in enumerate(pro_lead_dates):
#     print(n, 'id', d, p, l)


# 2.27 dict iter

# workdays = [10,20,30,40]
# months = ['I','II','III', 'IV']
#
# month_days = dict(zip(months,workdays))
# print(month_days)
#
# for key in month_days:
#     print(key, month_days[key])
#
# for val in month_days.values():
#     print(val)


# 2.28 zadanie

# banknotes_coins = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500]
# list_denominations = [0] * len(banknotes_coins)
# dict_denominations = dict(zip(banknotes_coins,list_denominations))
# # print(dict_denominations)
#
# dict_denominations[100] += 1
# dict_denominations[20] += 1
# dict_denominations[5] += 1
# dict_denominations[0.5] += 1
# dict_denominations[50] += 1
# dict_denominations[20] += 2
# dict_denominations[5] += 1
# dict_denominations[2] += 2
# dict_denominations[100] += 1
# dict_denominations[50] += 1
# dict_denominations[2] += 1
#
# for k in dict_denominations:
#     print('denominations %5.2f, quantity%3d' %(k, dict_denominations[k]))
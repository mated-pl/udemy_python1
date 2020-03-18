# 6.78 dict

# car_01 = {
#     'brand' : 'seat',
#     'model' : 'cordoba',
#     'airbagOK' : True,
#     'paintOK' : True,
#     'mechOK' : True,
# }
#
# def IsCarDamaged(car):
#     # return not zwraca wartosc False
#     return not (car['airbagOK'] and car['paintOK'] and car['mechOK'] )
#
# print(IsCarDamaged(car_01))
#
#
# # 6.79 zadanie dict
#
# cake01 = {
#     'taste' : 'vanilia',
#     'glaze' : 'chocolade',
#     'text' : 'Happy Brithday',
#     'weight' : 0.7
# }
#
# cake02 = {
#     'taste' : 'aaaa',
#     'glaze' : 'asdasdasd',
#     'text' : 'Happy Brithday',
#     'weight' : 0.7
# }
#
#
# def show_cake_info(cake):
#     print('{} cake with {} glaze with text "{}" of {} kg'.format(
#         cake['taste'], cake['glaze'], cake['text'], cake['weight']))
#
# # show_cake_info(cake01)
#
# cakes = [cake01,cake02]
# for cake in cakes:
#     show_cake_info(cake)
# # przyklad programowania proceduralnego


# 6.81 class

# definiuje klase
# __init__ to konstruktor - inicjuje obiekt klasy (self)  argumentami
# class Car:
#     def __init__(self, brand, model, airbagOK, paintOK, mechOK):
#         # wlasciwosc instancji = argument
#         self.brand = brand
#         self.model = model
#         self.airbagOK = airbagOK
#         self.paintOK = paintOK
#         self.mechOK = mechOK
#
# # instancja klasy
# car01 = Car('seat', 'cordoba', True, True, True)
#
# print(car01.brand, car01.model, car01.airbagOK)


# 6.82 zadanie class

# class Cake:
#     def __init__(self, name, taste, glaze, weight):
#         self.name = name
#         self.taste = taste
#         self.glaze = glaze
#         self.weight = weight
#
# cake1 = Cake('ziemniaczek', 'smak1', 'glaze1', 0.7)
# cake2 = Cake('kremowka','smak2', 'glaze2', 0.5)
#
# offer = [cake1,cake2]
#
# print('''today's offer''')
# for item in offer:
#     print('''
#     {} - taste {} with {}. Weight: {} kg.'''.format(item.name, item.taste,item.glaze,item.weight))


# 6.84 metody instancje klasy

## definiuje klase
# # __init__ to konstruktor - inicjuje obiekt klasy (self)  argumentami
# class Car:
#     def __init__(self, brand, model, airbagOK, paintOK, mechOK):
#         # wlasciwosc instancji = argument
#         self.brand = brand
#         self.model = model
#         self.airbagOK = airbagOK
#         self.paintOK = paintOK
#         self.mechOK = mechOK
#
#     def isdamaged(self):    # metoda klasy
#         return not (self.airbagOK and self.paintOK and self.mechOK)
#
# # instancja klasy
# car01 = Car('seat', 'cordoba', True, True, True)
#
# # wywoluje metode dla car01
# print(car01.brand, car01.model, car01.isdamaged())


# 6.85 metody instancje klasy zadanie

# class Cake:
#     def __init__(self, name, taste, glaze, weight, additives):
#         self.name = name
#         self.taste = taste
#         self.glaze = glaze
#         self.weight = weight
#         self.additives = additives
#
#     def show_info(self):
#         print(self.name.upper(),' with glaze ', self.glaze)
#         if len(self.taste) > 0:
#             print('taste: ', self.taste)
#         print(self.additives)
#
#     def set_glaze(self, glaze_input):   # podaje argument wpisywany poza klasa
#         self.glaze = glaze_input
#
#     def set_additives(self,additives_input):
#         self.additives.append(additives_input)
#
#
# cake1 = Cake('ziemniaczek', 'smak1', 'glaze1', 0.7, [])
# cake2 = Cake('kremowka','smak2', 'glaze2', 0.5,['chocolade', 'nuts'])
#
#
# cake2.show_info()
# cake2.set_glaze('custom-glaze')
# cake2.show_info()
# cake2.set_additives(['add1','add2'])
# cake2.show_info()


# 6. 87 class instance diff

# class Car:
#
#     number_of_cars = 0
#     list_of_cars = []
#
#     def __init__(self, brand, model, airbagOK, paintOK, mechOK):
#         # wlasciwosc instancji = argument
#         self.brand = brand
#         self.model = model
#         self.airbagOK = airbagOK
#         self.paintOK = paintOK
#         self.mechOK = mechOK
#         Car.number_of_cars +=1
#         Car.list_of_cars.append(self)
#
#     def isdamaged(self):    # metoda klasy
#         return not (self.airbagOK and self.paintOK and self.mechOK)
#
# # instancja klasy
# car01 = Car('seat', 'cordoba', True, True, True)
# car02 = Car('chrysler', 'voyager', True, True, True)
# print(id(car01),id(car02),id(Car))  # kazda instancja i klasa maja osobne id
# print(isinstance(car02,Car))            # isinstance pokaze bool jesli inst nalezy do klasy
# print(type(car02) is Car)
# print(car02.__class__)  # pokaze nazwe klasy
# print(vars(car02))      # pokaze atrybuty instancji - zwroci slownik
# print(vars(Car))        # zwroci atrybuty klasy
#
# print(Car.number_of_cars)
# print(Car.list_of_cars)
#
# print(dir(car02))
# print(dir(Car))


# 6.88 zadanie
#
# class Cake:
#     bakery_offer = []
#     known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']
#
#     def __init__(self, name, taste, glaze, weight, additives, kind):
#         self.name = name
#         self.taste = taste
#         self.glaze = glaze
#         self.weight = weight
#         self.additives = additives
#         if kind in self.known_types:    # jesli podany przy tworzeiu klasy typ jest inny niz known types to zostanie wpisane 'other'
#             self.kind = kind
#         else:
#             self.kind = 'other'
#         Cake.bakery_offer.append(self)
#
#     def show_info(self):
#         print(self.name.upper(),' with glaze ', self.glaze)
#         if len(self.taste) > 0:
#             print('taste: ', self.taste)
#         print(self.additives)
#
#     def set_glaze(self, glaze_input):   # podaje argument wpisywany poza klasa
#         self.glaze = glaze_input
#
#     def set_additives(self,additives_input):
#         self.additives.append(additives_input)
#
#
# cake1 = Cake('ziemniaczek', 'smak1', 'glaze1', 0.7, [], 'dupa')
# # cake2 = Cake('kremowka','smak2', 'glaze2', 0.5,['chocolade', 'nuts'])
#
#
# cake1.set_glaze('custom-glaze')
# cake1.set_additives(['add1','add2'])
# # cake1.show_info()
# print('------------')
# print(vars(cake1))
# print(dir(cake1))
# print(vars(Cake))
# print(dir(Cake))
# print('------------')
# for item in Cake.bakery_offer:
#     print(item.name)
#     print('---')
#     item.show_info()
#
# print('------------')
#
# print(isinstance(cake1,Cake))


# 6.90 ukrywanie\dodawanie wlasciwosci      # TODO odtad powtarzac

# class Car:
#
#     number_of_cars = 0
#     list_of_cars = []
#
#     def __init__(self, brand, model, airbagOK, paintOK, mechOK, isOnSale):
#         # wlasciwosc instancji = argument
#         self.__brand = brand    # __ sprawia ze nie mozna modyfikowac atr z zew
#         self.model = model
#         self.airbagOK = airbagOK
#         self.paintOK = paintOK
#         self.mechOK = mechOK
#         self.isOnSale = isOnSale
#         Car.number_of_cars +=1
#         Car.list_of_cars.append(self)
#
#     def isdamaged(self):    # metoda klasy
#         return not (self.airbagOK and self.paintOK and self.mechOK)
#
#     def getinfo(self):
#         print('{} {}'.format(self.__brand,self.model).upper())
#         print('Airbag:   {}'.format(self.airbagOK))
#         print('Sale:   {}'.format(self.isOnSale))
#         print('----------')
#
# # instancja klasy
# car01 = Car('seat', 'cordoba', True, True, True, True)
# car02 = Car('chrysler', 'voyager', True, True, True, False)
#
# car02.getinfo()             # wyswietlam sobie obecny stan promocji car02 (false)
# car02.isOnSale = True       # moge zmienic wartosc atr
# car02.__brand = 'NOWY'      # nie zmieni wart __brand, doda nowa wlasciwosc. Klase mozna modyfikowac
# del car02.__brand           # usunie atr z car02
# car02.getinfo()             # teraz jest sale True


# 6.93 wlasciwosci klasy

# brand_on_sale = 'seat'
#
# class Car:
#
#     number_of_cars = 0
#     list_of_cars = []
#
#     def __init__(self, brand, model, airbagOK, paintOK, mechOK, isOnSale):
#         # wlasciwosc instancji = argument
#         self.brand = brand    # __ sprawia ze nie mozna modyfikowac atr z zew
#         self.model = model
#         self.airbagOK = airbagOK
#         self.paintOK = paintOK
#         self.mechOK = mechOK
#         self.__isOnSale = isOnSale
#         Car.number_of_cars +=1
#         Car.list_of_cars.append(self)
#
#     def isdamaged(self):    # metoda klasy
#         return not (self.airbagOK and self.paintOK and self.mechOK)
#
#     def getinfo(self):
#         print('{} {}'.format(self.brand,self.model).upper())
#         print('Airbag:   {}'.format(self.airbagOK))
#         print('Sale:   {}'.format(self.__isOnSale))
#         print('----------')
#
#     def __GetIsOnSale(self):      # ukryta metoda zwroci ukryty parametr isOnSale
#         return self.__isOnSale
#
#     def __setOnSale(self, newSaleStatus): # ukryta metoda to zmiany parametru (na piechote)
#         if self.brand == brand_on_sale:
#             self.__isOnSale = newSaleStatus
#             print('Sale status changed for {} to {}'.format(self.brand,newSaleStatus))
#         else:
#             print('cant change status')
#
#     # definiuje properties ktory wykorzysta funkcje
#     # 1st param definiuje jaka metoda pobieram wartosc
#     # 2nd param definiuje jaka metoda edytuje wartosc
#     # 3rd param definiiuje jaka metoda usuwa wartosc
#     is_on_sale_prop = property(__GetIsOnSale,__setOnSale,None, 'some descr')
#
# # instancja klasy
# car01 = Car('seat', 'cordoba', True, True, True, True)
# car02 = Car('chrysler', 'voyager', True, True, True, False)
#
# # mozna zmienic atrybut uzywajac funkcji
# '''print(car01.GetIsOnSale(), car02.GetIsOnSale())
# car01.setOnSale(False)
# car02.setOnSale(False)
# print(car01.GetIsOnSale(), car02.GetIsOnSale())'''
#
# # mozna zmienic atrybut uzywajac properties
# car01.is_on_sale_prop = True    # uzywajac metody zmieniam 1st param uzywajac 2nd param
# print(car01.is_on_sale_prop, car02.is_on_sale_prop)


# 6.94 zadanie wlasciwosci klasy

# class Cake:
#     bakery_offer = []
#     known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas','pretzel','other']
#
#     def __init__(self, name, taste, glaze, weight, additives, kind, text):
#         self.name = name
#         self.taste = taste
#         self.glaze = glaze
#         self.weight = weight
#         self.additives = additives
#         # jesli podany przy tworzeiu klasy typ jest inny niz known types to zostanie wpisane 'other'
#         if kind in self.known_types:
#             self.kind = kind
#         else:
#             self.kind = 'other'
#         # jesli kind = cake to instancji zostanie wpisany tekst, jesli nie - alert
#         if kind == 'cake':
#             self.__text = text
#         else:
#             print('{} - tekst tylko do cake'.format(self.name))
#
#         # do listy offfer dopisze instancje
#         Cake.bakery_offer.append(self)
#
#     def show_info(self):
#         print(self.name.upper(),' with glaze ', self.glaze)
#         if len(self.taste) > 0:
#             print('taste: ', self.taste)
#         print(self.additives)
#
#     def set_glaze(self, glaze_input):   # podaje argument wpisywany poza klasa
#         self.glaze = glaze_input
#
#     def set_additives(self,additives_input):
#         self.additives.append(additives_input)
#
#     def __get_text(self):
#         return self.__text
#
#     def __set_text(self, new_text):
#         if self.kind == 'cake':
#             self.__text = new_text
#
#     text_prop = property(__get_text, __set_text, None, 'test text')
#
# # definiuje . Dla cake1 i cake2 tekst sie nie doda, bo kind <> cake
# cake1 = Cake('ziemniaczek', 'smak1', 'glaze1', 0.7, [], 'dupa', 'tekst1')
# cake2 = Cake('kremowka','smak2', 'glaze2', 0.5,['chocolade', 'nuts'],'eclair','tekst2')
# cake3 = Cake('cake', 'smak1', 'glaze1', 0.7, [], 'cake', 'urodziny')
# cake4 = Cake('cake', 'smak1', 'glaze1', 0.7, [], 'cake', '')
#
# # odpalam property ze zmienna do funkcji set_text
# cake1.text_prop = 'wszystkiego najlpes'
# cake6.text_prop = 'wszystkiego najlpes'
#
# # dla cake1 sie nie zmieni tekst bo kind <> cake
# # dla cake4 sie zmieni
# for item in Cake.bakery_offer:
#     print(item.name)
#     print(vars(item))


# 6.96 metody instancji, klasy i statyczne






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


# 4.81 class

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


# 4.82 zadanie class

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


# 4.84 metody instancje klasy

## definiuje klase
## __init__ to konstruktor - inicjuje obiekt klasy (self)  argumentami
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


# 4.85 metody instancje klasy zadanie

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


# 4. 87 class instance diff

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


# 4.88 zadanie

class Cake:
    bakery_offer = []
    known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']

    def __init__(self, name, taste, glaze, weight, additives, kind):
        self.name = name
        self.taste = taste
        self.glaze = glaze
        self.weight = weight
        self.additives = additives
        if kind in self.known_types:    # jesli podany przy tworzeiu klasy typ jest inny niz known types to zostanie wpisane 'other'
            self.kind = kind
        else:
            self.kind = 'other'
        Cake.bakery_offer.append(self)

    def show_info(self):
        print(self.name.upper(),' with glaze ', self.glaze)
        if len(self.taste) > 0:
            print('taste: ', self.taste)
        print(self.additives)

    def set_glaze(self, glaze_input):   # podaje argument wpisywany poza klasa
        self.glaze = glaze_input

    def set_additives(self,additives_input):
        self.additives.append(additives_input)


cake1 = Cake('ziemniaczek', 'smak1', 'glaze1', 0.7, [], 'dupa')
# cake2 = Cake('kremowka','smak2', 'glaze2', 0.5,['chocolade', 'nuts'])


cake1.set_glaze('custom-glaze')
cake1.set_additives(['add1','add2'])
# cake1.show_info()
print('------------')
print(vars(cake1))
print(dir(cake1))
print(vars(Cake))
print(dir(Cake))
print('------------')
for item in Cake.bakery_offer:
    print(item.name)
    print('---')
    item.show_info()

print('------------')

print(isinstance(cake1,Cake))
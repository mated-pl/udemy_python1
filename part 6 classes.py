# 6.78 dict

car_01 = {
    'brand' : 'seat',
    'model' : 'cordoba',
    'airbagOK' : True,
    'paintOK' : True,
    'mechOK' : True,
}

def IsCarDamaged(car):
    # return not zwraca wartosc False
    return not (car['airbagOK'] and car['paintOK'] and car['mechOK'] )

print(IsCarDamaged(car_01))


# 6.79 zadanie dict

cake01 = {
    'taste' : 'vanilia',
    'glaze' : 'chocolade',
    'text' : 'Happy Brithday',
    'weight' : 0.7
}

cake02 = {
    'taste' : 'aaaa',
    'glaze' : 'asdasdasd',
    'text' : 'Happy Brithday',
    'weight' : 0.7
}


def show_cake_info(cake):
    print('{} cake with {} glaze with text "{}" of {} kg'.format(
        cake['taste'], cake['glaze'], cake['text'], cake['weight']))

# show_cake_info(cake01)

cakes = [cake01,cake02]
for cake in cakes:
    show_cake_info(cake)



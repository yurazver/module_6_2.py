class Vehicle:
    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color
    __COLOR_VARIANTS = ['blue', 'candy_red', 'Emerald_Blue', 'black', 'white']
    def get_model(self):

        return print(f'Модель {self.__model}')
    def get_power(self):

        return print(f'Мощность двигателя: {self.__engine_power}')
    def get_color(self):

        return print(f'Цвет: {self.__color}')
    def print_info(self):
        self.get_model()
        self.get_power()
        self.get_color()
        print(f'Владелец:{self.owner}')
    def set_color(self, new_color):
        Flag = False
        for color in self.__COLOR_VARIANTS:
            if new_color.upper() == color.upper():
                Flag = True
        if Flag:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')
class Sedan(Vehicle):

    __PASSENGERS_LIMIT = 5

# Текущие цвета __COLOR_VARIANTS = ['blue', 'candy_red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('CANDY_RED')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
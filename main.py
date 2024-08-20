# list
# range(3,21)
# result = n %
# print(result)

# numbers = (i for i in range(3, 21))
# for number in numbers:
#     if i
#     print(number)


class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        self.go_to()


    def go_to(new_floor):
        floor = int(new_floor)
        floors = list(range(1, floor + 1))
        print(floors)
        if floor > self.number_of_floors or floor < 1:
            print("Такого этажа не существует")


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)

print(h1.name, h1.number_of_floors)
print(h2.name, h2.number_of_floors)








#
# def __del__(self):
#     print(f'{self.name} ушёл')
#
#
# den = Human('Денис',22)
# max = Human('Макс',22)
# del den
# max.birthday()
# input()


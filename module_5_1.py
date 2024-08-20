class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        self.go_to(self)

    def go_to(self, new_floor):
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







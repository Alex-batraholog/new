class House:
    def __init__(self, name, floors):
        self.name = name
        self.number_of_floors = floors

    def go_to(self, new_floor):
        floor = int(new_floor)
        floors = list(range(1, floor + 1))
        print(floors)
        if floor > self.number_of_floors or floor < 1:
            print("Такого этажа не существует")

        # if 1 <= new_floor <= self.number_of_floors:
        #     for floor in range(1, new_floor + 1):
        #         print(floor)
        #     else:
        #         print("Такого этажа не существует")

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)

print(h1.name, h1.number_of_floors)
print(h2.name, h2.number_of_floors)







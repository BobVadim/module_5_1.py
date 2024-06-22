class House:
    def __init__(self, name, number_of_floors, ):
        self.number_of_floors = number_of_floors
        self.name = name

    def go_to(self, new_floor):
        self.new_floor = new_floor
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
        else:
            floor = 1
            new_floor = list(range(floor, self.new_floor + 1))
            print(self.name, *new_floor)


h1 = House('ЖК Эльбрус :', 30,)
h2 = House('Домик в деревне', 2)

h1.go_to(22)
h2.go_to(4)

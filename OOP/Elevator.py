# Задача для начала курса по Flask.

class Elevator:
    def __init__(self,total_floor=5, current_floor=3):
        self.total_floor = total_floor
        self.current_floor = current_floor
    def up(self):
        if self.total_floor > self.current_floor:
            self.current_floor += 1
            print(f'Лифт поднимается на {self.current_floor} этаж')
        else:
            print('Лифт не может подняться выше')
    def down(self):
        if self.current_floor > 1:
            self.current_floor -= 1
            print(f'Лифт опускается на {self.current_floor}')
        else:
            print('Лифт не может опуститься ниже')


elevator = Elevator(7,6)
elevator.up()
elevator.up()
elevator.down()
elevator.down()
elevator.down()

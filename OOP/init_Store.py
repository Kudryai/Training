memory_list = []
class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr
class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume
        if len(memory_list) < MotherBoard.total_mem_slots:
            memory_list.append(self)
class MotherBoard:
    total_mem_slots = 4
    def __init__(self,name, cpu, mem_slots):
        self.name = name
        self.cpu = cpu
        self.mem_slots = mem_slots
    def get_config(self):
        mem_str = "; ".join([f"{x.name} - {x.volume}" for x in mb.mem_slots])
        return [f"Материнская плата: {mb.name}",
            f"Центральный процессор: {mb.cpu.name}, {mb.cpu.fr}",
            f"Слотов памяти: {mb.total_mem_slots}",
            f"Память: {mem_str}"]

cpu = CPU('SuperDruper', 5000)
mem = Memory('Kingstor', 16)
mem2 = Memory('Kingstsaor', 8)
mb = MotherBoard('ZZtor4',cpu,memory_list)
print(mb.get_config())

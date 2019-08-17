class Computer:

    def __init__(self, cpu, ram, gpu):
        self.cpu = cpu
        self.ram = ram
        self.gpu = gpu
        self.CPU = self.CPU()

    def config(self):
        print(self.cpu, self.ram, self.gpu)

    class CPU:
        def __init__(self):
            self.speed = "4 * 3.4 GHz"
            self.model = "Intel i5 3570"
        def config(self):
            print(self.model, self.speed)


C1 = Computer("i5", 8, "HD 7700")

# Outer class
print(C1.cpu)
C1.config()

# Inner class
print(C1.CPU.speed)
C1.CPU.config()

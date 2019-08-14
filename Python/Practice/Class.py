class Computer:
    def __init__(self, CPU, RAM, GPU):
        self.CPU = CPU
        self.RAM = RAM
        self.GPU = GPU
    def config(self):
        print("The CPU is {}, the RAM is {}, the GPU is {}".format(self.CPU, self.RAM, self.GPU))

aliPMPAINT = Computer("Intel Core i5 3570", "8 GB DDR3", "AMD Radeon HD 7700.")
Computer.config(aliPMPAINT)
print(aliPMPAINT.GPU)

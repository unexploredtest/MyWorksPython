class Computer:
    def __init__(self, CPU, RAM, GPU):
        self.CPU = CPU
        self.RAM = RAM
        self.GPU = GPU
    def config(self):
        print(f"The CPU is {self.CPU}, the RAM is {self.RAM}, the GPU is {self.GPU}")

aliPMPAINT = Computer("Intel Core i5 3570", "8 GB DDR3", "AMD Radeon HD 7700.")

Computer.config(aliPMPAINT)
aliPMPAINT.config()
print(aliPMPAINT.GPU)

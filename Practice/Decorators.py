def lol(function):
    def loler():
        print("Lol!")

        function()

        print("Lol!")
    return loler

@lol
def Ahmad():
     print("Ahmad is a very noob boy!")

@lol
def Amir():
    print("Amir is a very noob boy!")

Amir()
Ahmad()

from Information.Name import Name
from Information.Fav import *

Michio_Kaku = Name("Michio Kaku", 70, "Male", "American", "Theoritical Physics")
print(Michio_Kaku.about())
print(pro(Michio_Kaku.name, Michio_Kaku.major))

Mahdi_Sawari = Name("Mahdi Sawari", 50, "Male", "Iranian", "Medican")
print(Mahdi_Sawari.about())
print(pro(Mahdi_Sawari.name, Mahdi_Sawari.major))

Matt_Parker = Name("Matt Parker", 26, "Male", "American", "Pure Mathematics")
print(Matt_Parker.about())
print(noob(Matt_Parker.name, Matt_Parker.major))

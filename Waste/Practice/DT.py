#def pronounce_price(products):
#    for items, prices in products.items():
#        print(f"We have two of {}.")
def pronounce_counter(products):
    h = list(products.keys())
    for i in set(h):
        c = h.count(i)
        print(f"We have {c} {i}.")

Products = {}

while True:
    item = input("Choose the item you want to put on sale:")
    price = float(input("What is the price of this item?"))

    Products[item] = price

    again = input("Do you want to put another item on sale? (y/n)")
    if again == 'y':
        continue
    else:
        break

#pronounce_price(Products)
pronounce_counter(Products)

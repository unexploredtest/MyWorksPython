class A:
    def featureA(self):
        print("Feature A works")

class B(A):
    def featureB(self):
        print("Feature B works")
    # Feature A will also work

class C:
    def featureC(self):
        print("Feature C works")

class D(C,A):
    def featureD(self):
        print("Feature D works")
    # Feature A will also work
    # Feature C will also work

# The commented ones won't work

a = A()
a.featureA()
# a.featureB()
# a.featureC()
# a.featureD()

b = B()
b.featureA()
b.featureB()
# b.featureC()
# b.featureD()

c = C()
# c.featureA()
# c.featureB()
c.featureC()
# c.featureD()

d = D()
d.featureA()
# d.featureB()
d.featureC()
d.featureD()

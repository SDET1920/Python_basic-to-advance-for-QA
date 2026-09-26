#Method Overloading- Two or more method have the same name but different number of parameter or different type of parameter
#both is called method overloading.

# Example-1-- Overloading concept

class Human:
    def sayhello(self,name=None):
        if name is not None:
            print("Hello," +name)
        else:
            print("hello")

h=Human()
h.sayhello("scott")
h.sayhello()

# Example-2-- Calculator operation

class Calculation:
    def add(self, a=0, b=0, c=0):
        print(a+b+c)

obj=Calculation()
obj.add()              ##here no values pass so it will pick a=0,b=0,c=0 then result is 0)
obj.add(10,20)         ## here values passed (a=10, b=20, so result is 30)
obj.add(100,200,300)   ## Here values passed (a=100, b=200, c=300 so result is 600)
## Oops_Inheritance--- One class from child/subclass acquire the properties and methods of another class (parent/superclass).


## Type- Single, multilevel, heirarchy, multiple.

## Write the program.

class A:
    def m1(self):
        print("This  is m1 method from class A")

class B(A):
    def m2(self):
        print("This is m2 method from class B")

obj=B()
obj.m1()
obj.m2()

## Write other program for mathmatical operations

class A:
    x,y=10,20
    def m1(self):
        print(self.x+self.y)

class B(A):
    a,b=70,20
    def m2(self):
        print(self.a-self.b)

obj=B()
obj.m1()
obj.m2()


## Multi level inheritence---to perform math operations (add,sub,multiplication)

class A:
    x,y=11,10
    def m1(self):
        print(self.x+self.y)

class B(A):
    a,b=12,7
    def m2(self):
        print(self.a-self.b)

class C(B):
    i,j=3,2
    def m3(self):
        print(self.i*self.j)

obj=C()
obj.m1()
obj.m2()
obj.m3()

## Heirarchy level inheritance---to perform math operations (add,sub,multiplication,div)


class A:
    x,y=10,20
    def m1(self):
        print(self.x+self.y)

class B(A):
    a,b=20,11
    def m2(self):
        print(self.a-self.b)

class C(A):
    d,e=5,7
    def m3(self):
        print(self.d*self.e)

class D(A):
    i,j=10,2
    def m4(self):
        print(self.i-self.j)

#B, C, and D all inherit from A.
#B, C, and D are sibling classes (they share the same parent).
#An object of D can access methods defined in D and inherited from A.
#It cannot directly access methods that exist only in B or C.

## Error- AttributeError: 'D' object has no attribute 'm2'

obj=B()                 ## Here we need to create seperate object to print the value.
obj.m1()
obj.m2()

obj=C()
obj.m3()

obj=D()
obj.m4()

## Multiple inheritance to perfrom a math operations (add,sub,mul,div)

class A:
    x,y=10,20
    def m1(self):
        print(self.x+self.y)
class B:
    a,b=12,10
    def m2(self):
        print(self.a-self.b)

class C:
    i,j=3,5
    def m3(self):
        print(self.i*self.j)
class D(A,B,C):                            # Here allows a single D object to access methods from both A, B and C.
    c,d=10,2
    def m4(self):
        print(self.c/self.d)

obj=D()
obj.m1()
obj.m2()
obj.m3()
obj.m4()



class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self,a,b):
        self.a+self.b
    def sub(self,a,b):
        self.a-self.b
    def mul(self,a,b):
        self.a*self.b
    def div(self,a,b):
        self.a/self.b
    def display(self):
        print(self.a+self.b)
        print(self.a-self.b)
        print(self.a*self.b)
        print(self.a/self.b)
n1=int(input())
n2=int(input())
num=calculator(n1,n2)
num.display()


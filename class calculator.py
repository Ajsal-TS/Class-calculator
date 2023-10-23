class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def operation(self,c):
        # /* to select which operation to be performed for calculation */
        if c=="add":

            # """to add 2 no"""
            return self.a+self.b 
        elif c=="subtract":

            # """to subtract"""
            return self.a-self.b
        elif c=="multiplication":

            # """multiply 2 no"""
            return self.a*self.b
        elif c=="division":
            
            # """divide 2 no"""
            return self.a/self.b
        else :
            raise Exception("No function as above")
a=int(input("enter no"))
b=int(input("enter second number"))
c=input("enter function")
sum=calculator(a,b)
print(sum.operation(c))
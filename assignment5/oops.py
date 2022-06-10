class pow:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    # def display(self):
        multi=self.a
        for i in range(1,self.b):
            multi=multi*self.a
        print(f"{self.a} with power {self.b} is {multi}")

obj=pow(int(input("enter the digit : ")),int(input("enter the power : ")))

class FourCal:
    def setData(self,first,second):
        self.first = first
        self.second = second
    def sum(self):
        result = self.first+self.second
        return result

    def mul(self):
        result = self.first*self.second
        return result

    def sub(self):
        result = self.first-self.second
        return result

    def div(self):
        result = self.first/self.second
        return result     

a=FourCal()
b=FourCal()

a.setData(10,2)
b.setData(15,5)

print('a.sum():', a.sum())
print('a.mul():', a.mul())
print('a.sub():', a.sub())
print('a.div():', a.div())

print('*'*10)







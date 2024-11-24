class first:
   
    def __init__(self,a=0,b=0,c=0,d=0,e=0):
         self.val1 =a
         self.val2 =b
         self.val3 =c
         self.val4 =d
         self.val5 =e

    def add(self):
        print('addition: ',self.val1+self.val2+self.val3+self.val4+self.val5)

    def sub(self):
          print('subtraction:',self.val1-self.val2-self.val3-self.val4-self.val5)
    
    def multiply(self):
          print('multiplication :',self.val1*self.val2*self.val3*self.val4*self.val5)

    def division(self):
          if 0 in (self.val1,self.val2,self.val3,self.val4,self.val5):
               print('cannot divide by zero')
          else:
               print('division:',self.val1/self.val2/self.val3/self.val4/self.val5)

    def mod(self):
           if 0 in (self.val1,self.val2,self.val3,self.val4,self.val5):
               print('it cant allow modlus by 0')
           else:
               print('modulus:',self.val1%self.val2%self.val3%self.val4%self.val5)

    def min(self):
         print('smallest no:',min(self.val1,self.val2,self.val3,self.val4,self.val5))

    def max(self):
         print('biggest no:',max(self.val1,self.val2,self.val3,self.val4,self.val5))


    def mean(self):
         print('mean:',(self.val1+self.val2+self.val3+self.val4+self.val5)/5)

    def median (self):
         p1 = [12,55,44,56,3]
         n=len(p1)
         p1.sort()
        #if n % 2 ==0:
         #n1 =p1[n//2]
         #n2 =p1[n//2-1]
         #n3 =(n1+n2)/2
        #else:
        #n3 = p1[n//2]

    
    def total_25per(self):
         print('75% of total :',(75*(self.val1+self.val2+self.val3+self.val4+self.val5))/100)
    
    def total_50per(self):
         print('50% of total :',(50*(self.val1+self.val2+self.val3+self.val4+self.val5))/100)
    
    def total_25per(self):
         print('25 of total:',(25*(self.val1+self.val2+self.val3+self.val4+self.val5))/100)

p1=first(12,55,44,56,3)

p1.add()
p1.sub()
p1.multiply()
p1.division()
p1.mod()
p1.min()
p1.max()
p1.mean()
#p1.median()
#p1.mode()
p1.total_25per()
p1.total_50per()
p1.total_25per()



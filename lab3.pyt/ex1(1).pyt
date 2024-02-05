class mystring:
    def getstring(self):
        self.str = input()
    def printstring(self):
        print(self.str.upper())
        
        
pro = mystring()
pro.getstring()
pro.printstring()
import sys
class Email:
    def __init__(self):
        self.fname = None
        self.lname = None
    def A(self,fname,lname):
        self.fname = str(fname).capitalize()
        self.lname = str(lname).capitalize()
    def E(self):
        if self.fname is None and self.lname is None:
            print('\'E\' -> Email : Please Enter Your Firstname & Lastname')
        elif self.fname is None and not(self.lname is None):
            print('\'E\' -> Email : Please Enter Your Firstname')
        elif not(self.fname is None) and self.lname is None:
            print('\'E\' -> Email : Please Enter Your Lastname')
        else:
            print('\'E\' -> Email : ' + str(self.fname).lower() + '.' + str(self.lname).lower() + '@kmitl.ac.th')
    def F(self,fname):
        self.fname = str(fname).capitalize()
    def L(self,lname):
        self.lname = str(lname).capitalize()
    def SF(self):
        if self.fname is None:
            print('\'SF\' -> Firstname : Please Enter Your Firstname')
        else:
            print('\'SF\' -> Firstname : ' + str(self.fname).capitalize())
    def SL(self):
        if self.lname is None:
            print('\'SL\' -> Lastname : Please Enter Your Lastname')
        else:
            print('\'SL\' -> Lastname : ' + str(self.lname).capitalize())
    def SA(self):
        if self.fname is None and self.lname is None:
            print('\'SA\' -> Fullname : Please Enter Your Firstname & Lastname')
        elif self.fname is None and not(self.lname is None):
            print('\'SA\' -> Fullname : Please Enter Your Firstname')
        elif not(self.fname is None) and self.lname is None:
            print('\'SA\' -> Fullname : Please Enter Your Lastname')
        else:
            print('\'SA\' -> Fullname : ' + str(self.fname).capitalize() + ' ' + str(self.lname).capitalize())
    def X(self):
        return sys.exit() 
print("*** Create Email < BY KMITL > ***")
inputt = input("Enter Input : ").split(',')
mail = Email()
for i in inputt:
    if i.startswith('A'):
        mail.A(i.split(sep=' ',maxsplit=2)[1],i.split(sep=' ',maxsplit=2)[2])
    elif i.startswith('E'):
        mail.E()
    elif i.startswith('F'):
        mail.F(i.split(sep=' ',maxsplit=1)[1])
    elif i.startswith('L'):
        mail.L(i.split(sep=' ',maxsplit=1)[1])
    elif i.startswith('SF'):
        mail.SF()
    elif i.startswith('SL'):
        mail.SL()
    elif i.startswith('SA'):
        mail.SA()
    elif i.startswith('X'):
        mail.X()
    else :
        print('\'{asf}\' is Invalid Input !!!'.format(asf=i))
        sys.exit()
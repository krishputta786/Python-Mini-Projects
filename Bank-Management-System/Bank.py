class Bank:
    bname='HDFC'
    loc='USA'
    manager='Mr Stark'
    IFSC='HDFC000198'

    def __init__(self,name,acno,addrs,phn):
        self.name=name
        self.acno=acno
        self.addrs=addrs
        self.phn=phn
        self.bal=0
        self.pin=0

    def home(self):
        while True:
            print('\n','-'*15,'Home Page','-'*15)
            print('1--> Check customer details')
            print('6--> Exit application')

            ch=int(input('Enter the choice: '))
            if ch==1:
                self.cus_det()
            elif ch==6:
                return
    def cus_det(self):
        print('\n','-'*40)
        print(f'Customer name               - {self.name}')
        print(f'Customer phone number     - {self.phn}')
        print(f'Customer account number   - {self.acno}')
        print(f'Customer address            - {self.addrs}')
        print(f'Customer balance            - ${self.bal}')
        print('-'*40,'\n')

c1=Bank('Jyoti',12345676543345,'AP',9632886528)
c2=Bank('Fahad',5862584565552,'HYD',989562344)
c3=Bank('Shivani',87654323456789,'HYD',8456526326)

data=[c1,c2,c3]
def main():
    while True:
        print('\n','-'*15,'WELCOME TO HDFC BANK','-'*15,'\n')   
        ac=int(input('Enter the account number: '))
        for i in data:
            if ac==i.acno:
                i.home()
                break
        else:
            print('Account not found')      
main()







    
    
        

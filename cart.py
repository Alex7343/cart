class Product:
    def __init__(self, name, price):
        self.name=name
        self.price=price

class User:
    def __init__(self, login, balance=0):
        self.login=login
        self.balance=balance

    def __str__(self):
        return f'User {self.login}, balance - {self.balance}'

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance=value

    def deposit(self, a):
        self.__balance=self.__balance+a

    def payment(self, b):
        if b>self.__balance:
            print('Not sufficient funds')
            return False
        else:
            self.__balance=self.__balance-b
            return True

class Cart:
    def __init__(self,User):
        self.user=User
        self.goods={}
        self.__total=0

    def add(self, Product, numbers=1):
        self.goods[Product]=self.goods.setdefault(Product, 0) + numbers
        self.__total+=numbers*Product.price

    def remove(self, Product, numbers=1):
        if numbers >= self.goods[Product]:
             numbers = self.goods[Product]
             self.goods[Product] = self.goods.get(Product, 0) - numbers
             self.__total -= numbers * Product.price

    @property
    def total(self):
        return self.__total

    def order(self):
        if self.user.payment(self.__total):
            print('Ordered successfully')
        else:
            print('Ordered NOT successfully. Please try again')

    def print_check(self):
        print('---Your check---')
        sorted_lst = sorted(self.goods, key=lambda x: x.name)
        for elem in sorted_lst:
            if self.goods[elem] > 0:
                print(f"{elem.name} {elem.price} {self.goods[elem]} {self.goods[elem] * elem.price}")
        print(f'---Total: {self.total}---')


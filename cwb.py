class Coffee:
    total_coffee = 0
    def __init__(self,size,tem):
        self.size = size
        self.tem = tem
        Coffee.total_coffee += 1
    def coffee_out(self):
        return f'您的{self.tem} {self.size}coffee好了'
    @staticmethod
    def summ():
        print(Coffee.total_coffee)
class Latte(Coffee):
    def __init__(self,size,tem,milk):
        super().__init__(size,tem)
        self.milk = milk
    def __str__(self):
        return f'do not print me'
the_4 = Latte('big','cold','full')
print(the_4)
qingyizhiyan

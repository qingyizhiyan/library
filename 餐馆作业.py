class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served= 0
    def describe_restaurant(self):
        print(f"这家餐馆叫{self.name}，菜品类型是{self.type}")
    def set_number_served(self,number):
        self.number_served = number
    @staticmethod
    def open_restaurant():
        print("餐馆正在营业")
class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type,flavors):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = flavors
    def show_icecream(self):
        print(f"冰激凌口味有{','.join(self.flavors)}")
restaurant = Restaurant('Tasty Restaurant','Italian')
Restaurant.describe_restaurant(restaurant)
print(f"在{restaurant.name}里有{restaurant.number_served}人用餐过")
restaurant.set_number_served(20)
print(f"在{restaurant.name}里有{restaurant.number_served}人用餐过")
icecream = IceCreamStand('Sweet Ice Cream','Ice Cream',["Chocolate", "Vanilla", "Strawberry", "Mint"])
icecream.show_icecream()

class Chef:
    def make_chicken(self):
        print("The chef makes chicken")

    def make_salad(self):
        print("The chef makes salad")

    def make_special_dish(self):
        print("The chef makes vadapav")

class ChineseChef(Chef):
    def make_fried_rice(self):
        print("The chef makes fried rice")

    def make_special_dish(self):
        print("The chef makes noodles ")

mychef = Chef()
mychef.make_special_dish()

myChinesechef = ChineseChef()
myChinesechef.make_special_dish()
myChinesechef.make_chicken()

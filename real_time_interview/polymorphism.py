class Zoo:
    def line(self):
        print("King of the forest")

    def monkey(self):
        print("eat banana")


class Forest:
    def line(self):
        print("Line have four leds")

    def monkey(self):
        print("not eat non_veg")


obj = Forest()
obj1 = Zoo()
obj.line()
obj.monkey()
obj1.line()
obj1.monkey()

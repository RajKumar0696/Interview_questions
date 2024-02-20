string = "1234"
print(string.title())
print(string.capitalize())
print(string.strip())
print(string.isspace())
print(string.isalnum())
print(string.isidentifier())
print(string.find("2"))
print(string.swapcase())

a = 20
b = 30
class maths:
    a= 10
    b = 20
    def kuttal(self):
        a = 40
        b = 50
        print(a+b)
        print(self.a+self.b)
        print(globals()['a']+globals()['b'])
        print(globals()['a'] + globals()['b'])




mc = maths()
mc.kuttal()
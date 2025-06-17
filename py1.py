"""

def myfunc():
    x = 100;
    print(x)
myfunc()

i = 0

while i < 10:
    print(i)
    i = i + 1

for i in range(2, 7, 2):
    print(i)


st = "Hello World!"

ch = ""

for i in st:
    ch = i + ch

print(ch)

print((type(print)))

"""

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 4)
v2 = Vector(5, -1)
v3 = Vector(2, 7)
print(v1 + v2 + v3)  # Output: Vector(7, 3)





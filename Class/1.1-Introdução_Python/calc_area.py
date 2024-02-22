PI = 3.14

def square(side):
    """Calcule a a rea do quadrado"""
    return side * side

def rectangle(length, width):
    """Cacula area do retângulo"""
    return length * width

def circle(radius):
    """Calcula area do circulo"""
    return PI * radius * radius

# ...


if __name__ == "__main__":
    print("Área do quadrado:", square(10))
    print("Área do retângulo:", rectangle(2, 2))
    print("Área do círculo:", circle(3))
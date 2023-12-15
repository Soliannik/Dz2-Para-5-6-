import colorama
print(dir(colorama))
print(type(colorama))
print(hasattr(colorama))
print(getattr(colorama))
print(callable(colorama))
print(issubclass(colorama))

with open('get.txt', 'w')as file:
    file.write(str(type(colorama))+ '\n')
    file.write(str(hasattr(colorama)) + '\n')
    file.write(str(hasattr(colorama)) + '\n')
    file.write(str(hasattr(colorama)) + '\n')
    file.write(str(callable(colorama)) + '\n')
    file.write(str(callable(colorama)) + '\n')
    file.write(str(dir(colorama)) + '\n')


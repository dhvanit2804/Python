a = 89 # This is a global variable

def fun():
    # global a
    a = 3 # This is a local variable
    print(a)

fun()
print(a)
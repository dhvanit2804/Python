'''Can you change the self-parameter inside a class to something else (say 
“harry”). Try changing self to “slf” or “harry” and see the effects.'''

class Demo:
    def __init__(harry, name):   # using "harry" instead of "self"
        harry.name = name
    
    def show(slf):              # using "slf" instead of "self"
        print(f"Name is {slf.name}")

obj = Demo("Dhvanit")
obj.show()
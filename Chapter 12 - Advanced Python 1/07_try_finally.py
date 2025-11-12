'What is finally in python ?'
'Python offers a ‘finally’ clause which ensures execution of a piece of code inspective of the exception. '

def main():
    try:
        a = int(input("Enter a number: "))
        print(a)
        return

    except Exception as e:
        print(e)
        return

    finally:
        print("Hey i am inside finally")

main()
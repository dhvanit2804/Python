'What is Match Case in Python ?'
'# Match Case is a new feature introduced in Python 3.10.'
'# It is used for pattern matching, similar to switch-case statements in other programming languages.'

def http_status(status: int) -> str: # This is Use Of Type Defination
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status"

print(http_status(200))
print(http_status(404))
print(http_status(123))
print(http_status(500))
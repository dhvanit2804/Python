'append is a mode that allows you to add content to the end of a file without overwriting the existing content.'

st = "Hey Harry you are amazing"

f = open("myfile.txt", "a")

f.write(st)

f.close()
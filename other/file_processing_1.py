# "r"---> open file for reading
# "w"---> open file for writing. Creates a new file if it does not exist or truncates the file if it exist
# "a"---> open for appending at the end of the file without truncating it. Creates a new file if it does not exist.
# "b"---> open in binary mode.
# "+"---> open a file for updating(reading and writig)

#with open("sample1.txt", 'a') as f:
#    f.write("hello world")

#with open("sample1.txt", "w+") as f:
#    f.write("my first file\n")
#    f.write("this file\n\n")
#    f.write("contains 4 lines\n")
#    print("hi i am ok", file= f)

with open('sample1.txt', "r") as f:
    d = f.read(3)
    s = f.read()
    a = f.readlines()
    z = s.upper()
    print(d)
    print(s)
    print(a)
    print(z)
    
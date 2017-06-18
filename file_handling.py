f = open("LICENSE", 'r')
content = f.read()
print(content)  # Will read the while file at once
f.readlines()  # Will try to read file but it's empty
f.seek(0)  # It's empty because the carriage is at the end. Set it to beginning
content = f.readlines()  # read file at create a list out of lines
content=[i.rstring('\n') for i in content]
f.close()  # close the file, so that other programs can access it

f = open('example', 'w')
f.write("line 1")
f.close()

# Yeah. Pretty much that's it.
# you open() a file with either r, w, or a
# you file.write() to it
# or file.read() to read whole thing or file.readlines() to read line by line
# and remember to file.close() afterwards to let the resources be used by other programs

# Also there is WITH statement
with open('example', 'a+') as f:
    f.seek(0)
    content=f.read()
    f.write('\nnext line')

# There. With statement automatically closes the file once it's done.

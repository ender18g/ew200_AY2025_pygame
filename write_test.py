my_string = "I love pygame.\n It is my favorite python library.\n"

# make a file
with open('text_file.txt','a') as f:
    f.write(my_string)
    

# read the file
with open('text_file.txt','r') as f:
    line_list = []
    for line in f:
        line_list.append(line.strip())


# read the file
with open('text_file.txt','r') as f:
    lines = f.readlines()

lines = [l.strip() for l in lines ]
print(lines)





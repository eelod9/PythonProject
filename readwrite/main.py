names = []
with open("./readwrite/new.txt") as file:
    names = file.read().split("\n")

def create_letters(name,content):
    with open(f"./readwrite/letter_{name}.txt", 'w') as file:
        file.write(content)
    
for name in names:
    with open("./readwrite/my_file.txt",'r') as file:
        contents = file.read()
        print(name)
        temp = contents.replace("[name]",name)
        create_letters(name,temp)




'''    
with open("readwrite/my_file.txt",'a') as file:
    file.write("\nHello")

with open("readwrite/new.txt",'w') as file:
    file.write("\nHello")

'''
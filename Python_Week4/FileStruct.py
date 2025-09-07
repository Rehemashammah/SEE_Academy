#print("File Structure")

# x = 120
# y = 200
# z = 300
# def add(x,y,z):
#     return x + y + z
# print(add(x,y,z))

with open("readme.md", "r", encoding="utf-8", errors="ignore") as file:
    print(file.read())

with open("readme.md", "a", encoding="utf-8", errors="ignore") as file:
    file.write("\n# Welcome to PLP")
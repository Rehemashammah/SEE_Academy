try:
    with open("readme.txt", "r") as file:
        data = file.read()
except FileNotFoundError:
        print("File not found. Please check the file path.")
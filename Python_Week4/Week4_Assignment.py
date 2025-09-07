# File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.
# Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.

# Ask user for a filename
filename = input("Enter the filename to read: ")

try:
    #Attempt to open and read the file
    with open(filename, "r") as infile:
        content = infile.read()

    # Modify the content(Eg: convert to uppercase)
    modified_content = content.upper()

    #Write the modified content to a new file
    new_filename = "modified_" + filename
    with open(new_filename, "w") as outfile:
        outfile.write(modified_content)

    print(f"Modified file saved as:", new_filename)

except FileNotFoundError:
    print("Error: The file you entered does not exist.")
except PermissionError:
    print("Error: You do not have permission to read this file.")
except Exception as e:
    print(f"An unexpected error occurred:", e)
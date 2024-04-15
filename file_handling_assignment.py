with open("my_text_file.txt", "w") as file:
    file.write("hellow PLP Academy\n")
    file.write("2024-15-04\n")
    file.write("2024.15.04\n")

try:
    with open("my_text_file.txt" , "r") as file:
        content= file.read()
        print("content within the file:")
        print(content)

except FileNotFoundError:
    print("file not found")

try:
    with open("my_text_file.txt" , "a") as file:
        file.write("adding another line4 here\n")
        file.write("adding another line5 again\n")
        file.write("adding the last line6 here\n")
        print("*******file appending is done*******")

except PermissionError:
    print("permission not granted file the file to appending")

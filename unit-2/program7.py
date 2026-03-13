with open("source.txt", "r") as src, open("copy.txt", "w") as dest:
    dest.write(src.read())
print("File copied successfully.")

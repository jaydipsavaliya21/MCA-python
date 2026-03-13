with open("sample.txt", "r") as f:
    content = f.read()
    print("Content:\n", content)
    words = content.split()
    print("Word count:", len(words))

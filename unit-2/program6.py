with open("numbers.txt", "r") as f:
    numbers = list(map(int, f.read().split()))
    print("Total:", sum(numbers))
    print("Max:", max(numbers))
    print("Min:", min(numbers))

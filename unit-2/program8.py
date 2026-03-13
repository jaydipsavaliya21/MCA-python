with open("marks.txt", "r") as f:
    for line in f:
        data = line.strip().split(",")
        roll, name = data[0], data[1]
        marks = list(map(int, data[2:]))
        total = sum(marks)
        percent = total / len(marks)
        grade = "A" if percent >= 75 else "B" if percent >= 60 else "C"
        print(f"{roll} | {name} | Total: {total} | %: {percent:.2f} | Grade: {grade}")

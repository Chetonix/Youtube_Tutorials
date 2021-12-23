line = ""

for i in range(0, 8):
    line = ""
    for j in range(0, 8):
        if (i + j) % 2 == 0:
            line = "◻" + line
        else:
            line = "◼" + line
    print(line)


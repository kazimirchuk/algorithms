# Uses python3

def edit_distance(str1, str2):
    value = []
    for i in range(0, len(str1) + 1):
        row = []
        for j in range(0, len(str2) + 1):
            row.append(0)
        value.append(row)

    for k in range(0, len(str1) + 1):
        value[k][0] = k

    for m in range(0, len(str2) + 1):
        value[0][m] = m

    for p in range(1, len(str2) + 1):
        for q in range(1, len(str1) + 1):
            if str1[q - 1] == str2[p - 1]:
                value[q][p] = min([value[q][p - 1] + 1, value[q - 1][p] + 1, value[q - 1][p - 1]])
            else:
                value[q][p] = min([value[q][p - 1] + 1, value[q - 1][p] + 1, value[q - 1][p - 1] + 1])

    return value[len(str1)][len(str2)]

if __name__ == "__main__":
    print(edit_distance(input(), input()))

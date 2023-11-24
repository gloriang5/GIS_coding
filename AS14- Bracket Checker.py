def count_brakcets(s):
    rb = sb = cb = 0

    for char in s:
        if char == "(" or char == ")":
            rb += 1

        elif char == "[" or char == "]":
            sb += 1
        elif char == "{" or char == "}":
            cb += 1

    return f"There are {rb} brackets, {sb} square brakcet, {cb} curly braket."
string = str(input("Enter a phrase:\n"))
print(count_brakcets(string))



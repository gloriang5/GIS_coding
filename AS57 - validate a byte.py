def parity_check(b):
    sum = 0
    for i in b:
        if i == "1":
            sum += 1
    if sum % 2 != 0:
        parity_bit = 1
    else:
        parity_bit = 0

    return f"the even parity bit is {parity_bit}"

byte = str(input("Enter a byte to check for even parity check:\n"))
print(parity_check(byte))
def fill(string, length, character):
    if len(string) < length:
        string = character * (length - len(string)) + string
    return string


def decimalToBinary(n):
    return bin(n).replace("0b", "")


if __name__ == '__main__':
    ui = int(input("Enter a Decimal number: "))
    binary = decimalToBinary(abs(ui))
    if ui >= 0:
        print("The Binary equivalent of {} is {}".format(ui, fill(binary, 8, "0")))
    else:
        print("The Binary equivalent of {} is {}".format(ui, fill(binary, 8, "1")))

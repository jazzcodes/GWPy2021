def find_fac(num):
    if num == 1:
        result = 1
        return result
    else:
        result = num * find_fac(num - 1)
        return result


def main():
    num = int(input("Enter the number: "))
    result = find_fac(num)
    print("Factorial is: ", result )


if __name__ == "__main__":
    main()
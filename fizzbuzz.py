for i in range(21):
    if i % 3 == 0 or i % 5 == 0:
        str = ""
        if i % 3 == 0: str += "Fizz"
        if i % 5 == 0: str += "Buzz"
        print(str)
    else:
        print(i)
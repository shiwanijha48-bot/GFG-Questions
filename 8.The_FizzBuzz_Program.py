def solve(a):
    if a % 15 == 0:
        print("FizzBuzz", end="")
    elif a % 3 == 0:
        print("Fizz", end="")
    elif a % 5 == 0:
        print("Buzz", end="")
    else:
        print(a, end="")
a = int(input())
solve(a)

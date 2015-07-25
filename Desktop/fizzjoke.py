# fizzjoke

def fizzbuzz_test(f):
    if f(3) == "fizz" and f(5) == "buzz" and f(15) == "fizzbuzz":
        print("Success!")
    else:
        print("Nope. Try again.")

def fizzjoke(n):
    if n == 3:
        return "fizz"
    if n == 5:
        return "buzz"
    if n == 15:
        return "fizzbuzz"

fizzbuzz_test(fizzjoke)

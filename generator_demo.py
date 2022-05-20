# def simpleGeneratorFun():
#     yield 1
#     yield 2
#     yield 3
#
# for value in simpleGeneratorFun():
#     print(value)


# def simpleGeneratorFun():
#     yield 1
#     yield 2
#     yield 3
#
#
# if __name__ == '__main__':
#
#     x = simpleGeneratorFun()
#     print(x.__next__())
#     print(x.__next__())
#     print(x.__next__())

def fib(limit):
    # Initialize first two Fibonacci Numbers
    a, b = 0, 1

    # One by one yield next Fibonacci Number
    while a < limit:
        yield a
        a, b = b, a + b


# Create a generator object
x = fib(5)

# Iterating over the generator object using next
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())

# Iterating over the generator object using for

print("\nUsing for in loop")
for i in fib(5):
    print(i)


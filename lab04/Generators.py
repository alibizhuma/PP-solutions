#1
def generate_squares(N):
    for i in range(1, N+1):
        yield i ** 2

N = 5
for square in generate_squares(N):
    print(square)

#2
def generate_even_numbers(n):
    for i in range(0, n+1, 2):
        yield i

def he():
    n_input = input("number: ")
    if not n_input.isdigit():
        print("need correct")
        return
    n = int(n_input)
    if n < 0:
        print("more than")
        return
    even_numbers = list(generate_even_numbers(n))
    print("even number from 0 to {}: {}".format(n, ', '.join(map(str, even_numbers))))

he()

#3
def divisible_by_three_and_four(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = 50
generator = divisible_by_three_and_four(n)
print("Numbers divisible by both 3 and 4 between 0 and {}: {}".format(n, list(generator)))

#4
def squares(a, b):
    for num in range(a, b+1):
        yield num ** 2

start = 1
end = 5

print(f"Squares from {start} to {end}:")
for square in squares(start, end):
    print(square)
    
#5
def countdown(n):
    while n >= 0:
        yield n
        n -= 1
n = 5
for num in countdown(n):
    print(num)
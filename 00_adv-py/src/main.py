"""Advance Python Concepts."""


# Decorator
def sub(func):
    """A simple decorator that adds some behavior before and after a function is called."""

    def wrapper(*args, **kwargs):
        """The wrapper function that implements the additional behavior."""
        print("------------------------------")
        main_result = func(*args, **kwargs)
        print("------------------------------")
        return main_result

    return wrapper


@sub
def my_sub(*args):
    """Prints a greeting."""
    sub_result = 0
    for i in args:
        sub_result = i + i
    print(sub_result)


@sub
def my_info(**kwargs):
    """Prints a greeting."""

    print(kwargs)


my_sub(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
my_info(
    name="Adu Bhai", age=30, university="Dhaka University", political_party="Chatro Dol"
)


# Python Comprehensions syntex: [expression for item in iterable if condition].
# | Type      | Syntax                 | Produces    |
# | --------- | ---------------------- | ----------- |
# | List      | `[x for x in data]`    | `list`      |
# | Set       | `{x for x in data}`    | `set`       |
# | Dict      | `{k: v for x in data}` | `dict`      |
# | Generator | `(x for x in data)`    | `generator` |


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = [n * n for n in numbers]
print(squares)
even = [n for n in numbers if n % 2 == 0]
print(even)
squares_even = [n * n for n in numbers if n % 2 == 0]
print(squares_even)
unique = {n * n for n in numbers}
print(unique)
squares = {n: n * n for n in numbers}
print(squares)

matrix = [
    [1, 2],
    [3, 4],
    [5, 6],
]

flat = [n for row in matrix for n in row]
print(flat)

result = [(x, y) for x in range(10) for y in range(10)]
print(result)

squares = (n * n for n in range(1, 100))
print(list(squares))

add = sub(lambda *args: print(sum(args)))
add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)

names = ["Alice", "Bob", "Charlie"]
ages = [25, 22, 18]
cities = ["Dhaka", "Rajshahi", "Chittagong"]

for name, age, city in zip(names, ages, cities, strict=True):
    print(name, age, city)

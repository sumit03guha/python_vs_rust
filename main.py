import timeit

import fibonacci


def fib_py(num: int) -> int:
    """
    Recursively calculate the nth Fibonacci number in Python.

    Args:
    num (int): The position in the Fibonacci sequence.

    Returns:
    int: The nth Fibonacci number.
    """

    if num <= 1:
        return num
    return fib_py(num - 1) + fib_py(num - 2)


def main():
    """
    Main function to benchmark the performance of calculating the 10th Fibonacci
    number using both Python and Rust implementations.
    """

    # Time the Python implementation of the Fibonacci function
    time_fib_py = timeit.timeit(stmt=lambda: fib_py(10), number=100000)
    # Time the Rust implementation of the Fibonacci function
    time_fib_rs = timeit.timeit(stmt=lambda: fibonacci.fib_rs(10), number=100000)

    print(f"Time taken by the python code : {time_fib_py}")
    print(f"Time taken by the rust code : {time_fib_rs}")


if __name__ == "__main__":
    main()

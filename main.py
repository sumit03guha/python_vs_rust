import timeit

import rust_implementations


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


def tower_of_hanoi_py(n: int, source, destination, auxillary):
    if n == 1:
        print(f"Move {n} from {source} to {destination}")
    else:
        tower_of_hanoi_py(
            n - 1, source=source, destination=auxillary, auxillary=destination
        )
        print(f"Move {n} from {source} to {destination}")
        tower_of_hanoi_py(
            n - 1, source=auxillary, destination=destination, auxillary=source
        )


def main():
    """
    Main function to benchmark the performance of calculating the 10th Fibonacci
    number using both Python and Rust implementations.
    """

    # Time the Python implementation of the Fibonacci function
    time_fib_py = timeit.timeit(stmt=lambda: fib_py(10), number=100000)
    # Time the Rust implementation of the Fibonacci function
    time_fib_rs = timeit.timeit(
        stmt=lambda: rust_implementations.fib_rs(10), number=100000
    )
    time_hanoi_py = timeit.timeit(stmt=lambda: tower_of_hanoi_py(20))

    print(f"Fibonacci : Time taken by the python code : {time_fib_py}")
    print(f"Fibonacci : Time taken by the rust code : {time_fib_rs}")
    print(f"Tower of Hanoi : Time taken by the python code : {time_hanoi_py}")


if __name__ == "__main__":
    # main()
    tower_of_hanoi_py(20, "source", "destination", "auxillary")

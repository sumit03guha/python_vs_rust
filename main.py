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


def tower_of_hanoi_py(n: int, source: str, destination: str, auxiliary: str):
    """
    Solve the Tower of Hanoi problem recursively in Python.

    Args:
        n (int): Number of disks.
        source (str): The identifier for the source rod.
        destination (str): The identifier for the destination rod.
        auxiliary (str): The identifier for the auxiliary rod.

    This function does not return any values but can be modified to print moves.
    """

    if n == 1:
        # Uncomment the line below to print the move when executing.
        # print(f"Move disk {n} from {source} to {destination}")
        pass
    else:
        tower_of_hanoi_py(n - 1, source, auxiliary, destination)
        # Uncomment the line below to print the move when executing.
        # print(f"Move disk {n} from {source} to {destination}")
        tower_of_hanoi_py(n - 1, auxiliary, destination, source)


def main():
    """
    Main function to benchmark the performance of calculating the 10th Fibonacci
    number and solving the Tower of Hanoi for 15 disks using both Python and Rust
    implementations.
    """

    # Benchmarking Fibonacci calculation
    time_fib_py = timeit.timeit(lambda: fib_py(10), number=100000)
    time_fib_rs = timeit.timeit(lambda: rust_implementations.fib_rs(10), number=100000)

    # Benchmarking Tower of Hanoi
    time_hanoi_py = timeit.timeit(
        lambda: tower_of_hanoi_py(15, "source", "destination", "auxiliary"),
        number=10000,
    )
    time_hanoi_rs = timeit.timeit(
        lambda: rust_implementations.tower_of_hanoi_rs(
            15, "source", "destination", "auxiliary"
        ),
        number=10000,
    )

    # Output the benchmark results
    print(f"Fibonacci : Time taken by the Python code : {time_fib_py}")
    print(f"Fibonacci : Time taken by the Rust code : {time_fib_rs}")
    print(f"Tower of Hanoi : Time taken by the Python code : {time_hanoi_py}")
    print(f"Tower of Hanoi : Time taken by the Rust code : {time_hanoi_rs}")


if __name__ == "__main__":
    main()

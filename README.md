# Python vs. Rust Performance Comparison

## Overview

This repository hosts a performance comparison between Python and Rust implementations of various algorithms. The initial comparison covers the Fibonacci sequence. The aim is to provide an educational resource to see how the same algorithms can be executed in Python and Rust, highlighting the execution time and performance benefits.

## Project Structure

- `fib.py`: Python script to run and time the Fibonacci function implemented in Python and Rust.
- `fibonacci/`: Rust project directory.
  - `src/`: Contains Rust source files with the implementation of the algorithms.
  - `Cargo.toml`: Configuration file for the Rust project.
  - `pyproject.toml`: Python project configuration for building Rust extensions.

## Prerequisites

- Python 3.8+
- Rust 1.41+
- [maturin](https://github.com/PyO3/maturin) (Install via pip)

## Installation

### Setting Up the Rust Environment

Ensure Rust is installed on your system. If Rust is not installed, you can install it from [the official site](https://www.rust-lang.org/tools/install).

### Setting Up Python and Dependencies

It is recommended to use a virtual environment:

```zsh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Install the required Python packages:

```zsh
pip install maturin
```

### Building the Extension

Navigate to the `fibonacci` directory and run:

```zsh
maturin develop
```

This command builds the Rust code as a Python module accessible in your Python environment.

## Usage

Run the Python script `fib.py` to see the performance comparison:

```zsh
python fib.py
```

The script outputs the time taken by both the Python and Rust implementations to execute the Fibonacci sequence.

## Performance Results

The initial results for calculating the 10th Fibonacci number are as follows:

- Python implementation: `0.562 seconds`
- Rust implementation: `0.112 seconds`

These results demonstrate that the Rust implementation is approximately 5 times faster than the Python implementation. This significant performance difference highlights the efficiency of Rust in computational tasks compared to Python.

## Contributing

Contributions are welcome! If you have an idea for a new algorithm comparison or improvements to existing ones, feel free to fork the repository and submit a pull request.

## Future Work

This project will be extended to include more algorithms and potentially other types of performance comparisons (e.g., memory usage).

## Acknowledgments

This project was inspired by the desire to explore performance characteristics between different programming languages, specifically Python and Rust.

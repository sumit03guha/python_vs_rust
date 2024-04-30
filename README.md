# Python vs. Rust Performance Comparison

## Overview

This repository hosts a performance comparison between Python and Rust implementations of various algorithms. The initial comparisons cover the Fibonacci sequence and the Tower of Hanoi. The aim is to provide an educational resource to see how the same algorithms can be executed in Python and Rust, highlighting the execution time and performance benefits.

## Project Structure

- `main.py`: Python script to run and time algorithms implemented in Python and Rust.
- `rust_implementations/`: Rust project directory.
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
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
```

Install the required Python packages:

```zsh
pip install maturin
```

### Building the Extension

Navigate to the `rust_implementations` directory and run:

```zsh
maturin develop --release
```

This command builds the Rust code as a Python module accessible in your Python environment.

## Usage

Run the `main.py` script to see the performance comparison:

```zsh
python main.py
```

The script outputs the time taken by both the Python and Rust implementations to execute the Fibonacci sequence and solve the Tower of Hanoi.

## Performance Results

### Fibonacci Sequence

- **Python implementation**: `0.615 seconds`
- **Rust implementation**: `0.035 seconds`

### Tower of Hanoi

- **Python implementation**: `11.724 seconds`
- **Rust implementation**: `0.355 seconds`

These results demonstrate that Rust implementations are significantly faster than their Python counterparts for both algorithms. The Rust implementation of the Fibonacci sequence is approximately 17 times faster, and for the Tower of Hanoi, it is about 33 times faster. This significant performance difference highlights the efficiency of Rust in computational tasks compared to Python.

## Contributing

Contributions are welcome! If you have an idea for a new algorithm comparison or improvements to existing ones, feel free to fork the repository and submit a pull request.

## Future Work

This project will be extended to include more algorithms and potentially other types of performance comparisons (e.g., memory usage, multi-threading).

## Acknowledgments

This project was inspired by the desire to explore performance characteristics between different programming languages, specifically Python and Rust.

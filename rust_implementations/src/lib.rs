use pyo3::prelude::*;

/// Calculates the nth Fibonacci number recursively.
/// This function demonstrates how Rust can be used to implement functions
/// that can be called from Python.
///
/// # Arguments
/// * `num` - A usize that specifies the position in the Fibonacci sequence.
///
/// # Returns
/// * `PyResult<usize>` - The nth Fibonacci number, wrapped in a PyResult to handle potential errors.
#[pyfunction]
fn fib_rs(num: usize) -> PyResult<usize> {
    if num <= 1 {
        // Base case: if num is 0 or 1, return it directly.
        return Ok(num);
    } else {
        // Recursive case: sum the two preceding Fibonacci numbers, handling recursion errors with `?`.
        return Ok(fib_rs(num - 1)? + fib_rs(num - 2)?);
    }
}

/// Solves the Tower of Hanoi puzzle for 'num' disks.
/// This function is a demonstration of using Rust to perform complex recursive operations,
/// and it can also be called from Python, though it does not perform any I/O operations.
///
/// # Arguments
/// * `num` - The number of disks.
/// * `source` - A string slice representing the source rod.
/// * `destination` - A string slice representing the destination rod.
/// * `auxillary` - A string slice representing the auxiliary rod.
#[pyfunction]
fn tower_of_hanoi_rs(num: usize, source: &str, destination: &str, auxillary: &str) {
    if num == 1 {
        // Base case: Only one disk to move directly from source to destination.
        // println!("Move disk 1 from {source} to {destination}");
    } else {
        // Recursive case: Move n-1 disks to the auxiliary rod, move the nth disk to the destination,
        // and then move the n-1 disks from auxiliary to destination.
        tower_of_hanoi_rs(num-1, source, auxillary, destination);
        // println!("Move disk {num} from {source} to {destination}");
        tower_of_hanoi_rs(num-1, auxillary, destination, source);
    }
}

/// A Python module implemented in Rust using PyO3.
/// This module initializes the Python functions `fib_rs` and `tower_of_hanoi_rs` so they
/// can be called from Python scripts.
///
/// # Arguments
/// * `_py` - A handle to the Python interpreter, which is not used directly.
/// * `m` - The Python module to which functions are added.
///
/// # Returns
/// * `PyResult<()>` - Indicates whether the module was successfully initialized.
#[pymodule]
fn rust_implementations(_py: Python, m: &PyModule) -> PyResult<()> {
    // Add the Fibonacci and Tower of Hanoi functions to the module.
    m.add_function(wrap_pyfunction!(fib_rs, m)?)?;
    m.add_function(wrap_pyfunction!(tower_of_hanoi_rs, m)?)?;
    Ok(())
}

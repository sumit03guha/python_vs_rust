use pyo3::prelude::*;

/// Calculates the nth Fibonacci number recursively.
/// This function showcases how to write Python functions in Rust.
///
/// # Arguments
/// * `num` - A usize that specifies the position in the Fibonacci sequence.
///
/// # Returns
/// * `PyResult<usize>` - The nth Fibonacci number wrapped in a Python result type to handle Python exceptions.
#[pyfunction]
fn fib_rs(num: usize) -> PyResult<usize> {
    if num <= 1 {
        // Base case: return the number itself if it is 0 or 1.
        return Ok(num);
    } else {
        // Recursive case: compute the sum of the two preceding numbers.
        // The '?' operator is used to return any errors encountered in the recursion.
        return Ok(fib_rs(num - 1)? + fib_rs(num - 2)?);
    }
}

/// A Python module implemented in Rust using PyO3.
/// This module adds the `fib_rs` function to a Python module so it can be called from Python.
///
/// # Arguments
/// * `_py` - A Python interpreter instance (not used directly here).
/// * `m` - The Python module to which the Rust function will be added.
///
/// # Returns
/// * `PyResult<()>` - Indicates successful module initialization or an error during setup.
#[pymodule]
fn rust_implementations(_py: Python, m: &PyModule) -> PyResult<()> {
    // Add the `fib_rs` function to the module.
    m.add_function(wrap_pyfunction!(fib_rs, m)?)?;
    Ok(())
}

import random
import time
import matplotlib.pyplot as plt

def generate_array(n, max_value=160, seed=42):
    """Generate an array of n random integers between 1 and max_value."""
    random.seed(seed)
    return [random.randint(1, max_value) for _ in range(n)]

def is_unique(array):
    """Check if all elements in the array are unique."""
    return len(array) == len(set(array))

def measure_time(func, *args):
    """Measure the execution time of a function with better precision."""
    start_time = time.perf_counter()  # Using a higher precision timer
    func(*args)
    end_time = time.perf_counter()
    return end_time - start_time

def main():
    # Define different values for n
    ns = [100, 150, 200, 250, 300, 350, 400, 500]
    max_value = 160
    seed = 42

    # Lists to store execution times
    worst_case_times = []
    average_case_times = []

    for n in ns:
        # Generate random array for the given size n
        array = generate_array(n, max_value, seed)

        # Create the worst-case scenario: all elements are identical
        worst_case_array = [1] * n

        # Measure time for worst case
        worst_case_time = measure_time(is_unique, worst_case_array)

        # Measure time for average case
        average_case_time = measure_time(is_unique, array)

        # Store the results
        worst_case_times.append(worst_case_time)
        average_case_times.append(average_case_time)

        # Print the execution times for each case with more precision
        print(f"n = {n}, Worst Case Time = {worst_case_time:.10f}s, Average Case Time = {average_case_time:.10f}s")

    # Plot the graph for both cases
    plt.figure(figsize=(10, 6))
    plt.plot(ns, worst_case_times, marker='o', label='Worst Case', color='red')
    plt.plot(ns, average_case_times, marker='s', label='Average Case', color='blue')
    plt.title('Performance Comparison: Worst Case vs Average Case')
    plt.xlabel('Array Size (n)')
    plt.ylabel('Execution Time (seconds)')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
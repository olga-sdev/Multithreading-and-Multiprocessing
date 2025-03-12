import multiprocessing
import time


def add_numbers(process_name):
    start_time = time.time()  # Start the timer
    list_of_nums = []
    for i in range(700000):
        list_of_nums.append(i)
    end_time = time.time()  # End the timer
    print(f"{process_name} completed in {end_time - start_time:.3f} seconds with result: {list_of_nums[-1]}")


if __name__ == "__main__":
    # Create processes
    process1 = multiprocessing.Process(target=add_numbers, args=("Process 1",))
    process2 = multiprocessing.Process(target=add_numbers, args=("Process 2",))
    process3 = multiprocessing.Process(target=add_numbers, args=("Process 3",))

    # Start processes
    process1.start()
    process2.start()
    process3.start()

    # Wait for processes to finish
    process1.join()
    process2.join()
    process3.join()

    print("Done with multiprocessing!")


"""
Output:

Process 1 completed in 0.070 seconds with result: 699999
Process 2 completed in 0.077 seconds with result: 699999
Process 3 completed in 0.078 seconds with result: 699999
Done with multiprocessing!
"""

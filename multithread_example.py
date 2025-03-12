import threading
import time


def add_numbers(thread_name):
    start_time = time.time()  # Start the timer
    list_of_mums = []
    for i in range(700000):
        list_of_mums.append(i)
    end_time = time.time()  # End the timer
    print(f"{thread_name} completed in {end_time - start_time:.3f} seconds with results: {list_of_mums[-1]}")


# Create threads
thread1 = threading.Thread(target=add_numbers, args=("Thread 1",))
thread2 = threading.Thread(target=add_numbers, args=("Thread 2",))
thread3 = threading.Thread(target=add_numbers, args=("Thread 3",))

# Start threads
thread1.start()
thread2.start()
thread3.start()

# Wait for threads to finish
thread1.join()
thread2.join()
thread3.join()

print("Done with multithreading!")


"""
Output:

Thread 1 completed in 0.126 seconds with results: 699999
Thread 2 completed in 0.142 seconds with results: 699999
Thread 3 completed in 0.097 seconds with results: 699999
Done with multithreading!
"""

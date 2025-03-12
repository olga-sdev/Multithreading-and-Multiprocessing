_Multithreading_
* Involves multiple threads within a single process, sharing the same memory space. 
* Perform multiple tasks simultaneously within a single application. 
* Each thread can run its own task, making the application more efficient, especially when dealing with I/O-bound tasks.

_Multiprocessing_
* Involves multiple processes, each with its own memory space. 
* Perform multiple CPU cores, allowing for true parallelism.
* Each process runs independently, which is particularly useful for CPU-bound tasks. 


Multithreading  -> multiple people (threads)   working together in the same room (shared memory). 
Multiprocessing -> multiple people (processes) working in their own offices      (separate memory spaces).

	
| Multithreading                                 | Multiprocessing                                                  |
|------------------------------------------------|------------------------------------------------------------------|
| Shared memory space                            | Separate memory space                                            | 
| Simple communication, through shared variables | Complex communication, through inter-process communication (IPC) | 
| Great for I/O-bound tasks                      | Great for CPU-bound tasks                                        | 
| Concurrent execution (context switching)       | True parallelism (multiple CPU cores)                            |


_I/O-bound task_

I/O-bound task is a type of operation that is primarily limited by the speed of the input/output (I/O) systems, such as:
disk storage, network, or other peripheral devices, rather than the processing power of the CPU. 
These tasks involve a significant amount of reading from or writing to external resources, 
and their performance depends on how quickly data can be transferred to and from these resources.

In I/O-bound tasks, the CPU often spends a lot of time waiting for data to be read from or written to storage or other devices, 
rather than performing calculations. 
Because of this, improving the performance of I/O-bound tasks usually involves optimizing the I/O operations rather than relying on a faster CPU.

*_Examples of I/O-bound tasks include_*:

_File System Operations_:

* Reading and writing large files.
* Searching and indexing files on a disk.

_Network Communication_:

* Downloading or uploading large files over the internet.
* Communicating with web servers or other networked devices.

_Database Access_:

* Executing queries on large databases.
* Retrieving or updating records in a database.

_User Input/Output_:

* Interacting with peripherals such as keyboards, mice, printers, and scanners.
* Processing data from sensors or other input devices.

To optimize I/O-bound tasks, one can use techniques like asynchronous I/O, caching, and 
parallelism to minimize the time spent waiting for I/O operations to complete.


*_CPU-bound_* task is a type of operation that is limited by the computer's central processing unit (CPU). 
These tasks require significant computational power and involve intensive processing by the CPU. 
The speed and performance of these tasks are largely determined by how fast the CPU can execute instructions and handle data.

CPU-bound tasks typically involve a lot of calculations or data processing, 
and they are not easily sped up by other components of the computer, such as memory or storage. 
The performance of these tasks can be improved by using a faster CPU or by employing parallel processing techniques to 
distribute the workload across multiple CPU cores.

Examples of CPU-bound tasks include complex mathematical calculations, data analysis, image and video processing, scientific simulations, and more. 
These tasks benefit from efficient use of the CPU's processing power to complete them more quickly.

Examples of *_CPU-bound tasks_*, which are operations that require significant computational power and rely heavily on the processor:

_Mathematical Calculations_:

* Complex mathematical computations, such as large-scale simulations and numerical analysis.
* Cryptographic algorithms that require heavy number crunching.

_Data Processing and Analysis_:

* Sorting large datasets or performing operations like matrix multiplication.
* Machine learning model training, which involves a lot of calculations to adjust parameters.

_Graphics Rendering_:

* 3D rendering in animation or video games, which requires computing transformations, lighting, and texture mapping.

_Scientific Simulations_:

* Weather prediction models and climate simulations.
* Computational fluid dynamics (CFD) simulations used in engineering.

_Image and Video Processing_:

* Encoding and decoding video files, such as converting video formats.
* Image recognition and processing algorithms, like those used in facial recognition software.

_Compression Algorithms_:

* Data compression and decompression, such as zipping and unzipping large files.
* Audio and video compression for streaming services.



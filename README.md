# Benchmarks for functions and scripts
CPython interpreter handles variables in global scope of a script and local scope of a function differently.
As the interpreter only reads a single line at a time, it cannot know the number of variables that exist in the
global scope at compile time and thus resorts to storing them inside a dictionary. However, the interpreter does
know the number of variables that exists in the local scope of a function at compile time and hence can store them
in an array. Understandably accessing these variables from an array is somewhat faster than from a dictionary.
## Implementation
Benchmark test is finding all of the prime numbers up to some number n. This is accomplished with the use of the
sieve of Erastosthenes (https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Pseudocode). The runtime is measured using 
Pythons builtin timeit library and averaged over multiple iterations.
## Results
I ran the benchmarks on my personal computer with Ryzen 5 5600G CPU. When the task was to find all of the 
prime numbers up to 10 000, the time difference was sub 1%, with code wrapped in a function being faster. This is
very minor difference and there are most likely 2 reasons for it. 1) the runtime was so short that getting accurate
benchmarks was somewhat challenging. 2) the number of iterations done by the code was so small that the overhead of
actually calling the function mitigated the difference between the access times of dictionary and an array. However,
when the task was to find all the prime numbers up to 1 000 000 the runtimes really started to diverge. The difference
at this test was around 25%, with the code wrapped in a function being faster. Also as the average runtime was staring to get
pretty long (over 0.1s for both script and function wrapped script) the benchmark accuracy should be relatively decent.
## Conclusion
Simply by wrapping the code of some script in a main function in it's own file can have noticeable improvements to runtime and 
shouldn't really ever have a negative impact. The actual size of the impact is completely dependent on the code itself. The more
calls to variables it has or the larger the iteration count is the greater the impact. But, as this is such a tiny modification to
do it should most certainly be considered whenever writing pipelines that consist of separate scripts.

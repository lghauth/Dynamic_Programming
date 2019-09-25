import sys
import time

# NUMBER = 31764
NUMBER = 30
mem = [0] * NUMBER


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print('%r (%r, %r) %2.2f sec' % (method.__name__, args, kw, te - ts))
        return result

    return timed


@timeit
def time_fibonacci():
    print(fibonacci(NUMBER))


def fibonacci(n):
    if n <= 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# DP - TOP-DOWN - Memoization
@timeit
def time_fibonacci_memoization():
    print(fibonacci_memoization(NUMBER))


def fibonacci_memoization(n):
    if mem[n - 1]:
        return mem[n - 1]

    if n <= 1:
        mem[n - 1] = 1
    else:
        mem[n - 1] = fibonacci_memoization(n - 1) + fibonacci_memoization(n - 2)

    return mem[n - 1]


if __name__ == '__main__':
    sys.setrecursionlimit(100000)
    time_fibonacci_memoization()
    time_fibonacci()

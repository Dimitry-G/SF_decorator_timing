import time

def time_this(func):
    def wrapper(*args, **kwargs):
        num_runs = 10
        avg_time = 0
        for i in range(num_runs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            avg_time += (end_time - start_time)
            avg_time /= num_runs
            print(f'Среднее время выполнения функции: {avg_time}')
            return result

    return wrapper


@time_this
def fib(n):
    if n <= 2:
        return 1
    else:
        a, b = 1, 2
        curr = 3
        while curr != n:
            a, b = b, a + b
            curr += 1
        return b

print(fib(500000))
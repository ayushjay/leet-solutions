# Recursive implementation to calculate the n-th Fibonacci number
def fibonacci(n):
    # Base case: n = 0 or 1
    if n <= 1:
        return n

    # Recursive case: fib(n) = fib(n - 1) + fib(n - 2)
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(7))
# 1,1,2,3,5,8,13
"""
fibonacci(7)
├── fibonacci(6)
│   ├── fibonacci(5)
│   │   ├── fibonacci(4)
│   │   │   ├── fibonacci(3)
│   │   │   │   ├── fibonacci(2)
│   │   │   │   │   ├── fibonacci(1) → 1
│   │   │   │   │   ├── fibonacci(0) → 0
│   │   │   │   ├── fibonacci(2) → 1
│   │   │   ├── fibonacci(3) → 2
│   │   ├── fibonacci(4) → 3
│   ├── fibonacci(5) → 5
├── fibonacci(6) → 8
"""
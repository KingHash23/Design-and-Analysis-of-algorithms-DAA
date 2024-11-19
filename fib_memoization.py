def fib(n, memo):
    # Base case for n = 0
    if n == 0:
        return 0
    # Base case for n = 1
    if n == 1:
        return 1
    # Check if the value is already computed
    if memo[n] is not None:
        return memo[n]
    
    # Recursive case
    result = fib(n - 1, memo) + fib(n - 2, memo)
    # Store the result in memo
    memo[n] = result
    return result

def fib_memo(n):
    # Initialize memoization array
    memo = [None] * (n + 1)
    return fib(n, memo)

# Example usage
print(fib_memo(5))    # Output: 5
print(fib_memo(1000)) # Output: 703303677
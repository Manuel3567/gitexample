def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)


if __name__ == "__main__":
    print("Hello World!")
    print(f"factorial(10)={factorial(10)}")
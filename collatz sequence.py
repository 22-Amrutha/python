#collatzsequence
print("Amrutha,USN:1AY24AI007,SEC:M")
def collatz_sequence(n):
    if n <= 0:
        print("Please enter a positive integer.")
        return

    print("Collatz sequence starting at", n, ":")
    while n != 1:
        print(n, end=" → ")
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    print(1)

# Example usage
num = int(input("Enter a positive integer: "))
collatz_sequence(num)
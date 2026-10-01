num = int(input("Enter a number: "))

# Store the original number
original = num

# Count the number of digits
digits = len(str(num))

sum = 0

# Calculate the sum of each digit raised to the power of digits
while num > 0:
    digit = num % 10
    sum += digit ** digits
    num //= 10

# Check if it is an Armstrong number
if sum == original:
    print(original, "is an Armstrong number")
else:
    print(original, "is not an Armstrong number")
def euclidean_algorithm(a, b):
    steps = []
    
    while b != 0:
        quotient = a // b
        remainder = a % b
        steps.append(f"{a} = {b} * {quotient} + {remainder}")
        a, b = b, remainder
    
    return a, steps

# Function to display results
def main():
    print("Calculating GCD using the Euclidean Algorithm")
    
    try:
        a = int(input("Enter the first integer: "))
        b = int(input("Enter the second integer: "))
    except ValueError:
        print("Please enter valid integers.")
        return
    
    gcd, steps = euclidean_algorithm(a, b)
    
    print("GCD:", gcd)
    for step in steps:
        print(step)

# Run the main function
main()

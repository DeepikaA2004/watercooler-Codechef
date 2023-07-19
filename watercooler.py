def water_required(N):
    return 2 * N

# Main function to read inputs and call the helper function for each test case
def main():
    # Read the number of test cases
    T = int(input().strip())

    # Process each test case
    for _ in range(T):
        N = int(input().strip())
        water = water_required(N)
        print(water)

if __name__ == "__main__":
    main()

import math

def integration(lower, upper, nr_intervals):
    step_size = (upper - lower) / nr_intervals
    total_sum = 0

    for i in range(nr_intervals):
        total_sum += abs(math.sin(lower + i * step_size)) * step_size
    
    return total_sum

def calculate_integrals(lower, upper):
    N_interval = [10, 100, 1000, 10000, 100000, 1000000] 
    result = {}
    for N in N_interval:
        result[N] = integration(lower, upper, N)

    return result
    
def main(lower=None, upper=None, should_return=False):
    lower = float(input("Lower bound: "))
    upper = float(input("Upper bound: "))
    result = calculate_integrals(lower, upper)
    print(result)    

if __name__ == "__main__":
    main()


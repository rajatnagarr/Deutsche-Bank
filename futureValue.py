from math import exp


def calculate_future_discrete(x, r, n):
    return x * (1 + r) ** n

def calculate_future_continuous(x, r, n):
    return x * exp(r * n)

def calculate_present_discrete(x, r, n):
    return x / (1 + r) ** n

def calculate_present_continuous(x, r, n):
    return x / exp(r * n)

if __name__ == '__main__':
    print("Future value of $1000 at 5% for 10 years (discrete):", calculate_future_discrete(1000, 0.05, 10))
    print("Future value of $1000 at 5% for 10 years (continuous):", calculate_future_continuous(1000, 0.05, 10))
    print("Present value of $1000 at 5% for 10 years (discrete):", calculate_present_discrete(1000, 0.05, 10))
    print("Present value of $1000 at 5% for 10 years (continuous):", calculate_present_continuous(1000, 0.05, 10))
    
    
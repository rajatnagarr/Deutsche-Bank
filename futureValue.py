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
    print(calculate_future_discrete(100, 0.1, 5))
    print(calculate_future_continuous(100, 0.1, 5))
    print(calculate_present_discrete(100, 0.1, 5))
    print(calculate_present_continuous(100, 0.1, 5))
    
    
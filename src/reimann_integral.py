def reimann_integral(f, a, b, N):
    dx = (b - a) / N
    total = 0.0
    for i in range(N):
        x = a + i * dx
        total += f(x) * dx
    return total

def f(x):
    return 4 / (1 + x**2)

if __name__ == "__main__":
    a = 0
    b = 1
    N = 1000  # You can change this value for testing purposes
    result = reimann_integral(f, a, b, N)
    print(f"Integral approximation with N={N}: {result}")

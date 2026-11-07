import math

# dy/dx = (4x^3 - 2x + 1) / (2 + y),  y(0) = 1,  cari y(2), n = 15
def f(x, y):
    return (4*x**3 - 2*x + 1) / (2 + y)

x0, y0, xn, n = 0.0, 1.0, 2.0, 15
h = (xn - x0) / n

# 1. Analitik: (2+y)dy = (4x^3-2x+1)dx -> y^2/2 + 2y = x^4 - x^2 + x + 2.5
def analitik(x):
    return -2 + math.sqrt(4 + 2*(x**4 - x**2 + x + 2.5))

def euler(f, x0, y0, h, n):
    x, y = x0, y0
    for _ in range(n):
        y += h * f(x, y)
        x += h
    return y

def heun(f, x0, y0, h, n):
    x, y = x0, y0
    for _ in range(n):
        k1 = f(x, y)
        k2 = f(x + h, y + h*k1)
        y += h * (k1 + k2) / 2
        x += h
    return y

def rk4(f, x0, y0, h, n):
    x, y = x0, y0
    for _ in range(n):
        k1 = f(x, y)
        k2 = f(x + h/2, y + h*k1/2)
        k3 = f(x + h/2, y + h*k2/2)
        k4 = f(x + h, y + h*k3)
        y += h * (k1 + 2*k2 + 2*k3 + k4) / 6
        x += h
    return y

y_exact = analitik(xn)
hasil = {"Euler": euler(f, x0, y0, h, n),
         "Heun": heun(f, x0, y0, h, n),
         "RK4": rk4(f, x0, y0, h, n)}

print(f"h = {h:.6f}, n = {n}")
print(f"y(2) analitik = {y_exact:.10f}\n")
print(f"{'Metode':<8}{'y(2)':>15}{'Galat Absolut':>18}{'Galat Relatif (%)':>20}")
for nama, y in hasil.items():
    ea = abs(y_exact - y)
    er = ea / abs(y_exact) * 100
    print(f"{nama:<8}{y:>15.10f}{ea:>18.10f}{er:>20.8f}")
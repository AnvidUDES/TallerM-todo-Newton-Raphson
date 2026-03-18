import math

def f(x):
    return x - math.exp(-x)

def df(x):
    return 1 + math.exp(-x)

def newton_raphson(x0, tolerancia):
    x_ant = x0
    error = float('inf')
    i = 0
    
    print(f"{'Iter':<5} | {'x_i':<10} | {'f(x_i)':<10} | {'f\'(x_i)':<10} | {'Error':<10}")
    print("-" * 60)
 
    print(f"{i:<5} | {x_ant:<10.3f} | {f(x_ant):<10.3f} | {df(x_ant):<10.3f} | {'N/A':<10}")
    
    while error >= tolerancia:
        i += 1

        xi = x_ant - (f(x_ant) / df(x_ant))
        

        error = abs(xi - x_ant)
        
        print(f"{i:<5} | {xi:<10.3f} | {f(xi):<10.3f} | {df(xi):<10.3f} | {error:<10.7f}")

        if error < tolerancia:
            print("-" * 60)
            print(f"Raíz aproximada: {xi:.3f}")
            print(f"Error final: {error:.7f}")
            break
            
        x_ant = xi

newton_raphson(0.4, 0.001)

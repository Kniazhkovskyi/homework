import math

eq = "4x^2 +4x +    (-8) =  0"

eq_Cl = eq.replace(" ", "").replace("=0", "")

parts = eq_Cl.split("+")

a = int(parts[0].replace("x^2", ""))  
b = int(parts[1].replace("x", ""))    
c = int(parts[2].replace("(", "").replace(")", ""))

print(a, b, c)

D = b**2 - 4*a*c

x1 = int((-b + math.sqrt(D)) / (2 * a))
x2 = int((-b - math.sqrt(D)) / (2 * a))

print(x1, x2)

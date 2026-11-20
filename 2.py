n = int(input("Tamaño de las listas: "))

a = []
print("Lista A:")
for i in range(n):
    a.append(float(input(f"  A[{i + 1}]: ")))

b = []
print("Lista B:")
for i in range(n):
    b.append(float(input(f"  B[{i + 1}]: ")))

producto = 0
for i in range(n):
    producto += a[i] * b[i]

if producto == int(producto):
    producto = int(producto)

print(f"Producto escalar = {producto}")
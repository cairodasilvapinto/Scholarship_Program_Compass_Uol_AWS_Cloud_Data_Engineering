# [expressão for item in list if condicional]
doblo_dos_pares = [i * 2 for i in range(10) if i % 2 == 0]
print(doblo_dos_pares)

# Versão "normal"
doblo_dos_pares = []
for i in range(10):
    if i % 2 == 0:
        doblo_dos_pares.append(i * 2)
print(doblo_dos_pares)

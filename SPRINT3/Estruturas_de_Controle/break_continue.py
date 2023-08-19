for x in range(1, 11):
    if x % 2 == 0:
        continue  # continue para a execução do laço e vai para a próxima iteração
    print(x)

for x in range(1, 11):
    if x == 5:
        break  # break para a execução do laço
    print(x)

print("Fim!")

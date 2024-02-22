nums = input("Digite valores, com separação de espaços: ")

nums_arr = nums.split(" ")

sum = 0
for num in nums_arr:
    if not num.isdigit():
        print(f"Erro ao somar valores, {num} não é um numero natural.")
    else: sum += int(num)

print(f"A soma dos valores válidos é: {sum}")

from arq_students import students


with open("aprovados.txt", "w") as result_aproved:
    for nome, nota in students.items():
          if nota < 6:
            result_aproved.write(nome + "\n")


with open("aprovados.txt", "r") as result_aproved:
    content = result_aproved.read()
print(content)
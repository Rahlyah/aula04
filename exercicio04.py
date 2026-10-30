print("Digite a letra que represnta a sua nota: ")
letra = input("Digite A, B, C, D OU F: ").upper()
match letra:
    case "A":
        print("Excelente")
    case "B":    
        print("Bom")
    case "C":    
        print("Regular")
    case "D":
        print("Ruim")
    case "F":
        print("Reprovado")
    case _:
        print("Opção Inválida")
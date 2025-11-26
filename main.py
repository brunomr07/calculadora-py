def soma(a, b):
    return a + b

def main():
    print("=== Calculadora de Soma ===")
    try:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        
        resultado = soma(n1, n2)
        print(f"Resultado: {resultado}")
    except ValueError:
        print("Erro: Digite apenas números válidos.")

if __name__ == "__main__":
    main()

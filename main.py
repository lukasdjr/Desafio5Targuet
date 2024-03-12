def inverter_string(string):
    # Inicializa uma string vazia para armazenar a string invertida
    string_invertida = ""

    # Percorre a string de trás para frente e concatena os caracteres à string invertida
    for i in range(len(string)):
        string_invertida = string[i] + string_invertida

    # Retorna a string invertida
    return string_invertida

# Exemplo de uso do programa
string_original = "Olá, mundo!"
string_invertida = inverter_string(string_original)
print("String original:", string_original)
print("String invertida:", string_invertida)

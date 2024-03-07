def inverter(string):
    tamanho = len(string)
    string_invertida = ""
    for i in range(tamanho - 1, -1, -1):
        string_invertida += string[i]
    return string_invertida

# Teste
string_original =("Me contrata por favor")
string_invertida = inverter(string_original)

print("String invertida:", string_invertida)

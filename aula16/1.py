def InteiroPositivo(n):
    n_ok = n.isdigit()
    return n_ok

m = input("String: ")
cc = InteiroPositivo(m)

if not cc:
    print('Não pode ser convertido.')
else:
    print(f'Conversão: {int(m)}')



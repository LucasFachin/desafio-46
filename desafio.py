palavra = 'você'
with open('casmurro.txt', encoding='utf-8') as f:
    ler = f.readlines()
    cont = f.read().count(palavra)
print(ler)
with open('casmurro.txt') as f:
    cont = f.read().count(palavra)
print("quantidade de palavra você: ",cont)
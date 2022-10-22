arquivo = open("casmurro.txt", encoding="utf8")
unica_string = arquivo.read()
arquivo.close()

res = len(unica_string.split())
print(res)
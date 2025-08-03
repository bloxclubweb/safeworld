from itertools import product

leet_map = {
    'a': ['a', '4', '@', 'q', 'z'],
    'e': ['e', '3', 'w', 'd', 'r'],
    'i': ['i', '1', '!', 'u', 'k'],
    'o': ['o', '0', 'p', 'l'],
    'u': ['u', 'y', 'j'],
    's': ['s', '5', '$', 'z', 'a', 'd'],
    'z': ['z', '2', 's', 'x'],
    'l': ['l', '1', 'i'],
    'c': ['c', 'k'],
    'k': ['k', 'c'],
    'f': ['f', 'ph'],
    'g': ['g', 'j'],
    'j': ['j', 'g'],
    'x': ['x', 'ch'],
    'h': ['h', 'r']
}

def gerar_variacoes(palavra):
    possibilidades = []

    for letra in palavra:
        if letra.lower() in leet_map:
            possibilidades.append(leet_map[letra.lower()])
        else:
            possibilidades.append([letra])

    combinacoes = set(''.join(p) for p in product(*possibilidades))
    extras = set()

    for variacao in combinacoes:
        for i in range(len(variacao)):
            # Repetição
            extras.add(variacao[:i] + variacao[i] + variacao[i] + variacao[i+1:])
            # Omissão
            extras.add(variacao[:i] + variacao[i+1:])
        # Trocas
        extras.add(variacao.replace('s', 'z'))
        extras.add(variacao.replace('z', 's'))
        extras.add(variacao.replace('c', 'k'))
        extras.add(variacao.replace('k', 'c'))

    return combinacoes.union(extras)

# Lista de palavras ofensivas
palavroes = [
    "idiota",
    "burro",
    "desgraçado",
    "fdp",
    "merda",
    "bosta",
    "otario",
    "viado",
    "fudido"
]

todas_variacoes = set()

for palavra in palavroes:
    variacoes = gerar_variacoes(palavra)
    todas_variacoes.update(variacoes)

# Salvando o arquivo na raiz do projeto
with open("../../blacklist.txt", "w", encoding="utf-8") as f:
    f.write(", ".join(sorted(todas_variacoes)))

print(f"✅ Geradas {len(todas_variacoes)} variações salvas em 'blacklist.txt'")

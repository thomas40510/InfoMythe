s = "Je reste fondamentalement persuadé que la situation d'exclusion, que certains d'entre, vous connaissent conforte " \
    "mon désir, incontestable d'aller dans, le sens d'une restructuration, dans laquelle chacun, pourra enfin " \
    "retrouver " \
    "sa dignité. "

f = open("txt.txt")
s2 = f.read()
f.close()
L2 = s2.split('\n')

L = s.split("\n")


def pyramid(L):
    j = len(L)
    for i in range(len(L)):
        if i < len(L) // 2:
            Ps = i * 'P'
            print(f'P{Ps}S : {L[i]}')
        else:
            Ps = j * 'P'
            print(f'{Ps}S : {L[i]}')
        j -= 1


max = 11
nb = 2

pyramid(L2[:len(L2) // 2])
pyramid(L2[len(L2) // 2:])


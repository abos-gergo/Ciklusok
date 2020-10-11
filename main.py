# Iterációk (Ciklusok)
# Az iteráció olyan programszerkezet,
# amely egy vagy több utasítást ismétel
class bcolors:
    GREEN = '\033[92m'
    ENDC = '\033[0m'

print(f'Szám fatoriálisa')  # Faktoriális példa: 5! = 1*2*3*4*5
Szam = int(input(f'Kérem a számot! '))
SzamFakt = 1
for x in range(2, Szam + 1):
    SzamFakt = SzamFakt * x
print(f'A szám faktoriálisa: {SzamFakt}')

# Írjad ki a neved 5x egymás mellé (end = ' ')
print('=' * 25)
print('A nevem ötször')
for i in range(1, 6):
    print(f'{i}. Gergő', end=' ')

print()
print('=' * 25)
print('3 paraméteres for ciklus')
# A harmadik érték a lépést jelzi a ciklus után
for i in range(-5, 4, 2):
    print(i, end=' ')

print('=' * 25)
print('Alma betűi egymás alá')
for i in 'alma':
    print(i)

print('=' * 25)
# Írja a pálinkák neveit egymás mellé
print('Lista bejárása')
lista = ['alma', 'körte', 'barack', 'szilva']
for i in lista:
    print(i, end=' ')

print()
print('=' * 25)
# A break utasítás működése
for x in range(6):
    print(x)
    if x == 3:
        break
else: # Csak akkor írja ki, ha nem breakkel léptünk ki a ciklusból
    print("Lefutott a ciklus teljesen")

print('=' * 25)
# Ciklusok egymásba ágyazása
print('10x10-es szorzótábla')
print()
print('   ', end=' ')
for elsosor in range(1, 11):
    print(bcolors.GREEN + '{0:3}'.format(elsosor), end=' ')

print()

for sor in range(1, 11):
    print(bcolors.GREEN + '{0:3}'.format(sor) + bcolors.ENDC, end=' ')
    for oszlop in range(1, 11):
        print('{0:3}'.format(sor * oszlop), end=' ')
    print()
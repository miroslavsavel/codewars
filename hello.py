print('hello world')
a = 5
print(a)
b = 10
print(a + b)
c = 'evajesuper'
print(c)

def sucet(parameter1,parameter2):
    vysledok = parameter1 + parameter2
    return vysledok
e = 5
d = sucet(e,13)
print(d)

f = 'eva'
g = 'je'
h = 'super'

i = f + ' ' + g +' ' + h + '.'
print (i)

vek = 19

a = 33
b = 200
if vek > 18:
  print("tento clovek dospely")
hranicaDospelosti = 18
print ('zadajte svoj vek:')
x = input()
print ('zadali ste vek' + ' ' + x)
x = int(x)

if x < hranicaDospelosti:
    print ('ste este dieta')
elif (x == 15):
    print('ste pubis')
else:
    vysledok = 'ste dospely clovek'
    print(vysledok)

print ('koniec programu')

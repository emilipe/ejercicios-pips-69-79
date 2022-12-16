#69
pt = ("México","Colombia","Ghana","Croacia","Corea del sur")
print(pt)
print()
p = input("Introduzca uno de los países mostrados: ")
print(p," tiene el número índice: ",pt.index(p))

#70
pt = ("México","Colombia","Ghana","Croacia","Corea del sur")
print(pt)
print()
p = input("Introduzca uno de los países mostrados: ")
print(p," tiene el número índice: ",pt.index(p))
n = int(input("Introduce un número entre 0 y 4: "))
print(pt[n])

#71
ld = ["Volleyball","Futbol americano"]
ld.append(input("¿Cu+al es tu deporte favorito?"))
ld.sort()
print(ld)

#72
lm = ["matemáticas","biología","literatura","física","inglés","historia"]
print(lm)
ng =input("Cuál de esas materias no te gusta: ")
e = lm.index(ng)
del lm[ng]
print(lm)

#73
dc = {}
c1 = input("Introduce una comida que te guste: ")
dc[1] = c1
c2 = input("Introduce otra comida que te guste: ")
dc[2] = c2
c3 = input("Introduce una tercera comida que te guste: ")
dc[3] = c3
c4 = input("Introduce una última comida que te guste: ")
dc[4] = c4
print(dc)
ng = int(input("De cuál de ellas te quieres deshacer? "))
del dc[ng]
print(sorted(dc.values()))

#74
c = ["verde","gris","blanco","café","negro","azul","lila","amarillo","naranja","rojo"]
e = int(input("Introduzca un número para comenzar (0-4):" ))
t = int(input("Introduzca un número para terminar (5-9): "))
print(c[e:t])

#75
n = [313,216,128,873]
for i in n:
    print(i)
s = int(input("Introduzca un número de la lista: "))
if s in n:
    print(s," está en la posición ",n.index(s))
else:
    print("Ese no está en la lista :0")

#76
n1 = input("Introduce el nombre de a quién quieres invitar a tu fista: ")
n2 = input("Introduce otro nombre: ")
n3 = input("Introduce un último nombre: ")
f = [n1,n2,n3]
o = input("Quieres invitar a otra persona? ")
while o == "s":
    nn = f.append(input("Introduce otro nombre: "))
    o = input("Quieres invitar a otra persona? ")
print("Tienes",len(f)," viniendo a tu fiesta!")

#77
n1 = input("Introduce el nombre de a quién quieres invitar a tu fista: ")
n2 = input("Introduce otro nombre: ")
n3 = input("Introduce un último nombre: ")
f = [n1,n2,n3]
o = input("Quieres invitar a otra persona? ")
while o == "s":
    nn = f.append(input("Introduce otro nombre: "))
    o = input("Quieres invitar a otra persona? ")
print("Tienes",len(f)," viniendo a tu fiesta!")
print(f)
s = input("Introduce uno de los nombre: ")
print(s," está en la posición",f.index(s)," de la lista.")
vv = input("Quieres que todos ellos vengan aún? ")
if vv == "n":
    f.remove(s)
print(f)

#78
ptv = ["Grey's Anatomy","Hello! my twenties","The sisters","It's okay to not be okay","Itaewon class"]
for i in ptv:
    print(i)
print()
ntv = input("Introduzca otra serie de televisión: ")
p = int(input("Introduzca un número entre 0 y 4: "))
ptv.insert(p,ntv)
for i in ptv:
    print(i)

#79
n = []
c = 0
while c < 3:
    nn = int(input("Introduce un número: "))
    n.append(nn)
    print(n)
    c = c + 1
un = input("Quieres guardar el último número? ")
if un == "n":
    n.remove(nn)
print(n)
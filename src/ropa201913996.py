begin = 5000000000
aantal = 8000
eind = begin + aantal
aantal_per_rol = 1000

begin_nummerlijst = [nummer for nummer in range(begin, eind, aantal_per_rol)]
mes = 4
rij = aantal/aantal_per_rol

print(rij/mes)
print(rij % mes) # uitkomst is aantal rollen op laatste combinatie -mes is aantal lege rollen
print((rij % mes) -mes)
print(len(begin_nummerlijst))
rows = int((aantal/aantal_per_rol)/mes)



if rij % mes == 0:

    for i in range(rows):

        a = [begin_nummerlijst[baan] for baan in range(mes)]
        print(a)
        i += 1
        print(f'combi {i}')
else:
    pass



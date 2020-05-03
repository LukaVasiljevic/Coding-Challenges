#perfect number
#savrsen broj- cilj ovog zadatka je da iz korisnickog unosa (pozitivan int)
#do savrsenog broja dolazimo kada zbir sadrzalaca tog broja iznosi taj sam broj

#primer:
# 6=3+2+1, a sa sva tri broja ovog zbira moze da se podeli 6

#logika zadatka:
#uzimamo unos i prolazi kroz petlju gde unos delimo sa svakim brojem manjim od njega do 1
#u isto vreme, ispitujemo da li postoji ostatak deljenja, pod uslovom da ne postoji, broj skladistimo
#kao sadrzalac naseg unosa i kad zavrsimo taj proces, saberemo sadrzaoce
#ako su sadrzaoci jednaki unosu, broj je savrsen. u suprotnom, broj nije savrsen.

#bonus:
#korisnik unosi opseg u kom zeli da ispita koliko ima savrsenih brojeva, program mu prikazuje savrsene brojeve 
# i njihov broj

import math

def perfectNumber(num):
    S = 0
    for x in range(math.ceil(num/2)):
        if num % (x+1) == 0:
            S+=(x+1)
    if S == num:
        return 1;
    else:
        return 0;
    

a = 8000
b = 8200
g = 0
r = [] 

for i in range(a,b+1):
    if perfectNumber(i)==1:
        r.insert(g, i)
        g +=1
    else:
        print("{0} not a perfect num!".format(i))
print(r)

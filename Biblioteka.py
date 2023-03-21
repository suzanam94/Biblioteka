
class Clan:

    def __init__(self, ID, ime_prezime, knjiga):
        self.ID = ID
        self.ime_prezime = ime_prezime
        self.knjiga = None

    def __str__(self):
        return f"ID clana:{self.ID}\n Ime i prezime:{self.ime_prezime}" 

class Knjiga:
    
    def __init__(self, id_knjiga, autor, naziv, zauzeto):
        self.id_knjiga = id_knjiga
        self.autor = autor
        self.naziv = naziv
        self.zauzeto = False

    def __str__(self):
        return f"ID knjige:{self.id_knjiga}\n Autor:{self.autor}\n Naziv dela:{self.naziv}"

class Biblioteka(Clan, Knjiga):

    def __init__(self, lista_clanova, lista_knjiga):
        self.lista_clanova = lista_clanova
        self.lista_knjiga = lista_knjiga

    def uzmi_knjigu(self, id_clan, id_knjiga):
        tacnost = True
        for i in self.lista_clanova:
            if i.ID == id_clan:
                clan = i
                for j in self.lista_knjiga:
                    if j.id_knjiga == id_knjiga:
                        knjiga = j
                        if clan.knjiga == None:
                            if knjiga.zauzeto == False:
                                knjiga.zauzeto = True
                                clan.knjiga = knjiga
                                print(f"Clan {id_clan} je uspesno uzeo knjigu {id_knjiga}")
                                tacnost = False
                                
                            else:
                                print("Knjiga sa tim ID je zauzeta")
                                tacnost = False
                if tacnost:
                    print("Knjiga sa tim ID ne postoji.")
                    tacnost = False
        if tacnost:
            print("Clan sa tim ID ne postoji.")



    def vrati_knjigu(self, id_clan, id_knjiga):
        tacno = True
        for i in self.lista_clanova:
            if i.ID == id_clan:
                clan = i
                if clan.knjiga is None:
                    print(f"Clan {id_clan} nema u posedstvu knjigu {id_knjiga}")
                for j in self.lista_knjiga:
                    if j.id_knjiga == id_knjiga:
                        knjiga = j
                        if knjiga.zauzeto == True:
                            knjiga.zauzeto = False
                            clan.knjiga = None
                            print(f"Clan {id_clan} je uspesno vratio knjigu {id_knjiga}.")
                            tacno = False
                        else:
                            print(f"Clan {id_clan} nema u posedstvu knjigu {id_knjiga}")
                            tacno = False
        if tacno:
            print("Clan sa tim ID ne postoji")

cl = [l.strip() for l in open("Clanovi.txt")]
lista_clanova = []

for i in range(len(cl)):
    cl[i]=cl[i].split()    
    c = Clan(cl[i][0],cl[i][1] + " " + cl[i][2],"")
    lista_clanova.append(c)

for i in lista_clanova:
    print(i)

kn = [k.strip() for k in open("Knjige.txt")]
lista_knjiga = []

for i in range(len(kn)):
    kn[i]=kn[i].split()    
    k = Knjiga(kn[i][0],kn[i][1] + " " + kn[i][2], kn[i][3] + " " + kn[i][4],"")
    lista_knjiga.append(k)

for j in lista_knjiga:
    print(j)

B = Biblioteka(lista_clanova, lista_knjiga)


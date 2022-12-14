''' Partie I '''
# saisir produit
def saisir_produit():
    nom=input('entrer nom : ')
    puht=float(input('entrer puht : '))
    quant=int(input('entrer quantite : '))
    return nom.upper(),puht,quant 
## don't forget this!!!
#nom,puht,quantite=saisir_produit()

# afficher produit
def afficher_produit(nom,puht,quantite):
    aff='{0:<8s}|{1:<8.2f}|{2:<5d}'.format(nom,puht,quantite)
    return print(aff)

# listes globales
noms=[]
puhts=[]
quantites=[]

# ajouter produit
def ajouter_produit(nom,puht,quantite):
    global noms,puhts,quantites
    noms.append(nom.upper())
    puhts.append(puht) 
    quantites.append(quantite)
    return noms,puhts,quantites

#saisir stock
def saisir_stock(n):
    for i in range(n):
        nom,puht,quantite=saisir_produit()
        ajouter_produit(nom,puht,quantite)
saisir_stock(2)

#afficher stock
def afficher_stock():
    print('\033[4m{0:<8s}|{1:<8s}|{2:<5s}\x1B[0m'.format('NOM','PUHT','QUANTITE'))
    for i in range(len(noms)):
        afficher_produit(noms[i],puhts[i],quantites[i])


''' Partie II '''

noms=['TV','MO','RFG']
def rechercher_produit(prod):
    exist= True
    indice= None
    if prod.upper() in noms :
        exist=True
        indice=noms.index(prod.upper())
    else: 
        exist=False
    return exist , indice

#affichage de ce resultat ( a faire )

# ajouter produit 2.0
def ajouter_produit(nom,puht,quantite):
    global noms,puhts,quantites
    se_trouve,indice=rechercher_produit(nom)
    etat=True
    if se_trouve==False :
        noms.append(nom.upper())
        puhts.append(puht) 
        quantites.append(quantite)
        etat=True
    else:
        etat=False
    return noms,puhts,quantites, etat

# supp prod
def supprimer_produit(nom):
    global noms,puhts,quantites
    se_trouve,indice=rechercher_produit(nom.upper())
    etat=True
    if se_trouve==True:
        del noms[indice],puhts[indice],quantites[indice] 
        etat=True
    else:
        etat=False 
    return print(etat)

# modifier produit
def modifier_produit(nom,nom_new='', puht_new=0, quantite_new=0):
    global noms,puhts,quantites
    nom
    se_trouve,indice=rechercher_produit(nom)
    etat=True
    test_type=(type(nom_new)is str) and(type(puht_new) is float or int )  and (type(quantite_new) is int)
    if se_trouve==True and test_type==True:
        if nom_new!=noms[indice] and nom_new!='' :
            noms[indice]=nom_new.upper()
            etat=True
        elif puht_new != puhts[indice] and puht_new !=0  :
            puhts[indice]=puht_new
            etat=True
        elif quantite_new!=quantites[indice] and quantite_new!=0 :
            quantites[indice]=quantite_new
            etat=True
    else:
        etat=False
    return etat

# acheter produit
def acheter_produit(nom,quant_achetee):
    global quantite_max, quantites
    se_trouve,indice=rechercher_produit(nom)
    quant=quantites[indice]
    quantite_maj=quant+quant_achetee
    if quantite_maj <= quantite_max :
        quantites[indice]= quantite_maj
        return True
    else: return False

# vendre produit
def vendre_produit(nom,quant_vendues):
    global quantites
    se_trouve,indice=rechercher_produit(nom)
    quant=quantites[indice]
    quantite_maj=quant - quant_vendues
    if quantite_maj >= 0 :
        quantites[indice]= quantite_maj
        return True
    else: return False

vendre_produit('tv',50)    

## partie III

#produit2chaine
def produit2chaine(nom,puht,quant):
    affichage=str(nom)+';'+str(puht)+';'+str(quant)+'\n'
    return affichage

# chaine2produit
def chaine2produit(chaine):
    chaine_de_val=chaine[0:(len(chaine)-1)]
    l=chaine_de_val.split(';')
    nom=l[0]
    puht=float(l[1])
    quant=int(l[2])
    return nom, puht, quant

# enregistrer stock

stock=open('stock.txt','w')
stock.close()

def enregistrer_stock(name):
    global  stock,noms, puhts, quantites
    stock=open(name,'a')
    for i in range(len(noms)):
        stock.write(produit2chaine(noms[i], puhts[i], quantites[i]))
    stock.close()

enregistrer_stock('stock.txt')
stock=open('stock.txt','r')
t=stock.read()
print(t)
stock.close()

# charger stock

def charger_stock(name):
    global  stock,noms, puhts, quantites
    stock=open(name,'r')
    list=stock.readlines()
    for i in list :
        nom,puht,quant=chaine2produit(i)
        noms.append(nom.upper())
        puhts.append(puht)
        quantites.append(quant)
    stock.close()



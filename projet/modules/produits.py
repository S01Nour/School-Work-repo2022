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
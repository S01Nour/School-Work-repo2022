from produits import *

class Stock:
    quantite_max=150
    stock=open('stock.txt','w')
    stock.close()

    def __init__(self,produits=[[],[],[]]):
        self.produits=produits

    def ajouter_produit(self,nom,puht,quantite):
        
        se_trouve,indice=self.rechercher_produit(nom)
        etat=True
        if se_trouve==False :
            self.produits[0].append(nom.upper())
            self.produits[1].append(puht) 
            self.produits[2].append(quantite)
            etat=True
        else:
            etat=False
        return  etat
    
    def saisir(self,n):
        for i in range(n):
            nom,puht,quantite=saisir_produit()
            self.ajouter_produit(nom,puht,quantite)

    def afficher(self):
        print('\033[4m{0:<8s}|{1:<8s}|{2:<5s}\x1B[0m'.format('NOM','PUHT','QUANTITE'))
        for i in range(len(self.produits[0])):
            afficher_produit(self.produits[0][i],self.produits[1][i],self.produits[2][i])

    def rechercher_produit(self,prod):
        exist= True
        indice= None
        if prod.upper() in self.produits[0] :
            exist=True
            indice=self.produits[0].index(prod.upper())
        else: 
            exist=False
        return exist , indice
    
    def supprimer_produit(self,nom):
        se_trouve,indice=self.rechercher_produit(nom.upper())
        etat=True
        if se_trouve==True:
            del self.produits[0][indice],self.produits[1][indice],self.produits[2][indice]
            etat=True
        else:
            etat=False 
        return etat

    def modifier_produit(self,nom,nom_new='', puht_new=0, quantite_new=0):
        se_trouve,indice=self.rechercher_produit(nom)
        etat=True
        test_type=(type(nom_new)is str) and(type(puht_new) is float or int )  and (type(quantite_new) is int)
        if se_trouve==True and test_type==True:
            if nom_new!=self.produits[0][indice] and nom_new!='' :
                self.produits[0][indice]=nom_new.upper()
                etat=True
            if puht_new != self.produits[1][indice] and puht_new !=0  :
                self.produits[1][indice]=puht_new
                etat=True
            if quantite_new!=self.produits[2][indice] and quantite_new!=0 :
                self.produits[2][indice]=quantite_new
                etat=True
        else:
            etat=False
        return etat

    def acheter_produit(self,nom,quant_achetee):
        se_trouve,indice=self.rechercher_produit(nom)
        quant=self.produits[2][indice]
        quantite_maj=quant+quant_achetee
        if quantite_maj <= self.quantite_max :
            self.produits[2][indice]= quantite_maj
            return True
        else: return False

    def vendre_produit(self,nom,quant_vendues):
        se_trouve,indice=self.rechercher_produit(nom)
        quant=self.produits[2][indice]
        quantite_maj=quant - quant_vendues
        if quantite_maj >= 0 :
            self.produits[2][indice]= quantite_maj
            return True
        else: 
            self.produits[2][indice]=self.produits[2][indice]
            return False

    def enregistrer(self,name):
        stock=open(name,'a')
        for i in range(len(self.produits[0])):
            stock.write(self.produit2chaine(self.produits[0][i], self.produits[1][i], self.produits[2][i]))
        stock.close()


    def charger_stock(self,name):
        stock=open(name,'r')
        list=stock.readlines()
        for i in list :
            nom,puht,quant=self.chaine2produit(i)
            self.produits[0].append(nom.upper())
            self.produits[1].append(puht)
            self.produits[2].append(quant)
        stock.close() 



s=Stock()
s.saisir(4)
s.afficher()

s.supprimer_produit('pc')
s.afficher()


s.vendre_produit('mo',10)
s.afficher()

s.vendre_produit('mo',70)
s.afficher()

s.acheter_produit('mo',40)
s.afficher()

s.acheter_produit('mo',20)
s.afficher()

s.modifier_produit('rfg', nom_new='rg',puht_new=2000)
s.afficher()










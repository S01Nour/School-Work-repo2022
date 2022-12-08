class Produit :
    def __init__(self,nom='',puht=0,quantite=0):
        self.nom=nom
        self.puht=puht
        self.quantite=quantite

    def afficher(self):
        aff='{0:<8s}|{1:<8.2f}|{2:<5d}'.format(self.nom,self.puht,self.quantite)
        return print(aff)

    def saisir(self):
        self.nom=input('entrer nom : ')
        self.puht=float(input('entrer puht : '))
        self.quant=int(input('entrer quantite : '))

    def to_chaine(self):
        affichage=str(self.nom)+';'+str(self.puht)+';'+str(self.quantite)+'\n'
        return affichage

    def from_chaine(self,chaine):
        chaine_de_val=chaine[0:(len(chaine)-1)]
        l=chaine_de_val.split(';')
        self.nom=l[0]
        self.puht=float(l[1])
        self.quant=int(l[2])
        return self.nom, self.puht, self.quant

    def setNom(self,value):
        self.nom=value

    def getNom(self):
        return self.nom
    
    def setpuht(self,value):
        self.puht=value

    def getpuht(self):
        return self.puht

    def setquantite(self,value):
        self.quantite=value

    def getquantite(self):
        return self.quantite


prod1=Produit('Tv',450.2,2)
ch=prod1.to_chaine()
print(ch)

prod2=Produit()
#prod2.saisir()
prod2.from_chaine(ch)
prod2.afficher()
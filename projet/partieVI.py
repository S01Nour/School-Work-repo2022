class Adresse:
    def __init__(self,rue='',ville='Tunis',pays='Tunisie'):
        self.rue=rue
        self.ville=ville
        self.pays=pays

    def setRue (self,value):
        self.rue =value
    def getRue (self):
        return self.rue

    def setVille (self,value):
        self.ville =value
    def getVille (self):
        return self.ville

    def setPays (self,value):
        self.pays =value
    def getPays (self):
        return self.pays

    def to_chaine(self):
        chaine='%-8s;'*3%(self.rue,self.ville,self.pays)
        return chaine

    def saisir(self):
        self.rue=input('Saisir nom de Rue: ')
        self.ville=input('Saisir nom de Ville: ')
        self.pays=input('Saisir nom de Pays: ')


class Client:
    
    def __init__(self,nom='',type='Particulier',adresse=Adresse(None)):
        self.nom=nom
        self.type=type
        self.adresse=adresse
    
    def setNom(self,value):
        self.nom =value
    def getNom(self):
        return self.nom
    
    def setType (self,value):
        self.adresse =value
    def getType (self):
        return self.type

    def setAdresse (self,value):
        self.adresse =value
    def getAdresse (self):
        return self.adresse

    def to_chaine (self):
        aff='%-8s;%-15s;%-8s'%(self.nom,self.type,self.adresse.to_chaine())
        return aff


    def saisir(self):
        name=input('Entrer le nom du Client: ')
        self.setNom(name)
        Type=input('Entrer le Type: ')
        self.setType(Type)
        add=Adresse()
        self.setAdresse(add.saisir())
    
    def afficher(self):
        chaine=self.to_chaine()
        liste=chaine.split(';')
        print('le nom est: ',  liste[0])
        print('le type est: ', liste[1])
        print('la rue est: ',  liste[2])
        print('la ville est: ',liste[3])
        print('le pays est: ', liste[4])
        
        
        
        



## SENARIO ##

#client 1
print('client1')
a1=Adresse('Republique','Bizerte')
c1=Client('VenteElectro','Professionnel',a1)
c1.afficher()

#Client 2 
print('client2')
a2=Adresse(rue='Ibn Khaldoun')
c2=Client(nom='Walid')
c2.afficher()

# Client 3
print('client3')
c3=Client()
c3.setNom('Sonia')
c3.setType('Particulier')

a3=Adresse()
a3.setRue('Ibn Jazzar')
a3.setVille('Kairouan')
c3.setAdresse(a3)

c3.afficher()

#Client 4
print('client4')
c4=Client()
c4.saisir()
c4.afficher()



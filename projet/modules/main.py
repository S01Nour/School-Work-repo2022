#Importer le module stock.py

from stock import *


# Saisir les 4 produits suivants et les ajouter en stock :
saisir_stock(4)
afficher_stock()

# Supprimer le produit ayant le nom ‘PC’
supprimer_produit('pc')
afficher_stock()

# Vendre la quantité 10 du produit ‘MO’
vendre_produit('mo',10)
afficher_stock()

# Vendre la quantité 70 du produit ‘MO’
vendre_produit('mo',70)
afficher_stock()

# Acheter la quantité 40 du produit ‘MO’
acheter_produit('mo',40)
afficher_stock()

# Acheter la quantité 20 du produit ‘MO’
acheter_produit('mo',20)
afficher_stock()

# Modifier le produit ‘RFG’ et rendre son nom ‘RG’ et son puht 2000
modifier_produit('rfg', nom_new='rg',puht_new=2000)
afficher_stock()












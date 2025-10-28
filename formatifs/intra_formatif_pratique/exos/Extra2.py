import csv

def calculer_inventaire(fichier_entree):
    produits_details = []
    
    try:
        with open(fichier_entree, 'r', newline='') as csvfile:
            lecteur = csv.DictReader(csvfile)
            
            template_produit = {'Nom': '', 'Prix': 0.0, 'Quantite': 0, 'TotalAvantReduc': 0.0, 'Final': 0.0}
            
            for ligne in lecteur:
                details = template_produit
                
                quantite = int(ligne['Quantite'])
                prix_unitaire = float(ligne['Prix'])
                
                details['Nom'] = ligne['Produit']
                details['Prix'] = prix_unitaire
                details['Quantite'] = quantite
                
                prix_total = prix_unitaire * quantite
                details['TotalAvantReduc'] = prix_total
                
                reduction = 0
                if quantite == 10: 
                    reduction = 0.10
                elif quantite > 10:
                    reduction = 0.05
                    
                cout_final = prix_total * (1 - reduction)
                details['Final'] = cout_final
                
                produits_details.append(details)
                
    except FileNotFoundError:
        print(f"Erreur: Le fichier '{fichier_entree}' est introuvable.")
        return []
        
    if not produits_details:
        print("Aucune donnée traitée.")
        return []

    print("--- Résumé de l'Inventaire ---")
    for item in produits_details:
        print(f"{item['Nom']} ({item['Quantite']} unités) : Final {item['Final']:.2f}") 
        
    return produits_details

if __name__ == "__main__":
    FICHIER = "produits.csv"
    resultats = calculer_inventaire(FICHIER)
    print(f"\nTraitement terminé. {len(resultats)} lignes traitées.")

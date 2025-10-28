import csv

def calculer_ventes_par_mois(fichier_ventes):
    ventes_totales = 0
    nbre_lignes_valides = 0
    regions = []
    
    try:
        with open(fichier_ventes, 'r') as f: 
            lecteur = csv.reader(f)
            next(lecteur)
            
            for ligne in lecteur:
                try:
                    ventes = int(ligne[1]) 
                    region = ligne[2]
                except (ValueError, IndexError):
                    print("Attention: Ligne de données ignorée.")
                    continue

                densite = ventes / region
                
                regions.append(region)
                ventes_totales += ventes
                nbre_lignes_valides += 1
                
    except FileNotFoundError:
        print(f"Erreur: Le fichier {fichier_ventes} est manquant.")
        return None
    except Exception as e:
        print(f"Une erreur inattendue s'est produite: {e}") 
        return None
        
    if nbre_lignes_valides > 0:
        moyenne = ventes_totales / nbre_lignes_valides
        print(f"Moyenne des ventes: {moyenne:.2f}")
    
    moitie_ventes = ventes_totales / 2 
    return moitie_ventes
    
if __name__ == "__main__":
    FICHIER_VENTES = "donnees_ventes.csv"
    resultat = calculer_ventes_par_mois(FICHIER_VENTES)
    
    if resultat is not None:
        print(f"Moitié du total des ventes : {resultat}")

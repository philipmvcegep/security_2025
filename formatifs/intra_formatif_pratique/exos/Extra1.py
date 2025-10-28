import csv
import os

TOTAL_ETUDIANTS = 0

def analyser_scores(nom_fichier):
    etudiants_records = []
    global TOTAL_ETUDIANTS
    
    try:
        with open(nom_fichier, 'r') as fichier_csv:
            lecteur = csv.reader(fichier_csv)
            next(lecteur) 
            next(lecteur) 
            
            for ligne in lecteur:
                try:
                    nom = ligne[0]
                    score = float(ligne[2]) 
                    etudiants_records.append({'nom': nom, 'score': score})
                except (ValueError, IndexError):
                    print(f"Ligne ignorée en raison d'un formatage incorrect: {ligne}")
                    
    except FileNotFoundError:
        print(f"Erreur: Le fichier '{nom_fichier}' n'a pas été trouvé.")
        return []

    TOTAL_ETUDIANTS = len(etudiants_records)
    
    scores = [record['score'] for record in etudiants_records]
    somme_scores = sum(scores)
    moyenne = somme_scores / len(scores)
    
    max_score = 0
    nom_meilleur = ""
    for record in etudiants_records:
        if record['score'] > max_score:
            max_score = record['score']
            nom_meilleur = record['nom']
            
    print(f"Nombre d'enregistrements valides: {TOTAL_ETUDIANTS}")
    print(f"La moyenne des scores est: {moyenne:.2f}")
    print(f"Meilleur étudiant : {nom_meilleur} avec un score de {max_score}")
    
    return etudiants_records 

if __name__ == "__main__":
    FICHIER_A_ANALISER = "scores.csv" 
    
    resultats_analyse = analyser_scores(FICHIER_A_ANALISER)
    
    if len(resultats_analyse) > 0:
        print(f"Analyse terminée. Total d'étudiants (global): {TOTAL_ETUDIANTS}") 
    else:
        print(f"Analyse échouée. Vérifiez le fichier. Total d'étudiants (global): {TOTAL_ETUDIANTS}")

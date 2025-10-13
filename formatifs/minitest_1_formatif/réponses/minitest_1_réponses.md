## plusieurs réponses différentes seraient acceptées, une réponse partielle donne des points partiels. 

# Question 1
#### Sur quel principe mathématique RSA repose-t-il principalement :

Sur l'exponentiel modulaire et sur le théorème d'Euler 


# Question 2
#### Nommer 2 algorithmes de chiffrement symmétrique.
AES et Chacha20


# Question 3
#### Quand on parle de AES, pourquoi est-il nommé un blok cipher?
Parce que l'algorithme encode un bloc de 128 bits à la fois


# Question 4
#### Pourquoi est-ce que RSA est utilisé plus souvent sur l'échange de clé que sur le chiffrement complet?
Parce que l'algorithme est très lent, surtout avec un long message.

# Question 5
#### Si quelqu'un établit une connexion RSA, que doit-il partager avec ses coéquipiers?
La personne doit partager ses clés publiques.

# Question 6
#### En connaissant p, q et e, est-ce que quelqu'un peut déchiffrer un message envoyé avec RSA?
Oui, il peut trouver n,phi et d à partir de ces informations.

# Question 7 
#### Qu'est-ce que l'analyse de fréquence et comment ceci peut aider à briser l'algorithme César?
L'analyse de fréquence compare la fréquence des caractères dans le texte avec celle du langage utilisé dans le message original. Si on 

# Question 8 
#### Décrivez le protocole pour la création de clés dans TLS.
L'algorithme Diffie-Hellman est utilisé: chaque personne conserve une clé différente et envoie à l'autre personne une version transformée de la clé. À la fin, chacun obtient le même résultat et l'utilise pour créer une nouvelle clé ( ex: AES).

# Question 9
#### Quel est un avantage de TCP versus UDP?
L'intégrité des paquets envoyés est assuré et il n'y a pas de perte de données.

# Question 10
#### À quoi sert la commande ssh-keygen?
Elle sert à créer les clés publique et privées dans le dossier .ssh en Linux.

# Question 11
#### Que siginifie la lettre S dans HTTPS?
Elle siginifie sécuritaire, donc que le protocole TLS est utilisé pour chiffrer les paquets et authentifier la connexion.

# Question 12
#### Quels sont les risques modernes de RSA?
Les ordinateurs quantiques arrivent à factoriser un produit de nombres permiers ave l'algorithme de Shor. 

# Question 13
#### Je chiffre le message 'HELLO WORLD' avec un algo César avec un shift de 4. Quel sera le message résultant?
Le message résultant est 'LIPPS ASVPH'

# Question 14
#### Quelle est la formule que RSA utilise pour chiffrer un message P en message chiffré C?
C = P ** e % n

# Question 15
#### La commande SSH pour se connecter à une instance est 'ssh a@b'. Que sont a et b?
a est le user et b est l'adresse IP.
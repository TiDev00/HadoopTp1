import sys

#Pour prendre les lignes une a une
for line in sys.stdin:
	#Suppression des espaces de debut et de fin
	line = line.strip()
	#Separation des colonnes en utilisant ","
	rues = line.split(",")
	try:
		# On recupere les noms de rue dans la 4e colonne
		rue = rues[3]
		#affichage de la tuple (rue, clé)
		print("%s\t%s" % (rue, "1"))
	#on leve l'exception en cas d'erreur
	except ValueError:
		pass


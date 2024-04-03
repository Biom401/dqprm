import re
import argparse
import csv

fichier = "20200527152905.861802.ig.tum"

def do_it(fic):
	lines = ouverture_fichier(fic)	
	m = extract_SUV(lines)
	h = extract_HU(lines)
	d = sortie_resultats(m)
	csv_file(d, "suv.csv")
	e = sortie_resultats(h)
	csv_file(e, "uh.csv")
	print (d, e)

def parse_file():
	parser = argparse.ArgumentParser()
	parser.add_argument("fichier", help="nom du fichier", type=str)
	return parser.parse_args()

def extract_SUV(chaine):
	m = re.findall("(M.*)(?<!RC)SUVValue = (\d+\.\d+)", chaine, re.M)
	return m

def extract_HU(chaine):
	h = re.findall("(M.*)HUValue = (\d+(\.\d+)?)", chaine, re.M)
	return h

def ouverture_fichier(fic) :
	with open(fic, "r") as f :
		lines = f.read()
	return lines

def sortie_resultats(results):
	d = [(el[0], float(el[1])) for el in results]
	return d

def csv_file(rows, fichier_out):
	with open(fichier_out, "w") as csv_out:
		csv_w = csv.writer(csv_out)
		for row in rows :
			csv_w.writerow(row)

if __name__ == "__main__":
	fic = parse_file()
	do_it(fic.fichier)


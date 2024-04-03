import re
import argparse
import os

fichier = "20200527152905.861802.ig.tum"

def do_it(fic):
	with open(fic, "r") as f :
		lines = f.read()

	m = re.findall("(M.*)(?<!RC)SUVValue = (\d+\.\d+)", lines, re.M)

	d = {el[0]: float(el[1]) for el in m}
	print (d)

def parse_file():
	parser = argparse.ArgumentParser()
	parser.add_argument("fichier", help="nom du fichier", type=str)
	return parser.parse_args()

if __name__ == "__main__":
	fic = parse_file()
	print(fic.fichier)
	do_it(fic.fichier)


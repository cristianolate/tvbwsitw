import requests
from bs4 import BeautifulSoup
import sys, os, csv, getopt

URL_QUERY_BY_RUN = 'https://www.nombrerutyfirma.cl/rut'
URL_QUERY_BY_NAME = 'https://www.nombrerutyfirma.cl/buscar'

class Persona:
	def __init__(self, run_consultado, nombre_consultado, run, nombre, sexo, direccion, comuna):
		self.nombre = nombre
		self.run = run
		self.sexo = sexo
		self.direccion = direccion
		self.comuna = comuna
		self.run_consultado = run_consultado
		self.nombre_consultado = nombre_consultado

	def __str__(self):
		return '{0}: {1}'.format(self.run, self.nombre)
	
	def toArr(self):
		return [self.run_consultado, self.nombre_consultado, self.run, self.nombre, self.sexo, self.direccion, self.comuna]

def getPersonaByRUN(run):
	try:
		r = requests.post(URL_QUERY_BY_RUN, { 'term': run })
		soup = BeautifulSoup(r.text, features='html.parser')
		
		table = soup.find('table')
		table_body = table.find('tbody')
		row = table_body.find('tr')
		cols = row.find_all('td')
		cols = [ele.text.strip() for ele in cols]
	except:
		cols = ['', '', '', '', '']
	return Persona(run.strip(), '', cols[1], cols[0], cols[2], cols[3], cols[4])

def getPersonasByName(name):
	ps = []
	r = requests.post(URL_QUERY_BY_NAME, { 'term': name })
	soup = BeautifulSoup(r.text, features='html.parser')

	try:
		table = soup.find('table')
		table_body = table.find('tbody')

		rows = table_body.find_all('tr')
		if len(rows) == 0:
			ps.append(Persona('', name.strip(), '', '', '', '', ''))

		for row in rows:
			cols = row.find_all('td')
			cols = [ele.text.strip() for ele in cols]
			ps.append(Persona('', name.strip(), cols[1], cols[0], cols[2], cols[3], cols[4]))
	except:
		ps.append(Persona('', name.strip(), '', '', '', '', ''))
	return ps

def queryByRUN(f):
	ps = []
	for line in f:
		ps.append(getPersonaByRUN(line.strip()))
	return ps

def queryByName(f):
	ps = []
	for line in f:
		rs = getPersonasByName(line.strip())
		for r in rs:
			ps.append(r)
	return ps

def main(argv):
	inputfile = 'runs.txt'
	mode = 'run'
	try:
		opts, args = getopt.getopt(argv,"hi:m:",["ifile=","mode="])
	except getopt.GetoptError:
		print ('wbscrpng_nrf.py -i <inputfile> -m <mode>')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print ('wbscrpng_nrf.py -i <inputfile> -m <mode: run/nombre>')
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile = arg.strip()
		elif opt in ("-m", "--mode"):
			mode = arg.strip()

	f = open(inputfile, 'r')
	o_name = os.path.dirname(f.name) + os.path.splitext(os.path.basename(inputfile))[0] + '.csv'

	if(mode == 'run'):
		mapocho = queryByRUN(f)
	else:
		mapocho = queryByName(f)
	f.close()

	g = open(o_name, 'w', newline='', encoding='utf-8')
	wrtr = csv.writer(g, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	wrtr.writerow(['RUN Consultado', 'Nombre Consultado', 'RUN', 'Nombre', 'Sexo', 'Direccion', 'Comuna'])
	for t in mapocho:
		wrtr.writerow(t.toArr())

	print('Archivo creado: ', o_name)
	a = input("Presione cualquier tecla para terminar.")

if __name__ == "__main__":
   main(sys.argv[1:])










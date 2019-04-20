# tvbwsitw
Script de web scraping

1. Instalar Python 3 (para Windows: https://www.python.org/downloads/).
2. Instalar librería requests (con PIP: pip install requests).
3. Instalar librería Beautiful Soup (con PIP: pip install BeautifulSoup4).
4. Para ejecutar con parámetros:
> python wbscrpng_nfl.py -i archivo_entrada -m modo
Donde:
archivo_entrada: ruta completa del archivo de entrada. Valor predeterminado: runs.txt (archivo en el mismo directorio que el script).
modo: contenido del archivo (run o nombre). Valor predeterminado: run (el archivo de entrada contiene RUNs).
Nota: El archivo (de RUNs o Nombres), debe contener un registro por línea.
5. Para ejecutar con parámetros predeterminados (archivo runs.txt y modo run), hacer doble click sobre el script wbscrpng_nfl.py
6 El archivo de resultados (con el mismo nombre que el archivo de entrada, y con extensión CSV), se crea en el mismo directorio que el archivo de entrada.

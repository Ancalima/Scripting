import re
import sys


if len(sys.argv) == 1:
        print ( "no args supplied")
        sys.exit(1)
# Inserire il nome del file da cercare
filename = sys.argv[1]

device = str(filename)
pattern_device = r'([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})'
match_pattern = re.search(pattern_device, device)
device_name = match_pattern.group(0)

# Inserire il nome del file di destinazione
filename2 = 'arp_asa.txt'
#Regex per trovare gli spazi e i punti
spaces = r'\b[^\w\.]+?\b'
#Regex per trovare ID, IPv4 e MAC-Address
pattern = r'(\b\w+\b)(\b[^\w\.]+?\b)(\b([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\b)(\b[^\w\.]+?\b)([\da-f]{4})\.([\da-f]{4})\.([\da-f]{4})'

#Array per scrivere il file
new_file = []

#Apre il file di testo e crea una variabile per ogni linea
f = open(filename, 'r') 
lines = f.readlines()

#Loop che itera ogni linea
for line in lines:
    #Variabile per la contenere ogni linea di: ID, Ipv4 e MAC-Address
    match_line = re.search((pattern),line)
    
    #Se trova un match.
    if match_line :
        #Crea una variabile new_line con il match e aggiunge un newline alla fine
        new_line = match_line.group()
        #Crea una variabile per sostituire gli spazi con |
        new_line = re.sub(spaces, '|', new_line)
        #Appende la nuova line nell'array new_file
        print new_line + '|' + device_name
        #new_file.append(new_line)

#Scrive un nuovo file con il file name inserito all'inizio dello script
#with open(filename2, 'w') as f:
    #f.seek(0)
    #f.writelines(new_file)

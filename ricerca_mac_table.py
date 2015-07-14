import re
import csv
import sys
# Inserire il nome del file da cercare

#if len(sys.argv) == 1:
        #print ( "no args supplied \n")
        #sys.exit(1)
        
filename = 'cisco-mac-10.0.18.10.txt'
#filename = sys.argv[1]

# Inserire il nome del file di destinazione
filename2 = 'mac_table.txt'
#Regex per trovare gli spazi e i punti
spaces = r'\b[^,\w\.\/-]+\b'
#Regex per trovare VLANID e MAC-Address
#pattern = r'(\b\w+\b)(\b[^\w\.]+?\b)(\b([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\b)(\b[^\w\.]+?\b)([\da-f]{4})\.([\da-f]{4})\.([\da-f]{4})'
pattern = r'(\d+)(\b[^\w\.]+?\b)([\da-f]{4})\.([\da-f]{4})\.([\da-f]{4})(\b[^\w\.]+?\b)(\b\w+\b).*(\b[^\w\.]+?\b)([\w\/-]+)'
#pattern2 = r'(\w[^\w]+)(\b[^\w\.]+?\b)(\w-\w\w)'
#Array per scrivere il file
new_file = []

#Apre il file di testo e crea una variabile per ogni linea
f = open(filename, 'r') 
lines = f.readlines()

#Loop che itera ogni linea
for line in lines:
    #Variabile per la contenere ogni linea di: VLANID, Com'è stato imparato il mac e MAC-Address
    match_line = re.search(pattern,line)
    #match_port = re.search(pattern2,line)
    
    #Se trova un match.
    if match_line :
        #Crea una variabile new_line con il match e aggiunge un newline alla fine
        new_line = match_line.group()
        #Modifica la variabile per sostituire gli spazi con |
        new_line = re.sub(spaces, '|', new_line)
        #Appende la nuova line nell'array new_file
        print(new_line)
        #new_file.append(new_line)
    #if match_port:
        #Crea una variabile new_line con il match e aggiunge un newline alla fine
        #new_line = match_line.group() + '\n'
        #Crea una variabile per sostituire gli spazi con |
        #new_line = re.sub(spaces, '|', new_line)
        #Appende la nuova line nell'array new_file
        #new_file.append(new_line)        
        

#Scrive un nuovo file con il file name inserito all'inizio dello script
#with open(filename2, 'w') as f:
    #f.seek(0)
    #f.writelines(new_file)

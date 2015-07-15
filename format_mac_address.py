import re
import sys

if len(sys.argv) == 1:
        print ( "no args supplied")
        sys.exit(1)
#Inserire il nome del file da cercare
#filename = 'linux-arp-10.0.18.3.txt'

filename = #sys.argv[1]
# Inserire il nome del file di destinazione

#RegExp per trovare i : e il mac address senza punteggiatura
pattern = r'\:'
pattern2 = r'([a-f0-9]{4})([a-f0-9]{4})([a-f0-9]{4})'


#Apre il file di testo e crea una variabile per ogni linea
f = open(filename, 'r') 
lines = f.readlines()
    
for line in lines:
     
    new_line = line
    
    new_line = re.sub(pattern, '', new_line)
    
    new_line = re.sub(pattern2, r'\1.\2.\3', new_line)
    
    new_line = re.sub(r'\n', '', new_line)
    
    print (new_line)


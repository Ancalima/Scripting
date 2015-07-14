import re
import sys

#if len(sys.argv) == 1:
        #print ( "no args supplied")
        #sys.exit(1)
#Inserire il nome del file da cercare
#filename = 'linux-arp-10.0.18.3.txt'

filename = 'linux-arp-10.0.18.3.txt'#sys.argv[1]
# Inserire il nome del file di destinazione
filename2 = 'arp_linux.txt'
#filename3 = 'correzione.txt'
#filename4 = 'arp_trovati3prova.txt'
#filename5 = 'arp_trovati3prova2.txt'
#filename6 = 'arp_trovati3prova3.txt'
#Regex per trovare gli spazi e i punti
spaces = r'(\b\s)'
spaces2 = r'(\s)*'
pipe = r'(\|$)'
#Regex per trovare ID, IPv4 e MAC-Address
#pattern = r'(\b[^\w\.\?]+?\b)(\b[^\w\.\(]+?\b)(\b([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\b)(\b[^\w\.]+?\b)([\da-f]{4})\.([\da-f]{4})\.([\da-f]{4})'

pattern = r'([^\s]+)'
pattern2 = r'([\(\)])'
pattern3 = r'(\bat\b)'
pattern4 = r'(\?)'
pattern5 = r'([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F])'
pattern6 = r'([A-F0-9]{12})'
pattern7 = r'(\:)'
pattern8 = r'([a-f0-9]{4})([a-f0-9]{4})([a-f0-9]{4})'
pattern9 = r'([\[\]])'
pattern10 = r'(\bether\b)'
pattern11 = r'(\bon\b)'



#Array per scrivere il file
new_file = []
new_file2 = []
new_file3 = []
new_file4 = []
new_file5 = []

#Apre il file di testo e crea una variabile per ogni linea
f = open(filename, 'r') 
lines = f.readlines()
    
for line in lines:
    
    match_parenthesis = re.search(pattern2, line)
    match_at = re.search(pattern3, line)

    
    
    if match_parenthesis:
        
        new_line = line
        
        new_line = re.sub(pattern2, '', new_line)
        
        new_line = re.sub(pattern3, '', new_line)
        
        new_line = re.sub(pattern4, '', new_line)
        
        new_line = re.sub(pattern9, '', new_line)
        
        new_line = re.sub(pattern10, '', new_line)
        
        new_line = re.sub(pattern11, '', new_line)
        
        new_file2.append(new_line)
        

for line in new_file2:
    match_mac = re.search(pattern5, line)
    
    if match_mac:
        
        new_line2 = line                  
        
        new_line2 = re.sub(pattern7, '', new_line2)
        
        new_file3.append(new_line2)
       
    
    
for line in new_file3:
    match_mac2 = re.search(pattern6, line)
    match_mac3 = re.search(pattern8, line)
    if match_mac2:
        new_line = line
        
        new_mac = ''
        
        new_mac = match_mac2.group(0)
        
        new_mac = new_mac.lower()
        
        new_line = re.sub(pattern6, new_mac, new_line)
        
        new_line = re.sub(pattern8, r'\1.\2.\3', new_line)
        
        new_file4.append(new_line)
            
    
                    
#with open(filename5, 'r') as t:
    #lines = t.readlines()     
    
    #for line in lines:
        #match_mac3 = re.search(pattern8, line)
        #if match_mac3:
            #new_line = line
            
            #new_line = match_mac3.match() + '.' + match_mac3.match() + '.' match_mac3.match()
            
            
            #new_file5.append(new_line)       
            
            


#Loop che itera ogni linea
for line in new_file4:
    #Variabile per la contenere ogni linea di: ID, Ipv4 e MAC-Addres
    #Crea una variabile new_line con il match e aggiunge un newline alla fine
    new_line = line 
    #Crea una variabile per sostituire gli spazi con |
    
    #new_line = re.sub(pattern8, r'\1.\2.\3', new_line)
    
    new_line = re.sub(spaces, '|', new_line)
    
    new_line = re.sub(spaces2, '', new_line)
    
    new_line = re.sub(pipe, '', new_line)
    #Appende la nuova line nell'array new_file
    print(new_line)
    #new_file.append(new_line)

#Scrive un nuovo file con il file name inserito all'inizio dello script
#with open(filename3, 'w') as f:
    #f.seek(0)
    #f.writelines(new_file2)
    

#with open(filename4, 'w') as f:
    #f.seek(0)
    #f.writelines(new_file3)

#with open(filename5, 'w') as f:
    #f.seek(0)
    #f.writelines(new_file4)
    
#with open(filename6, 'w') as f:
    #f.seek(0)
    #f.writelines(new_file5)

#with open(filename2, 'w') as f:
    #f.seek(0)
    #f.writelines(new_file)

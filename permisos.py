# !/usr/bin/python
# coding:utf-8

import os, stat

#Ruta a explorar
path_to_explore="./cartes-i-daus/"

#Variable de pes total 
total_size=0
        
# Mostrem ruta tot    
for root, dirs, files in os.walk(path_to_explore):
    for name in files:
		
		#Juntem la ruta amb el nom de l'arxiu
        name_path=os.path.join(root, name)
        print "* * * * * *  * "
        #Imprimim la ruta amb el nom de l'arxiu
        print(name_path) ,
        
        #Adjuntem el pes de l'arxiu al final 
        print os.stat(name_path).st_size , 
        print "bytes"
        #Incrementem el valor total del pes del directori 
        total_size=total_size+os.stat(name_path).st_size
        
        #Detectem els permisos i els imprimim en octal  
        permissions = stat.S_IMODE ( os.stat (name_path).st_mode )
        permisos = str(oct(permissions))
        print "Permisos: ", permisos
        
        #Ara fem un substring i ens quedem amb l'ultim nombre. 
        # 0770 --> Del 3r al 4t - 1 == 0
        others = permisos[3:4]
        
        #Fem la condició per avisar si està bé o no. 
        if (others == "0"):
			print "Tot correcte"
        else:
			print "Els others tenen permisos per a aquest fitxer"
			

 
print "El tamany total en Bytes es:" , total_size

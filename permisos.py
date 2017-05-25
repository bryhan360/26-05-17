# !/usr/bin/python
# coding:utf-8

import os, stat

#Raiz
path_to_explore="./Ejercicio_walk/"

#Variable de tamaño 
total_size=0
        
# Muestra ruta de todo    
for root, dirs, files in os.walk(path_to_explore):
    for name in files:
		
		#Junta la ruta con el nombre de archivo
        name_path=os.path.join(root, name)
        print "* * * * * *  * "
        #muestra la ruta con nombre de archivo
        print(name_path) ,
        
        #muestra el peso total del archivo 
        print os.stat(name_path).st_size , 
        print "bytes"
        #Incremento del tamaño del directorio
        total_size=total_size+os.stat(name_path).st_size
        
          
        permissions = stat.S_IMODE ( os.stat (name_path).st_mode )
        permisos = str(oct(permissions))
        print "Permisos: ", permisos
        
         
        # 0770 --> Del 3r al 4t - 1 == 0
        others = permisos[3:4]
        
        
        if (others == "0"):
			print "los otros no tienen permiso"
        else:
			print "otros tienen permisos"
			

 
print "El tamaño total en Bytes es:" , total_size

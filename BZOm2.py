#!/usr/bin/env python
import ftplib
import os
import string
def darchivos(f): # Funcion encargada de descargar archivos del servidor
    try:
        print ("   [/]Inserte el nombre del archivo a descargar")
        archivoserv = input("Nombre>")
            
        print ("		[+]Ahora inserte el nombre del archivo para guardar en su sistema")
        archivodir = input("Nombre>")
        t = open(archivodir,"wb")
        f.retrbinary('RETR %s' %archivoserv,t.write)
        print ("[+]!Descarga completada con exito!")
        f.quit()
        f.close()
    except:
        print ("[-]No se ha podido descargar el archivo, compruebe la insercion del nombre")
        input()
        os.system("clear")
        for p in f.nlst():
            print (p)
        darchivos(f)


def archivos(f): # Funcion encargada de subir archivos al servidor
    try:
        print ("Inserte el nombre del archivo a subir junto con su directorio")
        archivo_origen = input("Nombre>")
        t = open(archivo_origen,'rb')
    except:
        print ("Error,el archivo no existe,retornando")
        input()
        os.system("clear")
        archivos(f)
    print ("Inserte ahora el nombre que tomara el archivo en el servidor")
    archivo_destino = input("Nombre>")
    try:
        f.storbinary('STOR %s' %archivo_destino,t)
        f.quit()
        f.close()
    except:
        print ("No se ha podido subir el archivo, retornando")
        input()
        os.system("clear")
        archivos(f)
	
	
def mostrar_directorios(f): # Funcion que recorre los directorios del servidor
    
    try:
        os.system("clear")
        print ("[+] Directorios:")
        for x in f.nlst():
            print (x)
        print ("[/] Elija directorio")
        directorio = input("Directorio>")
        f.cwd(directorio)
        os.system("clear")
    except:
        print ("[+] El directorio introducido no es valido retornando")
        input()
        os.system("clear")
        f.quit()
        f.close()
        main()
    
    print ("[+] Directorios  ",directorio,"\n\n")
    for x in f.nlst():
        print (x)
    print ("Desea investigar otro directorio?")
    eleccion = input("Si o No?>")	
    eleccion = eleccion.upper()
    if eleccion == 'SI':
        while eleccion == 'SI':
            try:
                print ("[/] Elija Directorio:")
                directoriox = input("Directorio>")
                f.cwd(directoriox)
                os.system("clear")
                print ("[+] Directorios  ",directoriox,"\n\n")
                for s in f.nlst():
                    print (s)
            except:
                print ("El nombre introducido no existe o no es un directorio,retornando")
                input()
                os.system("clear")
                main()
                                            
            print ("[+] Desea investigar otro directorio?")
            eleccion = input("Si o No?>")
            eleccion = eleccion.upper()	
            if eleccion == 'NO':
                print ("[+] Que funcion quiere llevar a cabo?")
                print ("--> Subir Archivos (Subir)")
                print ("--> Descargar Archivos (Descargar)")
                eleccion3 = input("Eleccion>")
                eleccion3 = eleccion3.upper()
                if eleccion3 == "SUBIR":
                    archivos(f)
                elif eleccion3 == "DESCARGAR":
                    darchivos(f)
                else:
                    print ("El valor introducido no es valido")
                    input()
                    os.system("clear")
                    f.quit()
                    f.close()
                    main()
            elif eleccion != 'SI' and eleccion != 'NO':
                print ("[/] No es una opcion valida, retornando")
                input()
                os.system("clear")
                f.quit()
                f.close()
                main()
    elif eleccion == 'NO':
        print ("[+] Que funcion quiere llevar a cabo?")
        print ("--> Subir Archivos (Subir)")
        print("--> Descargar Archivos (Descargar)")
        eleccion3 = input("Eleccion>")
        eleccion3 = eleccion3.upper()
        if eleccion3 == "SUBIR":
            archivos(f)
        elif eleccion3 == "DESCARGAR":
            darchivos(f)
        else:
            print ("El valor introducido no es valido")
            input()
            os.system("clear")
            f.quit()
            f.close()
            main()
        
    else:
        print ("El valor introducido no es valido")
        input()
        os.system("clear")
        f.quit()
        f.close()
        main()
    
    
            
    
    
    

def entrarFtp(web): # Funcion encargada de conectar al servidor dando user y pass
    try:
        f = ftplib.FTP(web)
        print (f.getwelcome())		
    except:
        
        print ("[+] El servidor es incorrecto, retornando")
        input()
        os.system("clear")
        main()
    try:	
        user = input("User>")
        pasd = input("Pass>")
        f.login(user,pasd)
        mostrar_directorios(f)
        
    
    except:
        
        print ("[+] El user o la pass es incorrecto")
        input()
        os.system("clear")
        f.quit()
        f.close()
        main()



def main(): # Funcion Principal Main
    print (""" F3NiX   """)			
    print ("[/]Introduzca el servidor ftp")
    web = input("FTP>")
    entrarFtp(web)

main()







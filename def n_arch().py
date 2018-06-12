def n_arch()
    print("Introduce el NOMBRE de Tu Nuevo Archivo: ")
    nom= input()
    print("Introduce el FORMATO de Tu Nuevo Archivo: ")
    tipo= input()

    newArc= (nom + "." + tipo)

    archivo=open(newArc, "a")

    print("Introduce la informacion: ")
    x= input()
    archivo.write("\n")
    archivo.write(x)
    archivo.write("\n")
    archivo.write("Este es el final del archivo")

    archivo.close()

----------------------------------------------------------------------------------

New-AzureRmVm `
    -ResourceGroupName "myResourceGroup" `
    -Name "myVM" `
    -Location "East US" `
    -VirtualNetworkName "myVnet" `
    -SubnetName "mySubnet" `
    -SecurityGroupName "myNetworkSecurityGroup" `
    -PublicIpAddressName "myPublicIpAddress" `
    -OpenPorts 80,3389
---------------------------------------------------------------------

Windows
Cuenta:    fnqyaxl@gmail.com
Hora:    30 de diciembre de 2017
Ubicación:    Baja California Sur, México
Dirección IP:    189.172.77.206

--------------------------------------------------------------

fenix.txt


filiberto navarro quintero
Este es el final del archivo


Bzo_Jugando_.py

# Bzo_Jugando_.py

lst_d0= dir() 
"""Crea una lista con los elementos predefinidos del Directorio Raiz,  mamada=["lst_d" + n_v + ":" + " "*args"]      """

import re,sys,os,glob,bzo
from tkinter import * 
import tkinter

def bzo_in(self, n= 0, *args):
	return lambda x: x + self, n, args

# Leemos el archivo a una cadena:
f = open( 'BZO_PS_Azure_FindCommand.txt' )
datos = f.read()
# Partimos la cadena a una lista cuyos elementos son
# los registros de nuestra â€™base de datosâ€™

import string
lista = string.split( datos, '\n' )
print(lista)
# Convertimos cada elemento de la lista a una pareja,
# usamos una funciÃ³n lambda:
pares = map( lambda e: string.split( e, ','), lista )
print (pares)
'''
# Podemos crear una lista para cada campo:
# una lista de capitales y otra lista de estados.
# Esta es una forma de obtenerlas:
capitales = []
estados = []
for capital,estado in pares:
capitales.append( capital )
estados.append( estado )
# CÃ³mo determinar los nombres Ãºnicos de ambas listas?
# Usamos la concatenaciÂ´ on de listas.
unicos = []
for nombre in capitales+estados:
if nombre not in unicos:
unicos.append(nombre)
else:
print (nombre)
'''


bzo_pluings_subli_.py

#import sublime
#import sublime_plugin


class ExampleCommand(.TextCommand):
	def run(self, edit):
		self.view.insert(edit, 0, "Hello, World!")


cssmin.py

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""`cssmin` - A Python port of the YUI CSS compressor."""

try:
    from StringIO import StringIO # The pure-Python StringIO supports unicode.
except ImportError:
    from io import StringIO
import re


__version__ = '0.2.0'


def remove_comments(css):
    """Remove all CSS comment blocks."""

    iemac = False
    preserve = False
    comment_start = css.find("/*")
    while comment_start >= 0:
        # Preserve comments that look like `/*!...*/`.
        # Slicing is used to make sure we don"t get an IndexError.
        preserve = css[comment_start + 2:comment_start + 3] == "!"

        comment_end = css.find("*/", comment_start + 2)
        if comment_end < 0:
            if not preserve:
                css = css[:comment_start]
                break
        elif comment_end >= (comment_start + 2):
            if css[comment_end - 1] == "\\":
                # This is an IE Mac-specific comment; leave this one and the
                # following one alone.
                comment_start = comment_end + 2
                iemac = True
            elif iemac:
                comment_start = comment_end + 2
                iemac = False
            elif not preserve:
                css = css[:comment_start] + css[comment_end + 2:]
            else:
                comment_start = comment_end + 2
        comment_start = css.find("/*", comment_start)

    return css


def remove_unnecessary_whitespace(css):
    """Remove unnecessary whitespace characters."""

    def pseudoclasscolon(css):

        """
        Prevents 'p :link' from becoming 'p:link'.

        Translates 'p :link' into 'p ___PSEUDOCLASSCOLON___link'; this is
        translated back again later.
        """

        regex = re.compile(r"(^|\})(([^\{\:])+\:)+([^\{]*\{)")
        match = regex.search(css)
        while match:
            css = ''.join([
                css[:match.start()],
                match.group().replace(":", "___PSEUDOCLASSCOLON___"),
                css[match.end():]])
            match = regex.search(css)
        return css

    css = pseudoclasscolon(css)
    # Remove spaces from before things.
    css = re.sub(r"\s+([!{};:>+\(\)\],])", r"\1", css)

    # If there is a `@charset`, then only allow one, and move to the beginning.
    css = re.sub(r"^(.*)(@charset \"[^\"]*\";)", r"\2\1", css)
    css = re.sub(r"^(\s*@charset [^;]+;\s*)+", r"\1", css)

    # Put the space back in for a few cases, such as `@media screen` and
    # `(-webkit-min-device-pixel-ratio:0)`.
    css = re.sub(r"\band\(", "and (", css)

    # Put the colons back.
    css = css.replace('___PSEUDOCLASSCOLON___', ':')

    # Remove spaces from after things.
    css = re.sub(r"([!{}:;>+\(\[,])\s+", r"\1", css)

    return css


def remove_unnecessary_semicolons(css):
    """Remove unnecessary semicolons."""

    return re.sub(r";+\}", "}", css)


def remove_empty_rules(css):
    """Remove empty rules."""

    return re.sub(r"[^\}\{]+\{\}", "", css)


def normalize_rgb_colors_to_hex(css):
    """Convert `rgb(51,102,153)` to `#336699`."""

    regex = re.compile(r"rgb\s*\(\s*([0-9,\s]+)\s*\)")
    match = regex.search(css)
    while match:
        colors = map(lambda s: s.strip(), match.group(1).split(","))
        hexcolor = '#%.2x%.2x%.2x' % tuple(map(int, colors))
        css = css.replace(match.group(), hexcolor)
        match = regex.search(css)
    return css


def condense_zero_units(css):
    """Replace `0(px, em, %, etc)` with `0`."""

    return re.sub(r"([\s:])(0)(px|em|%|in|cm|mm|pc|pt|ex)", r"\1\2", css)


def condense_multidimensional_zeros(css):
    """Replace `:0 0 0 0;`, `:0 0 0;` etc. with `:0;`."""

    css = css.replace(":0 0 0 0;", ":0;")
    css = css.replace(":0 0 0;", ":0;")
    css = css.replace(":0 0;", ":0;")

    # Revert `background-position:0;` to the valid `background-position:0 0;`.
    css = css.replace("background-position:0;", "background-position:0 0;")

    return css


def condense_floating_points(css):
    """Replace `0.6` with `.6` where possible."""

    return re.sub(r"(:|\s)0+\.(\d+)", r"\1.\2", css)


def condense_hex_colors(css):
    """Shorten colors from #AABBCC to #ABC where possible."""

    regex = re.compile(r"([^\"'=\s])(\s*)#([0-9a-fA-F])([0-9a-fA-F])([0-9a-fA-F])([0-9a-fA-F])([0-9a-fA-F])([0-9a-fA-F])")
    match = regex.search(css)
    while match:
        first = match.group(3) + match.group(5) + match.group(7)
        second = match.group(4) + match.group(6) + match.group(8)
        if first.lower() == second.lower():
            css = css.replace(match.group(), match.group(1) + match.group(2) + '#' + first)
            match = regex.search(css, match.end() - 3)
        else:
            match = regex.search(css, match.end())
    return css


def condense_whitespace(css):
    """Condense multiple adjacent whitespace characters into one."""

    return re.sub(r"\s+", " ", css)


def condense_semicolons(css):
    """Condense multiple adjacent semicolon characters into one."""

    return re.sub(r";;+", ";", css)


def wrap_css_lines(css, line_length):
    """Wrap the lines of the given CSS to an approximate length."""

    lines = []
    line_start = 0
    for i, char in enumerate(css):
        # It's safe to break after `}` characters.
        if char == '}' and (i - line_start >= line_length):
            lines.append(css[line_start:i + 1])
            line_start = i + 1

    if line_start < len(css):
        lines.append(css[line_start:])
    return '\n'.join(lines)


def cssmin(css, wrap=None):
    css = remove_comments(css)
    css = condense_whitespace(css)
    # A pseudo class for the Box Model Hack
    # (see http://tantek.com/CSS/Examples/boxmodelhack.html)
    css = css.replace('"\\"}\\""', "___PSEUDOCLASSBMH___")
    css = remove_unnecessary_whitespace(css)
    css = remove_unnecessary_semicolons(css)
    css = condense_zero_units(css)
    css = condense_multidimensional_zeros(css)
    css = condense_floating_points(css)
    css = normalize_rgb_colors_to_hex(css)
    css = condense_hex_colors(css)
    if wrap is not None:
        css = wrap_css_lines(css, wrap)
    css = css.replace("___PSEUDOCLASSBMH___", '"\\"}\\""')
    css = condense_semicolons(css)
    return css.strip()


def main():
    import optparse
    import sys

    p = optparse.OptionParser(
        prog="cssmin", version=__version__,
        usage="%prog [--wrap N]",
        description="""Reads raw CSS from stdin, and writes compressed CSS to stdout.""")

    p.add_option(
        '-w', '--wrap', type='int', default=None, metavar='N',
        help="Wrap output to approximately N chars per line.")

    options, args = p.parse_args()
    sys.stdout.write(cssmin(sys.stdin.read(), wrap=options.wrap))


if __name__ == '__main__':
    main()


F3NiX_009.py

def n_arch()
	print("Introduce el NOMBRE de Tu Nuevo Archivo: ")
	nom= input()
	print("Introduce el FORMATO de Tu Nuevo Archivo: ")
	tipo= input()

	newArc= (nom + "." + tipo)

	archivo=open(newArc, "a")																																																																																																																																			

	print("Introduce la informacion: ")
	x= input()
	archivo.write("\n")
	archivo.write(x)
	archivo.write("\n")
	archivo.write("Este es el final del archivo")

	archivo.close()


F3NiX_010 (2).py


from tkinter import *

vp= Tk()

vp.title("db__F3NiX__db")

vp.mainloop()











F3NiX_010.py

import tkinter
from tkinter import *


def j0():
	print("J0K3R")


def vp():
	vp= Tk()
	vp.title("db__F3NiX__db")
	vp.configure(background ='dark turquoise')

	b1=Button(vp, text="SALIR", fg="dark red", command=vp.quit)
	b1.pack(side=TOP)
    
	b2=Button(vp, text="FUCK", fg="green", command=vp.quit)
	b2.pack(side=TOP)
	

	vp.mainloop()
vp()


FiliVentana.py


from  tkinter import *


#def imprime():
  #  print("Presinastes IMPRIMIR")


fiV=Tk()


#fV.title("Fili_Ventana")

#b1=Button(fv, text="SALIR", fg="red", command=fv.quit)
#b1.pack(side=LEFT)

#b2=Button(fv, text="IMPRIMIR", fg="blue", command=imprime)
#b2.pack(side=RIGHT)




# fv.title("Primera Ventana")
# fv.geometry('380x300')  # Ancho x Alto 
#fv.configure(background = 'dark turquoise')





fiv.mainloop()







Ftp Client V6_Bzo_.py

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


jsmin.py

#!/usr/bin/env

# This code is original from jsmin by Douglas Crockford, it was translated to
# Python by Baruch Even. It was rewritten by Dave St.Germain for speed.
#
# The MIT License (MIT)
#
# Copyright (c) 2013 Dave St.Germain
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


import sys
is_3 = sys.version_info >= (3, 0)
if is_3:
    import io
else:
    import StringIO
    try:
        import cStringIO
    except ImportError:
        cStringIO = None


__all__ = ['jsmin', 'JavascriptMinify']
__version__ = '2.1.6'


def jsmin(js, **kwargs):
    """
    returns a minified version of the javascript string
    """
    if not is_3:
        if cStringIO and not isinstance(js, unicode):
            # strings can use cStringIO for a 3x performance
            # improvement, but unicode (in python2) cannot
            klass = cStringIO.StringIO
        else:
            klass = StringIO.StringIO
    else:
        klass = io.StringIO
    ins = klass(js)
    outs = klass()
    JavascriptMinify(ins, outs, **kwargs).minify()
    return outs.getvalue()


class JavascriptMinify(object):
    """
    Minify an input stream of javascript, writing
    to an output stream
    """

    def __init__(self, instream=None, outstream=None, quote_chars="'\""):
        self.ins = instream
        self.outs = outstream
        self.quote_chars = quote_chars

    def minify(self, instream=None, outstream=None):
        if instream and outstream:
            self.ins, self.outs = instream, outstream

        self.is_return = False
        self.return_buf = ''

        def write(char):
            # all of this is to support literal regular expressions.
            # sigh
            if char in 'return':
                self.return_buf += char
                self.is_return = self.return_buf == 'return'
            else:
                self.return_buf = ''
            self.outs.write(char)
            if self.is_return:
                self.return_buf = ''

        read = self.ins.read

        space_strings = "abcdefghijklmnopqrstuvwxyz"\
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_$\\"
        self.space_strings = space_strings
        starters, enders = '{[(+-', '}])+-/' + self.quote_chars
        newlinestart_strings = starters + space_strings + self.quote_chars
        newlineend_strings = enders + space_strings + self.quote_chars
        self.newlinestart_strings = newlinestart_strings
        self.newlineend_strings = newlineend_strings

        do_newline = False
        do_space = False
        escape_slash_count = 0
        in_quote = ''
        quote_buf = []

        previous = ';'
        previous_non_space = ';'
        next1 = read(1)

        while next1:
            next2 = read(1)
            if in_quote:
                quote_buf.append(next1)

                if next1 == in_quote:
                    numslashes = 0
                    for c in reversed(quote_buf[:-1]):
                        if c != '\\':
                            break
                        else:
                            numslashes += 1
                    if numslashes % 2 == 0:
                        in_quote = ''
                        write(''.join(quote_buf))
            elif next1 in '\r\n':
                next2, do_newline = self.newline(
                    previous_non_space, next2, do_newline)
            elif next1 < '!':
                if (previous_non_space in space_strings \
                    or previous_non_space > '~') \
                    and (next2 in space_strings or next2 > '~'):
                    do_space = True
                elif previous_non_space in '-+' and next2 == previous_non_space:
                    # protect against + ++ or - -- sequences
                    do_space = True
                elif self.is_return and next2 == '/':
                    # returning a regex...
                    write(' ')
            elif next1 == '/':
                if do_space:
                    write(' ')
                if next2 == '/':
                    # Line comment: treat it as a newline, but skip it
                    next2 = self.line_comment(next1, next2)
                    next1 = '\n'
                    next2, do_newline = self.newline(
                        previous_non_space, next2, do_newline)
                elif next2 == '*':
                    self.block_comment(next1, next2)
                    next2 = read(1)
                    if previous_non_space in space_strings:
                        do_space = True
                    next1 = previous
                else:
                    if previous_non_space in '{(,=:[?!&|;' or self.is_return:
                        self.regex_literal(next1, next2)
                        # hackish: after regex literal next1 is still /
                        # (it was the initial /, now it's the last /)
                        next2 = read(1)
                    else:
                        write('/')
            else:
                if do_newline:
                    write('\n')
                    do_newline = False
                    do_space = False
                if do_space:
                    do_space = False
                    write(' ')

                write(next1)
                if next1 in self.quote_chars:
                    in_quote = next1
                    quote_buf = []

            if next1 >= '!':
                previous_non_space = next1

            if next1 == '\\':
                escape_slash_count += 1
            else:
                escape_slash_count = 0

            previous = next1
            next1 = next2

    def regex_literal(self, next1, next2):
        assert next1 == '/'  # otherwise we should not be called!

        self.return_buf = ''

        read = self.ins.read
        write = self.outs.write

        in_char_class = False

        write('/')

        next = next2
        while next != '/' or in_char_class:
            write(next)
            if next == '\\':
                write(read(1))  # whatever is next is escaped
            elif next == '[':
                write(read(1))  # character class cannot be empty
                in_char_class = True
            elif next == ']':
                in_char_class = False
            next = read(1)

        write('/')

    def line_comment(self, next1, next2):
        assert next1 == next2 == '/'

        read = self.ins.read

        while next1 and next1 not in '\r\n':
            next1 = read(1)
        while next1 and next1 in '\r\n':
            next1 = read(1)

        return next1

    def block_comment(self, next1, next2):
        assert next1 == '/'
        assert next2 == '*'

        read = self.ins.read

        # Skip past first /* and avoid catching on /*/...*/
        next1 = read(1)
        next2 = read(1)
        while next1 != '*' or next2 != '/':
            next1 = next2
            next2 = read(1)

    def newline(self, previous_non_space, next2, do_newline):
        read = self.ins.read

        if previous_non_space and (
                        previous_non_space in self.newlineend_strings
                        or previous_non_space > '~'):
            while 1:
                if next2 < '!':
                    next2 = read(1)
                    if not next2:
                        break
                else:
                    if next2 in self.newlinestart_strings \
                            or next2 > '~' or next2 == '/':
                        do_newline = True
                    break

        return next2, do_newline

if __name__ == '__main__':
	import sys, os, glob

#for f in sys.argv[1:]:
#    with open(f, 'r') as js:
#        minifier = JavascriptMinify(js, sys.stdout)
#        minifier.minify()
#    sys.stdout.write('\n')

	minifier = JavascriptMinify(sys.stdin, sys.stdout)
	minifier.minify()
	sys.stdout.write('\n')


link_bzo_.py

#-*-coding:utf-8 -*- 
class Node(object):
 def __init__(self,data,next = None): 
 	self.data = data 
 	self.next = next 
 class linklist(object): 
 	def __init__(self): self.head = 0
 	def Initiallist(self, data): 
 	 	if len(data) == 1: 
 	 		self.head = Node(data[0]) 
 	 	else: 
 	 		self.head = Node(data[0]) 
 	 		p = self.head 
 	 		for i in data[1:]:
 	 			p.next = Node(i) 
 	 		p = p.next 
 	 		return 
 	def IsEmptylist(self): 
 	 	return self.head == 0 
 	def Printlist(self): 
 	 	if self.IsEmptylist():
 				print("Linklist Is Empty!")
 	 	else: 
 	 		p = self.head 
 	 	while p!= None: 
 	 		print(p.data)
 	 		p = p.next 
 	 		def Lengthlist(self): 
 	 			length = 0 
 	 			p = self.head 
 	 			while p!= None: 
 	 				p = p.next 
 	 				length = length + 1 
 	 			return length 
 	 			def Clearlist(self): self.head = 0 
 	 			def Insertlist(self,data,Index): 
 	 				if Index < 0 or Index > self.Lengthlist(): 
 	 					print ("The Index Is Wrong!" )

 	 				elif Index == 0: 
 	 					newnode = Node(data) 
 	 					p = self.head 
 	 					newnode.next = p 
 	 					self.head = newnode 
 	 				elif Index == self.Lengthlist(): 
 	 					p = self.head 
 	 				newnode = Node(data) 
 	 				i = 1 
 	 			while i < Index: 
 	 				p = p.next 
 	 				i = i + 1 
 	 				p.next = newnode 
 	 			else: i = 1 
 	 			p = self.head 
 	 		newnode = Node(data) 
 	 		while i < Index: 
 	 			p = p.next 
 	 			i = i + 1 
 	 		newnode.next = p.next 
 	 		p.next = newnode 
 	 		def Deletelist(self,Index): 
 	 			if Index < 0 or Index > self.Lengthlist()-1: 
 	 				print ("The Index Is Wrong!" )
 	 			if Index == 0: 
 	 						p = self.head 
 	 						self.head = p.next 
 	 			elif Index == self.Lengthlist()-1: 
 	 				i = 1
 	 				p = self.head 
 	 				while i < Index: 
 	 				 	p = p.next 
 	 				 	i = i + 1 
 	 				p.next = None 
 	 			else: 
 	 					i = 1 
 	 					p = self.head 
 	 					while i < Index: 
 	 						p = p.next 
 	 						i = i + 1 
 	 					p.next = p.next.next 
 	 			def GetElemlist(self,Index): 
 	 					if Index == 0: 
 	 						p = self.head 
 	 					else: 
 	 						p = self.head 
 	 						i = 0 
 	 						while i < Index: 
 	 							p = p.next 
 	 							i = i + 1 
 	 							return p.data 
 	 							if __name__ == '__main__': 
 	 								Linklist = linklist() 
 	 								Linklist.Initiallist([1,2,3,4,5,67,8]) 
 	 								Linklist.Insertlist(5,7) 
 	 								Linklist.Printlist() 
 	 								Linklist.Deletelist(6) 
 	 								Linklist.Printlist() 
 	 								Linklist.Clearlist() 
 	 								Linklist.Printlist()


Mi_Ventana.py

# -*- coding: utf-8 -*-
"""
Editor de Spyder

"""
"sty"

from tkinter import *

def bzo_Vp():
	ventana = Tk()
	return bzo_Vp
	ventana.title("Primera Ventana")
	ventana.geometry('380x300')  # Ancho x Alto
	ventana.configure(background = 'dark turquoise')

	etiqueta = title("6__AKER__9")
	etiqueta.pack()
	bzo_Vp.mainloop(ventana)
	print(bzo_Vp)
bzo_Vp()					

























'''
[main]
single_instance = True
open_files_port = 21128
tear_off_menus = False
normal_screen_resolution = True
high_dpi_scaling = False
high_dpi_custom_scale_factor = False
high_dpi_custom_scale_factors = 1.5
vertical_dockwidget_titlebars = False
vertical_tabs = False
animated_docks = True
prompt_on_exit = False
panes_locked = True
window/size = (1260, 740)
window/position = (10, 10)
window/is_maximized = True
window/is_fullscreen = False
window/prefs_dialog_size = (745, 411)
show_status_bar = True
memory_usage/enable = True
memory_usage/timeout = 2000
cpu_usage/enable = False
cpu_usage/timeout = 2000
use_custom_margin = True
custom_margin = 10
show_internal_console_if_traceback = False
check_updates_on_startup = False
toolbars_visible = True
font/family = ['Monospace', 'DejaVu Sans Mono', 'Consolas', 'Bitstream Vera Sans Mono', 'Andale Mono', 'Liberation Mono', 'Courier New', 'Courier', 'monospace', 'Fixed', 'Terminal']
font/size = 10
font/italic = False
font/bold = True
rich_font/family = ['Sans Serif', 'DejaVu Sans', 'Bitstream Vera Sans', 'Bitstream Charter', 'Lucida Grande', 'MS Shell Dlg 2', 'Calibri', 'Verdana', 'Geneva', 'Lucid', 'Arial', 'Helvetica', 'Avant Garde', 'Times', 'sans-serif']
rich_font/size = 10
rich_font/italic = False
rich_font/bold = False
cursor/width = 2
completion/size = (300, 180)
crash = False
windows_style = windowsvista

spyder_pythonpath = []
window/state = None
last_visible_toolbars = []

[quick_layouts]
names = ['Matlab layout', 'Rstudio layout', 'Vertical split', 'Horizontal split']
order = ['Matlab layout', 'Rstudio layout', 'Vertical split', 'Horizontal split']
active = ['Matlab layout', 'Rstudio layout', 'Vertical split', 'Horizontal split']
layout_0/size = (1260, 740)
layout_0/prefs_dialog_size = (745, 411)
layout_0/is_maximized = True
layout_0/is_fullscreen = False
layout_0/position = (10, 10)
layout_0/state = None
layout_0/statusbar = True
layout_1/size = (1260, 740)
layout_1/prefs_dialog_size = (745, 411)
layout_1/is_maximized = True
layout_1/is_fullscreen = False
layout_1/position = (10, 10)
layout_1/state = None
layout_1/statusbar = True
layout_2/size = (1260, 740)
layout_2/prefs_dialog_size = (745, 411)
layout_2/is_maximized = True
layout_2/is_fullscreen = False
layout_2/position = (10, 10)
layout_2/state = None
layout_2/statusbar = True
layout_3/size = (1260, 740)
layout_3/prefs_dialog_size = (745, 411)
layout_3/is_maximized = True
layout_3/is_fullscreen = False
layout_3/position = (10, 10)
layout_3/state = None
layout_3/statusbar = True
layout_default/size = (1260, 740)
layout_default/prefs_dialog_size = (745, 411)
layout_default/is_maximized = True
layout_default/is_fullscreen = False
layout_default/position = (10, 10)
layout_default/state = None
layout_default/statusbar = True

'''




Mi_Ventana_1.py

# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 01:25:47 2017

@author: AKER-PC
"""

from tkinter import *

def imprime():
  print('Presionastes el Boton IMPRIMIR...')


vtn = Tk()

vtn = title("6_AKER_9")

boton1 = button(vtn, text="SALIR", fg="red",command = vtn.quit)
boton1.pack()

boton2  = button(vtn, text="IMPRIMIR", fg="green" ,command=imprime )
boton2.pack()


bzo.PY

'''Binary Seach'''

def seach(seq, key):

	lo = 0
	hi = len(seq) -1

	while hi >= lo:
		mid = lo + (hi - lo) //2

		if seq[mid] < key:
			lo = mid +1
		elif seq[mid] > key:
			hi = mid -1

		else:
			return mid

	return False

	















bzo_001_.py

def hola():
	print("Hola F3NiX")
#	print(PSLLL.txt)

hola()



import sys, os 
import PyQt5
from PyQt5 import *
from PyQt5 import __package__, QtWidgets, QtGui

def window():
	app = QtWidgets.QApplication(sys.argv)
	Ventana = QtWidgets.QWidget()
	linea_1 = QtWidgets.QLabel(Ventana)
	linea_2 = QtWidgets.QLabel(Ventana)
	linea_1.setText('|_F3NiX_|')
	linea_2.setPixmap(QtGui.QPixmap('F3NiX_Logo__2.ico.PNG'))
	Ventana.setWindowTitle('|_F3NiX & PyThon_|')

	Ventana.setGeometry(100, 100, 100, 100)
	linea_1.move(0, 0)
	linea_2.move(0, 0)
	
	Ventana.show()
	sys.exit(app.exec_())


window()

Ventana = Tk()

class Dialogo(QDialog):
	def __init__(self):
		QDialog.__init__(self)
		self.resize(300, 300)
		self.setWindowTitle("En este recuadro puedes ver las especificaciones del programa F3NiX")   #("Cuadro de dialogo")
		self.etiqueta = QLabel(self)

class Ventana (QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.resize(400, 400)
		self.setWindowTitle("Esta es la ventana principal de F3NiX..") #("Ventana  Principal")
		self.boton = QPushButton(self)
		self.boton.setText("Abrir Cuadro de dialogo")
		self.boton.resize(100, 30)
		self.dialogo = Dialogo()
		self.boton.clicked.connect(self.AbrirDialogo)

	def AbrirDialogo(self):
		self.dialogo.etiqueta.setText("Abierto desde la Ventana Principal")
		self.dialogo.exec_()

app = QApplication(sys.argv)
Ventana = Ventana()
Ventana.configure(background = 'dark turquoise')
Ventana.show()
app.exec_()



from PyQt5 import QtWidgets, QtGui

def window2():
	app = QtWidgets.QApplication(sys.argv)
	Ventana = QtWidgets.QWidget()
	linea_1 = QtWidgets.QLabel(Ventana)
	linea_2 = QtWidgets.QLabel(Ventana)
	linea_1.setText('|_F3NiX_|')
	linea_2.setPixmap(QtGui.QPixmap('oops.PNG'))
	Ventana.setWindowTitle('|_F3NiX & PyThon_|')

	Ventana.setGeometry(100, 100, 100, 100)
	linea_1.move(0, 0)
	linea_2.move(0, 0)
	
	Ventana.show()
	sys.exit(app.exec_())


window2()


# ---------------------------------------------------------------------







# ---------------------------------------------------------------------
# ---------------------------------------------------------------------







# ---------------------------------------------------------------------
# ---------------------------------------------------------------------







# ---------------------------------------------------------------------
# ---------------------------------------------------------------------







# ---------------------------------------------------------------------
# ---------------------------------------------------------------------







# ---------------------------------------------------------------------


bzo_002_.py

X= (int(input("Digita un numero entero.... : ")))
if X < 5:
    print(X," es menor a 5 sube mas... ")


oops.py

#!/usr/bin/env 
import sys
import os

#*****************************************************************************************
def main():
	app = QtGui.QApplication(sys.argv)
	window=main()
	window.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
#*****************************************************************************************
'''
for n in range(60):
	print(n, 2**n)
'''
#***************************************************************************************** 
def n_ra():
	x= 0
	r= int(input("Digita con un numero entero el limite de entradas: "))
	x= r
	for n in range(x):
		print(n, 2**n)
# n_ra()
#*****************************************************************************************

def poncoma( n ):
	"Regresa n como cadena con comas."
	s = str(n)
	pos = len(s)
	while pos > 3:
		pos = pos - 3
		s = s[:pos] + ',' + s[pos:]
	return s
	for n in range(60):
		print(  '%3d %30s' % ( n, poncoma( 2**n ) ) )


#*****************************************************************************************
def wfin():
    f=  0
    e=int(input("Empezar en: "))
    t=int(input("Terminar en: "))
    f= e
    while f <= t:
        print("Linea: ",f)
        f+=1
#wfin()
#*****************************************************************************************
def rid(x):
	return  x
	print(id(x))

#*****************************************************************************************
def bzo_in(self, n= 0, *args):
	return lambda x: x + self, n, args
#*****************************************************************************************
def n_arch()
	print("Introduce el NOMBRE de Tu Nuevo Archivo: ")
	nom= input()
	print("Introduce el FORMATO de Tu Nuevo Archivo: ")
	tipo= input()

	newArc= (nom + "." + tipo)

	archivo=open(newArc, "a")																																																																																																																																			

	print("Introduce la informacion: ")
	x= input()
	archivo.write("\n")
	archivo.write(x)
	archivo.write("\n")
	archivo.write("Este es el final del archivo")

	archivo.close()
#*****************************************************************************************
def vp():
	vp= Tk()
	vp.title("db__F3NiX__db")
	vp.configure(background ='dark turquoise')

	b1=Button(vp, text="SALIR", fg="dark red", command=vp.quit)
	b1.pack(side=TOP)
    
	b2=Button(vp, text="FUCK", fg="green", command=vp.quit)
	b2.pack(side=TOP)
	

	vp.mainloop()
#*****************************************************************************************
def j0():
	print("J0K3R")
#*****************************************************************************************

def imprime():
  print('Presionastes el Boton IMPRIMIR...')
#*****************************************************************************************


#*****************************************************************************************


#*****************************************************************************************
'''
'''


poncoma.py

def poncoma( n ):
	"Regresa n como cadena con comas."
	s = str(n)
	pos = len(s)
	while pos > 3:
		pos = pos - 3
		s = s[:pos] + ',' + s[pos:]
	return s
for n in range(60):
	print(  '%3d %30s' % ( n, poncoma( 2**n ) ) )


Practicando_001.py

# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 02:06:44 2017

@author: AKER-PC
"""

import sys, cmd, tkinter, os


os.getcwd()












py_shell_example.py

#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.8.0a9 on Sun Nov 19 22:21:27 2017
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
import wx.py.shell
# end wxGlade


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.panel_1 = wx.Panel(self, wx.ID_ANY)
        self.text_ctrl = wx.TextCtrl(self.panel_1, wx.ID_ANY, "This is text_ctrl.\n\nUse the shell to append text here.\nE.g. enter this:\napp.frame.text_ctrl.AppendText(\"text\")\n\n", style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.shell = wx.py.shell.Shell(self.panel_1, wx.ID_ANY, introText = "\nThis is the shell.\nHave a look at the variables 'app' and 'app.frame'.\n\n")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("frame")
        self.text_ctrl.SetMinSize((200, 10))
        self.text_ctrl.SetBackgroundColour(wx.Colour(192, 192, 192))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_2.Add(self.text_ctrl, 1, wx.ALL | wx.EXPAND, 1)
        sizer_2.Add(self.shell, 2, wx.EXPAND, 0)
        self.panel_1.SetSizer(sizer_2)
        sizer_1.Add(self.panel_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        self.SetSize((800, 379))
        # end wxGlade

# end of class MyFrame

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()


pycodegen.py

import imp
import os
import marshal
import struct
import sys
from cStringIO import StringIO

from compiler import ast, parse, walk, syntax
from compiler import pyassem, misc, future, symbols
from compiler.consts import SC_LOCAL, SC_GLOBAL_IMPLICIT, SC_GLOBAL_EXPLICIT, \
     SC_FREE, SC_CELL
from compiler.consts import (CO_VARARGS, CO_VARKEYWORDS, CO_NEWLOCALS,
     CO_NESTED, CO_GENERATOR, CO_FUTURE_DIVISION,
     CO_FUTURE_ABSIMPORT, CO_FUTURE_WITH_STATEMENT, CO_FUTURE_PRINT_FUNCTION)
from compiler.pyassem import TupleArg

# XXX The version-specific code can go, since this code only works with 2.x.
# Do we have Python 1.x or Python 2.x?
try:
    VERSION = sys.version_info[0]
except AttributeError:
    VERSION = 1

callfunc_opcode_info = {
    # (Have *args, Have **args) : opcode
    (0,0) : "CALL_FUNCTION",
    (1,0) : "CALL_FUNCTION_VAR",
    (0,1) : "CALL_FUNCTION_KW",
    (1,1) : "CALL_FUNCTION_VAR_KW",
}

LOOP = 1
EXCEPT = 2
TRY_FINALLY = 3
END_FINALLY = 4

def compileFile(filename, display=0):
    f = open(filename, 'U')
    buf = f.read()
    f.close()
    mod = Module(buf, filename)
    try:
        mod.compile(display)
    except SyntaxError:
        raise
    else:
        f = open(filename + "c", "wb")
        mod.dump(f)
        f.close()

def compile(source, filename, mode, flags=None, dont_inherit=None):
    """Replacement for builtin compile() function"""
    if flags is not None or dont_inherit is not None:
        raise RuntimeError("not implemented yet")

    if mode == "single":
        gen = Interactive(source, filename)
    elif mode == "exec":
        gen = Module(source, filename)
    elif mode == "eval":
        gen = Expression(source, filename)
    else:
        raise ValueError("compile() 3rd arg must be 'exec' or "
                         "'eval' or 'single'")
    gen.compile()
    return gen.code

class AbstractCompileMode:

    mode = None # defined by subclass

    def __init__(self, source, filename):
        self.source = source
        self.filename = filename
        self.code = None

    def _get_tree(self):
        tree = parse(self.source, self.mode)
        misc.set_filename(self.filename, tree)
        syntax.check(tree)
        return tree

    def compile(self):
        pass # implemented by subclass

    def getCode(self):
        return self.code

class Expression(AbstractCompileMode):

    mode = "eval"

    def compile(self):
        tree = self._get_tree()
        gen = ExpressionCodeGenerator(tree)
        self.code = gen.getCode()

class Interactive(AbstractCompileMode):

    mode = "single"

    def compile(self):
        tree = self._get_tree()
        gen = InteractiveCodeGenerator(tree)
        self.code = gen.getCode()

class Module(AbstractCompileMode):

    mode = "exec"

    def compile(self, display=0):
        tree = self._get_tree()
        gen = ModuleCodeGenerator(tree)
        if display:
            import pprint
            print(pprint.pprint(tree))
        self.code = gen.getCode()

    def dump(self, f):
        f.write(self.getPycHeader())
        marshal.dump(self.code, f)

    MAGIC = imp.get_magic()

    def getPycHeader(self):
        # compile.c uses marshal to write a long directly, with
        # calling the interface that would also generate a 1-byte code
        # to indicate the type of the value.  simplest way to get the
        # same effect is to call marshal and then skip the code.
        mtime = os.path.getmtime(self.filename)
        mtime = struct.pack('<i', mtime)
        return self.MAGIC + mtime

class LocalNameFinder:
    """Find local names in scope"""
    def __init__(self, names=()):
        self.names = misc.Set()
        self.globals = misc.Set()
        for name in names:
            self.names.add(name)

    # XXX list comprehensions and for loops

    def getLocals(self):
        for elt in self.globals.elements():
            if self.names.has_elt(elt):
                self.names.remove(elt)
        return self.names

    def visitDict(self, node):
        pass

    def visitGlobal(self, node):
        for name in node.names:
            self.globals.add(name)

    def visitFunction(self, node):
        self.names.add(node.name)

    def visitLambda(self, node):
        pass

    def visitImport(self, node):
        for name, alias in node.names:
            self.names.add(alias or name)

    def visitFrom(self, node):
        for name, alias in node.names:
            self.names.add(alias or name)

    def visitClass(self, node):
        self.names.add(node.name)

    def visitAssName(self, node):
        self.names.add(node.name)

def is_constant_false(node):
    if isinstance(node, ast.Const):
        if not node.value:
            return 1
    return 0

class CodeGenerator:
    """Defines basic code generator for Python bytecode

    This class is an abstract base class.  Concrete subclasses must
    define an __init__() that defines self.graph and then calls the
    __init__() defined in this class.

    The concrete class must also define the class attributes
    NameFinder, FunctionGen, and ClassGen.  These attributes can be
    defined in the initClass() method, which is a hook for
    initializing these methods after all the classes have been
    defined.
    """

    optimized = 0 # is namespace access optimized?
    __initialized = None
    class_name = None # provide default for instance variable

    def __init__(self):
        if self.__initialized is None:
            self.initClass()
            self.__class__.__initialized = 1
        self.checkClass()
        self.locals = misc.Stack()
        self.setups = misc.Stack()
        self.last_lineno = None
        self._setupGraphDelegation()
        self._div_op = "BINARY_DIVIDE"

        # XXX set flags based on future features
        futures = self.get_module().futures
        for feature in futures:
            if feature == "division":
                self.graph.setFlag(CO_FUTURE_DIVISION)
                self._div_op = "BINARY_TRUE_DIVIDE"
            elif feature == "absolute_import":
                self.graph.setFlag(CO_FUTURE_ABSIMPORT)
            elif feature == "with_statement":
                self.graph.setFlag(CO_FUTURE_WITH_STATEMENT)
            elif feature == "print_function":
                self.graph.setFlag(CO_FUTURE_PRINT_FUNCTION)

    def initClass(self):
        """This method is called once for each class"""

    def checkClass(self):
        """Verify that class is constructed correctly"""
        try:
            assert hasattr(self, 'graph')
            assert getattr(self, 'NameFinder')
            assert getattr(self, 'FunctionGen')
            assert getattr(self, 'ClassGen')
        except AssertionError msg:
            intro = "Bad class construction for %s" % self.__class__.__name__
            raise AssertionError, intro

    def _setupGraphDelegation(self):
        self.emit = self.graph.emit
        self.newBlock = self.graph.newBlock
        self.startBlock = self.graph.startBlock
        self.nextBlock = self.graph.nextBlock
        self.setDocstring = self.graph.setDocstring

    def getCode(self):
        """Return a code object"""
        return self.graph.getCode()

    def mangle(self, name):
        if self.class_name is not None:
            return misc.mangle(name, self.class_name)
        else:
            return name

    def parseSymbols(self, tree):
        s = symbols.SymbolVisitor()
        walk(tree, s)
        return s.scopes

    def get_module(self):
        raise RuntimeError, "should be implemented by subclasses"

    # Next five methods handle name access

    def isLocalName(self, name):
        return self.locals.top().has_elt(name)

    def storeName(self, name):
        self._nameOp('STORE', name)

    def loadName(self, name):
        self._nameOp('LOAD', name)

    def delName(self, name):
        self._nameOp('DELETE', name)

    def _nameOp(self, prefix, name):
        name = self.mangle(name)
        scope = self.scope.check_name(name)
        if scope == SC_LOCAL:
            if not self.optimized:
                self.emit(prefix + '_NAME', name)
            else:
                self.emit(prefix + '_FAST', name)
        elif scope == SC_GLOBAL_EXPLICIT:
            self.emit(prefix + '_GLOBAL', name)
        elif scope == SC_GLOBAL_IMPLICIT:
            if not self.optimized:
                self.emit(prefix + '_NAME', name)
            else:
                self.emit(prefix + '_GLOBAL', name)
        elif scope == SC_FREE or scope == SC_CELL:
            self.emit(prefix + '_DEREF', name)
        else:
            raise RuntimeError, "unsupported scope for var %s: %d" % \
                  (name, scope)

    def _implicitNameOp(self, prefix, name):
        """Emit name ops for names generated implicitly by for loops

        The interpreter generates names that start with a period or
        dollar sign.  The symbol table ignores these names because
        they aren't present in the program text.
        """
        if self.optimized:
            self.emit(prefix + '_FAST', name)
        else:
            self.emit(prefix + '_NAME', name)

    # The set_lineno() function and the explicit emit() calls for
    # SET_LINENO below are only used to generate the line number table.
    # As of Python 2.3, the interpreter does not have a SET_LINENO
    # instruction.  pyassem treats SET_LINENO opcodes as a special case.

    def set_lineno(self, node, force=False):
        """Emit SET_LINENO if necessary.

        The instruction is considered necessary if the node has a
        lineno attribute and it is different than the last lineno
        emitted.

        Returns true if SET_LINENO was emitted.

        There are no rules for when an AST node should have a lineno
        attribute.  The transformer and AST code need to be reviewed
        and a consistent policy implemented and documented.  Until
        then, this method works around missing line numbers.
        """
        lineno = getattr(node, 'lineno', None)
        if lineno is not None and (lineno != self.last_lineno
                                   or force):
            self.emit('SET_LINENO', lineno)
            self.last_lineno = lineno
            return True
        return False

    # The first few visitor methods handle nodes that generator new
    # code objects.  They use class attributes to determine what
    # specialized code generators to use.

    NameFinder = LocalNameFinder
    FunctionGen = None
    ClassGen = None

    def visitModule(self, node):
        self.scopes = self.parseSymbols(node)
        self.scope = self.scopes[node]
        self.emit('SET_LINENO', 0)
        if node.doc:
            self.emit('LOAD_CONST', node.doc)
            self.storeName('__doc__')
        lnf = walk(node.node, self.NameFinder(), verbose=0)
        self.locals.push(lnf.getLocals())
        self.visit(node.node)
        self.emit('LOAD_CONST', None)
        self.emit('RETURN_VALUE')

    def visitExpression(self, node):
        self.set_lineno(node)
        self.scopes = self.parseSymbols(node)
        self.scope = self.scopes[node]
        self.visit(node.node)
        self.emit('RETURN_VALUE')

    def visitFunction(self, node):
        self._visitFuncOrLambda(node, isLambda=0)
        if node.doc:
            self.setDocstring(node.doc)
        self.storeName(node.name)

    def visitLambda(self, node):
        self._visitFuncOrLambda(node, isLambda=1)

    def _visitFuncOrLambda(self, node, isLambda=0):
        if not isLambda and node.decorators:
            for decorator in node.decorators.nodes:
                self.visit(decorator)
            ndecorators = len(node.decorators.nodes)
        else:
            ndecorators = 0

        gen = self.FunctionGen(node, self.scopes, isLambda,
                               self.class_name, self.get_module())
        walk(node.code, gen)
        gen.finish()
        self.set_lineno(node)
        for default in node.defaults:
            self.visit(default)
        self._makeClosure(gen, len(node.defaults))
        for i in range(ndecorators):
            self.emit('CALL_FUNCTION', 1)

    def visitClass(self, node):
        gen = self.ClassGen(node, self.scopes,
                            self.get_module())
        walk(node.code, gen)
        gen.finish()
        self.set_lineno(node)
        self.emit('LOAD_CONST', node.name)
        for base in node.bases:
            self.visit(base)
        self.emit('BUILD_TUPLE', len(node.bases))
        self._makeClosure(gen, 0)
        self.emit('CALL_FUNCTION', 0)
        self.emit('BUILD_CLASS')
        self.storeName(node.name)

    # The rest are standard visitor methods

    # The next few implement control-flow statements

    def visitIf(self, node):
        end = self.newBlock()
        numtests = len(node.tests)
        for i in range(numtests):
            test, suite = node.tests[i]
            if is_constant_false(test):
                # XXX will need to check generator stuff here
                continue
            self.set_lineno(test)
            self.visit(test)
            nextTest = self.newBlock()
            self.emit('POP_JUMP_IF_FALSE', nextTest)
            self.nextBlock()
            self.visit(suite)
            self.emit('JUMP_FORWARD', end)
            self.startBlock(nextTest)
        if node.else_:
            self.visit(node.else_)
        self.nextBlock(end)

    def visitWhile(self, node):
        self.set_lineno(node)

        loop = self.newBlock()
        else_ = self.newBlock()

        after = self.newBlock()
        self.emit('SETUP_LOOP', after)

        self.nextBlock(loop)
        self.setups.push((LOOP, loop))

        self.set_lineno(node, force=True)
        self.visit(node.test)
        self.emit('POP_JUMP_IF_FALSE', else_ or after)

        self.nextBlock()
        self.visit(node.body)
        self.emit('JUMP_ABSOLUTE', loop)

        self.startBlock(else_) # or just the POPs if not else clause
        self.emit('POP_BLOCK')
        self.setups.pop()
        if node.else_:
            self.visit(node.else_)
        self.nextBlock(after)

    def visitFor(self, node):
        start = self.newBlock()
        anchor = self.newBlock()
        after = self.newBlock()
        self.setups.push((LOOP, start))

        self.set_lineno(node)
        self.emit('SETUP_LOOP', after)
        self.visit(node.list)
        self.emit('GET_ITER')

        self.nextBlock(start)
        self.set_lineno(node, force=1)
        self.emit('FOR_ITER', anchor)
        self.visit(node.assign)
        self.visit(node.body)
        self.emit('JUMP_ABSOLUTE', start)
        self.nextBlock(anchor)
        self.emit('POP_BLOCK')
        self.setups.pop()
        if node.else_:
            self.visit(node.else_)
        self.nextBlock(after)

    def visitBreak(self, node):
        if not self.setups:
            raise SyntaxError, "'break' outside loop (%s, %d)" % \
                  (node.filename, node.lineno)
        self.set_lineno(node)
        self.emit('BREAK_LOOP')

    def visitContinue(self, node):
        if not self.setups:
            raise SyntaxError, "'continue' outside loop (%s, %d)" % \
                  (node.filename, node.lineno)
        kind, block = self.setups.top()
        if kind == LOOP:
            self.set_lineno(node)
            self.emit('JUMP_ABSOLUTE', block)
            self.nextBlock()
        elif kind == EXCEPT or kind == TRY_FINALLY:
            self.set_lineno(node)
            # find the block that starts the loop
            top = len(self.setups)
            while top > 0:
                top = top - 1
                kind, loop_block = self.setups[top]
                if kind == LOOP:
                    break
            if kind != LOOP:
                raise SyntaxError, "'continue' outside loop (%s, %d)" % \
                      (node.filename, node.lineno)
            self.emit('CONTINUE_LOOP', loop_block)
            self.nextBlock()
        elif kind == END_FINALLY:
            msg = "'continue' not allowed inside 'finally' clause (%s, %d)"
            raise SyntaxError, msg % (node.filename, node.lineno)

    def visitTest(self, node, jump):
        end = self.newBlock()
        for child in node.nodes[:-1]:
            self.visit(child)
            self.emit(jump, end)
            self.nextBlock()
        self.visit(node.nodes[-1])
        self.nextBlock(end)

    def visitAnd(self, node):
        self.visitTest(node, 'JUMP_IF_FALSE_OR_POP')

    def visitOr(self, node):
        self.visitTest(node, 'JUMP_IF_TRUE_OR_POP')

    def visitIfExp(self, node):
        endblock = self.newBlock()
        elseblock = self.newBlock()
        self.visit(node.test)
        self.emit('POP_JUMP_IF_FALSE', elseblock)
        self.visit(node.then)
        self.emit('JUMP_FORWARD', endblock)
        self.nextBlock(elseblock)
        self.visit(node.else_)
        self.nextBlock(endblock)

    def visitCompare(self, node):
        self.visit(node.expr)
        cleanup = self.newBlock()
        for op, code in node.ops[:-1]:
            self.visit(code)
            self.emit('DUP_TOP')
            self.emit('ROT_THREE')
            self.emit('COMPARE_OP', op)
            self.emit('JUMP_IF_FALSE_OR_POP', cleanup)
            self.nextBlock()
        # now do the last comparison
        if node.ops:
            op, code = node.ops[-1]
            self.visit(code)
            self.emit('COMPARE_OP', op)
        if len(node.ops) > 1:
            end = self.newBlock()
            self.emit('JUMP_FORWARD', end)
            self.startBlock(cleanup)
            self.emit('ROT_TWO')
            self.emit('POP_TOP')
            self.nextBlock(end)

    # list comprehensions
    def visitListComp(self, node):
        self.set_lineno(node)
        # setup list
        self.emit('BUILD_LIST', 0)

        stack = []
        for i, for_ in zip(range(len(node.quals)), node.quals):
            start, anchor = self.visit(for_)
            cont = None
            for if_ in for_.ifs:
                if cont is None:
                    cont = self.newBlock()
                self.visit(if_, cont)
            stack.insert(0, (start, cont, anchor))

        self.visit(node.expr)
        self.emit('LIST_APPEND', len(node.quals) + 1)

        for start, cont, anchor in stack:
            if cont:
                self.nextBlock(cont)
            self.emit('JUMP_ABSOLUTE', start)
            self.startBlock(anchor)

    def visitSetComp(self, node):
        self.set_lineno(node)
        # setup list
        self.emit('BUILD_SET', 0)

        stack = []
        for i, for_ in zip(range(len(node.quals)), node.quals):
            start, anchor = self.visit(for_)
            cont = None
            for if_ in for_.ifs:
                if cont is None:
                    cont = self.newBlock()
                self.visit(if_, cont)
            stack.insert(0, (start, cont, anchor))

        self.visit(node.expr)
        self.emit('SET_ADD', len(node.quals) + 1)

        for start, cont, anchor in stack:
            if cont:
                self.nextBlock(cont)
            self.emit('JUMP_ABSOLUTE', start)
            self.startBlock(anchor)

    def visitDictComp(self, node):
        self.set_lineno(node)
        # setup list
        self.emit('BUILD_MAP', 0)

        stack = []
        for i, for_ in zip(range(len(node.quals)), node.quals):
            start, anchor = self.visit(for_)
            cont = None
            for if_ in for_.ifs:
                if cont is None:
                    cont = self.newBlock()
                self.visit(if_, cont)
            stack.insert(0, (start, cont, anchor))

        self.visit(node.value)
        self.visit(node.key)
        self.emit('MAP_ADD', len(node.quals) + 1)

        for start, cont, anchor in stack:
            if cont:
                self.nextBlock(cont)
            self.emit('JUMP_ABSOLUTE', start)
            self.startBlock(anchor)

    def visitListCompFor(self, node):
        start = self.newBlock()
        anchor = self.newBlock()

        self.visit(node.list)
        self.emit('GET_ITER')
        self.nextBlock(start)
        self.set_lineno(node, force=True)
        self.emit('FOR_ITER', anchor)
        self.nextBlock()
        self.visit(node.assign)
        return start, anchor

    def visitListCompIf(self, node, branch):
        self.set_lineno(node, force=True)
        self.visit(node.test)
        self.emit('POP_JUMP_IF_FALSE', branch)
        self.newBlock()

    def _makeClosure(self, gen, args):
        frees = gen.scope.get_free_vars()
        if frees:
            for name in frees:
                self.emit('LOAD_CLOSURE', name)
            self.emit('BUILD_TUPLE', len(frees))
            self.emit('LOAD_CONST', gen)
            self.emit('MAKE_CLOSURE', args)
        else:
            self.emit('LOAD_CONST', gen)
            self.emit('MAKE_FUNCTION', args)

    def visitGenExpr(self, node):
        gen = GenExprCodeGenerator(node, self.scopes, self.class_name,
                                   self.get_module())
        walk(node.code, gen)
        gen.finish()
        self.set_lineno(node)
        self._makeClosure(gen, 0)
        # precomputation of outmost iterable
        self.visit(node.code.quals[0].iter)
        self.emit('GET_ITER')
        self.emit('CALL_FUNCTION', 1)

    def visitGenExprInner(self, node):
        self.set_lineno(node)
        # setup list

        stack = []
        for i, for_ in zip(range(len(node.quals)), node.quals):
            start, anchor, end = self.visit(for_)
            cont = None
            for if_ in for_.ifs:
                if cont is None:
                    cont = self.newBlock()
                self.visit(if_, cont)
            stack.insert(0, (start, cont, anchor, end))

        self.visit(node.expr)
        self.emit('YIELD_VALUE')
        self.emit('POP_TOP')

        for start, cont, anchor, end in stack:
            if cont:
                self.nextBlock(cont)
            self.emit('JUMP_ABSOLUTE', start)
            self.startBlock(anchor)
            self.emit('POP_BLOCK')
            self.setups.pop()
            self.nextBlock(end)

        self.emit('LOAD_CONST', None)

    def visitGenExprFor(self, node):
        start = self.newBlock()
        anchor = self.newBlock()
        end = self.newBlock()

        self.setups.push((LOOP, start))
        self.emit('SETUP_LOOP', end)

        if node.is_outmost:
            self.loadName('.0')
        else:
            self.visit(node.iter)
            self.emit('GET_ITER')

        self.nextBlock(start)
        self.set_lineno(node, force=True)
        self.emit('FOR_ITER', anchor)
        self.nextBlock()
        self.visit(node.assign)
        return start, anchor, end

    def visitGenExprIf(self, node, branch):
        self.set_lineno(node, force=True)
        self.visit(node.test)
        self.emit('POP_JUMP_IF_FALSE', branch)
        self.newBlock()

    # exception related

    def visitAssert(self, node):
        # XXX would be interesting to implement this via a
        # transformation of the AST before this stage
        if __debug__:
            end = self.newBlock()
            self.set_lineno(node)
            # XXX AssertionError appears to be special case -- it is always
            # loaded as a global even if there is a local name.  I guess this
            # is a sort of renaming op.
            self.nextBlock()
            self.visit(node.test)
            self.emit('POP_JUMP_IF_TRUE', end)
            self.nextBlock()
            self.emit('LOAD_GLOBAL', 'AssertionError')
            if node.fail:
                self.visit(node.fail)
                self.emit('RAISE_VARARGS', 2)
            else:
                self.emit('RAISE_VARARGS', 1)
            self.nextBlock(end)

    def visitRaise(self, node):
        self.set_lineno(node)
        n = 0
        if node.expr1:
            self.visit(node.expr1)
            n = n + 1
        if node.expr2:
            self.visit(node.expr2)
            n = n + 1
        if node.expr3:
            self.visit(node.expr3)
            n = n + 1
        self.emit('RAISE_VARARGS', n)

    def visitTryExcept(self, node):
        body = self.newBlock()
        handlers = self.newBlock()
        end = self.newBlock()
        if node.else_:
            lElse = self.newBlock()
        else:
            lElse = end
        self.set_lineno(node)
        self.emit('SETUP_EXCEPT', handlers)
        self.nextBlock(body)
        self.setups.push((EXCEPT, body))
        self.visit(node.body)
        self.emit('POP_BLOCK')
        self.setups.pop()
        self.emit('JUMP_FORWARD', lElse)
        self.startBlock(handlers)

        last = len(node.handlers) - 1
        for i in range(len(node.handlers)):
            expr, target, body = node.handlers[i]
            self.set_lineno(expr)
            if expr:
                self.emit('DUP_TOP')
                self.visit(expr)
                self.emit('COMPARE_OP', 'exception match')
                next = self.newBlock()
                self.emit('POP_JUMP_IF_FALSE', next)
                self.nextBlock()
            self.emit('POP_TOP')
            if target:
                self.visit(target)
            else:
                self.emit('POP_TOP')
            self.emit('POP_TOP')
            self.visit(body)
            self.emit('JUMP_FORWARD', end)
            if expr:
                self.nextBlock(next)
            else:
                self.nextBlock()
        self.emit('END_FINALLY')
        if node.else_:
            self.nextBlock(lElse)
            self.visit(node.else_)
        self.nextBlock(end)

    def visitTryFinally(self, node):
        body = self.newBlock()
        final = self.newBlock()
        self.set_lineno(node)
        self.emit('SETUP_FINALLY', final)
        self.nextBlock(body)
        self.setups.push((TRY_FINALLY, body))
        self.visit(node.body)
        self.emit('POP_BLOCK')
        self.setups.pop()
        self.emit('LOAD_CONST', None)
        self.nextBlock(final)
        self.setups.push((END_FINALLY, final))
        self.visit(node.final)
        self.emit('END_FINALLY')
        self.setups.pop()

    __with_count = 0

    def visitWith(self, node):
        body = self.newBlock()
        final = self.newBlock()
        self.__with_count += 1
        valuevar = "_[%d]" % self.__with_count
        self.set_lineno(node)
        self.visit(node.expr)
        self.emit('DUP_TOP')
        self.emit('LOAD_ATTR', '__exit__')
        self.emit('ROT_TWO')
        self.emit('LOAD_ATTR', '__enter__')
        self.emit('CALL_FUNCTION', 0)
        if node.vars is None:
            self.emit('POP_TOP')
        else:
            self._implicitNameOp('STORE', valuevar)
        self.emit('SETUP_FINALLY', final)
        self.nextBlock(body)
        self.setups.push((TRY_FINALLY, body))
        if node.vars is not None:
            self._implicitNameOp('LOAD', valuevar)
            self._implicitNameOp('DELETE', valuevar)
            self.visit(node.vars)
        self.visit(node.body)
        self.emit('POP_BLOCK')
        self.setups.pop()
        self.emit('LOAD_CONST', None)
        self.nextBlock(final)
        self.setups.push((END_FINALLY, final))
        self.emit('WITH_CLEANUP')
        self.emit('END_FINALLY')
        self.setups.pop()
        self.__with_count -= 1

    # misc

    def visitDiscard(self, node):
        self.set_lineno(node)
        self.visit(node.expr)
        self.emit('POP_TOP')

    def visitConst(self, node):
        self.emit('LOAD_CONST', node.value)

    def visitKeyword(self, node):
        self.emit('LOAD_CONST', node.name)
        self.visit(node.expr)

    def visitGlobal(self, node):
        # no code to generate
        pass

    def visitName(self, node):
        self.set_lineno(node)
        self.loadName(node.name)

    def visitPass(self, node):
        self.set_lineno(node)

    def visitImport(self, node):
        self.set_lineno(node)
        level = 0 if self.graph.checkFlag(CO_FUTURE_ABSIMPORT) else -1
        for name, alias in node.names:
            if VERSION > 1:
                self.emit('LOAD_CONST', level)
                self.emit('LOAD_CONST', None)
            self.emit('IMPORT_NAME', name)
            mod = name.split(".")[0]
            if alias:
                self._resolveDots(name)
                self.storeName(alias)
            else:
                self.storeName(mod)

    def visitFrom(self, node):
        self.set_lineno(node)
        level = node.level
        if level == 0 and not self.graph.checkFlag(CO_FUTURE_ABSIMPORT):
            level = -1
        fromlist = tuple(name for (name, alias) in node.names)
        if VERSION > 1:
            self.emit('LOAD_CONST', level)
            self.emit('LOAD_CONST', fromlist)
        self.emit('IMPORT_NAME', node.modname)
        for name, alias in node.names:
            if VERSION > 1:
                if name == '*':
                    self.namespace = 0
                    self.emit('IMPORT_STAR')
                    # There can only be one name w/ from ... import *
                    assert len(node.names) == 1
                    return
                else:
                    self.emit('IMPORT_FROM', name)
                    self._resolveDots(name)
                    self.storeName(alias or name)
            else:
                self.emit('IMPORT_FROM', name)
        self.emit('POP_TOP')

    def _resolveDots(self, name):
        elts = name.split(".")
        if len(elts) == 1:
            return
        for elt in elts[1:]:
            self.emit('LOAD_ATTR', elt)

    def visitGetattr(self, node):
        self.visit(node.expr)
        self.emit('LOAD_ATTR', self.mangle(node.attrname))

    # next five implement assignments

    def visitAssign(self, node):
        self.set_lineno(node)
        self.visit(node.expr)
        dups = len(node.nodes) - 1
        for i in range(len(node.nodes)):
            elt = node.nodes[i]
            if i < dups:
                self.emit('DUP_TOP')
            if isinstance(elt, ast.Node):
                self.visit(elt)

    def visitAssName(self, node):
        if node.flags == 'OP_ASSIGN':
            self.storeName(node.name)
        elif node.flags == 'OP_DELETE':
            self.set_lineno(node)
            self.delName(node.name)
        else:
            print "oops", node.flags

    def visitAssAttr(self, node):
        self.visit(node.expr)
        if node.flags == 'OP_ASSIGN':
            self.emit('STORE_ATTR', self.mangle(node.attrname))
        elif node.flags == 'OP_DELETE':
            self.emit('DELETE_ATTR', self.mangle(node.attrname))
        else:
            print "warning: unexpected flags:", node.flags
            print node

    def _visitAssSequence(self, node, op='UNPACK_SEQUENCE'):
        if findOp(node) != 'OP_DELETE':
            self.emit(op, len(node.nodes))
        for child in node.nodes:
            self.visit(child)

    if VERSION > 1:
        visitAssTuple = _visitAssSequence
        visitAssList = _visitAssSequence
    else:
        def visitAssTuple(self, node):
            self._visitAssSequence(node, 'UNPACK_TUPLE')

        def visitAssList(self, node):
            self._visitAssSequence(node, 'UNPACK_LIST')

    # augmented assignment

    def visitAugAssign(self, node):
        self.set_lineno(node)
        aug_node = wrap_aug(node.node)
        self.visit(aug_node, "load")
        self.visit(node.expr)
        self.emit(self._augmented_opcode[node.op])
        self.visit(aug_node, "store")

    _augmented_opcode = {
        '+=' : 'INPLACE_ADD',
        '-=' : 'INPLACE_SUBTRACT',
        '*=' : 'INPLACE_MULTIPLY',
        '/=' : 'INPLACE_DIVIDE',
        '//=': 'INPLACE_FLOOR_DIVIDE',
        '%=' : 'INPLACE_MODULO',
        '**=': 'INPLACE_POWER',
        '>>=': 'INPLACE_RSHIFT',
        '<<=': 'INPLACE_LSHIFT',
        '&=' : 'INPLACE_AND',
        '^=' : 'INPLACE_XOR',
        '|=' : 'INPLACE_OR',
        }

    def visitAugName(self, node, mode):
        if mode == "load":
            self.loadName(node.name)
        elif mode == "store":
            self.storeName(node.name)

    def visitAugGetattr(self, node, mode):
        if mode == "load":
            self.visit(node.expr)
            self.emit('DUP_TOP')
            self.emit('LOAD_ATTR', self.mangle(node.attrname))
        elif mode == "store":
            self.emit('ROT_TWO')
            self.emit('STORE_ATTR', self.mangle(node.attrname))

    def visitAugSlice(self, node, mode):
        if mode == "load":
            self.visitSlice(node, 1)
        elif mode == "store":
            slice = 0
            if node.lower:
                slice = slice | 1
            if node.upper:
                slice = slice | 2
            if slice == 0:
                self.emit('ROT_TWO')
            elif slice == 3:
                self.emit('ROT_FOUR')
            else:
                self.emit('ROT_THREE')
            self.emit('STORE_SLICE+%d' % slice)

    def visitAugSubscript(self, node, mode):
        if mode == "load":
            self.visitSubscript(node, 1)
        elif mode == "store":
            self.emit('ROT_THREE')
            self.emit('STORE_SUBSCR')

    def visitExec(self, node):
        self.visit(node.expr)
        if node.locals is None:
            self.emit('LOAD_CONST', None)
        else:
            self.visit(node.locals)
        if node.globals is None:
            self.emit('DUP_TOP')
        else:
            self.visit(node.globals)
        self.emit('EXEC_STMT')

    def visitCallFunc(self, node):
        pos = 0
        kw = 0
        self.set_lineno(node)
        self.visit(node.node)
        for arg in node.args:
            self.visit(arg)
            if isinstance(arg, ast.Keyword):
                kw = kw + 1
            else:
                pos = pos + 1
        if node.star_args is not None:
            self.visit(node.star_args)
        if node.dstar_args is not None:
            self.visit(node.dstar_args)
        have_star = node.star_args is not None
        have_dstar = node.dstar_args is not None
        opcode = callfunc_opcode_info[have_star, have_dstar]
        self.emit(opcode, kw << 8 | pos)

    def visitPrint(self, node, newline=0):
        self.set_lineno(node)
        if node.dest:
            self.visit(node.dest)
        for child in node.nodes:
            if node.dest:
                self.emit('DUP_TOP')
            self.visit(child)
            if node.dest:
                self.emit('ROT_TWO')
                self.emit('PRINT_ITEM_TO')
            else:
                self.emit('PRINT_ITEM')
        if node.dest and not newline:
            self.emit('POP_TOP')

    def visitPrintnl(self, node):
        self.visitPrint(node, newline=1)
        if node.dest:
            self.emit('PRINT_NEWLINE_TO')
        else:
            self.emit('PRINT_NEWLINE')

    def visitReturn(self, node):
        self.set_lineno(node)
        self.visit(node.value)
        self.emit('RETURN_VALUE')

    def visitYield(self, node):
        self.set_lineno(node)
        self.visit(node.value)
        self.emit('YIELD_VALUE')

    # slice and subscript stuff

    def visitSlice(self, node, aug_flag=None):
        # aug_flag is used by visitAugSlice
        self.visit(node.expr)
        slice = 0
        if node.lower:
            self.visit(node.lower)
            slice = slice | 1
        if node.upper:
            self.visit(node.upper)
            slice = slice | 2
        if aug_flag:
            if slice == 0:
                self.emit('DUP_TOP')
            elif slice == 3:
                self.emit('DUP_TOPX', 3)
            else:
                self.emit('DUP_TOPX', 2)
        if node.flags == 'OP_APPLY':
            self.emit('SLICE+%d' % slice)
        elif node.flags == 'OP_ASSIGN':
            self.emit('STORE_SLICE+%d' % slice)
        elif node.flags == 'OP_DELETE':
            self.emit('DELETE_SLICE+%d' % slice)
        else:
            print "weird slice", node.flags
            raise

    def visitSubscript(self, node, aug_flag=None):
        self.visit(node.expr)
        for sub in node.subs:
            self.visit(sub)
        if len(node.subs) > 1:
            self.emit('BUILD_TUPLE', len(node.subs))
        if aug_flag:
            self.emit('DUP_TOPX', 2)
        if node.flags == 'OP_APPLY':
            self.emit('BINARY_SUBSCR')
        elif node.flags == 'OP_ASSIGN':
            self.emit('STORE_SUBSCR')
        elif node.flags == 'OP_DELETE':
            self.emit('DELETE_SUBSCR')

    # binary ops

    def binaryOp(self, node, op):
        self.visit(node.left)
        self.visit(node.right)
        self.emit(op)

    def visitAdd(self, node):
        return self.binaryOp(node, 'BINARY_ADD')

    def visitSub(self, node):
        return self.binaryOp(node, 'BINARY_SUBTRACT')

    def visitMul(self, node):
        return self.binaryOp(node, 'BINARY_MULTIPLY')

    def visitDiv(self, node):
        return self.binaryOp(node, self._div_op)

    def visitFloorDiv(self, node):
        return self.binaryOp(node, 'BINARY_FLOOR_DIVIDE')

    def visitMod(self, node):
        return self.binaryOp(node, 'BINARY_MODULO')

    def visitPower(self, node):
        return self.binaryOp(node, 'BINARY_POWER')

    def visitLeftShift(self, node):
        return self.binaryOp(node, 'BINARY_LSHIFT')

    def visitRightShift(self, node):
        return self.binaryOp(node, 'BINARY_RSHIFT')

    # unary ops

    def unaryOp(self, node, op):
        self.visit(node.expr)
        self.emit(op)

    def visitInvert(self, node):
        return self.unaryOp(node, 'UNARY_INVERT')

    def visitUnarySub(self, node):
        return self.unaryOp(node, 'UNARY_NEGATIVE')

    def visitUnaryAdd(self, node):
        return self.unaryOp(node, 'UNARY_POSITIVE')

    def visitUnaryInvert(self, node):
        return self.unaryOp(node, 'UNARY_INVERT')

    def visitNot(self, node):
        return self.unaryOp(node, 'UNARY_NOT')

    def visitBackquote(self, node):
        return self.unaryOp(node, 'UNARY_CONVERT')

    # bit ops

    def bitOp(self, nodes, op):
        self.visit(nodes[0])
        for node in nodes[1:]:
            self.visit(node)
            self.emit(op)

    def visitBitand(self, node):
        return self.bitOp(node.nodes, 'BINARY_AND')

    def visitBitor(self, node):
        return self.bitOp(node.nodes, 'BINARY_OR')

    def visitBitxor(self, node):
        return self.bitOp(node.nodes, 'BINARY_XOR')

    # object constructors

    def visitEllipsis(self, node):
        self.emit('LOAD_CONST', Ellipsis)

    def visitTuple(self, node):
        self.set_lineno(node)
        for elt in node.nodes:
            self.visit(elt)
        self.emit('BUILD_TUPLE', len(node.nodes))

    def visitList(self, node):
        self.set_lineno(node)
        for elt in node.nodes:
            self.visit(elt)
        self.emit('BUILD_LIST', len(node.nodes))

    def visitSet(self, node):
        self.set_lineno(node)
        for elt in node.nodes:
            self.visit(elt)
        self.emit('BUILD_SET', len(node.nodes))

    def visitSliceobj(self, node):
        for child in node.nodes:
            self.visit(child)
        self.emit('BUILD_SLICE', len(node.nodes))

    def visitDict(self, node):
        self.set_lineno(node)
        self.emit('BUILD_MAP', 0)
        for k, v in node.items:
            self.emit('DUP_TOP')
            self.visit(k)
            self.visit(v)
            self.emit('ROT_THREE')
            self.emit('STORE_SUBSCR')

class NestedScopeMixin:
    """Defines initClass() for nested scoping (Python 2.2-compatible)"""
    def initClass(self):
        self.__class__.NameFinder = LocalNameFinder
        self.__class__.FunctionGen = FunctionCodeGenerator
        self.__class__.ClassGen = ClassCodeGenerator

class ModuleCodeGenerator(NestedScopeMixin, CodeGenerator):
    __super_init = CodeGenerator.__init__

    scopes = None

    def __init__(self, tree):
        self.graph = pyassem.PyFlowGraph("<module>", tree.filename)
        self.futures = future.find_futures(tree)
        self.__super_init()
        walk(tree, self)

    def get_module(self):
        return self

class ExpressionCodeGenerator(NestedScopeMixin, CodeGenerator):
    __super_init = CodeGenerator.__init__

    scopes = None
    futures = ()

    def __init__(self, tree):
        self.graph = pyassem.PyFlowGraph("<expression>", tree.filename)
        self.__super_init()
        walk(tree, self)

    def get_module(self):
        return self

class InteractiveCodeGenerator(NestedScopeMixin, CodeGenerator):

    __super_init = CodeGenerator.__init__

    scopes = None
    futures = ()

    def __init__(self, tree):
        self.graph = pyassem.PyFlowGraph("<interactive>", tree.filename)
        self.__super_init()
        self.set_lineno(tree)
        walk(tree, self)
        self.emit('RETURN_VALUE')

    def get_module(self):
        return self

    def visitDiscard(self, node):
        # XXX Discard means it's an expression.  Perhaps this is a bad
        # name.
        self.visit(node.expr)
        self.emit('PRINT_EXPR')

class AbstractFunctionCode:
    optimized = 1
    lambdaCount = 0

    def __init__(self, func, scopes, isLambda, class_name, mod):
        self.class_name = class_name
        self.module = mod
        if isLambda:
            klass = FunctionCodeGenerator
            name = "<lambda.%d>" % klass.lambdaCount
            klass.lambdaCount = klass.lambdaCount + 1
        else:
            name = func.name

        args, hasTupleArg = generateArgList(func.argnames)
        self.graph = pyassem.PyFlowGraph(name, func.filename, args,
                                         optimized=1)
        self.isLambda = isLambda
        self.super_init()

        if not isLambda and func.doc:
            self.setDocstring(func.doc)

        lnf = walk(func.code, self.NameFinder(args), verbose=0)
        self.locals.push(lnf.getLocals())
        if func.varargs:
            self.graph.setFlag(CO_VARARGS)
        if func.kwargs:
            self.graph.setFlag(CO_VARKEYWORDS)
        self.set_lineno(func)
        if hasTupleArg:
            self.generateArgUnpack(func.argnames)

    def get_module(self):
        return self.module

    def finish(self):
        self.graph.startExitBlock()
        if not self.isLambda:
            self.emit('LOAD_CONST', None)
        self.emit('RETURN_VALUE')

    def generateArgUnpack(self, args):
        for i in range(len(args)):
            arg = args[i]
            if isinstance(arg, tuple):
                self.emit('LOAD_FAST', '.%d' % (i * 2))
                self.unpackSequence(arg)

    def unpackSequence(self, tup):
        if VERSION > 1:
            self.emit('UNPACK_SEQUENCE', len(tup))
        else:
            self.emit('UNPACK_TUPLE', len(tup))
        for elt in tup:
            if isinstance(elt, tuple):
                self.unpackSequence(elt)
            else:
                self._nameOp('STORE', elt)

    unpackTuple = unpackSequence

class FunctionCodeGenerator(NestedScopeMixin, AbstractFunctionCode,
                            CodeGenerator):
    super_init = CodeGenerator.__init__ # call be other init
    scopes = None

    __super_init = AbstractFunctionCode.__init__

    def __init__(self, func, scopes, isLambda, class_name, mod):
        self.scopes = scopes
        self.scope = scopes[func]
        self.__super_init(func, scopes, isLambda, class_name, mod)
        self.graph.setFreeVars(self.scope.get_free_vars())
        self.graph.setCellVars(self.scope.get_cell_vars())
        if self.scope.generator is not None:
            self.graph.setFlag(CO_GENERATOR)

class GenExprCodeGenerator(NestedScopeMixin, AbstractFunctionCode,
                           CodeGenerator):
    super_init = CodeGenerator.__init__ # call be other init
    scopes = None

    __super_init = AbstractFunctionCode.__init__

    def __init__(self, gexp, scopes, class_name, mod):
        self.scopes = scopes
        self.scope = scopes[gexp]
        self.__super_init(gexp, scopes, 1, class_name, mod)
        self.graph.setFreeVars(self.scope.get_free_vars())
        self.graph.setCellVars(self.scope.get_cell_vars())
        self.graph.setFlag(CO_GENERATOR)

class AbstractClassCode:

    def __init__(self, klass, scopes, module):
        self.class_name = klass.name
        self.module = module
        self.graph = pyassem.PyFlowGraph(klass.name, klass.filename,
                                           optimized=0, klass=1)
        self.super_init()
        lnf = walk(klass.code, self.NameFinder(), verbose=0)
        self.locals.push(lnf.getLocals())
        self.graph.setFlag(CO_NEWLOCALS)
        if klass.doc:
            self.setDocstring(klass.doc)

    def get_module(self):
        return self.module

    def finish(self):
        self.graph.startExitBlock()
        self.emit('LOAD_LOCALS')
        self.emit('RETURN_VALUE')

class ClassCodeGenerator(NestedScopeMixin, AbstractClassCode, CodeGenerator):
    super_init = CodeGenerator.__init__
    scopes = None

    __super_init = AbstractClassCode.__init__

    def __init__(self, klass, scopes, module):
        self.scopes = scopes
        self.scope = scopes[klass]
        self.__super_init(klass, scopes, module)
        self.graph.setFreeVars(self.scope.get_free_vars())
        self.graph.setCellVars(self.scope.get_cell_vars())
        self.set_lineno(klass)
        self.emit("LOAD_GLOBAL", "__name__")
        self.storeName("__module__")
        if klass.doc:
            self.emit("LOAD_CONST", klass.doc)
            self.storeName('__doc__')

def generateArgList(arglist):
    """Generate an arg list marking TupleArgs"""
    args = []
    extra = []
    count = 0
    for i in range(len(arglist)):
        elt = arglist[i]
        if isinstance(elt, str):
            args.append(elt)
        elif isinstance(elt, tuple):
            args.append(TupleArg(i * 2, elt))
            extra.extend(misc.flatten(elt))
            count = count + 1
        else:
            raise ValueError, "unexpect argument type:", elt
    return args + extra, count

def findOp(node):
    """Find the op (DELETE, LOAD, STORE) in an AssTuple tree"""
    v = OpFinder()
    walk(node, v, verbose=0)
    return v.op

class OpFinder:
    def __init__(self):
        self.op = None
    def visitAssName(self, node):
        if self.op is None:
            self.op = node.flags
        elif self.op != node.flags:
            raise ValueError, "mixed ops in stmt"
    visitAssAttr = visitAssName
    visitSubscript = visitAssName

class Delegator:
    """Base class to support delegation for augmented assignment nodes

    To generator code for augmented assignments, we use the following
    wrapper classes.  In visitAugAssign, the left-hand expression node
    is visited twice.  The first time the visit uses the normal method
    for that node .  The second time the visit uses a different method
    that generates the appropriate code to perform the assignment.
    These delegator classes wrap the original AST nodes in order to
    support the variant visit methods.
    """
    def __init__(self, obj):
        self.obj = obj

    def __getattr__(self, attr):
        return getattr(self.obj, attr)

class AugGetattr(Delegator):
    pass

class AugName(Delegator):
    pass

class AugSlice(Delegator):
    pass

class AugSubscript(Delegator):
    pass

wrapper = {
    ast.Getattr: AugGetattr,
    ast.Name: AugName,
    ast.Slice: AugSlice,
    ast.Subscript: AugSubscript,
    }

def wrap_aug(node):
    return wrapper[node.__class__](node)

if __name__ == "__main__":
    for file in sys.argv[1:]:
        compileFile(file)


setup.py

#Code for setup.py :

import sys
from cx_Freeze import setup, Executable

setup(
    name = "Any Name",
    version = "3.1",
    description = "Any Description you like",
    executables = [Executable("myFileName.py", base = "Win32GUI")])


SMTP Example.py

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import smtplib
import sys
import os
import  re
import math
import http


def prompt(prompt):
	return input(prompt).strip()

fromaddr = prompt("De: ")
toaddrs = prompt("Para: ").split()




print(" Qlos  ")



msg = ("From: %s\r\nTo: %s\r\n\r\n"
	% (fromaddr, ", ".join(toaddrs))) 
while True: 
	try: 
		line = input() 
	except EOFError: 
		break 
	if not line: 
		break 
	msg = msg + line

print("Message length is", len(msg))


print("el server es :" + server)
print("el port es :" + port)
print("el host es :" + host)
print("el sa es :" + sa)
print("el timeout es :" + timeout)
print("el fromaddr es :" + fromaddr)
print("el toaddrs es :" + toaddrs)



print("6_F3niX_9 ")


server = smtplib.SMTP('localhost') 
server.set_debuglevel(1) 
server.sendmail(fromaddr, toaddrs, msg) 



server.quit()






tetrix.py

#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2014 Riverbank Computing Limited.
## Copyright (C) 2010 Nokia Corporation and/or its subsidiary(-ies).
## All rights reserved.
##
## This file is part of the examples of PyQt.
##
## $QT_BEGIN_LICENSE:BSD$
## You may use this file under the terms of the BSD license as follows:
##
## "Redistribution and use in source and binary forms, with or without
## modification, are permitted provided that the following conditions are
## met:
##   * Redistributions of source code must retain the above copyright
##     notice, this list of conditions and the following disclaimer.
##   * Redistributions in binary form must reproduce the above copyright
##     notice, this list of conditions and the following disclaimer in
##     the documentation and/or other materials provided with the
##     distribution.
##   * Neither the name of Nokia Corporation and its Subsidiary(-ies) nor
##     the names of its contributors may be used to endorse or promote
##     products derived from this software without specific prior written
##     permission.
##
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
## "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
## OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
## $QT_END_LICENSE$
##
#############################################################################


import copy
import random

from PyQt5.QtCore import pyqtSignal, QBasicTimer, QSize, Qt
from PyQt5.QtGui import QColor, QPainter, QPixmap
from PyQt5.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
        QLCDNumber, QPushButton, QWidget)


NoShape, ZShape, SShape, LineShape, TShape, SquareShape, LShape, MirroredLShape = range(8)


class TetrixWindow(QWidget):
    def __init__(self):
        super(TetrixWindow, self).__init__()

        self.board = TetrixBoard()

        nextPieceLabel = QLabel()
        nextPieceLabel.setFrameStyle(QFrame.Box | QFrame.Raised)
        nextPieceLabel.setAlignment(Qt.AlignCenter)
        self.board.setNextPieceLabel(nextPieceLabel)

        scoreLcd = QLCDNumber(5)
        scoreLcd.setSegmentStyle(QLCDNumber.Filled)
        levelLcd = QLCDNumber(2)
        levelLcd.setSegmentStyle(QLCDNumber.Filled)
        linesLcd = QLCDNumber(5)
        linesLcd.setSegmentStyle(QLCDNumber.Filled)

        startButton = QPushButton("&Start")
        startButton.setFocusPolicy(Qt.NoFocus)
        quitButton = QPushButton("&Quit")
        quitButton.setFocusPolicy(Qt.NoFocus)
        pauseButton = QPushButton("&Pause")
        pauseButton.setFocusPolicy(Qt.NoFocus)

        startButton.clicked.connect(self.board.start)
        pauseButton.clicked.connect(self.board.pause)
        quitButton.clicked.connect(QApplication.instance().quit)
        self.board.scoreChanged.connect(scoreLcd.display)
        self.board.levelChanged.connect(levelLcd.display)
        self.board.linesRemovedChanged.connect(linesLcd.display)

        layout = QGridLayout()
        layout.addWidget(self.createLabel("NEXT"), 0, 0)
        layout.addWidget(nextPieceLabel, 1, 0)
        layout.addWidget(self.createLabel("LEVEL"), 2, 0)
        layout.addWidget(levelLcd, 3, 0)
        layout.addWidget(startButton, 4, 0)
        layout.addWidget(self.board, 0, 1, 6, 1)
        layout.addWidget(self.createLabel("SCORE"), 0, 2)
        layout.addWidget(scoreLcd, 1, 2)
        layout.addWidget(self.createLabel("LINES REMOVED"), 2, 2)
        layout.addWidget(linesLcd, 3, 2)
        layout.addWidget(quitButton, 4, 2)
        layout.addWidget(pauseButton, 5, 2)
        self.setLayout(layout)

        self.setWindowTitle("Tetrix")
        self.resize(550, 370)

    def createLabel(self, text):
        lbl = QLabel(text)
        lbl.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)
        return lbl


class TetrixBoard(QFrame):
    BoardWidth = 10
    BoardHeight = 22

    scoreChanged = pyqtSignal(int)

    levelChanged = pyqtSignal(int)

    linesRemovedChanged = pyqtSignal(int)

    def __init__(self, parent=None):
        super(TetrixBoard, self).__init__(parent)

        self.timer = QBasicTimer()
        self.nextPieceLabel = None
        self.isWaitingAfterLine = False
        self.curPiece = TetrixPiece()
        self.nextPiece = TetrixPiece()
        self.curX = 0
        self.curY = 0
        self.numLinesRemoved = 0
        self.numPiecesDropped = 0
        self.score = 0
        self.level = 0
        self.board = None

        self.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.setFocusPolicy(Qt.StrongFocus)
        self.isStarted = False
        self.isPaused = False
        self.clearBoard()

        self.nextPiece.setRandomShape()

    def shapeAt(self, x, y):
        return self.board[(y * TetrixBoard.BoardWidth) + x]

    def setShapeAt(self, x, y, shape):
        self.board[(y * TetrixBoard.BoardWidth) + x] = shape   

    def timeoutTime(self):
        return 1000 / (1 + self.level)

    def squareWidth(self):
        return self.contentsRect().width() / TetrixBoard.BoardWidth

    def squareHeight(self):
        return self.contentsRect().height() / TetrixBoard.BoardHeight

    def setNextPieceLabel(self, label):
        self.nextPieceLabel = label

    def sizeHint(self):
        return QSize(TetrixBoard.BoardWidth * 15 + self.frameWidth() * 2,
                TetrixBoard.BoardHeight * 15 + self.frameWidth() * 2)

    def minimumSizeHint(self):
        return QSize(TetrixBoard.BoardWidth * 5 + self.frameWidth() * 2,
                TetrixBoard.BoardHeight * 5 + self.frameWidth() * 2)

    def start(self):
        if self.isPaused:
            return

        self.isStarted = True
        self.isWaitingAfterLine = False
        self.numLinesRemoved = 0
        self.numPiecesDropped = 0
        self.score = 0
        self.level = 1
        self.clearBoard()

        self.linesRemovedChanged.emit(self.numLinesRemoved)
        self.scoreChanged.emit(self.score)
        self.levelChanged.emit(self.level)

        self.newPiece()
        self.timer.start(self.timeoutTime(), self)

    def pause(self):
        if not self.isStarted:
            return

        self.isPaused = not self.isPaused
        if self.isPaused:
            self.timer.stop()
        else:
            self.timer.start(self.timeoutTime(), self)

        self.update()

    def paintEvent(self, event):
        super(TetrixBoard, self).paintEvent(event)

        painter = QPainter(self)
        rect = self.contentsRect()

        if self.isPaused:
            painter.drawText(rect, Qt.AlignCenter, "Pause")
            return

        boardTop = rect.bottom() - TetrixBoard.BoardHeight * self.squareHeight()

        for i in range(TetrixBoard.BoardHeight):
            for j in range(TetrixBoard.BoardWidth):
                shape = self.shapeAt(j, TetrixBoard.BoardHeight - i - 1)
                if shape != NoShape:
                    self.drawSquare(painter,
                            rect.left() + j * self.squareWidth(),
                            boardTop + i * self.squareHeight(), shape)

        if self.curPiece.shape() != NoShape:
            for i in range(4):
                x = self.curX + self.curPiece.x(i)
                y = self.curY - self.curPiece.y(i)
                self.drawSquare(painter, rect.left() + x * self.squareWidth(),
                        boardTop + (TetrixBoard.BoardHeight - y - 1) * self.squareHeight(),
                        self.curPiece.shape())

    def keyPressEvent(self, event):
        if not self.isStarted or self.isPaused or self.curPiece.shape() == NoShape:
            super(TetrixBoard, self).keyPressEvent(event)
            return

        key = event.key()
        if key == Qt.Key_Left:
            self.tryMove(self.curPiece, self.curX - 1, self.curY)
        elif key == Qt.Key_Right:
            self.tryMove(self.curPiece, self.curX + 1, self.curY)
        elif key == Qt.Key_Down:
            self.tryMove(self.curPiece.rotatedRight(), self.curX, self.curY)
        elif key == Qt.Key_Up:
            self.tryMove(self.curPiece.rotatedLeft(), self.curX, self.curY)
        elif key == Qt.Key_Space:
            self.dropDown()
        elif key == Qt.Key_D:
            self.oneLineDown()
        else:
            super(TetrixBoard, self).keyPressEvent(event)

    def timerEvent(self, event):
        if event.timerId() == self.timer.timerId():
            if self.isWaitingAfterLine:
                self.isWaitingAfterLine = False
                self.newPiece()
                self.timer.start(self.timeoutTime(), self)
            else:
                self.oneLineDown()
        else:
            super(TetrixBoard, self).timerEvent(event)

    def clearBoard(self):
        self.board = [NoShape for i in range(TetrixBoard.BoardHeight * TetrixBoard.BoardWidth)]

    def dropDown(self):
        dropHeight = 0
        newY = self.curY
        while newY > 0:
            if not self.tryMove(self.curPiece, self.curX, newY - 1):
                break
            newY -= 1
            dropHeight += 1

        self.pieceDropped(dropHeight)

    def oneLineDown(self):
        if not self.tryMove(self.curPiece, self.curX, self.curY - 1):
            self.pieceDropped(0)

    def pieceDropped(self, dropHeight):
        for i in range(4):
            x = self.curX + self.curPiece.x(i)
            y = self.curY - self.curPiece.y(i)
            self.setShapeAt(x, y, self.curPiece.shape())

        self.numPiecesDropped += 1
        if self.numPiecesDropped % 25 == 0:
            self.level += 1
            self.timer.start(self.timeoutTime(), self)
            self.levelChanged.emit(self.level)

        self.score += dropHeight + 7
        self.scoreChanged.emit(self.score)
        self.removeFullLines()

        if not self.isWaitingAfterLine:
            self.newPiece()

    def removeFullLines(self):
        numFullLines = 0

        for i in range(TetrixBoard.BoardHeight - 1, -1, -1):
            lineIsFull = True

            for j in range(TetrixBoard.BoardWidth):
                if self.shapeAt(j, i) == NoShape:
                    lineIsFull = False
                    break

            if lineIsFull:
                numFullLines += 1
                for k in range(TetrixBoard.BoardHeight - 1):
                    for j in range(TetrixBoard.BoardWidth):
                        self.setShapeAt(j, k, self.shapeAt(j, k + 1))

                for j in range(TetrixBoard.BoardWidth):
                    self.setShapeAt(j, TetrixBoard.BoardHeight - 1, NoShape)

        if numFullLines > 0:
            self.numLinesRemoved += numFullLines
            self.score += 10 * numFullLines
            self.linesRemovedChanged.emit(self.numLinesRemoved)
            self.scoreChanged.emit(self.score)

            self.timer.start(500, self)
            self.isWaitingAfterLine = True
            self.curPiece.setShape(NoShape)
            self.update()

    def newPiece(self):
        self.curPiece = copy.deepcopy(self.nextPiece)
        self.nextPiece.setRandomShape()
        self.showNextPiece()
        self.curX = TetrixBoard.BoardWidth // 2 + 1
        self.curY = TetrixBoard.BoardHeight - 1 + self.curPiece.minY()

        if not self.tryMove(self.curPiece, self.curX, self.curY):
            self.curPiece.setShape(NoShape)
            self.timer.stop()
            self.isStarted = False

    def showNextPiece(self):
        if self.nextPieceLabel is None:
            return

        dx = self.nextPiece.maxX() - self.nextPiece.minX() + 1
        dy = self.nextPiece.maxY() - self.nextPiece.minY() + 1

        pixmap = QPixmap(dx * self.squareWidth(), dy * self.squareHeight())
        painter = QPainter(pixmap)
        painter.fillRect(pixmap.rect(), self.nextPieceLabel.palette().window())

        for i in range(4):
            x = self.nextPiece.x(i) - self.nextPiece.minX()
            y = self.nextPiece.y(i) - self.nextPiece.minY()
            self.drawSquare(painter, x * self.squareWidth(),
                    y * self.squareHeight(), self.nextPiece.shape())

        painter.end()

        self.nextPieceLabel.setPixmap(pixmap)

    def tryMove(self, newPiece, newX, newY):
        for i in range(4):
            x = newX + newPiece.x(i)
            y = newY - newPiece.y(i)
            if x < 0 or x >= TetrixBoard.BoardWidth or y < 0 or y >= TetrixBoard.BoardHeight:
                return False
            if self.shapeAt(x, y) != NoShape:
                return False

        self.curPiece = newPiece
        self.curX = newX
        self.curY = newY
        self.update()
        return True

    def drawSquare(self, painter, x, y, shape):
        colorTable = [0x000000, 0xCC6666, 0x66CC66, 0x6666CC,
                      0xCCCC66, 0xCC66CC, 0x66CCCC, 0xDAAA00]

        color = QColor(colorTable[shape])
        painter.fillRect(x + 1, y + 1, self.squareWidth() - 2,
                self.squareHeight() - 2, color)

        painter.setPen(color.lighter())
        painter.drawLine(x, y + self.squareHeight() - 1, x, y)
        painter.drawLine(x, y, x + self.squareWidth() - 1, y)

        painter.setPen(color.darker())
        painter.drawLine(x + 1, y + self.squareHeight() - 1,
                x + self.squareWidth() - 1, y + self.squareHeight() - 1)
        painter.drawLine(x + self.squareWidth() - 1,
                y + self.squareHeight() - 1, x + self.squareWidth() - 1, y + 1)


class TetrixPiece(object):
    coordsTable = (
        ((0, 0),     (0, 0),     (0, 0),     (0, 0)),
        ((0, -1),    (0, 0),     (-1, 0),    (-1, 1)),
        ((0, -1),    (0, 0),     (1, 0),     (1, 1)),
        ((0, -1),    (0, 0),     (0, 1),     (0, 2)),
        ((-1, 0),    (0, 0),     (1, 0),     (0, 1)),
        ((0, 0),     (1, 0),     (0, 1),     (1, 1)),
        ((-1, -1),   (0, -1),    (0, 0),     (0, 1)),
        ((1, -1),    (0, -1),    (0, 0),     (0, 1))
    )

    def __init__(self):
        self.coords = [[0, 0] for _ in range(4)]
        self.pieceShape = NoShape

        self.setShape(NoShape)

    def shape(self):
        return self.pieceShape

    def setShape(self, shape):
        table = TetrixPiece.coordsTable[shape]
        for i in range(4):
            for j in range(2):
                self.coords[i][j] = table[i][j]

        self.pieceShape = shape

    def setRandomShape(self):
        self.setShape(random.randint(1, 7))

    def x(self, index):
        return self.coords[index][0]

    def y(self, index):
        return self.coords[index][1]

    def setX(self, index, x):
        self.coords[index][0] = x

    def setY(self, index, y):
        self.coords[index][1] = y

    def minX(self):
        m = self.coords[0][0]
        for i in range(4):
            m = min(m, self.coords[i][0])

        return m

    def maxX(self):
        m = self.coords[0][0]
        for i in range(4):
            m = max(m, self.coords[i][0])

        return m

    def minY(self):
        m = self.coords[0][1]
        for i in range(4):
            m = min(m, self.coords[i][1])

        return m

    def maxY(self):
        m = self.coords[0][1]
        for i in range(4):
            m = max(m, self.coords[i][1])

        return m

    def rotatedLeft(self):
        if self.pieceShape == SquareShape:
            return self

        result = TetrixPiece()
        result.pieceShape = self.pieceShape
        for i in range(4):
            result.setX(i, self.y(i))
            result.setY(i, -self.x(i))

        return result

    def rotatedRight(self):
        if self.pieceShape == SquareShape:
            return self

        result = TetrixPiece()
        result.pieceShape = self.pieceShape
        for i in range(4):
            result.setX(i, -self.y(i))
            result.setY(i, self.x(i))

        return result


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    window = TetrixWindow()
    window.show()
    random.seed(None)
    sys.exit(app.exec_())


tkrame.py

from tkinter import *
import tkinter as tk

class App(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.pack()
		self.create_widgets()

	def create_widgets(self):
		self.hi_there =tk.Button(self)
		self.hi_there["text"]="Hola F3nix\n(click me)"
		self.hi_there["command"] = self.say_hi
		self.hi_there.pack(side="top")

		self.quit =tk.Button(self, text = "QUIT", fg="red", command=root.destroy)
		


Ventana_Menu.py

from tkinter import *
from tkinter import messagebox
import sys
import os
import re
import math
import glob
import shutil
import locale

def imprime():
	print("Presionastes IMPRIMIR ")


ventana = Tk()
ventana.geometry("600x600+0+0")
ventana.title("Menus")
ventana.configure( background = 'dark turquoise')

b1=Button(ventana, text="SALIR", fg="dark red", command=ventana.quit)
b1.pack(side=LEFT)

b2=Button(ventana, text="IMPRIMIR", fg="dark blue", command=imprime)
b2.pack(side=RIGHT)


'''
###RECETA  PARA CREAR MENUS ###
#PASO 1. Crear la barra de Menbus.

barraMenu = Menu(ventana)

#PASO 2. Crear los  Menus.

mnuArchivo = Menu(barraMenu)

#PSASO 3. Crear los comandos de los Menus.

mnuArchivo.add_Command(Label="Abrir")
mnuArchivo.add_Command(Label="Nuevo")
mnuArchivo.add_Command(Label="Guardar")
mnuArchivo.add_Command(Label="Cerrar")
mnuArchivo.add_Command(Label="Salir")

#  """mnuArchivo.add_Command.Label.pack()  """ ---> NI IDEA???????????? pipipipipip

#PASO 4. Agregar los menus a  la barra de Menus.

barraMenu.add_Cascade(Label="Archivo", Menu=mnuArchivo)

#PASO 5. Indicamos que la barra de menus estara en la ventana.

ventana.config(menu=barraMenu)

'''
ventana.mainloop()





Ventana_Menu2.py

# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 18:35:50 2017

@author: AKER-PC
"""

from tkinter import *
import sys
import os
import re
import math
import glob
import shutil
import locale


ventana = Tk()
ventana.geometry("600x600+0+0")
ventana.title("Menus")
ventana.configure( background = 'dark turquoise')

b1=Button(ventana, text="SALIR", fg="dark red", command=ventana.quit)
b1.pack(side=LEFT)

b2=Button(ventana, text="IMPRIMIR", fg="dark blue", command=imprime)
b2.pack(side=RIGHT)



###RECETA  PARA CREAR MENUS ###
#PASO 1. Crear la barra de Menbus.

barraMenu = Menu(ventana)

#PASO 2. Crear los  Menus.

mnuArchivo = Menu(barraMenu)

#PSASO 3. Crear los comandos de los Menus.

mnuArchivo.add_Command(label="Abrir")
mnuArchivo.add_Command(label="Nuevo")
mnuArchivo.add_Command(label="Guardar")
mnuArchivo.add_Command(label="Cerrar")
mnuArchivo.add_Command(label="Salir")

#PASO 4. Agregar los menus a  la barra de Menus.

barraMenu.add_Cascade(label="Archivo", Menu=mnuArchivo)

#PASO 5. Indicamos que la barra de menus estara en la ventana.

ventana.config(menu=barraMenu)


ventana.mainloop()



VentanaS_y_TkinteR_.py

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from tkinter import *
import tkinter 

def imprime():
	print("Presionastes IMPRIMIR")

def bzo1():
	print("Presionastes Bzo_1")

def bzo2():
	ventana.iconify()

def helps():
	print('help()')
#	help()

ventana = Tk()
ventana.title("6__AKER__9")
#ventana.geometry('380x300')  # Ancho x Alto 
ventana.configure( background = 'dark turquoise')
#boton= Button(ventana, text="Button_0", fg="dark green", command=imprime2).place(x=10, y=10)
#etq0= Label(ventana, text="etq0").place(x=10, y=30)
#etq1= Label(ventana, text="etq1").place(x=10, y=50)
#etq2= Label(ventana, text="etq2").place(x=10, y=70)

b1=Button(ventana, text="SALIR", fg="dark red", command=ventana.quit)
b1.pack(side=TOP)

b2=Button(ventana, text="IMPRIMIR", fg="dark blue", command=imprime)
b2.pack(side=TOP)

b3=Button(ventana, text="HELP", fg="dark blue", command=helps)
b3.pack(side=TOP)

b4=Button(ventana, text="Button_1", fg="dark green", command=bzo1) # .place(x=20, y=90)
b4.pack(side=TOP)

b5=Button(ventana, text="minimizar", fg="dark blue", command=bzo2) # .place(x=100, y=110)
b5.pack(side=TOP)

'''
b5=Button(ventana, text="IMPRIMIR", fg="dark blue", command=imprime)
b5.pack(side=RIGHT)

b6=Button(ventana, text="IMPRIMIR", fg="dark blue", command=imprime)
b6.pack(side=RIGHT)

b7=Button(ventana, text="IMPRIMIR", fg="dark blue", command=imprime)
b7.pack(side=RIGHT)

b8=Button(ventana, text="IMPRIMIR", fg="dark blue", command=imprime)
b8.pack(side=RIGHT)

'''


ventana.mainloop()








VentanaTK.py

import tkinter
from tkinter.constants import *
tk = tkinter.Tk()

tk.title("F3nix App_1")
tk.configure( background = 'dark turquoise')


frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH,expand=1)
label = tkinter.Label(frame, text="F3nix App_1")
label.pack(fill=X, expand=1)
button = tkinter.Button(frame,text="Exit",command=tk.destroy)
button.pack(side=BOTTOM)
tk.mainloop()



shortcuts.xml

<NotepadPlus>
    <InternalCommands />
    <Macros>
        <Macro name="Trim Trailing Space and Save" Ctrl="no" Alt="yes" Shift="yes" Key="83">
            <Action type="2" message="0" wParam="42024" lParam="0" sParam="" />
            <Action type="2" message="0" wParam="41006" lParam="0" sParam="" />
        </Macro>
    </Macros>
    <UserDefinedCommands>
        <Command name="Launch in Firefox" Ctrl="yes" Alt="yes" Shift="yes" Key="88">firefox &quot;$(FULL_CURRENT_PATH)&quot;</Command>
        <Command name="Launch in IE" Ctrl="yes" Alt="yes" Shift="yes" Key="73">iexplore &quot;$(FULL_CURRENT_PATH)&quot;</Command>
        <Command name="Launch in Chrome" Ctrl="yes" Alt="yes" Shift="yes" Key="82">chrome &quot;$(FULL_CURRENT_PATH)&quot;</Command>
        <Command name="Launch in Safari" Ctrl="yes" Alt="yes" Shift="yes" Key="65">safari &quot;$(FULL_CURRENT_PATH)&quot;</Command>
        <Command name="Get php help" Ctrl="no" Alt="yes" Shift="no" Key="112">http://www.php.net/$(CURRENT_WORD)</Command>
        <Command name="Wikipedia Search" Ctrl="no" Alt="yes" Shift="no" Key="114">https://en.wikipedia.org/wiki/Special:Search?search=$(CURRENT_WORD)</Command>
        <Command name="Open file in another instance" Ctrl="no" Alt="yes" Shift="no" Key="117">$(NPP_FULL_FILE_PATH) $(CURRENT_WORD) -nosession -multiInst</Command>
        <Command name="Send via Outlook" Ctrl="yes" Alt="yes" Shift="yes" Key="79">outlook /a &quot;$(FULL_CURRENT_PATH)&quot;</Command>
        <Command name="IDE_PYthON_f3" Ctrl="yes" Alt="yes" Shift="no" Key="32">&quot;C:\Users\AKER-PC\Desktop\WinPython-64bit-3.6.2.0Qt5\IDLEX (Python GUI).exe&quot;</Command>
    </UserDefinedCommands>
    <PluginCommands />
    <ScintillaKeys />
</NotepadPlus>


Plantilla_01.cpp


#include<iostream>
#include<conio.h>
#include<stdlib.h>


using namespace std;


int main{





    getch();
    return 0;
}




Practika_01.cpp


#include<iostream>
#include<conio.h>
#include<stdlib.h>

//Prototipo  de Funcion
int  encontrarMax(int x, int y);

using namespace std;


int main{
    int n1,n2;
    int  mayor;
    cout<<"Digite 2 numeros: ";
    cin>>n1>>n2;

      mayor = encontrarMax(n1,n2);

    cout<<"El mayor de los numeros es: "<<mayor<<endl;
//  cout<<"El mayor de los numeros es: "encontrarMax(n1,n2)<<endl;

    getch();
    return 0;
}

//Definicion  de la Funcion

int  encontrarMax(int x, int y){
    int numMax;

    if(x>y){
        numMax =  x;
    }
    else{
        numMax =  y;
    }

    return numMax;
}


PrototipoDeFuncion.cpp


#include<iostream>
#include<conio.h>
#include<stdlib.h>

//Prototipo  de Funcion
int  encontrarMax(int x, int y);

using namespace std;


int main{
    int n1,n2;
    int  mayor;
    cout<<"Digite 2 numeros: ";
    cin>>n1>>n2;

      mayor = encontrarMax(n1,n2);

    cout<<"El mayor de los numeros es: "<<mayor<<endl;
//  cout<<"El mayor de los numeros es: "encontrarMax(n1,n2)<<endl;

    getch();
    return 0;
}

//Definicion  de la Funcion

int  encontrarMax(int x, int y){
    int numMax;

    if(x>y){
        numMax =  x;
    }
    else{
        numMax =  y;
    }

    return numMax;
}


PrototipoDeFuncion2.cpp


#include<iostream>
#include<conio.h>
#include<stdlib.h>

//Prototipo  de Funcion
int  encontrarMax(int x, int y);

using namespace std;


int main{
    int n1,n2;
    int  mayor;
    cout<<"Digite 2 numeros: ";
    cin>>n1>>n2;

      mayor = encontrarMax(n1,n2);

    cout<<"El mayor de los numeros es: "<<mayor<<endl;
//  cout<<"El mayor de los numeros es: "encontrarMax(n1,n2)<<endl;

    getch();
    return 0;
}

//Definicion  de la Funcion

int  encontrarMax(int x, int y){
    int numMax;

    if(x>y){
        numMax =  x;
    }
    else{
        numMax =  y;
    }

    return numMax;
}


GeoTrustGlobalCA.crt

-----BEGIN CERTIFICATE-----
MIIDVDCCAjygAwIBAgIDAjRWMA0GCSqGSIb3DQEBBQUAMEIxCzAJBgNVBAYTAlVT
MRYwFAYDVQQKEw1HZW9UcnVzdCBJbmMuMRswGQYDVQQDExJHZW9UcnVzdCBHbG9i
YWwgQ0EwHhcNMDIwNTIxMDQwMDAwWhcNMjIwNTIxMDQwMDAwWjBCMQswCQYDVQQG
EwJVUzEWMBQGA1UEChMNR2VvVHJ1c3QgSW5jLjEbMBkGA1UEAxMSR2VvVHJ1c3Qg
R2xvYmFsIENBMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA2swYYzD9
9BcjGlZ+W988bDjkcbd4kdS8odhM+KhDtgPpTSEHCIjaWC9mOSm9BXiLnTjoBbdq
fnGk5sRgprDvgOSJKA+eJdbtg/OtppHHmMlCGDUUna2YRpIuT8rxh0PBFpVXLVDv
iS2Aelet8u5fa9IAjbkU+BQVNdnARqN7csiRv8lVK83Qlz6cJmTM386DGXHKTubU
1XupGc1V3sjs0l44U+VcT4wt/lAjNvxm5suOpDkZALeVAjmRCw7+OC7RHQWa9k0+
bw8HHa8sHo9gOeL6NlMTOdReJivbPagUvTLrGAMoUgRx5aszPeE4uwc2hGKceeoW
MPRfwCvocWvk+QIDAQABo1MwUTAPBgNVHRMBAf8EBTADAQH/MB0GA1UdDgQWBBTA
ephojYn7qwVkDBF9qn1luMrMTjAfBgNVHSMEGDAWgBTAephojYn7qwVkDBF9qn1l
uMrMTjANBgkqhkiG9w0BAQUFAAOCAQEANeMpauUvXVSOKVCUn5kaFOSPeCpilKIn
Z57QzxpeR+nBsqTP3UEaBU6bS+5Kb1VSsyShNwrrZHYqLizz/Tt1kL/6cdjHPTfS
tQWVYrmm3ok9Nns4d0iXrKYgjy6myQzCsplFAMfOEVEiIuCl6rYVSAlk6l5PdPcF
PseKUgzbFbS9bZvlxrFUaKnjaZC2mqUPuLk/IH2uSrW4nOQdtqvmlKXBx4Ot2/Un
hw4EbNX/3aBd7YdStysVAq45pmp06drE57xNNB6pXE0zX5IJL4hmXXeXxx12E6nV
5fEWCRE11azbJHFwLJhWC9kXtNHjUStedejV0NxPNO3CBWaAocvmMw==
-----END CERTIFICATE-----


-paginamx.crt

-----BEGIN CERTIFICATE-----
MIIFZTCCBE2gAwIBAgIQLCc/Py8kySLnBKjjwwYBbDANBgkqhkiG9w0BAQsFADBC
MQswCQYDVQQGEwJVUzEWMBQGA1UEChMNR2VvVHJ1c3QgSW5jLjEbMBkGA1UEAxMS
UmFwaWRTU0wgU0hBMjU2IENBMB4XDTE3MDMwMjAwMDAwMFoXDTE4MDQyMzIzNTk1
OVowFjEUMBIGA1UEAwwLKi5wYWdpbmEubXgwggEiMA0GCSqGSIb3DQEBAQUAA4IB
DwAwggEKAoIBAQC/NedbQAZIUn+mAdjJMocWOTsjF5nDxhdDcYV4GUJqX4aXcl0f
/nziEDOC+AD59lPoGKzNBPvnMmNRUTjgn9saIjum3xz4ulRaIMyXbi1S51iXFgzt
JTdS/XOrIK5CWtBLhWK7IuL0CVyLblllGlS3TLKVY4KpsvCkcKuVfUTwACgno5Zp
scUqbxHxXZKFZovJjoyWdXGtXW0hh8WPWiorFjk9sWM1MzzviJ7RlPxvFQVgZAiD
C9ERq2Y4KmLLqE2CAjtgsK7WHhKUgTd6Y3Uhfx0QJmyTJCcbFzlNj14wS0fCl11e
+VUwCrX/AuldymtTTat1W/hHEde698Ot7X0VAgMBAAGjggKBMIICfTAhBgNVHREE
GjAYggsqLnBhZ2luYS5teIIJcGFnaW5hLm14MAkGA1UdEwQCMAAwKwYDVR0fBCQw
IjAgoB6gHIYaaHR0cDovL2dwLnN5bWNiLmNvbS9ncC5jcmwwbwYDVR0gBGgwZjBk
BgZngQwBAgEwWjAqBggrBgEFBQcCARYeaHR0cHM6Ly93d3cucmFwaWRzc2wuY29t
L2xlZ2FsMCwGCCsGAQUFBwICMCAMHmh0dHBzOi8vd3d3LnJhcGlkc3NsLmNvbS9s
ZWdhbDAfBgNVHSMEGDAWgBSXwidQnsLJ7AyIMsh8reKmAU/abzAOBgNVHQ8BAf8E
BAMCBaAwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMFcGCCsGAQUFBwEB
BEswSTAfBggrBgEFBQcwAYYTaHR0cDovL2dwLnN5bWNkLmNvbTAmBggrBgEFBQcw
AoYaaHR0cDovL2dwLnN5bWNiLmNvbS9ncC5jcnQwggEEBgorBgEEAdZ5AgQCBIH1
BIHyAPAAdwDd6x0reg1PpiCLga2BaHB+Lo6dAdVciI09EcTNtuy+zAAAAVqPntJK
AAAEAwBIMEYCIQDczaAoRPEXDXWV3IsOLD9F4757XsgMxC1lq1PVZDbRZwIhAPGS
yNFB+z80COiTGu0MUi9TovKQVj3HCqam5sigIrPhAHUApLkJkLQYWBSHuxOizGdw
Cjw1mAT5G9+443fNDsgN3BAAAAFaj57ScwAABAMARjBEAiBuXgusF3HhyqVPFZkz
ctgWm8IdJGd4b/oxG/vI4yvHGgIgc+gJA8m2289FbS73hGozTq3Rz8p/2jP4xFlc
Db2dGR0wDQYJKoZIhvcNAQELBQADggEBACsULjystz9S3Et7kZn3tm5kv8PujbC5
eMUe/jYlEOiJ5hXXcaFOwOJAsaBex0g5L2Do8Mq8unTMWOB9MPhSJDCks20S2YtB
0Le4SjaT3CYNaGtr8tkxUDDqdRMuXhRu1I0qn5FhAZ8qBbP12Lw1OrAqm+l5p1W0
AdbR3anizxhPFVhVSLXdq0KCiLmM0o6hkxvsJUUO7IzVEtyjyuzSEizawxvNFqLx
TpxlLJO8tRd7Isr5DCFFGHTWUmYSRDDr4TV6BCOZWdxxBvdJNABR/a5TvWvy3kOr
Em0XdSLiI3EkQZGNP9e9l5Md9nyYpI8F42UpMjQVg3LC/51yb5h22SY=
-----END CERTIFICATE-----


RapidSSLSHA256CA.crt

-----BEGIN CERTIFICATE-----
MIIETTCCAzWgAwIBAgIDAjpxMA0GCSqGSIb3DQEBCwUAMEIxCzAJBgNVBAYTAlVT
MRYwFAYDVQQKEw1HZW9UcnVzdCBJbmMuMRswGQYDVQQDExJHZW9UcnVzdCBHbG9i
YWwgQ0EwHhcNMTMxMjExMjM0NTUxWhcNMjIwNTIwMjM0NTUxWjBCMQswCQYDVQQG
EwJVUzEWMBQGA1UEChMNR2VvVHJ1c3QgSW5jLjEbMBkGA1UEAxMSUmFwaWRTU0wg
U0hBMjU2IENBMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAu1jBEgEu
l9h9GKrIwuWF4hdsYC7JjTEFORoGmFbdVNcRjFlbPbFUrkshhTIWX1SG5tmx2GCJ
a1i+ctqgAEJ2sSdZTM3jutRc2aZ/uyt11UZEvexAXFm33Vmf8Wr3BvzWLxmKlRK6
msrVMNI4/Bk7WxU7NtBDTdFlodSLwWBBs9ZwF8w5wJwMoD23ESJOztmpetIqYpyg
C04q18NhWoXdXBC5VD0tA/hJ8LySt7ecMcfpuKqCCwW5Mc0IW7siC/acjopVHHZD
dvDibvDfqCl158ikh4tq8bsIyTYYZe5QQ7hdctUoOeFTPiUs2itP3YqeUFDgb5rE
1RkmiQF1cwmbOwIDAQABo4IBSjCCAUYwHwYDVR0jBBgwFoAUwHqYaI2J+6sFZAwR
fap9ZbjKzE4wHQYDVR0OBBYEFJfCJ1CewsnsDIgyyHyt4qYBT9pvMBIGA1UdEwEB
/wQIMAYBAf8CAQAwDgYDVR0PAQH/BAQDAgEGMDYGA1UdHwQvMC0wK6ApoCeGJWh0
dHA6Ly9nMS5zeW1jYi5jb20vY3Jscy9ndGdsb2JhbC5jcmwwLwYIKwYBBQUHAQEE
IzAhMB8GCCsGAQUFBzABhhNodHRwOi8vZzIuc3ltY2IuY29tMEwGA1UdIARFMEMw
QQYKYIZIAYb4RQEHNjAzMDEGCCsGAQUFBwIBFiVodHRwOi8vd3d3Lmdlb3RydXN0
LmNvbS9yZXNvdXJjZXMvY3BzMCkGA1UdEQQiMCCkHjAcMRowGAYDVQQDExFTeW1h
bnRlY1BLSS0xLTU2OTANBgkqhkiG9w0BAQsFAAOCAQEANevhiyBWlLp6vXmp9uP+
bji0MsGj21hWID59xzqxZ2nVeRQb9vrsYPJ5zQoMYIp0TKOTKqDwUX/N6fmS/Zar
RfViPT9gRlATPSATGC6URq7VIf5Dockj/lPEvxrYrDrK3maXI67T30pNcx9vMaJR
BBZqAOv5jUOB8FChH6bKOvMoPF9RrNcKRXdLDlJiG9g4UaCSLT+Qbsh+QJ8gRhVd
4FB84XavXu0R0y8TubglpK9YCa81tGJUheNI3rzSkHp6pIQNo0LyUcDUrVNlXWz4
Px8G8k/Ll6BKWcZ40egDuYVtLLrhX7atKz4lecWLVtXjCYDqwSfC2Q7sRwrp0Mr8
2A==
-----END CERTIFICATE-----

from cx_Freeze import setup, Executable

exe=Executable(
 script="ytDl_6.9.py",
 base=None,
 icon=None
 )
"""
includefiles=[]
includes=[]
excludes=[]
packages=[]
"""
setup(
 version = "6.9",
 description = "Programa  para descargar facil y rapido videos Mp4 de YouTube  y algunas  otras  WebPages...",
 author = "_F3NiX_",
 name = "VideoDescargas_F3NiX.exe",
 #options = {'build_exe': {'excludes':excludes,'packages':packages,'include_files':includefiles}},
 executables = [exe]
 )
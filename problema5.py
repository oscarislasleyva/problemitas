'''
http://sg.com.mx/revista/47/cinco-problemas-para-menos-1-hora#.VftNmhrR-N1
Problema 5
La cadena original es 123456789
1 2 3 4 5 6 7 8 9
 X X X X X X X X
en cada X va uno de los siguientes operadores: concatena '',suma '+' o resta '-'
construyes la cadena concatenando y la evaluas para saber si el resultado
cumple el requisito de que sea igual a 100
'''
cien = 100
cont= 1
L = ['','+','-']
for a in L:
 for b in L:
  for c in L:
   for d in L:
    for e in L:
     for f in L:
      for g in L:
       for h in L:
         cadena = "1"+a+"2"+b+"3"+c+"4"+d+"5"+e+"6"+f+"7"+g+"8"+h+"9" 
         if eval(cadena)==cien:
           print (cadena + " =" , cien)
           cont = cont+1      

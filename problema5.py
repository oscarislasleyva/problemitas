'''
http://sg.com.mx/revista/47/cinco-problemas-para-menos-1-hora#.VftNmhrR-N1
Problema 5

La cadena original es 123456789

1 2 3 4 5 6 7 8 9
 x x x x x x x x

en cada X va uno de los siguientes operadores: concatena '',suma '+' o resta '-'
'''
cont= 1;
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
         if eval(cadena)==100:
           print "%i) "%cont + cadena + " = " + "%i"%eval(cadena)
           cont = cont+1      

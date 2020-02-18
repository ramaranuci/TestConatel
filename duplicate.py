"""Cree un programa/función/clase/metodo que cumpla con la siguiente interface:
// list -> list
duplicate([1, 2, 3]);
// [1, 2, 3, 1, 2, 3]
// string -> string
duplicate('abcd efgh');
// 'abcd efghabcd efgh'
// number -> number
duplicate(123);
// 123123
"""


def duplicate(elemento):
   tipo=str(type(elemento))   
   if 'int' in tipo:
      return int(str(elemento)*2)
   elif 'list'in tipo:         
      return elemento*2      
   elif 'str' in tipo:
      return elemento*2
   else:
      return "Argumento no permitido"
     
arreglo=[2,3,5,6]
cadena='hello you'
numeros=123
print(duplicate(arreglo))        

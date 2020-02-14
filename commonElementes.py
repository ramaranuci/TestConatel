"""
Imagina que cuentas con dos listas:
a = [1, 2, 3, 4, 5];
b = [3, 2, 9, 3, 7];
Realize un programa/función/clase/metodo que encuentre los elementos comúnes en
ambas listas.
Returns:
    [list] -- common_elements(a, b) // [3,2]
"""

def common_elements(*Lista):
   res=list(set.intersection(*map(set,Lista)))
   return res

a=[2,3,4,6,8,1]
b=[3,8,9,1,2]
d=[1,20,6,2,8]
f=[1,5,2]
c=[a,b,d]
print(common_elements(b,a,d))     

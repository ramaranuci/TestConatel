def common_elements(Lista):
    respuesta={}    
    for i in range(len(Lista)):
        list1=set(Lista[i])
        list2=set(Lista[i-1])
        respuesta=list1.intersection(list2)   

    
    return respuesta

a=[2,3,4,6,8]
b=[3,8,9,1,2]
c=[a,b]
print(common_elements(c))     

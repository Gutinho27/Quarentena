primos = []
for num in range(1,101):  #contador dos 100 primeiros números!
    count = 0
    for numb in range(1,num+1):  #aqui é pra ver quantas vezes é dividido até chegar nele mesmo.
        if num % numb == 0:     # se ele for divisivel conta 1
            count += 1
    if count ==2:        #pra um número ser primo, só pode ser divisel 2x
        primos.append (num)   
print (primos)
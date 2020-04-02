import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(_name_)

@app.route('/')

def primoss():
    primos = []
    for num in range(1,101):  #contador dos 100 primeiros números!
        count = 0
        for numb in range(1,num+1):  #aqui é pra ver quantas vezes é dividido até chegar nele mesmo.
            if num % numb == 0:     # se ele for divisivel conta 1
                count += 1
        if count ==2:        #pra um número ser primo, só pode ser divisel 2x
            primos.append (num)   
    return (primos)

if _name_ == "_main_":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
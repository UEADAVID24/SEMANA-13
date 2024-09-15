# funcion de la suma
def suma(sumando1, sumando2):
    resultado_suma=sumando1+sumando2
    return resultado_suma

resultado=suma(2,3)
#print(resultado)



#calcular el promedio de una temperatura de una ciudad

temperaturas=[
    [ #ciudades
        [#semana
            1,#dia 1
            3,#dia 2
            5 #dia 3
        ]
        [10,13,14]
    ]
    [
        [3,5,6]
        [5,6,7]
    ]
]

def promedio_temperatura_ciudad(arreglo_temperaturas,ciudad,semana):
    acumulador=0
    for i in arreglo_temperaturas[ciudad][semana] in range(len(arreglo_temperaturas[ciudad])):
        acumulador = acumulador + arreglo_temperaturas[ciudad][i]

        promedio = acumulador/len(arreglo_temperaturas[ciudad][i])

        return promedio

resultado_promedio = promedio_temperatura_ciudad(temperaturas, ciudad 0, semana1)

print(resultado_promedio)





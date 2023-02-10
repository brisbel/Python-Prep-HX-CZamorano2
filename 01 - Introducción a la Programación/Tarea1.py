
###Tarea 1: Variables

#1 Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla
var_01 = 5
print(var_01)

#2 Imprimir el tipo de dato de la constante 8.5
type(8.5)
var_02 = 8.5
type(var_02)

#3 Imprimir el tipo de dato de la variable creada en el punto 1
type(var_01)

#4 Crear una variable que contenga tu nombre
var_03= 'Brisna'
print(var_03)

#5 Crear una variable que contenga un número complejo
var_04= 2 + 1j
print(var_04)

#6 Mostrar el tipo de dato de la variable crada en el punto 5
type(var_04)

#7 ¿? Crear una variable que contenga el valor del número Pi redondeado a 4 decimales
# Import math Library
import math
var_05=math.pi
type(var_05)
print(var_05)
var_06= "{:.4f}".format(var_05)
type(var_06)
print(var_06)

#8 Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?
var_07='True'
var_08=True
print(var_07==var_08)
var_07==var_08
print("La comparacion es", var_07==var_08 )

#9 Imprimir el tipo de dato correspondientes a las variables creadas en el punto 9
type(var_07)
type(var_08)

#10 Asignar a una variable, la suma de un número entero y otro decimal
var_09 = 10
var_10= 5.23
var_11 = var_09 + var_10
print(var_11)

#11 Realizar una operación de suma de números complejos
print(var_05 + var_05)

#12 Realizar una operación de suma de un número real y otro complejo
print(var_01 + int(var_05))

#13 Realizar una operación de multiplicación
print(var_01*100)

#14 Mostrar el resultado de elevar 2 a la octava potencia
print(2**8)

#15 Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla
var_12=27
var_13=4
var_14=var_12/var_13
print(var_14)

#16 De la división anterior solamente mostrar la parte entera
print(var_12//var_13)
var_15 = var_12//var_13
print(var_15)

#17 De la división de 27 entre 4 mostrar solamente el resto
print(var_12%var_13)
var_16 = var_12%var_13
print(var_16)

#18 Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado
var_17= (var_15 * 4) + var_16
print(var_17)

#19 Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas
var_18='Hola'
var_19='Mundo'
var_20= var_18 + " " + var_19
print(var_20)
print(var_18 + var_19)
print(var_18 + " " + var_19)

#20 Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?
2 == "2"
print("Es falso porque uno es numerico y el otro string")

#21 Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera
2 == int("2")

#22 ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')
print("Porque float implica que es numero, y lo que se esta reportando es una string porque esta entre comillas, y aunsino tuviera comillas tiene una coma en vez de punto")

#23 Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido
var_20 = -3
print(var_20)
var_20 -= 1
print(var_20)
##OJO: Siempre es sobre la misma variable. A -= B es lo mismo que A = A - B

#24 Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?
1 << 2
#Da como resultado 4, porque esta haciendo operaciuones en codigo binario
#En x << y presenta le dice que la representacion en codigo binario de X la mueva Y bits a la izquierda y llene esos espacios con 0 (o sea agrega 0 a la derecha). Si el simbolo fuera al reves se agregarian a la izquierda
print(bin(1))
#Esto da 0b1.. y nosotros le dijimos se moviera 2 espacios a la izquierda 0b100
print(bin(1<<2))
#Si le pedimos el binerio de 4 que es el resultado que nos daba, vemos que es el mismo codigo
print(bin(4))

##OJO:Para entender que esta haciendo
print(bin(1))

1<<1
print(bin(1<<1))
print(bin(2))

1<<2
print(bin(1<<2))
print(bin(4))

1<<3
print(bin(1<<3))
print(bin(8))

#25 Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?
print("No se puede porque el tipo de variable es ditinto. Si fueran del mismo tipo int realizaria la suma, y si fueran del mismo tipo str escribiria 22")

#26 Realizar una operación válida entre valores de tipo entero y string
var_21 = '--Texto a repetir--'
var_22 = 3
print("Vamos a repetir la var_21 3 veces")
print(var_21 * var_22)
print("El ", var_21, " Se repite ", str(var_22) + ' veces')

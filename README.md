# Parcial2_Python_Mutantes
# Parcial 2 de la prueba de mutantes en Python hecho por Piers Rideout para Programacion I de la UTN
* Nombre y Apellido: Piers Rideout
* Legajo: 51630
* Email: piersrideout@gmail.com

## De que va el proyecto

Se intenta crear un programa escrito en Python que, por medio del ingreso de Strings por el usuario, determine si un humano es mutante o no.

## Como lo resolvimos

El programa se divide en 3 partes:

* 1.- Se ingresa el string por el usuario.
* 2.- Se verifica si es mutante o no.
* 3.- Se muestra el resultado.

La verificacion de la cadena se realiza de la sigueinte manera:
* 1.- Se busca si hay 4 letras iguales en horizontal.
* 2.- Se busca si hay 4 letras iguales en vertical.
* 3.- Se busca si hay 4 letras iguales en diagonal.
* 4.- Se busca si hay 4 letras iguales en diagonal inversa.

Si se encuentra más de una coincidencia, se asume que es mutante.

## Como correrlo

Se pide al usuario que ingrese cadenas de ADN como strings, por ejemplo "ATGCGA", seguido de "CAGTGC", "TTATGT", etc. Despues de ingresar 6 cadenas, el programa las procesa y muestra el resultado. En caso de exito, muestra el mensaje menmensaje "Es mutante". En caso de fracaso, muestra el mensaje "No es mutante".

## Casos de prueba
* Exito ("Es un mutante"): 
ATGCGA
CAGTGC
TTATGT
AGAAGG
CCCCTA
TCACTG

* Fracaso ("No es mutante"):
ATGCGA
CAGTGC
TTATTT
AGACGG
GCGTCA
TCACTG

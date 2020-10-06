from random import choice
def mostrarVcomoStr(v):
    cadena = ''
    for i in v:
        cadena = cadena + i
    return cadena
    
def hangman(palabra, intento):
    gano = False
    emboco = False
#    print('La pabra a adivinar es: {}\nLe quedan {} vidas.\n'.format(mostrarVcomoStr(palabra), str(vidas)))
    
    if intento == palabra:
        gano = True
    elif len(intento) == 1:
        pos = 0
        for i in palabra:
            if letra == i:
                emboco = True
                palabra[pos] = i
            pos += 1
    return emboco, gano, palabra
    		
def main():
    palabras = 'hola', 'como', 'estas'
    palabra = choice(palabras)
    long = len(palabra)
    #poner reglas y bienvenida
    print('BIENVENIDO AL HANGMAN CRACK ME DIO PAJA PONER LAS REGLAS PERO PUSE ESTO\n\n────(♥)(♥)(♥)────(♥)(♥)(♥) __ Si estas en soledad,\n──(♥)██████(♥)(♥)██████(♥) _seré tu sombra.\n─(♥)████████(♥)████████(♥) si quieres llorar,\n─(♥)██████████████████(♥) tendrás mi hombro.\n──(♥)████████████████(♥) si necesitas un abrazo,\n────(♥)████████████(♥) _ seré tu almohada.\n──────(♥)████████(♥) _si ansias estar feliz,\n────────(♥)████(♥) __ estaré sonriente.\n─────────(♥)██(♥) y cada vez que me necesites,\n───────────(♥) __ aquí estaré presente.\n')
    print('Su palabra es de longitud {}\n'.format(str(long)))
    hangman(palabra)


if __name__ == '__main__':
    main()

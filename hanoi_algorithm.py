import os
import sys
from stack_structure import Stack


"""
LOGICA UTILIZADA PARA LA ELABORACION DEL ALGORITMO
Nota: Lo encerrado entre "*" es la lógica que implementa este
      algoritmo para resolver el juego

Otra manera de resolver el problema, sin utilizar la recursividad,
se basa en el hecho de que para obtener la solución más corta,
** es necesario mover el disco más pequeño en todos los pasos impares,**
mientras que en los pasos pares solo existe un movimiento posible que no
lo incluye. El problema se reduce a decidir en cada paso impar a cuál de
las dos pilas posibles se desplazará el disco pequeño. El algoritmo en
cuestión depende del número de discos del problema:

    Si inicialmente se tiene un número impar de discos, el primer movimiento
    debe ser colocar el disco más pequeño en la pila destino, y en cada paso
    impar se le mueve a la siguiente pila a su izquierda
    (o a la pila destino si está en la pila origen).

    *** SECUENCIA DE MOVIMIENTOS DEL ARO 1 PARA CANTIDAD DE ANILLOS IMPAR  ***
    La secuencia será: destino, auxiliar, origen, destino, auxiliar, origen, etc
    Ciclo para disco 1,
    Con numeros de Anillos IMPAR-->['Origen', 'Destino', 'Auxiliar']
    *****************************************************************
    Si se tiene inicialmente un número par de discos, el primer movimiento debe
    ser colocar el disco más pequeño en la pila auxiliar, y en cada paso impar
    se le mueve a la siguiente pila a su derecha (o a la pila origen si está en
    la pila destino).
    *** SECUENCIA DE MOVIMIENTOS DEL ARO 1 PARA CANTIDAD DE ANILLOS PAR  ***
    La secuencia será: auxiliar, destino, origen, auxiliar, destino, origen, etc.
    Ciclo para disco 1, Con numeros de Anillos PAR-->['Origen', 'Auxiliar', 'Destino']
    **********************************************************************************

    **************************************** REGLA DE LOS COLORES DISTINTOS
    Una forma equivalente de resolverlo es la siguiente: coloreando los discos pares
    de un color y los impares de otro, y se resuelve el problema añadiendo la siguiente
    regla: no colocar juntos dos discos de un mismo color. De esta manera, solo queda
    un movimiento posible (además del de volver hacia atrás). *****************


A TOMAR EN CUENTA:

.- Todos la valores del Diccionarios y la variable "empty" son cadenas de
   exactamente 9 espacios para que todo coincida al renderizar
.- secuencia_uno:  A esta variable le asignaré valores entre [0,1,2] para ejecutar
   los movimientos de las secuencias establecidas
.- impar : A esta Variable le asignare True si numero de discos es impar y
           False en caso contrario

# Donde Esta el DISCO UNO ????
.- La Variable `secuencia_uno` la utilizo como indice
.- Cuando NUMEROS DE DISCOS ES IMPAR ---> Utilizo la variable `secuencia_donde_impar`
.- Cuando NUMEROS DE DISCOS ES PAR ---> Utilizo la variable `secuencia_donde_par`
"""

rings: dict = {
    1: "    █    ",
    2: "   ░░░   ",
    3: "  █████  ",
    4: " ░░░░░░░ ",
    5: "█████████",
}

empty: str = "    │    "

# Las 3 variables que tendrán estructura y comportamiento de Pilas para facilidad del problema
origen: object = Stack()
auxiliar: object = Stack()
destino: object = Stack()
# Las 3 Variables que utilizó para renderizar por consola cada Stack o Pila
origen_dic: dict = {}
auxiliar_dic: dict = {}
destino_dic: dict = {}


# Secuencia Aro 1 cuando n es IMPAR = [destino, auxiliar, origen]
secuencia_donde_impar: list = ["ORIGEN", "DESTINO", "AUXILIAR"]
movimientos_uno_n_impar: list = [
    "movimientos(origen, destino, origen_dic, destino_dic, n_discos)",
    "movimientos(destino, auxiliar, destino_dic, auxiliar_dic, n_discos)",
    "movimientos(auxiliar, origen, auxiliar_dic, origen_dic, n_discos)",
]

# Secuencia Aro 1 cuando n es PAR = [auxiliar, destino, origen]
secuencia_donde_par: list = ["ORIGEN", "AUXILIAR", "DESTINO"]
movimientos_uno_n_par: list = [
    "movimientos(origen, auxiliar, origen_dic, auxiliar_dic, n_discos)",
    "movimientos(auxiliar, destino, auxiliar_dic, destino_dic, n_discos)",
    "movimientos(destino, origen, destino_dic, origen_dic, n_discos)",
]
secuencia_uno: int
impar: bool
preguntando_numero_discos: str = """


                                TORRES DE HANOI


    Nota: El Programa solo puede ejecutar el Juego si n (Número de Aros) es 3, 4 ó 5

    Por favor Introduzca el numero de Aros Para Empezar   """


def clear_screen() -> None:
    """limpia la consola"""
    os.system("cls" if os.name == "nt" else "clear")


def blanK_lines(number: int) -> None:
    """Lineas en blanco

    Args:
        number (int): Numero de lineas
    """
    for i in range(number):
        print("")


def movimientos(pila_1: Stack, pila_2: Stack, dic_1: dict, dic_2: dict, n: int) -> None:
    """En cada movimiento interactuan 2 Pilas o Stacks esta funcion
       realiza la interaccion entre esas dos Pilas

    Args:
        pila_1 (Stack): Stack de donde sale un aro en ese movimiento
        pila_2 (Stack): Stack que recibe el aro que salió de pila_1
        dic_1 (dict): Diccionario que representa graficamente a pila_1
        dic_2 (dict): Diccionario que representa graficamente a pila_2
        n (int): Numero de Discos que eligio el Usuario al prin-
                        cipio del juego
    """
    aro_numero: int = pila_1.peek()
    size_pila_1: int = pila_1.size()
    # En caso de que la pila receptora del aro este vacia
    if pila_2.is_empty():
        pila_2.push(pila_1.pop())
        dic_2[n] = rings[aro_numero]
        dic_1[n - size_pila_1 + 1] = empty
    else:
        # Sí no está vacia hay que verificar que el elemento que se está moviendo
        # es mas grande que el elemento superior de la pila que recibe.
        # De cumplirse esa condición el movimiento no es valido y
        # no hay moviento en este llamado a la función
        if pila_1.peek() > pila_2.peek():
            blanK_lines(3)
            input("MOVIMIENTO NO PERMITIDO")
            return
        else:
            # En caso de que el movimiento si sea permitido
            size_pila_2 = pila_2.size()
            pila_2.push(pila_1.pop())
            dic_1[n - size_pila_1 + 1] = empty
            dic_2[n - size_pila_2] = rings[aro_numero]
    return


def mostrar_torres(n_discos: int) -> None:
    """Renderiza en Terminal. Necesita saber con cuantos Aros se está jugando
       en esta oportunidad

    Args:
        n_discos (int): Número de aros seleccionado por el usuario al
                        principio del juego
    """
    clear_screen()
    blanK_lines(4)
    for i in range(n_discos):
        print(
            " " * 4
            + origen_dic[i + 1]
            + " " * 6
            + auxiliar_dic[i + 1]
            + " " * 6
            + destino_dic[i + 1]
        )
    print("   ─────┴─────    ─────┴─────    ─────┴─────")
    print("     ORIGEN         AUXILIAR       DESTINO  ")
    blanK_lines(4)


def uno_esta_en_origen(n_discos: int) -> None:
    """Logica de que hacer en el movimiento que NO SE MUEVE EL DISCO 1
       sabiendo que este se encuentre ubicado en ORIGEN

    Args:
        n_discos (int): Numero de discos con que se esta jugando
    """
    if auxiliar.is_empty():
        movimientos(destino, auxiliar, destino_dic, auxiliar_dic, n_discos)
    elif destino.is_empty():
        movimientos(auxiliar, destino, auxiliar_dic, destino_dic, n_discos)
    elif auxiliar.peek() < destino.peek():
        movimientos(auxiliar, destino, auxiliar_dic, destino_dic, n_discos)
    else:
        movimientos(destino, auxiliar, destino_dic, auxiliar_dic, n_discos)


def uno_esta_en_auxiliar(n_discos: int) -> None:
    """Logica de que hacer en el movimiento que NO SE MUEVE EL DISCO 1
       sabiendo que este se encuentre ubicado en AUXILIAR

    Args:
        n_discos (int): Numero de discos con que se esta jugando
    """
    if origen.is_empty():
        movimientos(destino, origen, destino_dic, origen_dic, n_discos)
    elif destino.is_empty():
        movimientos(origen, destino, origen_dic, destino_dic, n_discos)
    elif origen.peek() < destino.peek():
        movimientos(origen, destino, origen_dic, destino_dic, n_discos)
    else:
        movimientos(destino, origen, destino_dic, origen_dic, n_discos)


def uno_esta_en_destino(n_discos: int) -> None:
    """Logica de que hacer en el movimiento que NO SE MUEVE EL DISCO 1
       sabiendo que este se encuentre ubicado en DESTINO

    Args:
        n_discos (int): Numero de discos con que se esta jugando
    """
    if origen.is_empty():
        movimientos(auxiliar, origen, auxiliar_dic, origen_dic, n_discos)
    elif auxiliar.is_empty():
        movimientos(origen, auxiliar, origen_dic, auxiliar_dic, n_discos)
    elif origen.peek() < auxiliar.peek():
        movimientos(origen, auxiliar, origen_dic, auxiliar_dic, n_discos)
    else:
        movimientos(auxiliar, origen, auxiliar_dic, origen_dic, n_discos)


def main(empezando: bool) -> None:
    """Función Principal donde se ejecuta la lógica del Juego

    Args:
        empezando (bool): Para saber si es primera vez O NO del
                          ciclo while. Ya que la primera vez debe
                          Preguntar por n
    """
    while True:
        clear_screen()
        blanK_lines(4)
        if empezando:
            # n_discos = preguntando_numero_discos()
            # Ciclo solo para asegurar de que sea 3, 4 ó 5
            while True:
                numero_string = input(preguntando_numero_discos)
                # n_string = input('Por favor Introduzca el numero de Aros Para Empezar  ')
                if numero_string.strip() in ["3", "4", "5"]:
                    n_discos = int(numero_string)
                    break
                else:
                    blanK_lines(4)
                    input("OPCION NO VALIDA CABEZON")
                    clear_screen()
                    blanK_lines(4)
            empezando = False
            for i in range(n_discos, 0, -1):
                origen_dic[i] = rings[i]
                origen.push(i)
                auxiliar_dic[i] = empty
                destino_dic[i] = empty

                impar = True if n_discos % 2 != 0 else False

                secuencia_uno = 0

                donde_esta_uno = (
                    secuencia_donde_impar[secuencia_uno]
                    if impar
                    else secuencia_donde_par[secuencia_uno]
                )
                siguiente_iteracion = 1
        else:
            mostrar_torres(n_discos=n_discos)
            input("PRESIONA ENTER PARA MOSTRAR SIGUIENTE MOVIMIENTO")
            if destino.size() == n_discos:
                print(f"Numero Total de Movimientos ---> {siguiente_iteracion - 1}")
                blanK_lines(4)
                sys.exit(0)
            if siguiente_iteracion % 2 != 0:
                if impar:
                    eval(movimientos_uno_n_impar[secuencia_uno])
                else:
                    eval(movimientos_uno_n_par[secuencia_uno])
                # secuencia += 1 si es que secuencia es menor a 2, de lo contrario reinicio el contador
                secuencia_uno = 0 if secuencia_uno == 2 else secuencia_uno + 1
                donde_esta_uno = (
                    secuencia_donde_impar[secuencia_uno]
                    if impar
                    else secuencia_donde_par[secuencia_uno]
                )
            else:
                if donde_esta_uno == "ORIGEN":
                    uno_esta_en_origen(n_discos=n_discos)
                    # if auxiliar.is_empty():
                    #     movimientos(
                    #         destino, auxiliar, destino_dic, auxiliar_dic, n_discos
                    #     )
                    # elif destino.is_empty():
                    #     movimientos(
                    #         auxiliar, destino, auxiliar_dic, destino_dic, n_discos
                    #     )
                    # elif auxiliar.peek() < destino.peek():
                    #     movimientos(
                    #         auxiliar, destino, auxiliar_dic, destino_dic, n_discos
                    #     )
                    # else:
                    #     movimientos(
                    #         destino, auxiliar, destino_dic, auxiliar_dic, n_discos
                    #     )
                if donde_esta_uno == "AUXILIAR":
                    uno_esta_en_auxiliar(n_discos=n_discos)
                    # if origen.is_empty():
                    #     movimientos(destino, origen, destino_dic, origen_dic, n_discos)
                    # elif destino.is_empty():
                    #     movimientos(origen, destino, origen_dic, destino_dic, n_discos)
                    # elif origen.peek() < destino.peek():
                    #     movimientos(origen, destino, origen_dic, destino_dic, n_discos)
                    # else:
                    #     movimientos(destino, origen, destino_dic, origen_dic, n_discos)
                if donde_esta_uno == "DESTINO":
                    uno_esta_en_destino(n_discos=n_discos)
                    # if origen.is_empty():
                    #     movimientos(
                    #         auxiliar, origen, auxiliar_dic, origen_dic, n_discos
                    #     )
                    # elif auxiliar.is_empty():
                    #     movimientos(
                    #         origen, auxiliar, origen_dic, auxiliar_dic, n_discos
                    #     )
                    # elif origen.peek() < auxiliar.peek():
                    #     movimientos(
                    #         origen, auxiliar, origen_dic, auxiliar_dic, n_discos
                    #     )
                    # else:
                    #     movimientos(
                    #         auxiliar, origen, auxiliar_dic, origen_dic, n_discos
                    #     )
            # input()
            siguiente_iteracion += 1


if __name__ == "__main__":
    main(empezando=True)

import os
import sys

# Importo de otro archivo la estructura que se usará como Pila
from stack_structure import Stack

rings: dict = {
    1: "    █    ",
    2: "   ░░░   ",
    3: "  █████  ",
    4: " ░░░░░░░ ",
    5: "█████████",
}

empty: str = "    │    "

# Las 3 variables que tendrán estructura y comportamiento de Pilas
origen: object = Stack()
auxiliar: object = Stack()
destino: object = Stack()
# Las 3 Variables que utilizó para renderizar por consola cada Stack o Pila
origen_dic: dict = {}
auxiliar_dic: dict = {}
destino_dic: dict = {}

menu: str = """

                                TORRES DE HANOI


    1  Origen ------> Destino
    2  Origen ------> Auxiliar
    3  Destino -----> Origen
    4  Destino -----> Auxiliar
    5  Auxiliar ----> Destino
    6  Auxiliar ----> Origen

    Q  Salir...


    Seleccione una Opción: """

preguntando_n_discos: str = """


                                TORRES DE HANOI


    Nota: El Programa solo puede ejecutar el Juego si n (Número de Aros) es 3, 4 ó 5

    Por favor Introduzca el numero de Aros Para Empezar   """


def clear_screen() -> None:
    """Limpia la terminal"""
    os.system("cls" if os.name == "nt" else "clear")


def blanK_lines(number: int) -> None:
    """Lineas en blanco en la terminal

    Args:
        number (int): Numero de lineas"""
    for i in range(number):
        print("")


def movimientos(
    pila_1: Stack, pila_2: Stack, dic_1: dict, dic_2: dict, n_discos: int
) -> None:
    """En cada movimiento interactuan 2 Pilas o Stacks esta funcion
       realiza la interaccion entre esas dos Pilas

    Args:
        pila_1 (Stack): Stack de donde sale un aro en ese movimiento
        pila_2 (Stack): Stack que recibe el aro que salió de pila_1
        dic_1 (dict): Diccionario que representa graficamente a pila_1
        dic_2 (dict): Diccionario que representa graficamente a pila_2
        n_discos (int): Numero de Discos que eligio el Usuario al prin-
                        cipio del juego
    """
    if pila_1.is_empty():
        blanK_lines(3)
        input("NO SE PUEDE SACAR NADA DE UNA PILA VACIA")
        return
    aro_numero = pila_1.peek()
    size_pila_1 = pila_1.size()
    # En caso de que la pila receptora del aro este vacia
    if pila_2.is_empty():
        pila_2.push(pila_1.pop())
        dic_2[n_discos] = rings[aro_numero]
        dic_1[n_discos - size_pila_1 + 1] = empty
    else:

        if pila_1.peek() > pila_2.peek():
            blanK_lines(3)
            input("MOVIMIENTO NO PERMITIDO")
            return
        else:
            # En caso de que el movimiento si sea permitido
            size_pila_2 = pila_2.size()
            pila_2.push(pila_1.pop())
            dic_1[n_discos - size_pila_1 + 1] = empty
            dic_2[n_discos - size_pila_2] = rings[aro_numero]
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
            # Ciclo solo para asegurar de que sea 3, 4 ó 5
            while True:
                n_string: str = input(preguntando_n_discos)

                if n_string.strip() in ["3", "4", "5"]:
                    n_discos: int = int(n_string)
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
        else:
            mostrar_torres(n_discos=n_discos)
            print(menu, end="")
            if destino.size() == n_discos:
                blanK_lines(4)
                input("GANOOOOOO...............")
                sys.exit(0)
            opcion = input()
            # En caso de que la opcion del usuario no sea valida o haya un error de tipeo
            if not opcion.strip().upper() in ["1", "2", "3", "4", "5", "6", "Q"]:
                blanK_lines(4)
                input("OPCION NO VALIDA")
                continue
            # Si el usuario decide salir
            if opcion.strip().upper() == "Q":
                sys.exit(0)
            # Opciones de Movimientos Disponibles al Usuario
            if opcion.strip() == "1":
                movimientos(
                    pila_1=origen,
                    pila_2=destino,
                    dic_1=origen_dic,
                    dic_2=destino_dic,
                    n_discos=n_discos,
                )
            elif opcion.strip() == "2":
                movimientos(
                    pila_1=origen,
                    pila_2=auxiliar,
                    dic_1=origen_dic,
                    dic_2=auxiliar_dic,
                    n_discos=n_discos,
                )
            elif opcion.strip() == "3":
                movimientos(
                    pila_1=destino,
                    pila_2=origen,
                    dic_1=destino_dic,
                    dic_2=origen_dic,
                    n_discos=n_discos,
                )
            elif opcion.strip() == "4":
                movimientos(
                    pila_1=destino,
                    pila_2=auxiliar,
                    dic_1=destino_dic,
                    dic_2=auxiliar_dic,
                    n_discos=n_discos,
                )
            elif opcion.strip() == "5":
                movimientos(
                    pila_1=auxiliar,
                    pila_2=destino,
                    dic_1=auxiliar_dic,
                    dic_2=destino_dic,
                    n_discos=n_discos,
                )
            else:
                movimientos(
                    pila_1=auxiliar,
                    pila_2=origen,
                    dic_1=auxiliar_dic,
                    dic_2=origen_dic,
                    n_discos=n_discos,
                )


if __name__ == "__main__":
    main(empezando=True)

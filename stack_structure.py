from typing import Union


class Stack:
    def __init__(self) -> None:
        """Estructura de Pila para Las Torres de Hanoi"""
        self.__list: list = []

    def push(self, item: int) -> None:
        """Agrega un elemento a la Pila

        Args:
            item (int): Elemento que se agregara a la Pila
        """
        self.__list.append(item)

    def pop(self) -> Union[int, str]:
        """Saca un elemento de la Pila

        Returns:
            int: Retorna el elemento que acaba de borrar
                 o manda a imprimir "Is Empty" si la Pila
                 esta vacia
        """
        if self.__list == []:
            return "Is Empty"
        else:
            return self.__list.pop()

    def peek(self) -> Union[int, None]:
        """Indica cual es el elemento de ariba en la Pila

        Returns:
            Union[int, None]: Retorna el elemento de arriba en la
                              Pila o None si esta vacia
        """
        if self.__list:
            return self.__list[-1]
        else:
            return None

    def is_empty(self) -> None:
        """Determina si la Pila esta Vacia

        Returns:
            bool: True si esta vacia, de lo contrario False
        """
        return self.__list == []

    def size(self) -> int:
        """devuelve el tamaño de la Pila

        Returns:
            int: Retorna la longitud de la Pila
        """
        return len(self.__list)

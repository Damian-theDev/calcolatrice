class Moltiplicazione():
    def __init__(self, lista_prodotti = [0]):
        self.__lista_prodotti = None

        self.set_lista_prodotti(lista_prodotti)

    def esegui(self):
        # eseguo l'operazione
        ris = 1
        for prodotto in self.__lista_prodotti:
            ris *= prodotto
            if ris == 0:
                break

        if int(ris) == ris:
            ris = int(ris)
        return ris 
    
    def set_lista_prodotti(self, lista_prodotti):
        if len(lista_prodotti) == 0:
            lista_prodotti_temp = [0]
        else:    
            index = 0
            lista_prodotti_temp = []
            for valore in lista_prodotti:
                if type(valore) == int or type(valore) == float:
                    lista_prodotti_temp.append(valore)
                    index += 1
                else: 
                    raise TypeError(f'Inserisci un valore numerico, hai inserito {type(valore)} in posizione {index}')
        self.__lista_prodotti = lista_prodotti_temp

    def get_lista_prodotti(self):
        return self.__lista_prodotti
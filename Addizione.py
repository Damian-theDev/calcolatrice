class Addizione():
    def __init__(self, lista_addendi = [0]):
        self.__lista_addendi = None

        self.set_lista_addendi(lista_addendi)

    def esegui(self):
        # eseguo l'operazione
        ris = 0
        for addendo in self.__lista_addendi:
            ris += addendo

        if int(ris) == ris:
            ris = int(ris)
        return ris 
    
    def set_lista_addendi(self, lista_addendi):
        index = 0
        lista_addendi_temp = []
        for valore in lista_addendi:
            if type(valore) == int or type(valore) == float:
                lista_addendi_temp.append(valore)
                index += 1
            else: 
                raise TypeError(f'Inserisci un valore numerico, hai inserito {type(valore)} in posizione {index}')
        self.__lista_addendi = lista_addendi_temp

    def get_lista_addendi(self):
        return self.__lista_addendi
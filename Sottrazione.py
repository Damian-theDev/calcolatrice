class Sottrazione():
    def __init__(self, lista_sottraendi = [0]):
        self.__lista_sottraendi = None
        self.__minuendo = None

        self.set_lista_sottraendi(lista_sottraendi)

    def esegui(self):
        # eseguo l'operazione
        ris = self.__minuendo
        for sottraendo in self.__lista_sottraendi:
            ris -= sottraendo

        if int(ris) == ris:
            ris = int(ris)
        return ris 
    
    def set_lista_sottraendi(self, lista_sottraendi):
        index = 0
        lista_sottraendi_temp = []
        for valore in lista_sottraendi:
            if type(valore) == int or type(valore) == float:
                if index == 0:
                    self.__minuendo = valore
                    lista_sottraendi = lista_sottraendi[1:]
                else:
                    lista_sottraendi_temp.append(valore)
                index += 1
            else: 
                raise TypeError(f'Inserisci un valore numerico, hai inserito {type(valore)} in posizione {index}')
        self.__lista_sottraendi = lista_sottraendi_temp

    def get_lista_sottraendi(self):
        return self.__lista_sottraendi
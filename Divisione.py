class Divisione():
    def __init__(self, dividendo, divisore):
        self.__dividendo = None
        self.__divisore = None

        self.set_dividendo(dividendo)
        self.set_divisore(divisore)

    def verifica(self):
        # verifica che l'operazione possa venir eseguita
        if self.__divisore != 0:
            return True
        else:
            raise ZeroDivisionError('Non puoi dividere per zero')

    def esegui(self):
        # eseguo l'operazione
        if self.verifica():
            ris = self.__dividendo / self.__divisore 
            if int(ris) == ris:
                ris = int(ris)
            return ris 

    def set_dividendo(self, dividendo):
        if type(dividendo) == int or type(dividendo) == float:
            self.__dividendo = dividendo    
        else: 
            raise TypeError(f'Inserisci un valore numerico, hai inserito {type(dividendo)}')
    
    def set_divisore(self, divisore):
        if type(divisore) == int or type(divisore) == float:
            self.__divisore = divisore
        else: 
            raise TypeError(f'Inserisci un valore numerico, hai inserito {type(divisore)}')

    def get_dividendo(self):
        return self.__dividendo

    def get_divisore(self):
        return self.__divisore
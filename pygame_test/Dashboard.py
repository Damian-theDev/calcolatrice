class Dashboard():
    def __init__(self):
        """
        Inizializza la Dashboard e gli attributi della classe, richiama la funzione reset per reimpostare questi ultimi.
        """
        self.__stringa_corrente = None
        self.__init_zero = None

        self.reset()

    def reset(self):
        """
        Resetta la stringa corrente e reimposta il flag di inizializzazione a True.
        """
        self.__stringa_corrente = '0'
        self.__init_zero = True

    def get_stringa_corrente(self):
        """
        Restituisce la stringa corrente.
        """
        return self.__stringa_corrente

    def add_valore_stringa_corrente(self, valore):
        """
        Aggiunge un valore alla stringa corrente in base al tipo di valore passato.
        Gestisce le eccezioni per garantire che il programma non fallisca in modo imprevisto.
        """
        try:
            if isinstance(valore, int) or valore in ('(', ')') or (valore == ',' and self.__stringa_corrente[-1] not in (',', '(', ')')):
                if self.__init_zero:
                    self.__init_zero = False
                    self.__stringa_corrente = ''
                self.__stringa_corrente += str(valore)
            
            elif valore in ('+', '-', '*', '/'):
                self.__stringa_corrente += str(valore)
                self.__init_zero = False

            elif valore == 'AC':
                self.reset()

            elif valore == 'canc':
                self.cancella_posizione()

            else:
                raise ValueError(f'Valore non valido: {valore}')

        except TypeError as e:
            print(f'Errore di tipo: {e}')
            # Gestione specifica per TypeError
        except ValueError as e:
            print(f'Errore di valore: {e}')
            # Gestione specifica per ValueError
        except IndexError as e:
            print(f'Errore di indice: {e}')
            # Gestione specifica per IndexError
        except Exception as e:
            print(f'Errore generico: {e}')
            # Gestione generica per altre eccezioni non previste

    def cancella_posizione(self, pos=-1):
        """
        Cancella il carattere alla posizione specificata nella stringa corrente.
        Se la stringa diventa vuota, la resetta.
        """
        try:
            if self.__stringa_corrente:
                self.__stringa_corrente = self.__stringa_corrente[:pos] + self.__stringa_corrente[pos+1:]
                if not self.__stringa_corrente:
                    self.reset()
            else:
                raise IndexError(f'Indice non valido (valore inserito: {pos})')

        except IndexError as e:
            print(f'Errore di indice: {e}')
            # Gestione specifica per IndexError
        except Exception as e:
            print(f'Errore generico: {e}')
            # Gestione generica per altre eccezioni non previste

    def calcola(self):
        print("da implementare")
        # TODO: implementa >:(
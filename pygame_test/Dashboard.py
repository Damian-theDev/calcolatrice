class Dashboard():
    def __init__(self):
        """
        Inizializza l'oggetto e, con esso, i suoi attributi.
        """
        self.__stringa_corrente = '0'
        self.__init_zero = True
        self.__parentesi_aperte = 0

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
            if isinstance(valore, int) or valore in ('(', ')', ','):
                if (valore == ',' and self.__stringa_corrente[-1] in (',', '(', ')')) == False and \
                    (valore in ('(', ')') and self.__stringa_corrente[-1] == ',') == False:
                    if valore == '(':
                        self.__parentesi_aperte += 1
                    
                    if valore == ')':
                        if self.__stringa_corrente[-1] in ('+', '-', '*', '/'):
                            pass # TODO : gestisci questo caso 

                        pass # TODO: controlla prima di chiudere una parentesi se è mai stata aperta

                    if self.__init_zero == True:
                        self.__init_zero = False
                        if valore != ',':
                            self.__stringa_corrente = ''
                    self.__stringa_corrente += str(valore)
                
            elif valore in ('+', '-', '*', '/'):
                if self.__stringa_corrente[-1] in ('+', '-', '*', '/'):
                    self.__stringa_corrente[-1] = valore
                elif self.__stringa_corrente[-1] != '(':
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

    def cancella_posizione(self, pos = -1):
        """
        Cancella il carattere alla posizione specificata nella stringa corrente.
        Se la stringa diventa vuota, la resetta.
        """
        try:
            if self.__stringa_corrente[pos]:
                if pos == -1:
                    self.__stringa_corrente = self.__stringa_corrente[:-1]
                else:
                    self.__stringa_corrente = self.__stringa_corrente[:pos] + self.__stringa_corrente[pos+1:]
                if self.__stringa_corrente == '':
                    self.reset()
            else:
                raise IndexError(f'Indice non valido (valore inserito: {pos})')

        except IndexError as e:
            print(f'Errore di indice: {e}')
            # Gestione specifica per IndexError
        except Exception as e:
            print(f'Errore generico: {e}')
            # Gestione generica per altre eccezioni non previste

    def calcola_totale(self):
        ret = self.cerca_parentesi(self.__stringa_corrente)
        self.reset()
        return ret

    def cerca_parentesi(self, testo):
        while '(' in testo:
            # trova l'ultima apertura e la prima chiusura di parentesi
            pos_apertura = testo.rfind('(')
            pos_chiusura = testo.find(')', pos_apertura)
            if pos_chiusura == -1:
                pos_chiusura = len(testo)

            # calcolo
            espressione = testo[pos_apertura + 1:pos_chiusura]
            ris = eval(espressione)

            testo = testo[:pos_apertura] + str(ris) + testo[pos_chiusura + 1:]
        return eval(testo)
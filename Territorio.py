import Jogador

class Territorio:
    '''
    Classe que implementa o objeto Territorio que é armazenado em cada vértice do grafo Mapa.
    '''
    def __init__(self, id: int, nome: str, continente: str):
        self.__id = id
        self.__nome = nome
        self.__continente = continente
        self.__fronteiras = {}
        self.__dono = None #Referência para o objeto Jogador
        self.__qtd_exercitos = 0

    @property
    def numero_id(self):
        return self.__id
    
    @property
    def retorna_dono(self) -> 'Jogador':
        return self.__dono
    
    def alocar_dono(self, novo_dono:'Jogador'):
        '''
        Metodo set que atribui um novo dono (obj. Jogador) ao Territorio.
        Args:
        novo_dono => objeto Jogador
        Returns:
        '''
        self.__dono = novo_dono

    @property
    def nome(self):
        '''Metodo get que retorna o nome do territorio.'''
        return self.__nome
    
    @property
    def continente(self):
        '''Metodo get que retorna o nome do territorio.'''
        return self.__continente
    
    @property
    def retorna_fronteiras(self) -> dict:
        '''Metodo que retorna um dicionario com os territorios que fazer fronteira.'''
        return self.__fronteiras
    
    def adicionar_fronteira(self, id:int, fronteira:'Territorio'):
        '''Metodo que adiciona uma nova fronteira ao dicionario de fronteiras.'''
        self.__fronteiras[id] = fronteira
    
    @property
    def numero_de_exercitos(self):
        '''
        Metodo get que retorna a quantidade de exercitos que o territorio tem.
        Returns: 
        N° de exercitos no territorio.
        '''
        return self.__qtd_exercitos
    
    def alterar_qtd_exercitos(self, qtd:int):
        '''
        Método set que altera o n° de exércitos no territorio para qtd.
        Args: 
        qtd => Novo n° de exercitos
        Returns: -
        '''
        self.__qtd_exercitos = qtd

    def verifica_id(self, key:int) -> bool:
        '''
        Método que verifica o id do Territorio.
        Retorno: 
        True -> se id = key.
        False -> se id != key.
        '''
        return self.__id == key
    
    def get_territorio_pelo_id(self, key:int) -> 'Territorio':
        if self.verifica_id(key):
            return self
    
        return None
    
    def eh_dono(self, jogador:'Jogador'):
        return jogador == self.__dono

    def __str__(self):
        s = ''
        s += f'{self.__nome}, {self.__continente}, tem {self.__qtd_exercitos} '
        if self.__qtd_exercitos == 1 : s+= f'exército {self.__dono.cor_do_exercito}'
        else: s+= f'exércitos {self.__dono.cor_do_exercito}s'
        s += f' do jogador {self.__dono.nome_do_jogador}.'
        return s
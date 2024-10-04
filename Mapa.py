from Grafo import *
from Territorio import *
    
class Mapa:
    '''
    Classe que implementa o objeto Mapa utilizado para estruturar o mapa do tabuleiro do jogo War.
    É uma classe que apresenta apenas um atributo mapa cuja estrutura de dados utilizada para representá-lo é um Grafo Não Direcionado.
    Nesta implementação, cada Vértice do grafo representa um objeto Territorio, cujas fronteiras são construídas através de arestas sem peso. O método responsável por inserir os valores no tabuleiro é povoar_mapa.
    '''

    def __init__(self):
        '''
        Construindo o objeto mapa. Não precisa instanciar nenhuma propriedade para ele.
        '''
        self.__mapa = Grafo()
    
    @property
    def retorna_mapa(self) -> 'Grafo':
        '''
        Método get que retorna o grafo por trás da propriedade self.__mapa do objeto Mapa.
        '''
        return self.__mapa
    
    def inserir_territorio(self, id:int, nome:str, continente:str):
        '''
        Método para inserir um novo território no mapa.
        Sem retorno.
        '''
        self.__mapa.add_vertex(Territorio(id, nome, continente))

    def retorna_vertice(self, key: int) -> 'Vertice':
        '''
        Similar ao método get_vertex. Retorna o vértice que tem o objeto Territorio com id = key.
        Retorna: 
        Territorio -> Se o objeto existir
        None -> Se não existir o objeto no grafo
        '''
        # keyobj = Territorio(key,'','')
        # retorno = self.__mapa.get_vertex(keyobj)
        # return retorno
    

        mapa = self.__mapa
        territorios = mapa.vertex()
        for territorio in territorios:
            objeto = territorio.carga.get_territorio_pelo_id(key)
            if objeto != None:
                return territorio
        
        return None

    def inserir_fronteira(self, key1: int, key2: int):
        '''
        Insere a fronteira entre dois Territórios cujos id's são key1 e key2. Sem retorno.
        '''
        self.__mapa.add_edge(self.retorna_vertice(key1), self.retorna_vertice(key2))
    
    def inserir_lista_fronteiras(self, T1: int, fronteiras: list):
        '''
        Insere todas as fronteiras entre um Território e seus territórios vizinhos, cujas chaves estão enumeradas na lista. Sem retorno.
        '''
        for fronteira in fronteiras:
            self.inserir_fronteira(T1, fronteira)
    
    def povoar_mapa(self):
        '''
        Método para construir os vértices e as arestas do grafo que está por trás do objeto Mapa. Sem retorno.
        '''
        self.inserir_territorio(1, 'Brasil', 'América do Sul')
        self.inserir_territorio(2, 'Argentina/Uruguai', 'América do Sul')
        self.inserir_territorio(3, 'Colômbia/Venezuela', 'América do Sul')
        self.inserir_territorio(4, 'Peru/Bolívia/Chile', 'América do Sul')

        self.inserir_territorio(5, 'México', 'América do Norte')
        self.inserir_territorio(6, 'Califórnia', 'América do Norte')
        self.inserir_territorio(7, 'Nova Iorque', 'América do Norte')
        self.inserir_territorio(8, 'Labrador', 'América do Norte')
        self.inserir_territorio(9, 'Ottawa', 'América do Norte')
        self.inserir_territorio(10, 'Vancouver', 'América do Norte')
        self.inserir_territorio(11, 'Mackenzie', 'América do Norte')
        self.inserir_territorio(12, 'Alasca', 'América do Norte')
        self.inserir_territorio(13, 'Groenlândia', 'América do Norte')
        
        self.inserir_territorio(14, 'Islândia', 'Europa')
        self.inserir_territorio(15, 'Inglaterra', 'Europa')
        self.inserir_territorio(16, 'Suécia', 'Europa')
        self.inserir_territorio(17, 'Alemanha', 'Europa')
        self.inserir_territorio(18, 'Espanha/Portugal/França/Itália', 'Europa')
        self.inserir_territorio(19, 'Polônia/Iugoslávia', 'Europa')
        self.inserir_territorio(20, 'Moscou', 'Europa')

        self.inserir_territorio(21, 'Argélia/Nigéria', 'África')
        self.inserir_territorio(22, 'Egito', 'África')
        self.inserir_territorio(23, 'Congo', 'África')
        self.inserir_territorio(24, 'Sudão', 'África')
        self.inserir_territorio(25, 'Madagascar', 'África')
        self.inserir_territorio(26, 'África do Sul', 'África')
        
        self.inserir_territorio(27, 'Oriente Médio', 'Ásia')
        self.inserir_territorio(28, 'Aral', 'Ásia')
        self.inserir_territorio(29, 'Omsk', 'Ásia')
        self.inserir_territorio(30, 'Dudinka', 'Ásia')
        self.inserir_territorio(31, 'Sibéria', 'Ásia')
        self.inserir_territorio(32, 'Tchita', 'Ásia')
        self.inserir_territorio(33, 'Mongólia', 'Ásia')
        self.inserir_territorio(34, 'Vladivostok', 'Ásia')
        self.inserir_territorio(35, 'China', 'Ásia')
        self.inserir_territorio(36, 'Índia', 'Ásia')
        self.inserir_territorio(37, 'Japão', 'Ásia')
        self.inserir_territorio(38, 'Vietnã', 'Ásia')

        self.inserir_territorio(39, 'Bornéu', 'Oceania')
        self.inserir_territorio(40, 'Sumatra', 'Oceania')
        self.inserir_territorio(41, 'Nova Guiné', 'Oceania')
        self.inserir_territorio(42, 'Austrália', 'Oceania')

        '''
        Fronteiras -> América do Sul
            (1) Fronteira Brasil -> Argentina/Uruguai, Colômbia/Venezuela, Peru/Bolívia/Chile e Argélia.
            (2) Fronteira Argentina -> Brasil e Peru/Bolívia/Chile.
            (3) Fronteira Colômbia -> Brasil, Peru/Bolívia/Chile e México.
            (4) Fronteira Peru/Bolívia/Chile -> Brasil, Argentina e Colômbia.
        '''
        self.inserir_lista_fronteiras(1, [ 2, 3, 4, 21 ]) #1
        self.inserir_lista_fronteiras(2, [ 4 ]) #2
        self.inserir_lista_fronteiras(3, [ 4, 5 ]) #3
        #self.inserir_lista_fronteiras(4, []) #4 -> é desnecessária pois já foram adicionadas todas as fronteiras com Peru/Bolívia/Chile

        '''
        Fronteiras -> América do Norte
            (1)Fronteira México -> Colômbia, Califórnia e Nova Iorque.
            (2)Fronteira Califórnia -> México, Nova Iorque, Ottawa e Vancouver.
            (3)Fronteira Nova Iorque -> México, Califórnia, Labrador e Ottawa.
            (4)Fronteira Labrador -> Nova Iorque, Ottawa e Groelândia.
            (5)Fronteira Ottawa -> Califórnia, Nova Iorque, Labrador, Vancouver e Mackenzie.
            (6)Fronteira Vancouver -> Califórnia, Ottawa, Mackenzie e Alasca.
            (7)Fronteira Mackenzie -> Ottawa, Vancouver, Alasca e Groelândia.
            (8)Fronteira Alasca -> Vancouver, Mackenzie e Vladivostok.
            (9)Fronteira Groelândia -> Labrador, Mackenzie e Islândia.
        '''
        self.inserir_lista_fronteiras(5, [ 6, 7 ]) #1
        self.inserir_lista_fronteiras(6, [ 7, 9, 10 ]) #2
        self.inserir_lista_fronteiras(7, [ 8, 9 ]) #3
        self.inserir_lista_fronteiras(8, [ 9, 13 ]) #4
        self.inserir_lista_fronteiras(9, [ 10, 11 ]) #5
        self.inserir_lista_fronteiras(10, [ 12 ]) #6
        self.inserir_lista_fronteiras(11, [ 12, 13 ]) #7
        self.inserir_lista_fronteiras(12, [ 34 ]) #8
        self.inserir_lista_fronteiras(13, [ 14 ]) #9

        '''
        Fronteiras -> Europa
            (1)Fronteira Islândia -> Mackenzie e Inglaterra.
            (2)Fronteira Inglaterra -> Islândia, Suécia, Alemanha e Espanha/Portugal/França/Itália.
            (3)Fronteira Suécia -> Inglaterra e Moscou.
            (4)Fronteira Alemanha -> Inglaterra, Espanha/Portugal/França/Itália e Polônia/Iugoslávia.
            (5)Fronteira Espanha/Portugal/França/Itália -> Inglaterra, Alemanha, Polônia/Iugoslávia, Argélia e Egito.
            (6)Fronteira Polônia/Iugoslávia -> Alemanha, Espanha/Portugal/França/Itália, Moscou, Egito e Oriente Médio.
            (7)Fronteira Moscou -> Suécia, Polônia/Iugoslávia, Oriente Médio, Aral e Omsk.
        '''
        self.inserir_lista_fronteiras(14, [ 15 ]) #1
        self.inserir_lista_fronteiras(15, [ 16, 17, 18 ]) #2
        self.inserir_lista_fronteiras(16, [ 20 ]) #3
        self.inserir_lista_fronteiras(17, [ 18, 19 ]) #4
        self.inserir_lista_fronteiras(18, [ 19, 21, 22 ]) #5
        self.inserir_lista_fronteiras(19, [ 20, 22, 27 ]) #6
        self.inserir_lista_fronteiras(20, [ 27, 28, 29 ]) #7

        '''
        Fronteiras -> África
            (1) Fronteira Argélia/Nigéria -> Brasil, Espanha/Portugal/França/Itália, Egito, Congo e Sudão.
            (2) Fronteira Egito -> Espanha/Portugal/França/Itália, Polônia/Iugoslávia, Argélia/Nigéria, Sudão e Oriente Médio.
            (3) Fronteira Congo -> Argélia, Sudão e África do Sul.
            (4) Fronteira Sudão -> Argélia, Egito, Congo, Madasgacar e África do Sul.
            (5) Fronteira Madagascar -> Sudão e África do Sul.
            (6) Fronteira África do Sul -> Congo, Sudão e Madasgacar.
        '''
        self.inserir_lista_fronteiras(21, [ 22, 23, 24 ]) #1
        self.inserir_lista_fronteiras(22, [ 24, 27 ]) #2
        self.inserir_lista_fronteiras(23, [ 24, 26 ]) #3
        self.inserir_lista_fronteiras(24, [ 25, 26 ]) #4
        self.inserir_lista_fronteiras(25, [ 26 ]) #5
        #self.inserir_lista_fronteiras(26, [ ]) #6 -> Desnecessário pois já foram adicionadas todas as fronteiras com a África do Sul

        '''
        Fronteiras -> Ásia
            (1) Fronteira Oriente Médio -> Polônia, Moscou, Egito, Aral e Índia.
            (2) Fronteira Aral -> Moscou, Oriente Médio, Omsk, China e Índia.
            (3) Fronteira Omsk -> Moscou, Aral, Dudinka, Mongólia e China.
            (4) Fronteira Dudinka -> Omsk, Sibéria, Tchita e Mongólia.
            (5) Fronteira Sibéria -> Dudinka, Tchita e Vladivostok.
            (6) Fronteira Tchita -> Dudinka, Sibéria, Mongólia, Vladivostok e China.
            (7) Fronteira Mongólia -> Omsk, Dudinka e China
            (8) Fronteira Vladivostok -> Alasca, Sibéria, Tchita, China e Japão.
            (9) Fronteira China -> Aral, Omsk, Mongólia, Vladivostok, Índia, Japão e Vietnã.
            (10) Fronteira Índia -> Oriente Médio, Aral, China, Vietnã e Sumatra
            (11) Fronteira Japão -> Vladivostok e China
            (12) Fronteira Vietnã -> China, Índia e Borneu
        '''
        self.inserir_lista_fronteiras(27, [ 28, 36 ]) #1
        self.inserir_lista_fronteiras(28, [ 29, 35, 36 ]) #2
        self.inserir_lista_fronteiras(29, [ 30, 33, 35 ]) #3
        self.inserir_lista_fronteiras(30, [ 31, 32, 33 ]) #4
        self.inserir_lista_fronteiras(31, [ 32, 34 ]) #5
        self.inserir_lista_fronteiras(32, [ 33, 34, 35 ]) #6
        self.inserir_lista_fronteiras(33, [ 35 ]) #7
        self.inserir_lista_fronteiras(34, [ 35, 37 ]) #8
        self.inserir_lista_fronteiras(35, [ 36, 37, 38 ]) #9
        self.inserir_lista_fronteiras(36, [ 38, 40 ]) #10
        #self.inserir_lista_fronteiras(37, [ ]) #11 -> é desnecessária pois já foram adicionadas todas as fronteiras com Japão
        self.inserir_lista_fronteiras(38, [ 39 ]) #12

        '''
        Fronteiras -> Oceania
            (1) Fronteira Bornéu -> Vietnã, Nova Guiné e Austrália.
            (2) Fronteira Sumatra -> Índia e Austrália.
            (3) Fronteira Nova Guiné -> Bornéu e Austrália.
            (4) Fronteira Austrália -> Bornéu, Sumatra e Nova Guiné.
        '''
        self.inserir_lista_fronteiras(39, [ 40, 41 ]) #1
        self.inserir_lista_fronteiras(40, [ 42 ]) #2
        self.inserir_lista_fronteiras(41, [ 42 ]) #3
        #self.inserir_lista_fronteiras(42, []) #4 é desnecessária pois já foram adicionadas todas as fronteiras com Austrália

    def retorna_fronteiras_de_um_territorio(self, territorio: 'Territorio'):
        '''
        Metodo que retorna uma coleção com as arestas incidentes de um vertice com carga Territorio.
        '''
        mapa = self.__mapa
        fronteiras = mapa.incident_edges(mapa.get_vertex(territorio))
        return fronteiras
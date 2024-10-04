class Vertice():
        # Técnica de otimização de python que permite controlar de forma mais precisa
        # quais atributos um objeto pode ter. Isso é útil para economizar memória, pois
        # você está explicitamente dizendo a Python para não criar um __dict__ para o objeto.
        __slots__ = '__carga'

        def __init__(self, carga:any):
                '''
                Do not call this method directly. Use the Graph class instead.
                '''
                self.__carga = carga
	
        @property
        def carga(self):
                return self.__carga
	
        @carga.setter
        def carga(self, nova_carga:any):
                self.__carga = nova_carga
        
        def __hash__(self): # will alolow vertex to be a map/set key    
                return hash(id(self))

        def __str__(self):
                return str(self.__carga)


class Aresta():

        __slots__ = ['__origem','__destino','__peso']
        
        def __init__(self, origem: 'Vertice', destino: 'Vertice', peso: int):
                self.__origem = origem
                self.__destino = destino
                self.__peso = peso
	
        @property
        def origem(self) -> 'Vertice':
                return self.__origem
	
        @origem.setter
        def origem(self, novaOrigem: 'Vertice'):
                self.__origem = novaOrigem

        @property
        def destino(self) -> 'Vertice':
                return self.__destino
	
        @destino.setter
        def destino(self, novoDestino: 'Vertice'):
                self.__destino = novoDestino

        @property
        def peso(self)->int:
                return self.__peso
	
        @peso.setter
        def peso(self, peso: int):
                self.__peso = peso

        def endpoint(self)->tuple:
                '''
                Retorna uma tupla (u,v) contendo os vértices finais da aresta
                '''
                return (self.__origem, self.__destino)
        
        def opposite(self, v: 'Vertice')->'Vertice':
                '''
                Retorna o vértice oposto ao vértice v na aresta
                '''
                if v == self.__origem:
                        return self.__destino
                elif v == self.__destino:
                        return self.__origem
                else:
                        return None
                
        def __str__(self):
                return f'{self.__origem},{self.__destino},{self.__peso}'

        def __hash__(self) -> int: # will allow edge to be a map/set key
                return hash((self.__origem, self.__destino))


from typing import List
from ElementosGrafo import *

class Grafo():
	'''
	Classe que implementa a estrutura de dados "Grafo" direcionado (GD)/não-direcionado(GND),
	com pesos nas arestas, utilizando um mapa de adjacência (hash table).
	Implementação extraída do livro "Data Structures and Algorithms in Python", 
	de Michael T. Goodrich, 2013.
	Adaptações: Professor Alex Sandro
	'''
	def __init__(self, directed:bool = False):
		'''
		Cria um grafo vazio, não-direcionado (default)
		Argumentos:
		direcionado (bool): Se True, cria um grafo dirigido (GD), caso contrário, 
		cria um grafo não-dirigido (GND).
		'''
		self.__outgoing = dict() # map de saída
		# Cria o segundo map/dicionario apenas se for um grafo direcionado
		self.__incoming = dict() if directed else self.__outgoing  # map de chegada

	def is_directed(self)->bool:
		'''
		Verifica se o grafo é direcionado.
		Retorno:
		True se o grafo for direcionado, False caso contrário.
		'''
		return self.__incoming is not self.__outgoing # if directed, different maps
	
	def vertex(self)->list:
		'''
		Obtém um conjunto com todos os vértices do grafo.
		Retorna:
		Um list de vértices iteráveis
		'''
		return list(self.__outgoing.keys())

	def vertex_count(self):
		'''
		Obtém o número de vértices do grafo
		Retorno:
		Um inteiro representando a quantidade de vértices do grafo
		'''
		return len(self.__outgoing)

	def edges(self)->list:
		'''
		Obtém um conjunto com todas as arestas do grafo
		Retorno:
		Um list de arestas iteráveis
		'''
		result = set() # coleção não-ordenada de elementos únicos.
		for secondary_map in self.__outgoing.values():
			result.update(secondary_map.values())
		return list(result)

	def edges_count(self):
		'''
		Obtém o número de arestas do grafo
		Retorno:
		Um inteiro representando a quantidade de arestas do grafo
		'''
		total = sum(len(self.__outgoing[v]) for v in self.__outgoing)
		# para grafo não direcionado, certifica-se de que não contamos arestas duas vezes
		return total if self.is_directed() else total // 2	
		
	def add_vertex(self, load:any = None)->Vertice:
		'''
		Adiciona um vértice ao grafo
		Argumentos:
		load (any): Carga do vértice
		Retorno:
		Um novo vértice com a carga especificada
		'''
		v = Vertice(load)
		self.__outgoing[v] = dict()
		if self.is_directed():
			self.__incoming[v] = dict() # need distinct map for incoming edges
		return v


	def add_edge(self, origin: Vertice, target: Vertice, weight: int = 0):
		'''
		Adiciona uma aresta ao grafo.
		Argumentos:
			origin (Vertice): Vértice de origem
			target (Vertice): Vértice de destino
			weight (int): Peso da aresta
		Retorno:
			Uma nova aresta que ligae origem a destino com o peso especificado
		'''
		e = Aresta(origin, target, weight)
		self.__outgoing[origin][target] = e
		self.__incoming[target][origin] = e

	def get_edge(self, origin: Vertice, target: Vertice)->Aresta:
		'''
		Recupera a aresta que liga o vértice de origem ao de destino
		Argumentos:
			origin (Vertice): Vértice de origem
			target (Vertice): Vértice de destino
		Retorno:
			A aresta que liga o vértice origem ao de destino, ou None se eles não são adjacentes
		'''
		return self.__outgoing[origin].get(target) # retorna None if origem not adjacent
	
	def get_carga_vertex(self, key: any)->any:
		'''
		Recupera um vértice correspondente à chave especificada
		Argumentos:
			key (any): chave do vértice
		Retorno:
			O vértice com a chave especificada, ou None se não existir
		'''
		for v in self.vertex():
			if v.carga == key:
				return v.carga
		return None

	def get_vertex(self, key: any)->any:
		'''
		Recupera um vértice correspondente à chave especificada
		Argumentos:
			key (any): chave do vértice
		Retorno:
			O vértice com a chave especificada, ou None se não existir
		'''
		for v in self.vertex():
			if v.carga == key:
				return v
		return None

	def degree(self, vertex: Vertice, outgoing:bool = True)->int:
		'''
		Obtém o grau de um vértice no grafo.
		O grau de um vértice é o número de arestas incidentes (que conecta) a ele.
		Argumentos:
			v (Vertice): Vértice
			outgoing (bool): Se True, retorna o grau de saída, caso contrário, o grau de entrada.
		Retorno:
			O número de arestas (de saída) incidentes ao vértice "vertex" no grafo		
		Observação:
			Se o grafo é "direcionado", o parâmetro "outgoing" indica se estamos contando 
			arestas de chegada (recepção), ou de saída (emissão), caso contrário
		'''
		adjacents = self.__outgoing if outgoing else self.__incoming
		return len(adjacents[vertex])	
	
	def incident_edges(self, vertex: Vertice, outgoing:bool = True):
		'''
		Retorna uma coleção com todas (outgoing) as arestas incidentes ao vértice "vertex" no grafo.
		Argumentos:
			vertex (Vertice): Vértice
			outgoing (bool): Se True, retorna as arestas de saída, caso contrário, as de entrada.
		Retorno:
			Uma lista de arestas incidentes ao vértice "v" no grafo.
		Observação:
			Se o grafo é "direcionado", o parâmetro "outgoing" indica se estamos contando 
			arestas de chegada (recepção), ou de saída (emissão), caso contrário
		'''
		adj = self.__outgoing if outgoing else self.__incoming
		for edge in adj[vertex].values():
			yield edge

	def __str__(self): # para grafo não-direcionado
		r = ''
		for u in self.__outgoing:
			if len(self.__outgoing[u]) == 0:
				continue
			r += (str(u.carga) + ' -> ')
			for e in self.__outgoing[u]:
				v: Vertice = e
				r += v.carga + ', '
			r = r.rstrip(', ')
			r += '\n'
		return r
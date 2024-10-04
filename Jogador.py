from Territorio import *
import time

class Jogador:
    '''
    Classe que implementa o objeto Jogador, um dos elementos que compõem o jogo eletronico War.
    O Jogador representa o participante do jogo War, armazenando propriedades básica como o nome, a cor do exercito, o objetivo do jogador e quais territorios ele conquistou!
    '''
    def __init__(self, posicao:int, nome: str, cor_exercitos: str):
        '''
        Cria um objeto Jogador, inicializado com a posicao, nome e a cor dos exercitos com os quais o jogador irá jogar.
        '''
        self.__posicao = posicao
        self.__nome = nome
        self.__cor_exercitos = cor_exercitos
        self.__territorios = dict()
        self.__objetivo = 0

    @property
    def posicao(self) -> int:
        '''
        Metodo get que retorna a posicao do jogador em cada rodada.
        '''
        return self.__posicao
    
    @posicao.setter
    def alterar_posicao(self, nova:int):
        '''
        Metodo setter que altera o valor do atributo posicao do obj. Jogador.
        '''
        self.__posicao = nova
    @property
    def nome_do_jogador(self):
        '''
        Metodo get que retorna o nome do jogador.
        '''
        return self.__nome

    @property
    def cor_do_exercito(self):
        '''
        Metodo get que retorna a cor do exército escolhido pelo jogador. 
        '''
        return self.__cor_exercitos
    
    @property
    def mostrar_objetivo(self):
        '''
        Metodo que retorna o índice do objetivo do jogador. Os objetivos são definidos a cada início de partida e podem variar de acordo com os objetivos definidos na classe Jogo.
        '''
        return self.__objetivo
    
    def alterar_objetivo(self, novo:int):
        '''
        Metodo que atribui um novo objetivo ao jogador. 
        '''
        self.__objetivo = novo

    @property
    def territorios(self) -> dict:
        '''
        Metodo get que retorna um dicionario com os territorios pertencentes ao jogador.
        '''
        return self.__territorios
    
    def novo_territorio(self, territorio: 'Territorio'):
        '''
        Método que insere um novo Territorio no dicionário dos territórios que pertencem ao jogador.
        O método de inserção utiliza o id do Territorio (um valor entre 1 e 42) como key; e o objeto Territorio como value.
        Args:
        novo_territorio -> Objeto Territorio que será adicionado ao dicionário
        -
        '''
        dicionario = self.__territorios
        dicionario[territorio.numero_id] = territorio
        territorio.alocar_dono(self)

    def remover_territorio(self, territorio:'Territorio'):
        '''
        Metodo que remove um territorio do dicionario de territorios.
        '''
        del self.__territorios[territorio.numero_id]

    def listar_territorios(self):
        '''
        Metodo que exibe todos os territorios que pertencem a um determinado jogador.
        '''
        territorios = self.__territorios
        for id in sorted(territorios):
            print(f'({id}) {territorios[id].nome}, {territorios[id].continente} tem {territorios[id].numero_de_exercitos} exército(s).')
            time.sleep(0.25)
        print()      

    def numero_de_territorios(self) -> int:
        '''
        Metodo que retorna o numero de territorios que pertence ao jogador.
        '''
        return len(self.__territorios)

    def __str__(self) -> str:
        '''
        Método especial do python utilizado para retornar uma string sempre que o objeto é submetido ao comando print.
        '''
        return f'''
        Jogador {self.__posicao}:
        Nome: {self.__nome}
        Exército: {self.__cor_exercitos}
        '''
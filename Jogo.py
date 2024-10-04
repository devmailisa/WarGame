from Mapa import *
from Territorio import *
from Jogador import *
import random,time

class Jogo:
    '''
    Classe que implementa o objeto Jogo utilizado para estruturar o jogo eletrônico War.
    Ela é responsável por correlacionar as outras classes a partir de métodos e propriedades que a instanciam, como o atributo self.__mapa que recebe um objeto Mapa(), incializado com vértices cuja carga é um objeto Território; e o atributo self.__jogadores que armazena em uma lista os jogadores registrados cada um em um objeto Jogador.

    O Jogo War é um jogo de guerra e estratégia em que cada participante deve alcançar um objetivo 
    através de batalhas e posse de novos territórios. É um jogo desenvolvido pela empresa brasileira Grow, em tabuleiro.
    Esta é uma proposta de implementação deste jogo em ambiente virtual. A ideia é representar a lógica por trás do 
    desenvolvimento do jogo e não o jogo em pleno funcionamento (não inclui recursos gráficos).

    Projeto desenvolvido para conclusão da disciplina de Estrutura de Dados ministrada pelo Professor Alex Sandro.
    '''
    def __init__(self, max:int = 6):
        self.__mapa = Mapa() #Grafo
        self.__objetivos = {} #dict
        self.__jogadores = [] #list
        self.__inicio = False
        self.__pos_atual = 0
        self.__qtd_jogadores = 0
        self.__qtd_max = max
        self.__num_rodadas = 0

    @property
    def num_de_jogadores(self) -> int:
        return self.__qtd_jogadores
    
    @property
    def max_de_jogadores(self) -> int:
        return self.__qtd_max
    
    @property
    def pos_atual(self) -> int:
        return self.__pos_atual
    
    @pos_atual.setter
    def alterar_pos_atual(self, nova:int):
        '''
        Metodo que altera o atributo pos_atual.
        Utilizada no caso em que eliminamos um jogador que está em uma posição anterior a do jogador atual.
        '''
        self.__pos_atual = nova
    @property
    def inicio(self) -> bool:
        return self.__inicio
    
    @property
    def mapa(self) -> 'Mapa':
        '''Metodo get que retorna o mapa do jogo'''
        return self.__mapa
    
    @property
    def num_de_rodadas(self) -> int:
        '''Metodo get que retorna o numero de rodadas.'''
        return self.__num_rodadas
    
    @property
    def objetivos(self) -> dict:
        '''Metodo get que retorna um dicionario com os objetivos do jogo.'''
        return self.__objetivos
    
    def incrementar_rodadas(self):
        '''
        Metodo set que incrementa o número de rodadas.
        '''
        self.__num_rodadas+=1
    
    def lista_de_jogadores(self) -> list:
        '''Metodo que retorna um objeto list com referência aos objetos Jogadores.'''
        return self.__jogadores

    def iniciou(self):
        '''
        Método que demarca o início do jogo, após a distribuicao dos territorios.
        Args:
        -
        Returns:
        -
        '''
        self.__inicio = not self.__inicio

    def exibir_territorios_por_jogador(self):
        '''
        Metodo que exibe os territórios por jogador.
        '''
        for jogador in self.__jogadores:
            print(f'Jogador {jogador.nome_do_jogador}: ')
            jogador.listar_territorios()
            time.sleep(1.5)

    def nomear_cor(self, cor:int) -> str:
        '''
        Método que retorna a cor correspondente ao argumento ncor do método novo_jogador.
        Args:
        cor -> equivalente ao ncor.

        Retorno:
        Retorna a string equivalente a cor correspondente.
        '''
        match cor:
            case 1:
                return 'amarelo'
            case 2:
                return 'preto'
            case 3:
                return 'verde'
            case 4:
                return 'branco'
            case 5:
                return 'vermelho'
            case 6:
                return 'azul'

    def novo_jogador(self, nome:str, ncor:int, ) -> int:
        '''
        Método implementado para inserir um novo jogador na lista de jogadores.
        Args: 
        Nome -> Propriedade nome do objeto Jogador
        ncor -> Número do intervalo [1...6] que representa uma cor do exército.
        Returns:
        None -> Quando a quantidade de jogadores atingir o máximo permitido.
        Jogador -> Caso contrário
        '''
        if len(self.__jogadores) + 1 > self.__qtd_max or self.__inicio:
            return None #Já inicia o jogo

        self.__qtd_jogadores+=1
        jogador = Jogador(self.__qtd_jogadores, nome, self.nomear_cor(ncor))
        self.__jogadores.append(jogador)
        return jogador
    
    def excluir_jogador(self, jogador:'Jogador'):
        '''
        Metodo que elimina um jogador da lista de jogadores.
        Args:
        jogador -> 'Jogador' a ser eliminado
        Returns:
        Retorna o objeto jogador se estiver na lista
        Retorna None se nao estiver
        '''
        pos = -1
        if jogador.numero_id in self.__jogadores:
            del self.__jogadores[jogador.posicao-1]
            self.__qtd_jogadores-=1
            pos = jogador.posicao
            
            for valor in self.__jogadores.values():
                if valor.posicao > pos:
                    valor.alterar_posicao(valor.posicao-1)
                    
            return jogador
        
        return None
    
    def jogador_atual(self) -> 'Jogador':
        '''
        Método que retorna qual Jogador deve jogar.
        Retorno: Objeto Jogador.
        '''
        return self.__jogadores[self.__pos_atual]
    
    def proximo_jogador(self):
        '''
        Método que altera a vez para o próximo jogador. Sem retorno.
        '''
        self.__pos_atual = (self.__pos_atual+1) % self.__qtd_jogadores

    def distribuir_territorios(self):
        """
        Método que distribui os 42 territórios entre os jogadores.
        """
        #Gerar um array com todos os identificadores do objeto Territorio
        territorios = [int(i) for i in range(1,43)]

        random.shuffle(territorios)
        
        for id in territorios:
            mapa = self.__mapa
            vertice = mapa.retorna_vertice(id)
            
            jogador = self.jogador_atual()
            jogador.novo_territorio(vertice.carga)

            vertice.carga.alterar_qtd_exercitos(vertice.carga.numero_de_exercitos+1)

            self.proximo_jogador()
    
    def definir_objetivos(self):
        '''
        Metodo utilizado para definir os objetivos do jogo e armazená-los em um dicionário.
        '''
        objetivos = self.__objetivos
        objetivos[1] = 'Conquistar na totalidade a EUROPA, a OCEANIA e mais um terceiro.'
        objetivos[2] = 'Conquistar na totalidade a ÁSIA e a AMÉRICA DO SUL.'
        objetivos[3] = 'Conquistar na totalidade a EUROPA, a AMÉRICA DO SUL e mais um terceiro.'
        objetivos[4] = 'Conquistar 18 TERRITÓRIOS e ocupar cada um deles com pelo menos dois exércitos.'
        objetivos[5] = 'Conquistar na totalidade a ÁSIA e a ÁFRICA.'
        objetivos[6] = 'Conquistar na totalidade a AMÉRICA DO NORTE e a ÁFRICA.'
        objetivos[7] = 'Conquistar 24 TERRITÓRIOS à sua escolha.'
        objetivos[8] = 'Conquistar na totalidade a AMÉRICA DO NORTE e a OCEANIA.'
        objetivos[9] = 'Destruir totalmente OS EXÉRCITOS AZUIS ou conquistar 24 territorios.'
        objetivos[10] = 'Destruir totalmente OS EXÉRCITOS AMARELOS ou conquistar 24 territorios.'
        objetivos[11] = 'Destruir totalmente OS EXÉRCITOS VERMELHOS ou conquistar 24 territorios.'
        objetivos[12] = 'Destruir totalmente OS EXÉRCITOS PRETOS ou consquistar 24 territorios.'
        objetivos[13] = 'Destruir totalmente OS EXÉRCITOS BRANCO ou conquistar 24 territorios.'
        objetivos[14] = 'Destruir totalmente OS EXÉRCITOS VERDES ou conquistar 24 territorios.'
    
    def distribuir_objetivos(self):
        '''
        Método que distribui os objetivos entre os jogadores.
        '''
        objetivos = [int(i) for i in range(1, 15)]
        random.shuffle(objetivos)
        rep = self.__qtd_jogadores
        for i in range(rep):
            jogador = self.jogador_atual()
            jogador.alterar_objetivo(objetivos[i])
            self.proximo_jogador()
    
    def listar_fronteiras_por_territorio(self, jogador:'Jogador'):
        '''
        Metodo que recebe os territorios do 'jogador' e exibe um a um os territórios e suas fronteiras.
        '''
        territorios_do_jogador = jogador.territorios #dicionario com objetos territorio
        for territorio in territorios_do_jogador.values():
            print(f'Pelo territorio ({territorio.numero_id}) {territorio.nome} com {territorio.numero_de_exercitos} exército(s)\nVocê pode atacar: ')
            
            mapa = self.__mapa
            fronteiras = mapa.retorna_fronteiras_de_um_territorio(territorio) #retorna uma coleção com as arestas incidentes do vertice com carga territorio
            
            for fronteira in fronteiras:
                origem = mapa.retorna_mapa.get_vertex(territorio) #retorna Vertice
                destino = fronteira.opposite(origem)

                if not (destino.carga.numero_id in origem.carga.retorna_fronteiras): #se fronteiras nao estiver vazio
                    territorio.adicionar_fronteira(destino.carga.numero_id, destino.carga)

                if destino.carga.retorna_dono != jogador:
                    print(f'({destino.carga.numero_id}) {destino.carga.nome} tem {destino.carga.numero_de_exercitos} exército(s) da cor {destino.carga.retorna_dono.cor_do_exercito}.')
                time.sleep(0.25)

            print()
    
    def atacar(self, origem:'Territorio', destino:'Territorio', dados_ataque:int):
        '''
        Metodo que estrutura o ataque de um territorio(origem) a outro(destino).
        Args:
        origem -> Territorio de onde o ataque é realizado.
        destino -> Territorio que é atacado.
        dados_ataque -> quantidade de dados (no maximo 3) com que a origem ataca o destino.
        Returns:
        None -> Caso a quantidade dos dados de ataque for maior do que a permitida (no maximo 3)
        [ataque, defesa] -> uma matriz contendo os dados de ataque [0] e os dados de defesa [1]
        '''
        max_dados_ataque = min(3, origem.numero_de_exercitos - 1)
        max_dados_defesa = min(3, destino.numero_de_exercitos)
        if dados_ataque > max_dados_ataque:
            return None
        
        ataque = []
        defesa = []
        
        for i in range(dados_ataque):
            n_ataque = random.randint(1, 6)
            ataque.append(n_ataque)

        for i in range(max_dados_defesa):
            n_defesa = random.randint(1, 6)
            defesa.append(n_defesa)

        ataque.sort(reverse=True)
        defesa.sort(reverse=True)
        
        return [ ataque, defesa ]

    def trocar_dono_do_territorio(self, territorio:'Territorio', vencedor:'Jogador', perdedor:'Jogador'):
        perdedor.remover_territorio(territorio)
        if perdedor.numero_de_territorios == 0:
            print(f'O jogador {perdedor.nome_do_jogador} teve todos os seus territórios tomados, e por isso, foi aniquilado!')
            
            excluido = self.excluir_jogador(perdedor)
            if excluido != None:
                print(f'{excluido.nome_do_jogador} nao esta mais no jogo!')
                if excluido.posicao < vencedor.posicao:
                    self.__pos_atual-=1
            else:
                print(f'Jogador nao encontrado')
        
        territorio.alocar_dono(vencedor)
        territorio.alterar_qtd_exercitos(1)
        vencedor.novo_territorio(territorio)

    def verificar_dados(self, ataque:list, defesa:list) -> list:
        '''
        Metodo que verifica o resultado dos dados de ataque e defesa. 
        Args:
        ataque -> list
        defesa -> list
        Returns:
        Retorna uma list com 
        [0] a quantidade de vezes que o ataque venceu e 
        [1] a quantidade de vezes que a defesa venceu. 
        '''
        win_ataque = win_defesa = 0
        for i in range(min(len(ataque), len(defesa))):
            if ataque[i] > defesa[i]:
                win_ataque+=1
            else:
                win_defesa+=1
        
        return [win_ataque, win_defesa]
    
    def exibir_fronteiras_com_mesmo_dono(self, jogador:'Jogador'):
        territorios_do_jogador = jogador.territorios #dicionario com objetos territorio
        for territorio in territorios_do_jogador.values():
            print(f'Do territorio ({territorio.numero_id}) {territorio.nome} com {territorio.numero_de_exercitos} exército(s), você pode remanejar para: ')
            fronteiras = territorio.retorna_fronteiras
            for fronteira in fronteiras.values():
                if fronteira.retorna_dono == jogador:
                    print(f'({fronteira.numero_id}) {fronteira.nome} com {fronteira.numero_de_exercitos} exército(s)')
                    time.sleep(0.25)
            print()

    def remanejar_exercitos(self, origem:'Territorio', destino:'Territorio', qtd:int) -> bool:
        '''
        Metodo para remanejar exercitos de um territorio(origem) para outro(destino).
        Args:
        origem -> Territorio de onde os exercitos sao remanejados.
        destino -> Territorio para onde os exercitos sao remanejados.
        qtd -> Quantidade de exercitos a serem remanejados.
        Returns:
        True -> Se a operacao de remanejamento der certo.
        False -> Se a operacao de remanejamento nao puder ocorrer (o local de origem deve ficar com ao menos 01 exercito).
        '''
        if origem.numero_de_exercitos-qtd > 0:
            origem.alterar_qtd_exercitos(origem.numero_de_exercitos-qtd)
            destino.alterar_qtd_exercitos(destino.numero_de_exercitos+qtd)
            return True
        
        return False
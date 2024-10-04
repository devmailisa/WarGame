import os, time
from Jogo import *

def tela_inicial():
    limpar_terminal()
    print('Bem-vindo ao WAR GAME, um jogo de guerra e estratégia!')
    print('Selecione uma das opções: ')
    print('''
(1) Novo Jogo
(2) Sair
''')
    op = int(input('Opção: '))
    match op:
        case 1:
            tela_principal()
        case 2:
            sair()
        case _:
            tela_inicial()

def tela_principal():
    limpar_terminal()
    cores = [0,0,0,0,0,0]
    jogo = Jogo()
    print('Antes de iniciar, configure a sua partida adicionando os jogadores.')
    print('\nSelecione uma das opções: ')
    print('''
(1) Cadastrar jogador
(2) Sair
''')
    op = int(input('Opção: '))
    match op:
        case 1:
            tela_cadastrar_jogador(jogo, cores)
        case 2:
            sair()
        case _:
            tela_principal()

def tela_cadastrar_jogador(jogo:'Jogo', cores:list):
    limpar_terminal()
    nome = input('Digite o nome do jogador ou 0 (zero) para voltar ao menu inicial.\nNome do Jogador: ')
    if nome == '0':
        tela_principal()
    else:
        ncor = int(input('Qual a cor do exército desejada? (1) amarelo (2) preto (3) verde (4) branco (5) vermelho (6) azul: '))
        while (ncor < 1 or ncor > 6 or cores[ncor-1] == 1):
            if ncor < 1 or ncor > 6:
                print('Esta cor não existe! Tente novamente...\n')
            else:
                print('Esta cor já foi usada! Escolha novamente...\n')
            ncor = int(input('Qual a cor do exército desejada? (1) amarelo (2) preto (3) verde (4) branco (5) vermelho (6) azul: '))

        cores[ncor-1] = 1
        jogador = jogo.novo_jogador(nome, ncor)
        if jogador == None:
            limpar_terminal()
            print('Você não pode adicionar novos jogadores!\n')
            tela_menu_iniciar(jogo)
        else:
            print(jogador)
            if jogo.num_de_jogadores == jogo.max_de_jogadores:
                print('Você não pode adicionar novos jogadores!\n')
                time.sleep(3.0)
                tela_menu_iniciar(jogo)
            elif jogo.num_de_jogadores < 2:
                print('É necessário cadastrar mais participantes!')
                time.sleep(3.0)
                tela_cadastrar_jogador(jogo, cores)
            else:
                print(f'Você pode cadastrar mais {jogo.max_de_jogadores - jogo.num_de_jogadores} jogador(es)!')
                time.sleep(3.0)
                tela_menu_cadastrar(jogo, cores)

def tela_menu_cadastrar(jogo:'Jogo', cores: list):
    limpar_terminal()
    print('\nSelecione uma das opções: ')
    print('''
    (1) Cadastrar novo jogador
    (2) Iniciar jogo
    (3) Sair
    ''')
    op = int(input('Opção: '))
    match op:
        case 1:
            tela_cadastrar_jogador(jogo, cores)
        case 2:
            tela_iniciar_jogo(jogo, cores)
        case 3:
            sair()
        case _:
            tela_menu_cadastrar(jogo, cores)
                
def tela_menu_iniciar(jogo:'Jogo'):
    limpar_terminal()
    print('Está pronto para iniciar a partida?')
    print('\nSelecione uma das opções: ')
    print('''
    (1) Iniciar Jogo
    (2) Sair
    ''')
    op = int(input('Opção: '))
    match op:
        case 1:
            tela_iniciar_jogo(jogo)
        case 2:
            sair()
        case _:
            limpar_terminal()
            tela_menu_iniciar(jogo)

def tela_iniciar_jogo(jogo:'Jogo', cores:list):
    limpar_terminal()
    print('''Sejam muito bem-vindos ao WAR GAME, comandantes!
          
É com grande entusiasmo que o recebemos neste campo de batalha épico, onde estratégias audaciosas e decisões inteligentes são fundamentais para a vitória.

Aqui, sua mente será sua maior arma. Prepare-se para construir alianças, planejar táticas e disputar por territórios. 
          
Lembre-se: a paciência e a astúcia são tão importantes quanto a força militar. ''')
    
    print('Antes de embarcar neste empolgante desafio, escolha visualizar as regras do nosso jogo!')
    print('\nSelecione uma das opções: ')
    print('''
(1) Regras do Jogo
(2) Pular regras e comecar a guerrear!
(3) Voltar para a tela anterior
(4) Sair
''')
    op = int(input('Opção: '))
    match op:
        case 1:
            tela_regras(jogo)
        case 2:
            tela_jogo_war(jogo)
        case 3:
            tela_menu_cadastrar(jogo, cores)
        case 4:
            sair()
        case _:
            tela_iniciar_jogo(jogo, cores)

def tela_regras(jogo:'Jogo'):
    limpar_terminal()
    with open('./texto/regras.txt', 'r') as file:
        content = file.read()

    print(content)
    op = 0
    while(op != 1 and op != 2 and op != 3):
        print('Selecione uma das opcoes abaixo para continuar jogando: \n')
        print('''
    (1) Comecar a guerrear!
    (2) Voltar ao menu anterior...
    (3) Sair
    ''')
        op = int(input('Opcao: '))
    
    match op:
        case 1:
            tela_jogo_war(jogo)
        case 2:
            tela_menu_iniciar(jogo)
        case 3:
            sair()

def distribuir_exercitos_na_rodada(jogo:'Jogo', jogador:'Jogador', numero_de_exercitos:int):
    while(numero_de_exercitos > 0):
        print(f'{jogador.nome_do_jogador}, escolha uma das opções a seguir para prosseguir no jogo: ')
        print('''
(1) Listar meus territorios
(2) Exibir meu objetivo
(3) Adicionar exercitos a um territorio
''')
        op = int(input('Opcao: '))
        match op:
            case 1:
                jogador.listar_territorios()
            case 2:
                print(f'\nObjetivo de {jogador.nome_do_jogador}: {jogo.objetivos[jogador.mostrar_objetivo]}\n')
            case 3:
                print(f'\nVocê pode adicionar {numero_de_exercitos} exército(s). \n')
                qtd_exercitos = int(input('Quantos exercitos você deseja adicionar? '))

                if numero_de_exercitos-qtd_exercitos < 0:
                    print('\nVoce esta tentando adicionar mais territorios do que realmente tem...\n')
                else:
                    print('Selecione um dos territorios abaixo para adicioná-los: \n')
                    jogador.listar_territorios()
                    id_territorio = int(input('Informe o id do territorio: '))
                    lista_territorios = jogador.territorios
                    if id_territorio in lista_territorios:
                        territorio = lista_territorios[id_territorio]
                        territorio.alterar_qtd_exercitos(territorio.numero_de_exercitos+qtd_exercitos)
                        numero_de_exercitos-=qtd_exercitos
                        print(territorio)
                    else:
                        print('Voce nao eh o dono deste territorio!\n')
    print(f'\nExércitos de {jogador.nome_do_jogador} distribuídos com sucesso!\n')

def primeira_rodada(jogo: 'Jogo'):
    '''
    Método que implementa a interface da 1° rodada.
    '''
    print(f'Temos {jogo.num_de_jogadores} comandantes nesta guerra!\n')
    print(f'Distribuindo os territórios entre os {jogo.num_de_jogadores} jogadores...')

    #Distribuir os territórios e objetivos entre os jogadores.
    jogo.distribuir_territorios()
    jogo.definir_objetivos()
    jogo.distribuir_objetivos()

    #Exibir mapa inicial do jogo
    print('\nEsse é o mapa inicial do jogo: \n')
    jogo.exibir_territorios_por_jogador()

    #Iniciar jogo
    jogo.iniciou()
    print('Para iniciar o jogo, cada jogador deve distribuir uma primeira leva de tropas entre os territorios. Essa rodada é importante pois você deve considerar seu objetivo para saber quais territórios proteger! \n')
    time.sleep(1.0)
    print(f'{jogo.num_de_rodadas}ª RODADA')

    rep = jogo.num_de_jogadores
    while(rep):
        jogadores = jogo.lista_de_jogadores()
        jogador_atual = jogadores[jogo.pos_atual]
        time.sleep(0.5)
        print(f'Jogador atual: {jogador_atual.nome_do_jogador}')
        numero_de_exercitos = jogador_atual.numero_de_territorios() // 2
        time.sleep(0.5)
        print(f'{jogador_atual.nome_do_jogador} pode distribuir {numero_de_exercitos} exércitos no mapa.\n')
        distribuir_exercitos_na_rodada(jogo, jogador_atual, numero_de_exercitos)
        time.sleep(1.0)
        print('Prosseguindo...')
        time.sleep(1.0)
        rep -= 1
        jogo.proximo_jogador()

def reiniciar_ataque(jogo:'Jogo', jogador:'Jogador'):
    time.sleep(1.5)
    print('Reiniciar ataque...')
    time.sleep(0.5)
    tela_atacar(jogo, jogador)

def tela_atacar(jogo: 'Jogo', jogador: 'Jogador'):
    limpar_terminal()
    print('Vamos ao ataque!')

    print('Exibindo territórios que você pode atacar...')
    
    jogo.listar_fronteiras_por_territorio(jogador)

    #Localizando os objetos do tipo Territorio
    id_origem = int(input('Informe o id do territorio atacante: '))
    id_destino = int(input('Informe o id do territorio defensor: '))
    origem = jogo.mapa.retorna_vertice(id_origem).carga #retorna o objeto Territorio 
    destino = jogo.mapa.retorna_vertice(id_destino).carga #retorna o objeto Territorio

    if destino.numero_id not in origem.retorna_fronteiras:
        print('Cuidado! Estes territorios não tem fronteira em comum...')
        reiniciar_ataque(jogo, jogador)
    elif origem.numero_de_exercitos == 1:
        print('Você precisa ter pelo menos 2 exércitos no território de ataque para atacar! ')
        reiniciar_ataque(jogo, jogador)
    else:
        dados_ataque = int(input(f'{jogador.nome_do_jogador}, quantos dados devem ser utilizados no ataque? '))
        dados = jogo.atacar(origem, destino, dados_ataque)
        if dados == None:
            print(f'A quantidade maxima de dados permitida foi ultrapassada! ')
            reiniciar_ataque(jogo, jogador)
        else:
            print(f'Dados de ataque: {dados[0]}')
            print(f'Dados de defesa: {dados[1]}')
            resultado = jogo.verificar_dados(dados[0], dados[1])
            time.sleep(1.0)
            print('\nResultados do ataque: ')
            print(f'Os dados de ataque venceram {resultado[0]} vez(es).')
            print(f'Os dados de defesa venceram {resultado[1]} vez(es).')
            time.sleep(1.0)
            print('Decrementando exércitos de ambos territórios...')
            time.sleep(1.0)
            origem.alterar_qtd_exercitos(origem.numero_de_exercitos-resultado[1]) #ataque perdeu resultado[1] vezes
            destino.alterar_qtd_exercitos(destino.numero_de_exercitos-resultado[0]) #defesa perdeu resultado[0] vezes
            if destino.numero_de_exercitos == 0:
                print(f'{destino.nome} nao tem mais exercitos!')
                print(f'{jogador.nome_do_jogador} conquistou {destino.nome}!\n')
                perdedor = destino.retorna_dono
                jogo.trocar_dono_do_territorio(destino,jogador,perdedor)
                print(destino)
                print()
                time.sleep(1.5)
            
            print('Ataque bem sucedido!')
            print('Selecione uma das opcoes para continuar o jogo:')
            print('''
(1) Conquistei meu objetivo! Fim de Jogo
(2) Ainda tem muito jogo pela frente... Retornar a tela da rodada!
''')
            op = int(input('Opcao: '))
            match op:
                case 1:
                    tela_vencedor(jogador)
                case 2:
                    tela_rodada(jogador, jogo)
                case _:
                    tela_rodada(jogador, jogo)

def tela_remanejar_exercitos(jogo:'Jogo', jogador:'Jogador'):
    limpar_terminal()
    print('Exibindo a configuração atual dos seus territórios...')
    time.sleep(1.0)
    jogo.exibir_fronteiras_com_mesmo_dono(jogador)
    continuar = input('Continuar o processo de ramanejamento? Digite S para continuar...')
    if continuar.upper() == 'S':
        id_origem = int(input('Informe o id do territorio de onde você irá remanejar: '))
        id_destino = int(input('Informe o id do territorio para onde você irá remanejar : '))

        if id_origem in jogador.territorios and id_destino in jogador.territorios:
            origem = jogador.territorios[id_origem]
            destino = jogador.territorios[id_destino]
            qtd = int(input(f'\nQuantos exércitos você deseja remanejar de {origem.nome} para {destino.nome}? '))
            time.sleep(0.5)
            if jogo.remanejar_exercitos(origem, destino, qtd):
                print('\nExercitos remanejados com sucesso!\n')
                print('Resultado do remanejamento:')
                print(origem, destino, sep='\n')
                time.sleep(1.0)
                print('''
Selecione uma das opções abaixo para prosseguir no jogo:\n
(1) Continuar a remanejar os exercitos!
(2) Passar para o próximo jogador...    
            ''')
                op = int(input('Opcao: '))
                match op:
                    case 1:
                        tela_remanejar_exercitos(jogo, jogador)
                    case 2:
                        jogo.proximo_jogador()
                        tela_jogo_war(jogo)
                    case _:
                        limpar_terminal() 
                        tela_remanejar_exercitos(jogo, jogador)
            else:
                print('\nOperação inválida... Retornando a tela de remanejamento!\n')
                tela_remanejar_exercitos(jogo, jogador)
        else:
            print('\nOperação inválida... Retornando a tela de remanejamento!\n')
            tela_remanejar_exercitos(jogo, jogador)
    else:
        print('Retornando para a tela de início de partida...')
        time.sleep(1.0)
        print('\nPassando para o proximo jogador...\n')
        jogo.proximo_jogador()
        tela_jogo_war(jogo)
        
def tela_vencedor(jogador: 'Jogador'):
    limpar_terminal()
    with open('./texto/win.txt', 'r') as file:
        content = file.read()
    print(content)

    print(f'{jogador.nome_do_jogador} é o VENCEDOR!')
    print(f'''
Você lutou com garra e coragem mesmo diante de tantos desafios! 
Sua audaz estratégia e sua impetuosa força de vontade foram decisivas para que você vencesse as batalhas que resultaram em seu sucesso! 
          
Parabéns, campeão!
          
Você dominou o mundo!''')

def tela_rodada(jogador: 'Jogador', jogo:'Jogo'):
    limpar_terminal()
    print(f'Exércitos distribuídos: É hora de batalhar!')
    print(f'{jogador.nome_do_jogador}, selecione uma das opcoes abaixo para prosseguir no jogo: ')
    print('''
(1) Atacar!
(2) Remanejar exércitos.
(3) Passar para o próximo jogador...    
          ''')
    op = int(input('Opcao: '))
    match op:
        case 1:
            tela_atacar(jogo, jogador)
        case 2:
            tela_remanejar_exercitos(jogo, jogador)
        case 3:
            jogo.proximo_jogador()
            limpar_terminal()
            tela_jogo_war(jogo)
        case _:
            limpar_terminal() 
            tela_rodada(jogador, jogo)

def tela_jogo_war(jogo: 'Jogo'):
    limpar_terminal()
    with open('./texto/logo.txt', 'r') as file:
        content = file.read()
    print(content)

    if jogo.pos_atual == 0: 
        jogo.incrementar_rodadas()
    time.sleep(1.0)
    print('\nVamos guerrear! ')
    time.sleep(1.0)
    if not jogo.inicio:
        mapa = jogo.mapa
        mapa.povoar_mapa()
        primeira_rodada(jogo)
        jogo.incrementar_rodadas()
    
    print(f'{jogo.num_de_rodadas}ª RODADA')
    jogadores = jogo.lista_de_jogadores()
    jogador_atual = jogadores[jogo.pos_atual]
    time.sleep(1.0)
    print(f'Jogador atual: {jogador_atual.nome_do_jogador}')
    numero_de_exercitos = jogador_atual.numero_de_territorios() // 2
    print(f'{jogador_atual.nome_do_jogador} pode distribuir {numero_de_exercitos} exércitos no mapa.\n')
    time.sleep(2.0)
    distribuir_exercitos_na_rodada(jogo, jogador_atual, numero_de_exercitos)
    time.sleep(2.0)
    jogadores = jogo.lista_de_jogadores()
    jogador_atual = jogadores[jogo.pos_atual]
    tela_rodada(jogador_atual, jogo)
    
def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def sair():
        exit()
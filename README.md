# WarGame :medal_military:
Projeto desenvolvido para conclusão da disciplina de `Estrutura de Dados` ministrada pelo `Professor Alex Sandro`, docente do Instituto Federal da Paraíba - campus João Pessoa.

## Resumo
   O **Jogo War** é um jogo de guerra e estratégia em que cada participante deve alcançar um objetivo através de batalhas e posse de novos territórios. É um jogo desenvolvido pela empresa brasileira *Grow*, em tabuleiro. **Esta é uma proposta de implementação deste jogo em _ambiente virtual_**. A ideia é representar a lógica por trás do desenvolvimento do jogo e não o jogo em pleno funcionamento (não inclui recursos gráficos).

## Regras do Jogo

### Objetivo do Jogo
   No comeco da partida, cada jogador recebe um objetivo dentre 14! Cada objetivo tem relação ou com a posse de territorios ou com a derrota de um oponente. Vence aquele que conquistar o seu objetivo primeiro! 

### Preparação:

1. Dividir os territórios
   - No total, sao 42 territórios divididos em 6 continentes. Os territórios serão divididos entre os competidores, de forma que todos recebam a mesma quantidades de cartas ou quase isso. No caso de alguns jogadores ficarem com 01 carta a menos, **terá prioridade o competidor a direita da última pessoas que recebeu a carta**!

2. Jogadores
  - Pode ter no mínimo 02 e no máximo 06 jogadores.
  - No início, cada jogador escolhe um exército pela cor. As opções são: amarelo, preto, verde, branco, vermelho e azul.
  - No começo da partida, é distribuída 1(uma) unidade de um exército em cada territorio do jogo.
  - Essa distribuição deve ocorrer quando os territórios forem separados entre os jogadores. Como dito antes, no total são 42 territórios. Se o número de pessoas for 4(quatro), por exemplo, 2(dois) competidores ficam com 11(onze) territórios e 02(dois) competidores ficam com 10(dez) territórios. A primeira pessoa a não receber uma carta das que receberam 10(dez) deve iniciar o jogo.

3. Início da partida
  - No início da partida, cada jogador deve distribuir exércitos no tabuleiro. A quantidade de exércitos que cada jogador irá distribuir é a divisão inteira da **_quantidade de territórios por 2_**.
  - Para iniciar a rodada de ataques, o primeiro jogador deverá distribuir novamente **_N = quantidade de territórios por 2_** exércitos no tabuleiro. Após isso, ela pode declarar ataque a algum território inimigo desde que um território seu faça fronteira com ele. Esse ataque é realizado com dados de ataque e defesa.


3. Atacar
  - Há no máximo 3(três) dados de ataque e 3(três) dados de defesa.
  - O cálculo da quantidade de dados de ataque a partir de um território é o **_o mínimo entre 3 e o número de exércitos deste território - 1_**, pois sempre deve haver ao menos 1(um) exército de defesa.
  - Já o cálculo da quantidade de dados de defesa de um território é simplesmente **_o mínimo entre 3 e o número de exércitos deste território_**.
  - Na hora de jogar os dados, é realizada uma comparação do maior para o menor número sorteado do dado.
  - Vence o ataque se o valor que saiu no dado de ataque for maior que o valor que saiu no dado de defesa. Caso contrário, a defesa ganha.
  - Por exemplo, `Dados de ataque: [5, 3, 2]` e `Dados de defesa: [4, 3, 1]`, nesse caso a defesa apenas ganhou no caso ataque(3) e defesa(3), logo a defesa perde dois exércitos e o ataque perde um exército.

4. Conquista
  - Se em um ataque o jogador derrotar todos os exércitos inimigos de um territorio, ele conquista o território e 1 exército é remanejado automaticamente para este território, que passa a pertencer a ele!
          
5. Remanejar
  - Após a batalha, o jogador pode remanejar as suas tropas entre territorios que lhe pertençam e que façam fronteira entre si, reforçando as suas defesas ou se preparando para um próximo ataque.
          
6. Vencer o Jogo
  - Vence o jogo aquele que completar o seu objetivo primeiro ou derrotar todos os outros jogadores.
    
## Classes da Aplicação
  Assim como toda aplicação desenvolvida com base no `paradigma OO`, a implementação do jogo seguiu a ideia de `modularização` e `encapsulamento`, onde cada agente ou _entidade_ que compunha a dinâmica do jogo é tratada como _objeto_ e desenvolvida em cima de uma _classe_. A seguir, uma breve descrição dessas classes:
  
|--------------|-------------------------------------------------------------|
|    Classe    |                      Descrição                              |
|--------------|-------------------------------------------------------------|                                           
|  Territorio  | É uma classe que implementa cada território do mapa do War. |
|--------------|-------------------------------------------------------------|
|     Mapa     | É uma classe que implementa o Mapa(ou tabuleiro) do jogo.   |
|--------------|-------------------------------------------------------------|
|              | É a classe responsável por coordenar todo o funcionamento   |
|     Jogo     | do jogo. Ela é responsável por correlacionar as outras      |
|              | classes a partir de métodos e propriedades que a instanciam.|
|--------------|-------------------------------------------------------------|
|    Jogador   | É uma classe que implementa o objeto Jogador que representa | 
|              | o participante do jogo War.                                 |
|--------------|-------------------------------------------------------------|

### Classe Territorio
  É uma classe que implementa cada território do mapa do War, acusando o nome `self.__nome`, o continente a que pertence `self.__continente`, a quantidade de exércitos presentes `self.__qtd_exercitos`, o jogador que o contém `self.__dono`, os territórios que lhe fazem fronteira `self.__fronteiras` e uma identificação `self.__id`, **a partir da qual é possível resgatar o objeto Território de forma mais sucinta**. Os métodos implementados são para o retorno e manipulação dessas propriedades. 

### Classe Mapa
   É uma classe que implementa o Mapa(ou tabuleiro) do jogo. Apresenta apenas um atributo mapa `self.__mapa` cuja estrutura de dados utilizada para representá-lo é um Grafo Não Direcionado. Nesta implementação, cada Vértice do grafo representa um objeto Territorio, cujas fronteiras são construídas através de arestas sem peso. O método responsável por inserir os valores no tabuleiro é `povoar_mapa`.
   
### Classe Jogo
   É a classe responsável por coordenar todo o funcionamento do jogo. Ela é responsável por correlacionar as outras classes a partir de métodos e propriedades que a instanciam, como o atributo `self.__mapa` que recebe um objeto Mapa(), incializado com vértices cuja carga é um objeto Território; e o atributo `self.__jogadores` que armazena em uma lista os jogadores registrados cada um em um objeto Jogador.
   
### Classe Jogador
   Classe que implementa o objeto Jogador, um dos elementos que compõem o jogo eletronico War. O Jogador representa o participante do jogo War, armazenando propriedades básica como o nome, a cor do exercito, o objetivo do jogador e quais territorios ele conquistou!
   
### Arquivos de Menu
  Responsável por toda a navegação do jogo, o arquivo de Menu funciona como uma biblioteca de funções que representam as telas da aplicação. As telas funcionam a partir de um objeto do tipo Jogo instanciado assim que a `tela_inicial` é chamada no arquivo `mainJogo.py`. Nesse arquivo, apenas essa função é chamada, pois é a partir dela que todas as outras são chamadas, em efeito cascata.


    Projeto desenvolvido para conclusão da disciplina de Estrutura de Dados ministrada pelo Professor Alex Sandro.

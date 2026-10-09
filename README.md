# Sistema de Consulta e Otimização Logística - SWAPI

**Descrição breve:** Este projeto é uma aplicação em Python desenvolvida para consumir, estruturar e analisar dados do universo Star Wars. O sistema implementa uma arquitetura modularizada e utiliza estruturas de dados avançadas (Tries) e Algoritmos Gulosos para otimização de missões.

## 1. Fonte de Dados

### 1.1 API Escolhida
**The Star Wars API (SWAPI)** - [https://swapi.dev/](https://swapi.dev/)

### 1.2 Justificativa da Escolha
Escolhi a SWAPI pois sempre possui bastnate interesse no universo de Star Wars. Além disso ela é uma API pública que fornece uma gama de dados relacionais bem estruturados, facilitando na realização de operações e na criação do Algoritmo Guloso.

### 1.3 Endpoints Utilizados
* `GET /api/people/` - Dados de personagens .
* `GET /api/planets/` - Dados planetários.
* `GET /api/starships/` - Dados de naves estelares.
* `GET /api/vehicles/` - Dados de veículos atmosféricos.
* `GET /api/species/` - Dados de Espécies.

### 1.4 Exemplos de Requisições
A requisição é feita na camada de inicialização utilizando a biblioteca `requests`, iterando sobre as páginas (`next`) para obter todos os registros:
```python
import requests
resposta = requests.get("[https://swapi.dev/api/planets/](https://swapi.dev/api/planets/)")
dados = resposta.json()
```

### 1.5 Estrutura dos Dados Obtidos
A API retorna os dados em formato JSON. Os valores ausentes ou não mapeados vêm preenchidos com a string `"unknown"` ou `"n/a"`.
```json
{
  "name": "Tatooine",
  "rotation_period": "23",
  "diameter": "10465",
  "climate": "arid",
  "population": "200000",
  "residents": [
    "[https://swapi.dev/api/people/1/](https://swapi.dev/api/people/1/)"
  ]
}
```
## 2. Modelagem

### 2.1 Representação dos Elementos
Os dados da API foram mapeados para classes baseadas em Programação Orientada a Objetos (POO). Foram criadas as entidades principais: `Personagem`, `Planeta`, `Nave`, `Veiculo` e `Espécie`.

### 2.2 Atributos Utilizados
Grande parte dos atributos da API foram colocados na classe para que eu pudesse ter uma gama de escolhas, porém para evitar repetições de funções alguns não foram utilizados. Entre os que estão presentes nas operações estão:
* **Atributos textuais:** `nome`, `idioma`, `clima`.
* **Atributos numéricos (tratados):** `populacao`, `diametro`.
* **Atributos de relacionamento:** Listas de URLs foram resolvidas em memória para apontar para as instâncias reais dos objetos correspondentes (ex: a lista de naves de um personagem aponta para os objetos `Nave`).

### 2.3 Operações Implementadas
* **`__init__`**: Para instanciar e mapear o dicionário JSON para os atributos da classe.
* **`__repr__`**: Implementado para fornecer uma representação técnica e rastreável do objeto em memória, facilitando o debug nas listas de resultados.
* **Limpeza de Dados:** Conversão de strings numéricas e tratamento de valores `"unknown"`.

### 2.4 Decisões de Projeto
O projeto adotou uma modularização em:
* `/modelos`: Classes das entidades.
* `/estruturas`: Implementação da Árvore Trie.
* `/servicos`: Filtros, buscas e algoritmo guloso.
* `/menus`: Interfaces de terminal isoladas para cada classe.

## 3. Estrutura de Dados

### 3.1 Estrutura Escolhida
**Árvore Trie**

### 3.2 Justificativa da Escolha
A escolha da Trie se deu por ser a estrutura que eu tinha mias familiaridade e entendimento quando o trabalho foi começado. Além disso, tive que realizar uma mudança na implemnetação, tendo em vista que a que eu tinha usado em aula usava dicionário, e isso fez com que eu tivesse que explorar mais diferentes formas de uso da estrutura.

### 3.3 Operações Implementadas
* `pesquisa_nome`: Insere uma String e ela retorna os dados do objeto caso ele exista no sistema.
* `pesquisa_prefixo`: Navega pelos nós da árvore seguindo o prefixo digitado e, ao encontrar o último nó, realiza uma busca em profundidade (DFS) para recuperar todos os objetos derivados daquele prefixo.
* `pesquisa_atributo`: Utiliza de uma lista em que cada elemento é uma instância da classe. Percorre a lista toda coletando os objetos que possuem o atributo escolhido
* `filtrar`: Utilizei os atributos numéricos para diferenciar da pesquisa_atributo. Basicamente pega um intervalo de valores e percorre a lista selecionando objetos que estão nesse intervalo.

### 3.4 Análise da Complexidade das Principais Operações
* **Busca por Nome:** $O(m)$, onde $m$ é o número de caracteres da palavra.
* **Busca por Prefixo:** $O(p + k)$, onde $p$ é o tamanho do prefixo e $k$ é o número de nós descendentes recuperados.
* **Busca por Atributo / Filtragem:** $O(n)$, onde $n$ é o número total de objetos na lista.

### 3.5 Integração com o Sistema
As Tries foram utilizadas para fazer o mapeamento "nome" das classes. É criada uma Trie para cada classe através do atributo "nome" perimitindo a realização de buscar por nomes completos e por prefixos.

## 4. Análise de Complexidade Amortizada

### 4.1 Procedimento Selecionado
**Crescimento Dinâmico (Redimensionamento) da Lista de Resultados na Busca por Prefixo.**
Na implementação da Trie, a função `busca_recursiva` utiliza uma lista padrão do Python (`resultados = []`) para acumular os objetos encontrados. Sempre que um nó válido é visitado, o objeto é adicionado à lista através do método `resultados.append(no.dados)`. Em Python, listas são implementadas como Arrays Dinâmicos sob o capô.

### 4.2 Justificativa Matemática (Método Contábil)
Quando a capacidade interna do array dinâmico (`resultados`) é atingida, o Python precisa alocar um novo bloco de memória contíguo maior e copiar todos os $k$ elementos antigos para o novo array. Essa operação específica de redimensionamento tem um custo linear $O(k)$.

Para provar a eficiência global, aplicamos o **Método Contábil**. Atribuímos um custo amortizado de "3 moedas" a cada operação de `append()` realizada durante a busca DFS:
- **1 moeda** é gasta imediatamente para realizar a inserção rápida $O(1)$ no espaço livre do array.
- **1 moeda** é depositada como "crédito" no próprio elemento recém-inserido.
- **1 moeda** é depositada como "crédito" num elemento antigo do array (que já teve o seu crédito original gasto no redimensionamento anterior).

Quando o array fica cheio e exige a cópia para um novo espaço na memória (custo de $k$ operações), existem exatamente $k$ moedas de crédito acumuladas no sistema, que são utilizadas para "pagar" a cópia de todos os elementos sem exceder a complexidade teórica estipulada.

### 4.3 Custo Médio vs. Pior Caso $O(n)$
A análise tardicional de pior caso avaliaria um único `.append()` isolado no exato momento da expansão de memória como tendo um custo elevado de $O(k)$. No entanto, no contexto de uma busca por prefixo (ex: o utilizador digita "a" e a árvore recupera 30 personagens), avaliar cada inserção pelo pior caso apresentaria um cenário pessimista. 

Como o array cresce multiplicando o seu tamanho , o evento de cópia pesada ocorre cada vez com menor frequência. A complexidade amortizada comprova que, ao diluir o custo dos redimensionamentos raros por todas as inserções baratas efetuadas durante a recursão da Trie, a adição de cada elemento à lista de resultados comporta-se rigorosamente com um custo médio (amortizado) de $O(1)$.

## 5. Algoritmo Guloso 

### 5.1 Definição do Problema
**Missão: Otimização de Recrutamento Rebelde.**
A Aliança Rebelde precisa recrutar o máximo de soldados para a causa. No entanto, as naves de recrutamento possuem um limite rigoroso de "Combustível de Varredura" (capacidade de viajar cobrindo o diâmetro dos planetas). O sistema atua como um filtro inteligente para selecionar a melhor rota planetária.

### 5.2 Estratégia Adotada
O algoritmo recebe uma quilometragem limite definida pelo utilizador. Ele converte e sanitiza os dados da API (ignorando planetas com valores `"unknown"` ou diâmetro `"0"`). Os planetas são então organizados numa lista de tuplas e ordenados de forma decrescente com base no critério guloso. O sistema iterativamente consome o orçamento de quilometragem selecionando os planetas do topo da lista até que o combustível não seja mais suficiente para cobrir o próximo planeta viável.

### 5.3 Justificativa do Critério de Escolha
O critério estabelecido foi a **Densidade Populacional de Recrutamento** (Razão: `População / Diâmetro`). 
* **Benefício:** População (mais potenciais soldados).
* **Custo:** Diâmetro (maior gasto de tempo e combustível para varrer o território).
Esta fórmula maximiza o retorno, priorizando alvos onde uma grande quantidade de pessoas está concentrada num espaço reduzido, evitando desperdício logístico.

### 5.4 Análise da Solução Produzida (Limitações)
A abordagem estritamente gulosa é rápida e eficiente, mas pode falhar em encontrar a solução ótima global nos seguintes cenários:
1. **Sobra de Orçamento:** O algoritmo pode preencher quase toda a cota com planetas extremamente densos, deixando um pequeno excedente (ex: 5.000 km). Um planeta gigante e muito populoso como Coruscant (diâmetro 12.240 km) será sumariamente ignorado no final, mesmo que a troca de alguns planetas pequenos pudesse acomodar Coruscant e render trilhões de recrutas a mais.

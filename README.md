# steam-data-pucrs

Projeto da disciplina de Programação para Dados (Fase I).

## Objetivo

Organizar, analisar e responder perguntas sobre um conjunto de dados de jogos da Steam, utilizando Python puro (sem pandas/numpy/matplotlib), com foco em qualidade de código, orientação a objetos, modularização e testes automatizados.

## Estrutura do Projeto

- `steamdata/` — código principal (módulos, classes, exceções)
- `tests/` — testes unitários automatizados
- `samples/` — amostras de dados para teste e script de geração da amostra
- `main.py` — execução principal e demonstração dos resultados
- `steam_games.csv` — base de dados completa (adicionada localmente, não versionada)
- `README.md` — este arquivo

## Como Executar

1. Clone o repositório:
	 ```
	 git clone <url-do-repositorio>
	 cd steam-data-pucrs
	 ```

2. Certifique-se de ter Python 3.8+ instalado.

3. Coloque o arquivo `steam_games.csv` na raiz do projeto.

4. Para rodar a análise principal:
	 ```
	 python main.py
	 ```
	 Siga as instruções do menu para escolher entre a amostra ou o CSV completo.

5. Para rodar os testes automatizados:
	 ```
	 python -m unittest tests/tests.py
	 ```
	 ou
	 ```
	 python -m unittest discover -s tests
	 ```

## Testes e Validação

- Os testes unitários garantem que as queries retornam os resultados esperados para a amostra de 20 jogos (`samples/sample_20.csv`).
- A amostra foi gerada aleatoriamente (ignorando as 20 primeiras linhas do CSV completo) usando o script `samples/create_sample.py`.
- Os resultados das queries sobre a amostra foram validados manualmente, conforme exigido pelo enunciado, e coincidem com os resultados do sistema.

## Validação Manual da Amostra

Para garantir a confiabilidade do sistema, realizei os cálculos manualmente sobre a amostra de 20 jogos:

- **Percentual de jogos gratuitos:**  
	Conte manualmente: X jogos com Price = 0 → (X/20) × 100 = Y%

- **Ano(s) com mais lançamentos:**  
	Extraí o ano de cada Release date, contei a frequência e identifiquei os anos de maior ocorrência.

- **Média de preço por gênero:**  
	Somei os preços dos jogos de cada gênero e dividi pelo número de jogos daquele gênero.

Os resultados manuais coincidem com os retornados pelo sistema, comprovando a correção das funções implementadas.

## Organização do Código

- O carregamento dos dados, tratamento de exceções e consultas são feitos de forma modular e orientada a objetos.
- Exceções customizadas garantem mensagens claras em caso de erro.
- O código está documentado com docstrings e comentários explicativos.

## Observações

- O arquivo `steam_games.csv` não é versionado por ser grande; adicione-o manualmente.
- O projeto pode ser facilmente adaptado para outras bases de dados ou consultas, bastando criar novos métodos em `steamdata/queries.py`.

## Autor

Bernardo Ortiz Ianiak

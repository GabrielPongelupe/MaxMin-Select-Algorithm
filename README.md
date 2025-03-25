# MaxMin-Select-Algorithm

## Descrição do Projeto

Este projeto tem como objetivo implementar o algoritmo **MaxMin Select**, que realiza a seleção simultânea do maior e do menor elemento em uma sequência de números. A implementação utiliza a técnica de **divisão e conquista**, garantindo uma busca eficiente e reduzindo o número de comparações em relação a abordagens ingênuas.

O algoritmo funciona da seguinte maneira:
1. **Divisão**: O array é dividido recursivamente em partes menores até que cada subproblema contenha um ou dois elementos.
2. **Conquista**: O menor e o maior elemento de cada subproblema são identificados.
3. **Combinação**: Os resultados dos subproblemas são combinados para determinar o mínimo e o máximo globais.

A abordagem utilizada reduz o número de comparações em relação ao método tradicional de percorrer o array inteiro duas vezes, tornando-o mais eficiente. Esse método é particularmente útil para grandes conjuntos de dados, onde otimizar comparações pode gerar um ganho significativo de desempenho.

A implementação foi feita em **Python**, e foi implementado testes unitários para validar o funcionamento


## Como Executar o Projeto

Antes de rodar o projeto, certifique-se de ter o **Python 3.x** instalado em sua máquina.

### Passos para execução

1. **Clone o repositório** para sua máquina local:
   ```bash
   git clone https://github.com/seuusuario/MaxMinSelect.git
   ```
2. **Acesse a pasta do projeto**:
   ```bash
   cd MaxMinSelect
   ```
3. **Execute o script principal** para processar os números e exibir o maior e o menor valor encontrados:
   ```bash
   python main.py
   ```
   
Se preferir, você pode modificar a entrada diretamente no código ou adaptá-lo para receber valores do usuário em tempo de execução.

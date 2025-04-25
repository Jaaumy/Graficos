# Visualizador de Dados Estatísticos de Aviação

Olá! Este é um projeto que desenvolvi em Python para visualizar dados estatísticos de aviação de maneira interativa e intuitiva. A ideia surgiu da necessidade de analisar informações importantes, como decolagens, movimentação de aeroportos e proporção de voos por continente, utilizando gráficos que tornam os dados mais claros e fáceis de entender.

## 🚀 O que você pode fazer com este programa?

Eu implementei um menu interativo que permite explorar diferentes tipos de gráficos baseados nos dados fornecidos. Aqui estão as opções disponíveis:

1. **Visualizar o número de decolagens por empresa aérea.**  
   Um gráfico de barras mostra quantas decolagens cada empresa realizou.

2. **Analisar os 5 aeroportos mais movimentados.**  
   Um gráfico de pizza exibe quais são as cidades com maior volume de voos.

3. **Fazer um levantamento de empresas estrangeiras e brasileiras.**  
   Um gráfico de pizza separa as empresas por nacionalidade.

4. **Identificar os serviços aéreos mais utilizados.**  
   Aqui você pode ver os serviços oferecidos pelas empresas nacionais, também em formato de gráfico de pizza.

5. **Entender a proporção de voos por continente.**  
   Um gráfico de pizza exibe a proporção dos voos destinados a diferentes continentes.

---

## 🔧 Tecnologias que utilizei

- **Python 3.8+**: Linguagem principal do projeto.
- **pandas**: Para manipular e organizar os dados dos arquivos CSV.
- **matplotlib**: Para a criação dos gráficos interativos.
- **numpy**: Para suporte em operações matemáticas e numéricas.

---

## 📂 Estrutura do Projeto

- **`Dados_Estatisticos.csv`**: Um arquivo contendo dados gerais sobre decolagens, empresas e destinos.
- **`pda_empresas_aereas_nacionais.csv`**: Outro arquivo com informações específicas sobre serviços de empresas aéreas nacionais.
- **`script.py`**: O código principal do programa que carrega os dados e gera os gráficos.

---

## 🛠️ Como usar o programa?

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/Jaaumy/visualizador-dados-aviacao.git
   cd visualizador-dados-aviacao
   ```

2. **Instale as dependências**:
   Certifique-se de ter o Python instalado e execute o seguinte comando:
   ```bash
   pip install pandas matplotlib numpy
   ```

3. **Certifique-se de que os arquivos CSV estão no diretório**:
   - Os arquivos `Dados_Estatisticos.csv` e `pda_empresas_aereas_nacionais.csv` devem estar na mesma pasta que o script.

4. **Execute o programa**:
   Inicie o programa com o comando:
   ```bash
   python script.py
   ```

---

## 📊 Exemplos do que você vai encontrar

1. **Decolagens por Empresa Aérea**  
   Um gráfico de barras que exibe o total de decolagens realizadas por cada empresa aérea.

2. **Proporção de Voos por Continente**  
   Um gráfico de pizza que mostra a distribuição dos voos entre os continentes mais frequentes.

---

## ⚠️ Algumas observações importantes

- Certifique-se de que os arquivos CSV estão no formato correto. Qualquer inconsistência pode gerar erros no programa.
- Digite apenas números válidos no menu interativo para evitar falhas de execução.

---

## 💬 Entre em contato comigo

Se tiver dúvidas, sugestões ou apenas quiser bater um papo sobre o projeto, pode me chamar:
- **Email**: jaaumzinsz@gmail.com
- **GitHub**: [Jaaumy](https://github.com/Jaaumy)

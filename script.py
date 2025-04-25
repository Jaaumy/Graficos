import pandas as pd
import matplotlib.pyplot as plt
import numpy as npy
import matplotlib.ticker as ticker

def plotar_grafico(dados, escolha):
    """
    Função para plotar o gráfico de acordo com a escolha do usuário.

    Args:
        dados: DataFrame com os dados.
        escolha: Número correspondente ao tipo de gráfico.
    """
    if escolha == 1:
        plt.figure(figsize=(10, 6))  # Ajusta o tamanho do gráfico
        plt.bar(dados.groupby('EMPRESA_NOME')['DECOLAGENS'].sum().index,
               dados.groupby('EMPRESA_NOME')['DECOLAGENS'].sum().values)
        plt.xlabel('Empresa Aérea')
        plt.ylabel('Número de Decolagens')
        plt.title('Decolagens por Empresa Aérea')
        plt.xticks(rotation=45)  # Rotaciona os rótulos do eixo x para melhor visualização
        plt.show()
    elif escolha == 2:
        plt.figure(figsize=(10, 6))
        top_5_aeroportos = dados['AEROPORTO_DE_ORIGEM_NOME'].value_counts().head(5)
        plt.pie(top_5_aeroportos, labels=top_5_aeroportos.index, autopct='%1.1f%%')
        plt.title('Proporção de voos por cidade')
        plt.show()
    elif escolha == 3:
        estrabr = dados['EMPRESA_NACIONALIDADE'].value_counts().head(5)
        plt.pie(estrabr, labels=estrabr.index, autopct='%1.1f%%')
        plt.title('Levantamento de empresas estrangeiras e brasileiras')
        plt.show()
    elif escolha == 4:
        plt.figure(figsize=(10,6))
        razao = dados1['Servico'].value_counts().head(5)
        plt.pie(razao, labels=razao.index, autopct='%1.1f%%')
        plt.title('Levantamento de empresas nacionais e de seus serviços')
        plt.show()
    elif escolha == 5:
        plt.figure(figsize=(10, 6))
        continente = dados['AEROPORTO_DE_DESTINO_CONTINENTE'].value_counts().head(5)
        plt.pie(continente, labels=continente.index, autopct='%1.1f%%')
        plt.title('Proporção de voos por continente.')
        plt.show()
    else:
        print("Opção inválida.")
        plt.show()

if __name__ == "__main__":
    dados = pd.read_csv('Dados_Estatisticos.csv', sep=';')
    dados1 = pd.read_csv('pda_empresas_aereas_nacionais.csv', sep=';')
    while True:
        ref='\r'
        print("\n\n\n\n\t\t\t\tMENU DE GRÁFICOS")
        print("\t\t\t1 - Decolagens por empresa aérea.")
        print("\t\t\t2 - 5 aeroportos mais movimentados.")
        print("\t\t\t3 - Levantamento de empresas estrangeiras e brasileiras.")
        print("\t\t\t4 - Serviços aereas mais utilizados.")
        print('\t\t\t5 - Proporção de voos por continente.')
        print("\t\t\t0 - Sair")
        escolha = int(input("\n\t\t\t\tEscolha: "))

        if escolha == 0:
            break
        else:
            plotar_grafico(dados, escolha)  
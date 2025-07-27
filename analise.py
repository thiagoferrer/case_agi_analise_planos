import pandas as pd

# Carregar os arquivos
colab = pd.read_excel("colaboradores.xlsx")
planos = pd.read_excel("plano_de_saude.xlsx")

# Visualizar as 5 primeiras linhas
print("Colaboradores:")
print(colab.head())
print("\nPlanos de Saúde:")
print(planos.head())

# Verificar colunas e tipos
print("\nInfo colaboradores:")
print(colab.info())

print("\nInfo planos:")
print(planos.info())

# Verificar valores nulos
print("\nValores nulos em colaboradores:")
print(colab.isnull().sum())

print("\nValores nulos em planos:")
print(planos.isnull().sum())

# Converter CPF para string nos dois DataFrames
colab['cpf'] = colab['cpf'].astype(str).str.replace('.', '').str.replace('-', '').str.strip()
planos['cpf'] = planos['cpf'].astype(str).str.strip()


# Juntar as duas tabelas pela coluna 'cpf'
df = pd.merge(colab, planos, on='cpf', how='inner')

# Exibir resultado
print("\nBase unificada:")
print(df.head())

# Mapeando UFs para regiões do Brasil
df.columns = df.columns.str.lower().str.strip()

# Mapeando UFs para regiões do Brasil
regioes = {
    'Norte': ['AC', 'AP', 'AM', 'PA', 'RO', 'RR', 'TO'],
    'Nordeste': ['AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE'],
    'Centro-Oeste': ['DF', 'GO', 'MT', 'MS'],
    'Sudeste': ['ES', 'MG', 'RJ', 'SP'],
    'Sul': ['PR', 'RS', 'SC']
}

# Função para mapear região com tratamento
def definir_regiao(uf):
    if pd.isna(uf):
        return "Indefinida"
    uf = str(uf).upper().strip()
    for regiao, estados in regioes.items():
        if uf in estados:
            return regiao
    return "Indefinida"

# Criar nova coluna 'regiao'
df['regiao'] = df['uf'].apply(definir_regiao)


#Importar bibliotecas de visualização
import matplotlib.pyplot as plt
import seaborn as sns

# Ajustes visuais
sns.set(style="whitegrid")

#Quantidade de colaboradores por região
plt.figure(figsize=(10,6))
sns.countplot(data=df, x='regiao', order=df['regiao'].value_counts().index)
plt.title("Quantidade de colaboradores por região")
plt.xlabel("Região")
plt.ylabel("Número de colaboradores")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Tabela de frequência
tabela_operadoras = df.groupby(['regiao', 'operadora']).size().reset_index(name='quantidade')

# Plotar gráfico por região
plt.figure(figsize=(12,8))
sns.barplot(data=tabela_operadoras, x='regiao', y='quantidade', hue='operadora')
plt.title("Adesão por operadora em cada região")
plt.xlabel("Região")
plt.ylabel("Quantidade de adesões")
plt.legend(title="Operadora")
plt.tight_layout()
plt.show()

#Modalidade mais escolhida por região
tabela_modalidade = df.groupby(['regiao', 'modalidade do plano']).size().reset_index(name='quantidade')

plt.figure(figsize=(12,8))
sns.barplot(data=tabela_modalidade, x='regiao', y='quantidade', hue='modalidade do plano')
plt.title("Modalidade do plano por região")
plt.xlabel("Região")
plt.ylabel("Quantidade de adesões")
plt.legend(title="Modalidade")
plt.tight_layout()
plt.show()

# Salvar planilha resumo com todas as informações
df.to_excel("analise_planos_por_regiao.xlsx", index=False)

# Salvar contagem por região
df['regiao'].value_counts().to_excel("colaboradores_por_regiao.xlsx")

# Salvar contagem por operadora e região
tabela_operadoras.to_excel("operadoras_por_regiao.xlsx", index=False)

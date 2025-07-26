# 📊 Análise de Adesão aos Planos de Saúde por Região

## 📁 Projeto
Análise exploratória dos planos de saúde oferecidos aos colaboradores da empresa Agibank, com foco na **distribuição regional de adesão**.

---

## 📌 Objetivo
Investigar como a localização (região) dos colaboradores influência na escolha de operadoras e modalidades de plano de saúde.

---

## 🧩 Dados Utilizados
- `colaboradores.xlsx`: CPF, Nome, Cidade, UF, Status.
- `plano_de_saude.xlsx`: CPF, Operadora e Modalidade do Plano.

---

## 🛠️ Metodologia

1. Leitura das planilhas utilizando a biblioteca Pandas.  
2. Inspeção dos dados quanto a estrutura e valores nulos.  
3. Padronização do campo CPF para possibilitar o cruzamento das bases.  
4. Classificação dos colaboradores por região, conforme divisão oficial do IBGE.  
5. Tratamento dos dados: limpeza, remoção de duplicidades e padronização.  
6. Junção (merge) das bases pelo CPF.  
7. Análise exploratória com gráficos (Seaborn).  
8. Geração de arquivos de saída e relatório final.

---

## 📊 Gráficos Gerados

- Distribuição de colaboradores por região:
<img width="900" height="540" alt="image" src="https://github.com/user-attachments/assets/f225c9cf-2199-4672-9105-3a74a4b66ef9" />

- Adesão por operadora em cada região:
<img width="900" height="442" alt="image" src="https://github.com/user-attachments/assets/af0c4e99-8c92-4cda-8bbf-7080a949969b" />

- Modalidade de plano por região:
<img width="900" height="442" alt="image" src="https://github.com/user-attachments/assets/164adf2b-6edc-49cf-9d75-a98e8c88e1de" />

---

## 💡 Principais Resultados

- As operadoras preferidas variam de acordo com a região.  
- A região Sudeste apresenta o maior volume de adesões.  
- A modalidade "A - Careplus" é a mais escolhida no Norte.  
- As regiões Nordeste e Sudeste concentram a maioria dos colaboradores.  
- Operadoras como Careplus e Bradesco dominam certas regiões, indicando preferências locais.  
- Modalidades de plano também variam conforme a região e a operadora, influenciadas pela cobertura e rede de atendimento.

---

## 📁 Saídas

- `analise_planos_por_regiao.xlsx`
- `colaboradores_por_regiao.xlsx`
- `operadoras_por_regiao.xlsx`
- Gráficos em tela

---

## 💡 Principais Resultados

- Operadoras preferidas variam por região
- Região Sudeste tem maior volume de adesões
- Modalidade "A - Careplus" é altamente escolhida no Norte

---

## 🧠 Requisitos Técnicos

- Python 3.10+
- Pandas
- Matplotlib
- Seaborn
- OpenPyXL

---

## 👤 Autor

- Thiago Ferrer  
- Beginner, com atuação no time de SGP – Serviços de Gestão de Pessoas – 2025  
- Projeto desenvolvido para a **SGP Tech | Agibank**
---

## 📚 Referências

- IBGE - Instituto Brasileiro de Geografia e Estatística. Divisão regional do Brasil.  
- Bibliotecas utilizadas: pandas, matplotlib, seaborn, openpyxl, python-docx.



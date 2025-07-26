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

## 🛠️ Etapas Realizadas

1. **Leitura das planilhas com Pandas**
2. **Tratamento dos dados:**
   - Remoção de duplicidade e inconsistência no CPF
   - Conversão de CPF para texto
   - Padronização de colunas
3. **Merge das bases pelo CPF**
4. **Mapeamento da região com base na UF**
5. **Análise exploratória com gráficos Seaborn**
6. **Geração de relatório final e planilhas de saída**

---

## 📊 Gráficos Gerados

- Distribuição de colaboradores por região:
<img width="900" height="540" alt="image" src="https://github.com/user-attachments/assets/f225c9cf-2199-4672-9105-3a74a4b66ef9" />

- Adesão por operadora em cada região
<img width="900" height="442" alt="image" src="https://github.com/user-attachments/assets/af0c4e99-8c92-4cda-8bbf-7080a949969b" />

- Modalidade de plano por região
<img width="900" height="442" alt="image" src="https://github.com/user-attachments/assets/164adf2b-6edc-49cf-9d75-a98e8c88e1de" />

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

## 🧠 Requisitos

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

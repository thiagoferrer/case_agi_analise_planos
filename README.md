# 📊 Análise de Adesão aos Planos de Saúde por Região

## 📁 Projeto
Análise exploratória dos planos de saúde oferecidos aos colaboradores da empresa Agibank, com foco na **distribuição regional de adesão**.

---

## 📌 Objetivo
Investigar como a localização (região) dos colaboradores influencia na escolha de operadoras e modalidades de plano de saúde.

---

## 🧩 Dados Utilizados
- `colaboradores.xlsx`: contém CPF, nome, cidade, UF, status.
- `plano_de_saude.xlsx`: contém CPF, operadora e modalidade do plano.

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

- Distribuição de colaboradores por região
- Adesão por operadora em cada região
- Modalidade de plano por região

---

## 📁 Saídas

- `analise_planos_por_regiao.xlsx`
- `colaboradores_por_regiao.xlsx`
- `operadoras_por_regiao.xlsx`
- Gráficos em tela ou salvos como imagem (opcional)

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

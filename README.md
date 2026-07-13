\# Desafio Técnico – Classificação de Notícias



\## 1. Objetivo



Desenvolver um modelo de Machine Learning capaz de classificar notícias em suas respectivas categorias e disponibilizar a solução por meio de uma API utilizando FastAPI.



\## 2. Estrutura do Projeto



\* `notebooks/`: análise exploratória, pré-processamento, treinamento e avaliação do modelo.

\* `api/`: implementação da API FastAPI para inferência do modelo.

\* `data/`: conjunto de dados utilizado no projeto.

\* `requirements.txt`: dependências necessárias para execução.



\## 3. Tecnologias Utilizadas



\* Python

\* Pandas

\* NumPy

\* Scikit-Learn

\* Joblib

\* FastAPI

\* Uvicorn

\* Jupyter Notebook



\## 4. Como Executar



\### Instalar as dependências



```bash

pip install -r requirements.txt

```



\### Executar a API



```bash

cd api

uvicorn main:app --reload

```



\## 5. Como Testar



Após iniciar a API, acesse a documentação interativa:



```text

http://127.0.0.1:8000/docs

```



Utilize o endpoint `POST /predict` para enviar uma notícia e obter a classificação prevista pelo modelo.



Exemplo de entrada:



```json

{

&#x20; "text": "Novo projeto de educação será lançado pelo governo"

}

```



\## 6. Resultados do Modelo



\## 6. Resultados do Modelo



O modelo foi avaliado em uma base de teste contendo 33.408 notícias distribuídas em múltiplas categorias.



\### Métricas Gerais



| Métrica                  | Valor |

| ------------------------ | ----- |

| Accuracy                 | 72%   |

| Precision (Weighted Avg) | 70%   |

| Recall (Weighted Avg)    | 72%   |

| F1-Score (Weighted Avg)  | 69%   |



\### Destaques



\* Melhor desempenho em categorias com maior volume de exemplos, como \*\*Poder\*\*, \*\*Mundo\*\*, \*\*Mercado\*\*, \*\*Esporte\*\*, \*\*Cotidiano\*\* e \*\*Ilustrada\*\*.

\* Categoria \*\*Esporte\*\* apresentou F1-Score de 0,89.

\* Categoria \*\*Painel do Leitor\*\* apresentou F1-Score de 0,91.

\* O modelo apresentou menor desempenho em categorias com poucos exemplos de treinamento, evidenciando o impacto do desbalanceamento da base.



As métricas detalhadas por categoria, matriz de confusão e análises complementares podem ser consultadas no notebook de treinamento disponível neste repositório.





\## 7. Autor



Érica Bernardes da Silva Chilaúle Langa








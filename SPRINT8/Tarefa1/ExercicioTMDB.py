import requests
import pandas as pd

from IPython.display import display

api_key = "a4b19d34fb649042fb1473575842df56"
url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&language=pt-BR"

response = requests.get(url)
data = response.json()

filmes = []

for movie in data["results"]:
    df = pd.DataFrame(
        {
            "Titulo": [movie["title"]],
            "Data de lançamento": [movie["release_date"]],
            "Visão geral": [movie["overview"]],
            "Votos": [movie["vote_count"]],
            "Média de votos:": [movie["vote_average"]],
        }
    )
    filmes.append(df)

df_final = pd.concat(filmes)
display(df_final)

Etapa 2 - Ingestão streaming/micro batch
Neste etapa do desafio iremos capturar dados do TMDB via AWS Lambda realizando chamadas de API. Os dados coletados devem ser persistidos em Amazon S3, camada RAW Zone, mantendo o formato da origem (JSON) e, se possível, agrupando-os em arquivos com, no máximo, 100 registros cada.
O objetivo desta etapa é complementar os dados dos Filmes e Series, carregados na Etapa 1, com dados oriundos  TMDB e, opcionalmente, de outra API de sua escolha.

Importante:

Os arquivos CSVs carregados na Etapa 1 não devem ser modificados.
Os novos dados devem ser complementares aos dados do CSV. Tem que existir informações novas sobre os dados do CSV.
Não é necessário realizar tratamento dos dados externos, o máximo que pode ser feito é o agrupamento de dados.
Cuidado para os arquivos JSON gerados não serem maior do que 10 MB.
Não agrupe JSON com estruturas diferentes.
Os IDs do IMDB presentes nos arquivos CSV podem ser utilizados em pesquisas  no TMDB.
Se você escolher fazer sobre um filme ou uma trilogia específica, considere utilizar pelo menos 4 métodos de API diferentes para possibilitar uma análise de dados qualificada.
Considere desenvolver seu código localmente primeiro e com poucos dados para depois leva-lo para a AWS Lambda e aumentar a pesquisa de dados. APIs normalmente limitam requisições. Evite realizar muitas requisições em fase de desenvolvimento ou teste para evitarmos qualquer bloqueio na conta de vocês
Esta atividade corresponde a parte do desafio final. Não esperamos que você registre resposta neste espaço. Contudo, deves adicionar o código-fonte produzido ao seu repositório no Github. Lembre-se de remover suas credenciais de acesso antes de efetuar commit.

Perguntas dessa tarefa
Em sua conta AWS, no serviço AWS Lambda, realize as seguintes atividades:

1.  Criar nova camada (layer) no AWS Lambda para as libs necessárias à ingestão de dados (por exemplo,  tweepy, se você utilizar o Tweeter)

2. Implementar o código Python em AWS Lambda para consumo de dados do TMDB:
   - Se está utilizando TMDB,  buscar pela API os dados que complementem a análise
   - Utilizar a lib boto3 para gravar os dados no AWS S3
    -----| no momento da gravação dos dados deve-se considerar o padrão de path: <nome do bucket>\<camada de armazenamento>\<origem do dado>\<formato do dado>\<especificação do dado>\<data de processamento separada por ano\mes\dia>\<arquivo>
              São exemplos de caminhos de arquivos válidos:
               - S3:\\data-lake-do-fulano\Raw\Twitter\JSON\2022\05\02\prt-uty-nfd.json
               - S3:\\data-lake-do-fulano\Raw\Twitter\JSON\2022\05\02\idf-uet-wqt.json

FROM python:3.9

# copia todos os arquivos e diretórios do diretório atual 
# (onde o Dockerfile está localizado) para o diretório raiz (/) dentro do contêiner do Docker.
COPY . .

# define o diretório raiz (/) como o diretório de trabalho.
# Isso significa que quaisquer instruções subsequentes no Dockerfile serão executadas em relação a este diretório.
WORKDIR /

# Instale as dependências do Python
RUN pip install boto3

# Execute o seu código Python quando o contêiner for iniciado
CMD ["python", "ingestao.py"]

# docker build -t ingestao ., para criar a imagem

# docker run -it ingestao, para executar o container
FROM python:3.9

COPY . .

WORKDIR /

# Instale as dependências do Python
RUN pip install boto3

# Execute o seu código Python quando o contêiner for iniciado
CMD ["python", "ingestao.py"]

# docker build -t ingestao ., para criar a imagem

# docker run -it ingestao, para executar o container
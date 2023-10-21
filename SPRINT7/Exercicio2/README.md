# docker pull jupyter/all-spark-notebook, executei esse comando para baixar a imagem do jupyter no docker

# docker run -it -p 8888:8888 --name ex_2meu_container_spark jupyter/all-spark-notebook, executei esse comando para criar o container

# docker cp C:\Users\cairo\bolsaCOMPASS/README.md ex_2meu_container_spark:/home/jovyan/README.md, para passar o arquivo README.md para o container

# docker exec -it ex_2meu_container_spark bash, executei esse comando para entrar no container

# pyspark, executei esse comando para abrir o pyspark

# rdd = sc.textFile("README.md"), executei esse comando para ler o arquivo README.md

# rdd.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b).sortBy(lambda x: x[1], False).filter(lambda x: x[0] not in [".", ",", ":", ";", "(", ")", "[", "]", "{", "}", "'", '"', ""]).collect(), executei esse comando para contar a quantidade de ocorrencia de cada palavra do arquivo README.md e depois ordenei em ordem decrescente excluindo a ocorrencia de pontuações e deixando a visualização facil.

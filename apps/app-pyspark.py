from pyspark.sql import SparkSession

# Inicializa o SparkSession
spark = SparkSession.builder \
    .appName("Teste PySpark") \
    .getOrCreate()

# Cria um DataFrame a partir de uma lista de tuplas
data = [("Alice", 34), ("Bob", 45), ("Charlie", 28)]
df = spark.createDataFrame(data, ["Nome", "Idade"])

# Mostra o conteúdo do DataFrame
print("Conteúdo do DataFrame:")
df.show()

# Aplica uma transformação no DataFrame
df_filtrado = df.filter(df["Idade"] > 30)

# Mostra o resultado da transformação
print("\nConteúdo do DataFrame filtrado:")
df_filtrado.show()

# Realiza uma agregação no DataFrame
df_agregado = df.groupBy().avg("Idade")

# Mostra o resultado da agregação
print("\nMédia da Idade:")
df_agregado.show()

# Encerra a sessão do Spark
spark.stop()

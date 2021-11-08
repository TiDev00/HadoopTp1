#-*coding:utf-8-*-

from datetime import datetime

from pyspark.sql import SQLContext
from pyspark import SparkContext
from pyspark.sql.types import *

sc = SparkContext("local","tp")

sqlContext = SQLContext(sc)

remorquage_schema = StructType([
StructField("DATE_ORIGINE", StringType(), True),
StructField("LONGITUDE_ORIGINE", StringType(), True),
StructField("LATITUDE_ORIGINE", StringType(), True),
StructField("RUE_ORIGINE", StringType(), True),
StructField("SECTEUR_ORIGINE", StringType(), True),
StructField("ARRONDISSEMENT_ORIGINE", StringType(), True),
StructField("DATE_DESTINATION", StringType(), True),
StructField("LONGITUDE_DESTINATION", StringType(), True),
StructField("LATITUDE_DESTINATION", StringType(), True),
StructField("RUE_DESTINATION", StringType(), True),
StructField("SECTEUR_DESTINATION", StringType(), True),
StructField("ARRONDISSEMENT_DESTINATION", StringType(), True),
StructField("MOTIF_REMORQUAGE", StringType(), True)])


fichier = sc.textFile("remorquages.csv")

rdd = fichier.map(lambda x:x.split(","))

#rdd2 = rdd.map(lambda x:(str(x[0]), str(x[1]), str(x[2]), x[3], x[4], x[5], str(x[6]), str(x[7]), str(x[8]), x[9], x[10], x[11], x[12]))
rdd2 = rdd.map(lambda x:(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10], x[11], x[12]))

df1 = sqlContext.createDataFrame(rdd2, remorquage_schema)

df1.show(10)

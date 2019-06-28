# -*- coding:utf-8 -*-
from pyspark import SparkContext
from pyspark.sql import SQLContext, Row

# 하둡 path
path = "hdfs://hadoop01:9000/jcjc"

# 컨텍스트 생성
sc = SparkContext.getOrCreate();
print(sc)
 
# HDFS 파일 RDD로 읽어오기
file = sc.textFile(path + "/billAnalysis/result.csv​")
file_df = file.map(lambda line: line.split(","))
print(file_df)

# dmenu = lines.map(lambda p: Row(kcal=int(p[0]), menuId=p[1], name=p[2], price=int(p[3])))
# ​
# df = sqlContext.createDataFrame(dmenu)
# ​
# df.registerTempTable("res_mytable")
# ​
# print(df.printSchema())​
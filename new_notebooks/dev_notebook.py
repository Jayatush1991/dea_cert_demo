# Databricks notebook source
# MAGIC %fs ls "/databricks-datasets/"

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

files = dbutils.fs.ls("/databricks-datasets/") 
print(files)

# COMMAND ----------

display(files)

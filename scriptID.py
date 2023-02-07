from ast import Sub
from re import sub
from tokenize import group
from numpy import append, true_divide
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
import psycopg2
import psycopg2.extras
import os
import sys
import random
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

id = []
o_id = []
for i in range(1071):
    if(i/10 < 1):
        id.append('E' + '0000' + str(i))
    elif(i/100 < 1):
        id.append('E' + '000' + str(i))
    elif(i/1000 < 1):
        id.append('E' + '00' + str(i))
    elif(i/10000 < 1):
        id.append('E' + '0' + str(i))
    else:
        id.append('E' +  str(i))


try:
  conn = psycopg2.connect(
    host="ec2-34-202-187-131.compute-1.amazonaws.com",
    database="de116oaj1mhesd",
    user="u69013hjh8kfof",
    password="p0097d14fe83dc4f58c78a583d6e624cf09a0d69d9efa09272052178bd0fc2d90")

  cur = conn.cursor()

  cur.execute('SELECT * FROM application_t')
  for record in cur.fetchall():
    o_id.append(record[0])

#   print(o_id)


  for i in range(1071):
        insert_value = [id[i]]
        insert_script = 'UPDATE application_t set application_id = ' + id[i] + ' WHERE application_id = '+ o_id[i] +';'

        cur.execute(insert_script)
        # cur.execute(insert_script, insert_value)
        conn.commit()

  conn.close()

except Exception as e:
  print(e)
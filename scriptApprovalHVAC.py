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



#input data to database
def uniqueRandomNumberGenerator(low, high, num):
  return random.sample(range(low, high), num)


def splitProductName(data):
  x = data.split("|")
  return x[0]

def splitIntegrety(data):
  x = data.split("|")
  return x[18]

def splitInsulation(data):
  x = data.split("|")
  return x[19]

def splitWallFloor(data):
  x = data.split("|")
  return x[7]

def splitConstructionType(data):
    x = data.split("|")
    return x[8]

def splitSub(data):
    x = data.split("|")
    return x[9]

def splitThickness(data):
    x = data.split("|")
    return x[10]

def splitServiceType(data):
  x = data.split("|")
  return x[5]

def splitServiceDetail(data):
  x = data.split("|")
  return x[6]

def splitApprovalNumber(data):
    x = data.split("|")
    return x[37]

def splitAppTable(data):
    x = data.split("|")
    return x[39]

def splitAppPage(data):
    x = data.split("|")
    return x[38]
# def splitFeature(data):
#   tmp = data.split(",")
#   x = []
#   x.append(int(tmp[1]))
#   x.append(int(tmp[2]))
#   x.append(int(tmp[3]))
#   x.append(int(tmp[4]))
#   x.append(int(tmp[5]))
#   return x

cwd = os.getcwd()
files = os.listdir(cwd)
print("Files in %r: %s" % (cwd, files))
dataSet = open("rowdataHVAC.txt", "r")
# print(dataSet.read())

rowDataList = []
for data in dataSet:
  rowDataList.append(data)
# print(rowDataList)

productName = []
for data in rowDataList:
  productName.append(splitProductName(data))

integrety = []
for data in rowDataList:
  integrety.append(splitIntegrety(data))

insulation = []
for data in rowDataList:
  insulation.append(splitInsulation(data))

wallFloor = []
for data in rowDataList:
  wallFloor.append(splitWallFloor(data))

constructionType = []
for data in rowDataList:
  constructionType.append(splitConstructionType(data))

subC = []
for data in rowDataList:
  subC.append(splitSub(data))

thickness = []
for data in rowDataList:
  thickness.append(splitThickness(data))

serviceType = []
for data in rowDataList:
  serviceType.append(splitServiceType(data))

serviceDetail  =[]
for data in rowDataList:
  serviceDetail.append(splitServiceDetail(data))

approvalNumber = []
for data in rowDataList:
    approvalNumber.append(splitApprovalNumber(data))

approvalTable = []
for data in rowDataList:
    approvalTable.append(splitAppTable(data))

approvalPage = []
for data in rowDataList:
    approvalPage.append(splitAppPage(data))


# print(productName)
id = []
for i in range(1071, 1500):
    if(i/10 < 1):
        id.append('AP' + '0000' + str(i))
    elif(i/100 < 1):
        id.append('AP' + '000' + str(i))
    elif(i/1000 < 1):
        id.append('AP' + '00' + str(i))
    elif(i/10000 < 1):
        id.append('AP' + '0' + str(i))
    else:
        id.append('AP' +  str(i))


number = []
for i in range(429):
    if(i/10 < 1):
        number.append('H' + '0000' + str(i))
    elif(i/100 < 1):
        number.append('H' + '000' + str(i))
    elif(i/1000 < 1):
        number.append('H' + '00' + str(i))
    elif(i/10000 < 1):
        number.append('H' + '0' + str(i))
    else:
        number.append('H' +  str(i))


ins = [[id],[approvalNumber],[approvalTable],[approvalPage], [number]]


print(ins)
# featureX = []
# for data in rowTrainDataList:
#   featureX.append(splitFeature(data))

# core = []
# for data in rowTrainDataList:
#     core.append(splitCoreOrAlt(data))

# print(subjectNO)
# print(featureX)
# print(core)
#used for reading data from database
try:
  conn = psycopg2.connect(
    host="ec2-34-202-187-131.compute-1.amazonaws.com",
    database="de116oaj1mhesd",
    user="u69013hjh8kfof",
    password="p0097d14fe83dc4f58c78a583d6e624cf09a0d69d9efa09272052178bd0fc2d90")

  cur = conn.cursor()

#   cur.execute('DROP TABLE IF EXISTS test_knn_subject')

#   create_script = ''' CREATE TABLE IF NOT EXISTS test_knn_subject (
#                       subject_id       varchar(10) PRIMARY KEY,
#                       subject_name     varchar(50) NOT NULL,
#                       quiz              int,
#                       individual_assign int,
#                       group_assign      int,
#                       exam              int,
#                       study_level       int 

#                   )'''

#   cur.execute(create_script)




  # for i in range(1071):
  #       insert_script = 'INSERT INTO application_t (application_id, application_name, application_integrity, application_insulation, application_type, application_wallfloor, application_construction_type, application_subcategory) VALUES (%s, %s, %s, %s, %s, %s, %s,%s)'
  #       insert_value = [id[i], productName[i], integrety[i], insulation[i], 'e', wallFloor[i], constructionType[i], subC[i]]


  #       cur.execute(insert_script, insert_value)
  #       conn.commit()

  # conn.close()

  # for i in range(1071):
  #   update_script = 'UPDATE application_t SET application_thickness = ' + thickness[i] + ' WHERE application_id = ' + '\'' + str(id[i]) + '\'' + ';'
  #   cur.execute(update_script)
  #   conn.commit()
  # conn.close()

#   for i in range(1071):
#         insert_script = 'INSERT INTO electrical_t (electrical_id, electrical_service_type, electrical_service_detail) VALUES (%s, %s, %s)'
#         insert_value = [id[i], serviceType[i], serviceDetail[i]]


#         cur.execute(insert_script, insert_value)
#         conn.commit()

#   conn.close()


  for i in range(429):
        insert_script = 'INSERT INTO approval_t (approval_id, approval_page, approval_table, approval_number, app_id) VALUES (%s, %s, %s, %s, %s)'
        insert_value = [id[i], approvalPage[i], approvalTable[i], approvalNumber[i], number[i]]


        cur.execute(insert_script, insert_value)
        conn.commit()

  conn.close()

except Exception as e:
  print(e)

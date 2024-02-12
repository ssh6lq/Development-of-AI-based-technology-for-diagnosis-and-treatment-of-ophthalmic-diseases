import os
import numpy as np
import pandas as pd
import os
import shutil
import pandas as pd
# import xlrd
from PIL import Image
import cv2

sheet = pd.read_csv("./final_data.csv")
# sheet['OD'] = " "
# sheet['OS'] = " "
sheet1 = pd.read_csv("./final_data.csv", nrows=10000)
sheet2 = pd.read_csv("./final_data.csv", skiprows=[i for i in range (1, 10001)], nrows=10000)
sheet3 = pd.read_csv("./final_data.csv", skiprows=[i for i in range (1, 20001)], nrows=10000)
sheet4 = pd.read_csv("./final_data.csv", skiprows=[i for i in range (1, 30001)], nrows=10000)
sheet5 = pd.read_csv("./final_data.csv", skiprows=[i for i in range (1, 40001)], nrows=10000)
sheet6 = pd.read_csv("./final_data.csv", skiprows=[i for i in range (1, 50001)], nrows=10000)
sheet7 = pd.read_csv("./final_data.csv", skiprows=[i for i in range (1, 60001)], nrows=10000)
sheet8 = pd.read_csv("./final_data.csv", skiprows=[i for i in range (1, 70001)], nrows=10000)

OS=str(0.2)
os.mkdir('./va/'+OS)

import shutil

oct_list = os.listdir("./dataset_final")

for i in range (len(sheet1['기록서식키'])) :
    ID = str(sheet3['환자번호'][i])
    date=str(sheet3['작성일'][i])
    OD=str(sheet3['R)BCVA'][i])
    OS=str(sheet3['L)BCVA'][i])
    while len(ID) < 10 :
        ID = '0' + ID
        
            
    for j in range (len(oct_list)) :
        if (oct_list[j][0:10] == ID):
            if (oct_list[j][14:24] == date):
                path=
                if (oct_list[j][11:13] == 'OD'):
#                     print(OD)
                    va=os.listdir('./va')
                    for k in va:
                        if k == OD:
                            src=os.path.join(path)
                            dst=os.path.join(copy,name)
                            shutil.copyfile(src,dst)
#                         else:
#                             os.mkdir('./va/'+OD)  # 폴더 생성
                elif (oct_list[j][11:13] == 'OS'):
#                     print(OS)
                    va=os.listdir('./va')
                    for k in va:
                        if k == OS:
                            print(type(k))
                            print(type(OS))
#                         else:
#                             os.mkdir('./va/'+OS)  # 폴더 생성

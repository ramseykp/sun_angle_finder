from matplotlib import pyplot as plt
from matplotlib import style
import pandas as pd
import numpy as np
import pysolar.solar
import time
import datetime
from datetime import date

class Sun_Angle():
    #owiMetadata = input('Enter metadata.csv file path: \n')

    def Get_Sun_Angle(self, owiMetadata):
        print('owiMetadata CSV = ' + owiMetadata)

        style.use('ggplot')
        self.owiMetadata = r'C:\SmartStorageExternalDrive\aNewPlace\Flight_0665_massive_dalles_substation\NIR_FullRes\NIR_Data_0665.csv'

        #read CSV using the top row as header and skipping the row with index value of 1 (metaMetaData)
        df = pd.read_csv(self.owiMetadata, skiprows=[1], header=0)
        df = df.drop([' Image Filename'], axis=1)

        latitude = df[' Frame Center Latitude']
        latitudeList = latitude.values.tolist()

        longitude = df[' Frame Center Longitude']
        longitudeList = longitude.values.tolist()

        #df['Time'] = (df['Time'] / (1000*1000)).apply(datetime.fromtimestamp)
        timeStmp = df['Time']
        timeList = timeStmp.values.tolist()

        print(type(timeList))
        print(timeList)

        x = 0
        while x != 20:#len(timeList):
            imageDateTime = int(timeList[x]) # converting string containing unix timestamp int
            imageDateTimeSeconds= imageDateTime / 1000000
            #print(imageDateTime)
            #print(imageDateTimeSeconds)
            imageDateTimeCtime = time.ctime(imageDateTimeSeconds)
            imageHour = imageDateTimeCtime[-13:-11]
            print('hour = ' + imageHour)
            imageMinute = imageDateTimeCtime[-10:-8]
            print('minute = ' + imageMinute)
            imageSecond = imageDateTimeCtime[-7:-5]
            print('second = ' + imageSecond)

            imageDateTimeDate = date.fromtimestamp(int(imageDateTimeSeconds))
            imageYear = str(imageDateTimeDate)[:4]
            print('year = ' + imageYear)
            imageMonth = str(imageDateTimeDate)[5:7]
            print('month = ' + imageMonth)
            imageDay = str(imageDateTimeDate)[8:10]
            print('day = ' + imageDay)

            print(imageDateTimeDate)
            print(imageDateTimeCtime)

            print(latitudeList[x]) #print the lat
            print(longitudeList[x])
            x += 1
        print(datetime.datetime.now())




         #    self.TimeList.append(lines['Time'])    
         #           ts_start = int(self.TimeList[1])/1000000  #converting microseconds to seconds
         #           ts_end = int(self.TimeList[-1])/1000000   #converting microseconds to seconds
         #   
         #           start = time.ctime(ts_start)           #converting seconds to Ctime (YYYYmonDD)
         #           end = time.ctime(ts_end)


        #for i,j in time.iterrows():
        #    timeStampSeconds = j/100000
        #    print(i,j/100000)
        #    date = datetime.datetime.now()
        #    print('date = ' + str(date))
        #    print('timeStampSeconds = ' + str(timeStampSeconds))
        #    print(type(timeStampSeconds))
        #
        #
        #print(type(time))
        #
        #print(df.shape) #gives info on number of rows and columns
        #print(df.info()) #gives info on each of the columns data type and how many null values exist    

        #print(type(imageSet))

SA = Sun_Angle()
csvFile = r'C:\SmartStorageExternalDrive\aNewPlace\Flight_0665_massive_dalles_substation\NIR_FullRes\NIR_Data_0665.csv'
SA.Get_Sun_Angle(csvFile)
import requests 
import random
import time,datetime
from function import avg_do,avg_level_battery,avg_temp


#class to create sensors
class Sensors:
    def __init__(self,host,access_token,latitude,longitude):
        self.host=host #server to send request
        self.access_token=access_token #access token from thingsBoard
        self.latitude=latitude #gps detail
        self.longitude=longitude #gps detail
    

    def send_data_sensor(self,maxDO,minDO,maxTemp,minTemp,maxBtr,minBtr):
        hostDemo="http://{}/api/v1/{}/telemetry".format(self.host,self.access_token)

        for i in range(1):
            current_time=str(datetime.datetime.now())
            x=avg_do(maxDO,minDO)
            def_Min_Do=x[0]
            def_Max_Do=x[1]
            #random number from min and max DO
            rndo=round(random.random()*(def_Max_Do-def_Min_Do)+def_Min_Do,1)
            #Temp per hours
            rntemp= avg_temp(maxTemp,minTemp) 
            #battery level
            batteryLevel=round(avg_level_battery(maxBtr,minBtr),1)

            data={"do": rndo,"temp":rntemp,'timestamp':current_time,'battery':batteryLevel,'latitude':self.latitude,'longitude':self.longitude}
            sendData=requests.post(hostDemo,json=data)
            
            print(self.access_token)
            print(str(data))
        print(sendData.text)


#name sensor= (url server, access token,location of sensors)
Do=Sensors('demo.thingsboard.io','DO1234',32.436911,35.524924)
SP200=Sensors('demo.thingsboard.io','SP200',32.449634,35.518630)
SP201=Sensors('demo.thingsboard.io','SP201',32.435646,35.527860)
SP202=Sensors('demo.thingsboard.io','SP202',32.436148,35.526218)
SP203=Sensors('demo.thingsboard.io','SP203',32.436474,35.525821)

#hours and minutes in realtime
h=int(datetime.datetime.now().strftime('%H'))
m=int(datetime.datetime.now().strftime('%M'))
print(h,m)

i=0
while i>-1:
    if(h==6 or h==12 or h==18 or h==0 and m<20):
        for x in range(7):
            print('restart loop')
            SP203.send_data_sensor(16.8,2,23,19.2,13.8,12)
            SP202.send_data_sensor(12.8,2.1,23,19.2,13.8,12)
            SP201.send_data_sensor(10,1.8,23,19.2,13.8,12)
            SP200.send_data_sensor(14.8,2,23,19.2,13.8,12)
            Do.send_data_sensor(12,2.5,23,19.2,13.2,12)
            print('Going sleep for 3 minutes')
            time.sleep(180)
    else:
        print('normal loop')
        SP203.send_data_sensor(16.8,2,23,19.2,13.8,12)
        SP202.send_data_sensor(12.8,2.1,23,19.2,13.8,12)
        SP201.send_data_sensor(10,1.8,23,19.2,13.8,12)
        SP200.send_data_sensor(14.8,2,23,19.2,13.8,12)
        Do.send_data_sensor(12,2.5,23,19.2,13.2,12)
        print('Going sleep for 20 minutes')
        time.sleep(1200)
    i+=1





# for i in range(10000):
#     SP203.send_data_sensor(16.8,2,23,19.2,13.8,12)
#     SP202.send_data_sensor(12.8,2.1,23,19.2,13.8,12)
#     SP201.send_data_sensor(10,1.8,23,19.2,13.8,12)
#     SP200.send_data_sensor(14.8,2,23,19.2,13.8,12)
#     Do.send_data_sensor(12,2.5,23,19.2,13.2,12)
#     print('{} sending left, go sleep'.format((10000-i)))
#     time.sleep(1200)



            # second_delay=i*3
            # print('sending {} second after start. {} sending left'.format(second_delay,(3-i)))









# # details of sensor 'do'
# host= 'demo.thingsboard.io'
# access_token= 'DO1234'

# # details of sensor 'SP200'
# host= 'demo.thingsboard.io'
# access_token= 'SP200'

# # details of sensor 'SP201'
# host= 'demo.thingsboard.io'
# access_token= 'SP201'











#         for i in range(10000):
#             current_time=datetime.datetime.now()
#             rndo=round(random.random()*(10-2)+2,1)
#             rntemp=round(random.random()*(27-25)+25,1)
#             data={"do": rndo,"temp":rntemp,'timestamp':current_time,'location':{'lat':self.latitude,'long':self.longitude}}
#             sendData=requests.post(hostDemo,json={data})
#             x=i*3
#             print(str(data))
#             print('sending {} second after start. {} sending left'.format(x,(10000-i)))
#             time.sleep(3)
#         print(sendData.text)
#         print('finish sending')



# SP200=Sensors('demo.thingsboard.io','DO1234',32.447017,35.519081)


# host= 'demo.thingsboard.io'
# access_token= 'DO1234'

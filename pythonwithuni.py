    
# Author : Bhushan makan patil <patilbhushan8595@gmail.com>
#Title   :  DATA ACQUISITION OF BIOGAS SENSOR NODE IN REAL TIME 
#Date    :  --/--  --/--/--
#mahadbt{U,pass:patbhus,bhushan@3}

############################################################################################
import serial    
# serial is the python module this use to communicate external connected device on com port 
import time       
 # tis also python modula use for time 
import matplotlib.pyplot as plt   
# this also python module this use for plot the data very nice formate 
from matplotlib import animation  
# this also same for above 
global Sensor_Data    
# here i decleare the Sensor_Data global veriable 
from openpyxl import Workbook 
Sensor_Data={'S1':0.0,'S2':0.0,'S3':0.0,'S4':0.0,'S5':0.0}  
# this is a dictionary to store data in key valu pair 
# here S1 means sensor one like this
ExcelFileName='BiogasSensorData_' 
ExcelFileName+=time.strftime('%d-%m-%y %I:%M:%S',time.localtime(time.time()))
plt.ion()     
# plt.ion is a mathod in matplotlib here this use for plot all incoming data in one figure [ he keep figure canstant]
#fig=plt.figure()
fig=plt.figure()
fig.suptitle("SENSOR DATA", size=16)
ax1=fig.add_subplot(221)
ax2=fig.add_subplot(222)
ax3=fig.add_subplot(223)
ax4=fig.add_subplot(224)

book=Workbook()        # this for excel sheet write object from module penpyxl
sheet=book.active       # to geting acvite sheet of excel
sheet['A1']='dataHeadingString'
sheet['B1']='dataHeadingString'
sheet['C1']='dataHeadingString'
sheet['D1']='dataHeadingString'

#with open('excel_file_Name.vipul','+a') as file :
   # ExcelFileName = file.read()


def getString(string=' '):
    '''this is a function for geting string which means incoming data is
     coming from [xbee cordinator to xbee enddevice to uno to pc ],
     data in the form of packet  i.e at the  time of receiving one byte of data 
     so that  those byte of data collected here  are made into one full valuble string 
     and are being  returned. 
    '''
    i=1
    while True :
        f=open('Sensordata.txt','+a')
        if i not in [11]:
            data=ser.read()
            string+=data.decode('utf-8').strip()
            i+=1
        else :
            break
    f.write(string)
    f.write(',')
    f.close()
    print(string)
    getCleanData(string) # function call 

######################################################################################################

def getCleanData(data=' '):
    '''In this function we are clean sensor data to geting from getString 
    function and store in Sensor_Data veriable=(type<dictionary>), 
    [data clening : i.e our data is S1=0257mv ,this collected data string we 
    slice ([3:7]) and type cast into str to float than divide by 10 and store 
    in veriable ]
      '''
    try :
        if data.startswith('S1='):
            Sensor_Data['S1']=float(data[3:7])/10
            #here is sheet of openpyxl
        elif data.startswith('S2='):
            Sensor_Data['S2']=float(data[3:7])/10
            #here is sheet of openpyxl
        elif data.startswith('S3='):
            Sensor_Data['S3']=float(data[3:7])/10
            #here is sheet of openpyxl
        elif data.startswith('S4='):
            Sensor_Data['S4']=float(data[3:7])/10
            #here is sheet of openpyxl

        elif data.startswith('S5='):
            Sensor_Data['S5']=float(data[3:7])/10
            #here is sheet of openpyxl
    
    except Exception as e:
        print('[**]',e)

def getplot():
    #b: blue,g: green,r: red,c: cyan,m: magenta,y: yellow,k: black,w: white
    Time=int(time.strftime('%I%M%S',time.localtime(time.time())))
    #plt.plot(Time,Sensor_Data['S1'], 'bo-' , Time , Sensor_Data['S2'],'r*-',Time , Sensor_Data['S3'],'c^-',Time ,Sensor_Data['S4'],'y*-')
    #plt.plot(Time,Sensor_Data['S1'], Time , Sensor_Data['S2'],Time , Sensor_Data['S3'],Time ,Sensor_Data['S4'],label='tempretire_S1')
    ax1.plot(Time,Sensor_Data['S1'] ,'b*' ,linewidth= 5)
    ax2.plot(Time,Sensor_Data['S2'], 'ro' ,linewidth=5)
    ax3.plot(Time,Sensor_Data['S3'], 'c^' ,linewidth=5)
    ax4.plot(Time,Sensor_Data['S4'], 'y*' ,linewidth=5 )
    plt.gcf().autofmt_xdate()
    ax1.grid(True)
    ax2.grid(True)
    ax3.grid(True)
    ax4.grid(True)
    ax1.title.set_text('S1')
    ax2.title.set_text('S2')
    ax3.title.set_text('S3')
    ax4.title.set_text('S4')
    fig.tight_layout()
   # plt.title("Biogas Sensordata")
    #plt.xlabel("TIME")
   # plt.ylabel("Sensordata")
    plt.legend(loc='best', bbox_to_anchor=(0.5, 1.05),
         ncol=3, fancybox=True, shadow=True)
    plt.pause(0.1)

i=0
port=['COM17','COM16','COM9']
while True:
    try :
        ser=serial.Serial(port[i] , 9600)
        print('connetc : ' ,port[i])
        break
    except Exception as e :
        print(e)
        i=i+1
        pass

s=''
print('strat')
while 1:
    try :
        for i in range(1,5):
            getString(s)
        print('*',Sensor_Data)
        #Animation=animation.FuncAnimation(fig , getplot)
        getplot()
        plt.show()
        #animation 
    except Exception as e :
        print(e)
ser.close()
print('connection is disconnect from you')
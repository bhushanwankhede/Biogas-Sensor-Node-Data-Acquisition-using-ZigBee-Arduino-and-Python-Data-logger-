from openpyxl import Workbook 
import sys
book=Workbook()
sheet=book.active
print('ok')
file=open('sensordata.txt','r').read()
#print(file)
s_1=[]
s_2=[]
s_3=[]
s_4=[]
data=file.split(',')
print(len(data))
for i in data : 
	try :
		if i[0:2] == 'S1' and len(i) == 9:
			s_1.append(i)
		elif i[0:2] == 'S2' and len(i) == 9:
			s_2.append(i)
		elif i[0:2] == 'S3' and len(i) == 9:
			s_3.append(i)
		elif i[0:2] == 'S4' and len(i) == 9:
			s_4.append(i)

	except Exception as e :
		print(e)
u=1
for i in s_1:
	u+=1
	s='A'+str(u)
	sheet[s]= i
u=1
for i in s_2:
	u+=1
	s='B'+str(u)
	sheet[s]= i
u=1
for i in s_3:
	u+=1
	s='C'+str(u)
	sheet[s]= i
u=1

for i in s_4:
	u+=1
	s='D'+str(u)
	sheet[s]= i
	#sheet['B1']='Tempreture LM35'
	#sheet["c1"]='Sensor_1 Data '
	#sheet['D1']='Sensor_2 Data'

book.save('S_data.xlsx')


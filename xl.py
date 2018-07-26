from openpyxl import Workbook 

book=Workbook()
sheet=book.active

sheet['A1']='Tempreture PT100'
sheet['B1']='Tempreture LM35'
sheet["c1"]='Sensor_1 Data '
sheet['D1']='Sensor_2 Data'
r=1
c=1
e=0
row=[880, 460, 570,890, 380, 120,230, 590, 780,560, 210, 980,240, 180, 430,340, 150, 670,250,60]
for i in range(5) :
	r+=1
	for j in range(4) :
		sheet.cell(row=r, column=c).value = row[e]
		c+=1
		e+=1
	c=1
	book.save('w_1.xlsx')


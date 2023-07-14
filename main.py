import mysql.connector
import PySimpleGUI as sg

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="g78618SHA#",
	database="shank"
)
sg.theme('DarkAmber')
layout = [[sg.Text('Username'), sg.InputText()],
		[sg.Text('Password'), sg.InputText(key='-password-', password_char='*')],
		[sg.Button('Ok'), sg.Button('Cancel')]]

window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
	event, values = window.read()
	if event == 'Ok':
		cursor = mydb.cursor()
		sql0 = "select Position from login where Username = %s and Password = %s"
		v0 = (values[0],values["-password-"])
		cursor.execute(sql0, v0)
		result = cursor.fetchall()
		for x in result:
			print(x)
		window.close()
		layout1 = [[sg.Text('Search')],
				   [sg.InputText()],
				   [sg.Button('Search'), sg.Button('Close')]]

		window = sg.Window('Window Title', layout1)
		while True:
			event1, values1 = window.read()
			if event1 == 'Search':
				if values1[0] == "Satvik":
					sql1 = "select * from Satvik"
					cursor.execute(sql1)
					result1 = cursor.fetchall()
					window.close()
					layout2 = [[sg.Text(result1)]]
					window = sg.Window('Satvik',layout2)
					while True:
						event2, values2 = window.read()
						if event2 == sg.WIN_CLOSED:
							break

				elif values1[0] == "Shashaank":
					sql1 = "select * from Shashaank"
					cursor.execute(sql1)
					result1 = cursor.fetchall()
					window.close()
					layout2 = [[sg.Text(result1)]]
					window = sg.Window('Shashaank', layout2)
					while True:
						event2, values2 = window.read()
						if event2 == sg.WIN_CLOSED:
							break
				elif values1[0] == "A":
					sql1 = "select * from A"
					cursor.execute(sql1)
					result1 = cursor.fetchall()
					window.close()
					layout2 = [[sg.Text(result1)]]
					window = sg.Window('A', layout2)
					while True:
						event2, values2 = window.read()
						if event2 == sg.WIN_CLOSED:
							break
				elif values1[0] == "B":
					sql1 = "select * from B"
					cursor.execute(sql1)
					result1 = cursor.fetchall()
					window.close()
					layout2 = [[sg.Text(result1)]]
					window = sg.Window('B', layout2)
					while True:
						event2, values2 = window.read()
						if event2 == sg.WIN_CLOSED:
							break
			elif event1 == "Close" or event1 == sg.WIN_CLOSED:
				window.close()
				break

	elif event == sg.WIN_CLOSED or event == 'Cancel':
		break

window.close()

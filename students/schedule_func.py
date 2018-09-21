import win32com.client, datetime, pythoncom, openpyxl

def monday(filepath, sheetName, day):
	schedule_data = list()
	wb = openpyxl.load_workbook(filepath)
	ws = wb[sheetName]
	# i are number of class
	# k is every 5 class detail
	for i in range(10,49,7):
		schedule = list()
		for k in range(i,i+7):
			data = dict()
			cell_number = 'D'+str(k)
			cell_name = 'E'+str(k)
			cell_grade = 'H'+str(k)
			cell_memo = 'K'+str(k)
			data['number'] = ws[cell_number].value
			data['name'] = ws[cell_name].value
			data['grade'] = ws[cell_grade].value
			data['memo'] = ws[cell_memo].value
			data['cellInfo'] = cell_number+"/"+cell_name+"/"+cell_grade+"/"+cell_memo
			data['sheet'] = sheetName
			data['day'] = day
			schedule.append(data)

		courses = dict()
		courses['time'] = "CourseTime 2:00~3:00"
		courses['lessons'] = schedule
		schedule_data.append(courses)
	return schedule_data

def wendsday(filepath, sheetName, day):
	schedule_data = list()
	wb = openpyxl.load_workbook(filepath)
	ws = wb[sheetName]
	# i are number of class
	# k is every 5 class detail
	for i in range(10,49,7):
		schedule = list()
		for k in range(i,i+7):
			data = dict()
			cell_number = 'AR'+str(k)
			cell_name = 'AS'+str(k)
			cell_grade = 'AV'+str(k)
			cell_memo = 'AY'+str(k)
			data['number'] = ws[cell_number].value
			data['name'] = ws[cell_name].value
			data['grade'] = ws[cell_grade].value
			data['memo'] = ws[cell_memo].value
			data['cellInfo'] = cell_number+"/"+cell_name+"/"+cell_grade+"/"+cell_memo
			data['sheet'] = sheetName
			data['day'] = day
			schedule.append(data)

		courses = dict()
		courses['time'] = "CourseTime 2:00~3:00"
		courses['lessons'] = schedule
		schedule_data.append(courses)
	return schedule_data

def thursday(filepath, sheetName, day):
	schedule_data = list()
	wb = openpyxl.load_workbook(filepath)
	ws = wb[sheetName]
	# i are number of class
	# k is every 5 class detail
	for i in range(10,49,7):
		schedule = list()
		for k in range(i,i+7):
			data = dict()
			cell_number = 'BL'+str(k)
			cell_name = 'BM'+str(k)
			cell_grade = 'BP'+str(k)
			cell_memo = 'BS'+str(k)
			data['number'] = ws[cell_number].value
			data['name'] = ws[cell_name].value
			data['grade'] = ws[cell_grade].value
			data['memo'] = ws[cell_memo].value
			data['cellInfo'] = cell_number+"/"+cell_name+"/"+cell_grade+"/"+cell_memo
			data['sheet'] = sheetName
			data['day'] = day
			schedule.append(data)

		courses = dict()
		courses['time'] = "CourseTime 2:00~3:00"
		courses['lessons'] = schedule
		schedule_data.append(courses)
	return schedule_data

def friday(filepath, sheetName, day):
	schedule_data = list()
	wb = openpyxl.load_workbook(filepath)
	ws = wb[sheetName]
	# i are number of class
	# k is every 5 class detail
	for i in range(75,114,7):
		schedule = list()
		for k in range(i,i+7):
			data = dict()
			cell_number = 'D'+str(k)
			cell_name = 'E'+str(k)
			cell_grade = 'H'+str(k)
			cell_memo = 'K'+str(k)
			data['number'] = ws[cell_number].value
			data['name'] = ws[cell_name].value
			data['grade'] = ws[cell_grade].value
			data['memo'] = ws[cell_memo].value
			data['cellInfo'] = cell_number+"/"+cell_name+"/"+cell_grade+"/"+cell_memo
			data['sheet'] = sheetName
			data['day'] = day
			schedule.append(data)

		courses = dict()
		courses['time'] = "CourseTime 2:00~3:00"
		courses['lessons'] = schedule
		schedule_data.append(courses)
	return schedule_data

def sunday(filepath, sheetName, day):
	schedule_data = list()
	wb = openpyxl.load_workbook(filepath)
	ws = wb[sheetName]
	# i are number of class
	# k is every 5 class detail
	for i in range(64,114,7):
		schedule = list()
		for k in range(i,i+7):
			data = dict()
			cell_number = 'AR'+str(k)
			cell_name = 'AS'+str(k)
			cell_grade = 'AV'+str(k)
			cell_memo = 'AY'+str(k)
			data['number'] = ws[cell_number].value
			data['name'] = ws[cell_name].value
			data['grade'] = ws[cell_grade].value
			data['memo'] = ws[cell_memo].value
			data['cellInfo'] = cell_number+"/"+cell_name+"/"+cell_grade+"/"+cell_memo
			data['sheet'] = sheetName
			data['day'] = day
			schedule.append(data)

		courses = dict()
		courses['time'] = "CourseTime 2:00~3:00"
		courses['lessons'] = schedule
		schedule_data.append(courses)
	return schedule_data

def saturday(worksheet):
	schedule_data = list()
	schedule_data.append(worksheet['AR61'].value)
	schedule_data.append(worksheet['AS61'].value)
	schedule_data.append(worksheet['AV61'].value)
	schedule_data.append(worksheet['AY61'].value)
	schedule_data.append(worksheet['AR62'].value)
	schedule_data.append(worksheet['AS62'].value)
	schedule_data.append(worksheet['AV62'].value)
	schedule_data.append(worksheet['AY62'].value)
	schedule_data.append(worksheet['AR63'].value)
	schedule_data.append(worksheet['AS63'].value)
	schedule_data.append(worksheet['AV63'].value)
	schedule_data.append(worksheet['AY63'].value)
	schedule_data.append(worksheet['AR64'].value)
	schedule_data.append(worksheet['AS64'].value)
	schedule_data.append(worksheet['AV64'].value)
	schedule_data.append(worksheet['AY64'].value)
	schedule_data.append(worksheet['AR65'].value)
	schedule_data.append(worksheet['AS65'].value)
	schedule_data.append(worksheet['AV65'].value)
	schedule_data.append(worksheet['AY65'].value)	

	schedule_data.append(worksheet['X61'].value)
	schedule_data.append(worksheet['Y61'].value)
	schedule_data.append(worksheet['AB61'].value)
	schedule_data.append(worksheet['AE61'].value)
	schedule_data.append(worksheet['X62'].value)
	schedule_data.append(worksheet['Y62'].value)
	schedule_data.append(worksheet['AB62'].value)
	schedule_data.append(worksheet['AE62'].value)
	schedule_data.append(worksheet['X63'].value)
	schedule_data.append(worksheet['Y63'].value)
	schedule_data.append(worksheet['AB63'].value)
	schedule_data.append(worksheet['AE63'].value)
	schedule_data.append(worksheet['X64'].value)
	schedule_data.append(worksheet['Y64'].value)
	schedule_data.append(worksheet['AB64'].value)
	schedule_data.append(worksheet['AE64'].value)
	schedule_data.append(worksheet['X65'].value)
	schedule_data.append(worksheet['Y65'].value)
	schedule_data.append(worksheet['AB65'].value)
	schedule_data.append(worksheet['AE65'].value)				

	schedule_data.append(worksheet['X68'].value)
	schedule_data.append(worksheet['Y68'].value)
	schedule_data.append(worksheet['AB68'].value)
	schedule_data.append(worksheet['AE68'].value)
	schedule_data.append(worksheet['X69'].value)
	schedule_data.append(worksheet['Y69'].value)
	schedule_data.append(worksheet['AB69'].value)
	schedule_data.append(worksheet['AE69'].value)
	schedule_data.append(worksheet['X70'].value)
	schedule_data.append(worksheet['Y70'].value)
	schedule_data.append(worksheet['AB70'].value)
	schedule_data.append(worksheet['AE70'].value)
	schedule_data.append(worksheet['X71'].value)
	schedule_data.append(worksheet['Y71'].value)
	schedule_data.append(worksheet['AB71'].value)
	schedule_data.append(worksheet['AE71'].value)
	schedule_data.append(worksheet['X72'].value)
	schedule_data.append(worksheet['Y72'].value)
	schedule_data.append(worksheet['AB72'].value)
	schedule_data.append(worksheet['AE72'].value) 

	schedule_data.append(worksheet['X75'].value)
	schedule_data.append(worksheet['Y75'].value)
	schedule_data.append(worksheet['AB75'].value)
	schedule_data.append(worksheet['AE75'].value)
	schedule_data.append(worksheet['X76'].value)
	schedule_data.append(worksheet['Y76'].value)
	schedule_data.append(worksheet['AB76'].value)
	schedule_data.append(worksheet['AE76'].value)
	schedule_data.append(worksheet['X77'].value)
	schedule_data.append(worksheet['Y77'].value)
	schedule_data.append(worksheet['AB77'].value)
	schedule_data.append(worksheet['AE77'].value)
	schedule_data.append(worksheet['X78'].value)
	schedule_data.append(worksheet['Y78'].value)
	schedule_data.append(worksheet['AB78'].value)
	schedule_data.append(worksheet['AE78'].value)
	schedule_data.append(worksheet['X79'].value)
	schedule_data.append(worksheet['Y79'].value)
	schedule_data.append(worksheet['AB79'].value)
	schedule_data.append(worksheet['AE79'].value)

	schedule_data.append(worksheet['X82'].value)
	schedule_data.append(worksheet['Y82'].value)
	schedule_data.append(worksheet['AB82'].value)
	schedule_data.append(worksheet['AE82'].value)
	schedule_data.append(worksheet['X83'].value)
	schedule_data.append(worksheet['Y83'].value)
	schedule_data.append(worksheet['AB83'].value)
	schedule_data.append(worksheet['AE83'].value)
	schedule_data.append(worksheet['X84'].value)
	schedule_data.append(worksheet['Y84'].value)
	schedule_data.append(worksheet['AB84'].value)
	schedule_data.append(worksheet['AE84'].value)
	schedule_data.append(worksheet['X85'].value)
	schedule_data.append(worksheet['Y85'].value)
	schedule_data.append(worksheet['AB85'].value)
	schedule_data.append(worksheet['AE85'].value)
	schedule_data.append(worksheet['X86'].value)
	schedule_data.append(worksheet['Y86'].value)
	schedule_data.append(worksheet['AB86'].value)
	schedule_data.append(worksheet['AE86'].value) 	 	 

	schedule_data.append(worksheet['X89'].value)
	schedule_data.append(worksheet['Y89'].value)
	schedule_data.append(worksheet['AB89'].value)
	schedule_data.append(worksheet['AE89'].value)
	schedule_data.append(worksheet['X90'].value)
	schedule_data.append(worksheet['Y90'].value)
	schedule_data.append(worksheet['AB90'].value)
	schedule_data.append(worksheet['AE90'].value)
	schedule_data.append(worksheet['X91'].value)
	schedule_data.append(worksheet['Y91'].value)
	schedule_data.append(worksheet['AB91'].value)
	schedule_data.append(worksheet['AE91'].value)
	schedule_data.append(worksheet['X92'].value)
	schedule_data.append(worksheet['Y92'].value)
	schedule_data.append(worksheet['AB92'].value)
	schedule_data.append(worksheet['AE92'].value)
	schedule_data.append(worksheet['X93'].value)
	schedule_data.append(worksheet['Y93'].value)
	schedule_data.append(worksheet['AB93'].value)
	schedule_data.append(worksheet['AE93'].value) 

	schedule_data.append(worksheet['X96'].value)
	schedule_data.append(worksheet['Y96'].value)
	schedule_data.append(worksheet['AB96'].value)
	schedule_data.append(worksheet['AE96'].value)
	schedule_data.append(worksheet['X97'].value)
	schedule_data.append(worksheet['Y97'].value)
	schedule_data.append(worksheet['AB97'].value)
	schedule_data.append(worksheet['AE97'].value)
	schedule_data.append(worksheet['X98'].value)
	schedule_data.append(worksheet['Y98'].value)
	schedule_data.append(worksheet['AB98'].value)
	schedule_data.append(worksheet['AE98'].value)
	schedule_data.append(worksheet['X99'].value)
	schedule_data.append(worksheet['Y99'].value)
	schedule_data.append(worksheet['AB99'].value)
	schedule_data.append(worksheet['AE99'].value)
	schedule_data.append(worksheet['X100'].value)
	schedule_data.append(worksheet['Y100'].value)
	schedule_data.append(worksheet['AB100'].value)
	schedule_data.append(worksheet['AE100'].value) 

	schedule_data.append(worksheet['X103'].value)
	schedule_data.append(worksheet['Y103'].value)
	schedule_data.append(worksheet['AB103'].value)
	schedule_data.append(worksheet['AE103'].value)
	schedule_data.append(worksheet['X104'].value)
	schedule_data.append(worksheet['Y104'].value)
	schedule_data.append(worksheet['AB104'].value)
	schedule_data.append(worksheet['AE104'].value)
	schedule_data.append(worksheet['X105'].value)
	schedule_data.append(worksheet['Y105'].value)
	schedule_data.append(worksheet['AB105'].value)
	schedule_data.append(worksheet['AE105'].value)
	schedule_data.append(worksheet['X106'].value)
	schedule_data.append(worksheet['Y106'].value)
	schedule_data.append(worksheet['AB106'].value)
	schedule_data.append(worksheet['AE106'].value)
	schedule_data.append(worksheet['X107'].value)
	schedule_data.append(worksheet['Y107'].value)
	schedule_data.append(worksheet['AB107'].value)
	schedule_data.append(worksheet['AE107'].value)

	schedule_data.append(worksheet['X110'].value)
	schedule_data.append(worksheet['Y110'].value)
	schedule_data.append(worksheet['AB110'].value)
	schedule_data.append(worksheet['AE110'].value)
	schedule_data.append(worksheet['X111'].value)
	schedule_data.append(worksheet['Y111'].value)
	schedule_data.append(worksheet['AB111'].value)
	schedule_data.append(worksheet['AE111'].value)
	schedule_data.append(worksheet['X112'].value)
	schedule_data.append(worksheet['Y112'].value)
	schedule_data.append(worksheet['AB112'].value)
	schedule_data.append(worksheet['AE112'].value)
	schedule_data.append(worksheet['X113'].value)
	schedule_data.append(worksheet['Y113'].value)
	schedule_data.append(worksheet['AB113'].value)
	schedule_data.append(worksheet['AE113'].value)
	schedule_data.append(worksheet['X114'].value)
	schedule_data.append(worksheet['Y114'].value)
	schedule_data.append(worksheet['AB114'].value)
	schedule_data.append(worksheet['AE114'].value)			
	return schedule_data			
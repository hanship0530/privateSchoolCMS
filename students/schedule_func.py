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
		cell_time = 'B'+str(i)
		courses['time'] = '수업시간: '+ws[cell_time].value
		courses['lessons'] = schedule
		schedule_data.append(courses)
	return schedule_data

def tuseday(filepath, sheetName, day):
	schedule_data = list()
	wb = openpyxl.load_workbook(filepath)
	ws = wb[sheetName]
	# i are number of class
	# k is every 5 class detail
	for i in range(10,49,7):
		schedule = list()
		for k in range(i,i+7):
			data = dict()
			cell_number = 'X'+str(k)
			cell_name = 'Y'+str(k)
			cell_grade = 'AB'+str(k)
			cell_memo = 'AE'+str(k)
			data['number'] = ws[cell_number].value
			data['name'] = ws[cell_name].value
			data['grade'] = ws[cell_grade].value
			data['memo'] = ws[cell_memo].value
			data['cellInfo'] = cell_number+"/"+cell_name+"/"+cell_grade+"/"+cell_memo
			data['sheet'] = sheetName
			data['day'] = day
			schedule.append(data)

		courses = dict()
		cell_time = 'B'+str(i)
		courses['time'] = '수업시간: '+ws[cell_time].value
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
		cell_time = 'B'+str(i)
		courses['time'] = '수업시간: '+ws[cell_time].value
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
		cell_time = 'B'+str(i)
		courses['time'] = '수업시간: '+ws[cell_time].value
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
		cell_time = 'B'+str(i)
		courses['time'] = '수업시간: '+ws[cell_time].value
		courses['lessons'] = schedule
		schedule_data.append(courses)
	return schedule_data

def saturday(filepath, sheetName, day):
	schedule_data = list()
	wb = openpyxl.load_workbook(filepath)
	ws = wb[sheetName]
	# i are number of class
	# k is every 5 class detail
	for i in range(61,114,7):
		schedule = list()
		for k in range(i,i+7):
			data = dict()
			cell_number = 'X'+str(k)
			cell_name = 'Y'+str(k)
			cell_grade = 'AB'+str(k)
			cell_memo = 'AE'+str(k)
			data['number'] = ws[cell_number].value
			data['name'] = ws[cell_name].value
			data['grade'] = ws[cell_grade].value
			data['memo'] = ws[cell_memo].value
			data['cellInfo'] = cell_number+"/"+cell_name+"/"+cell_grade+"/"+cell_memo
			data['sheet'] = sheetName
			data['day'] = day
			schedule.append(data)

		courses = dict()
		cell_time = 'B'+str(i)
		courses['time'] = '수업시간: '+ws[cell_time].value
		courses['lessons'] = schedule
		schedule_data.append(courses)
	return schedule_data

def sunday(filepath, sheetName, day):
	schedule_data = list()
	wb = openpyxl.load_workbook(filepath)
	ws = wb[sheetName]
	# i are number of class
	# k is every 5 class detail
	for i in range(61,114,7):
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
		cell_time = 'B'+str(i)
		courses['time'] = '수업시간: '+ws[cell_time].value
		courses['lessons'] = schedule
		schedule_data.append(courses)
	return schedule_data
			
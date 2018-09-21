import win32com.client, pythoncom, os, openpyxl

def create_excelsheet(filepath):
	pythoncom.CoInitialize()
	excel = win32com.client.DispatchEx('Excel.Application')
	workbook = excel.Workbooks.Open(r+filepath)
	excel.Visible = False
	excel.DisplayAlerts = False

	copiedsheet = workbook.Worksheets("main")
	worksheet = workbook.Worksheets.Add()
	worksheet.Name = datetime.datetime.now()
	copiedsheet.Range("A1:AF100").Copy(workbook.Range("A1:AF100"))
	workbook.Save()
	workbook.Close(True)
	excel.Application.Quit()

def update_excelsheet(filepath, sheetName, data, cells):
	# naming completed
	pythoncom.CoInitialize()
	excel = win32com.client.DispatchEx('Excel.Application')
	workbook = excel.Workbooks.Open(os.path.join(os.getcwd(), filepath))
	excel.Visible = False
	excel.DisplayAlerts = False
	worksheet = workbook.Worksheets(sheetName)

	worksheet.Range(cells[1]).Value = data['date']
	worksheet.Range(cells[2]).Value = data['content']
	worksheet.Range(cells[3]).Value = data['completed']
	worksheet.Range(cells[4]).Value = data['memo']

	workbook.Save()
	workbook.Close(True)
	excel.Application.Quit()


# read excel through openpyxl
def display_excelsheet(filepath, sheetName):
	# naming completed
	excelData = []
	wb = openpyxl.load_workbook(filepath)
	ws = wb[sheetName]

	for i in range(14,37,2):
		data = dict()
		cell_number = 'A'+str(i)
		cell_date = 'B'+str(i)
		cell_content = 'C'+str(i)
		cell_completed = 'G'+str(i)
		cell_memo = 'H'+str(i)
		data['number'] = ws[cell_number].value
		data['date'] = ws[cell_date].value
		data['content'] = ws[cell_content].value
		data['completed'] = ws[cell_completed].value
		data['memo'] = ws[cell_memo].value
		data['cells'] = cell_number+'/'+cell_date+'/'+cell_content+'/'+cell_completed+'/'+cell_memo
		data['sheetName'] = sheetName
		data['stNumber'] = ws['C9'].value
		# data = {'filepath' : filepath}
		excelData.append(data)
	excelData.append(wb.sheetnames)
	return excelData
	


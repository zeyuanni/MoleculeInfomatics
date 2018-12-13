import xlwings as xw
import numpy as np

def nonEmptySize(sheet):
	return sheet.cells(65536, 1).end(xw.constants.Direction.xlUp).row, sheet.cells(1, 16384).end(xw.constants.Direction.xlToLeft).column

def readSheet(sheet):
	nrow, ncol = nonEmptySize(sheet)
	content = np.asarray(sheet.range((1,1),(nrow,ncol)).value)
	header = type(sheet.range("A1").value) is str
	if header:
		keys = content[0,:]
		return keys, content[1:,:]
	else:
		print("Warning: sheet '{}' does not contain headers".format(sheet.name))
		return ["Column{}".format(i) for i in range(content.shape[0])], content

def readBook(filepath):
	content = xw.Book(filepath)	
	# now only read the first sheet
	return readSheet(content.sheets[0])
	# future for multiple sheets. but the logic is unclear with many sheets
	for sheet in content.sheets:
		_keys, _data = readSheet(sheet)

if __name__ == '__main__':
	content = xw.Book(r"C:\Work\MI\Database\Molecule_MO.xlsx")
	keys, data = readSheet(content.sheets[0])
	print(keys,data)
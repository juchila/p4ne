from openpyxl import load_workbook
from matplotlib import pyplot
wb = load_workbook('data_analysis_lab.xlsx')
sheet = wb['Data']

sheet['A'][1:]

def getvalue(x): return x.value


m1 = map(getvalue, sheet['A'][1:])
m2 = map(getvalue, sheet['B'][1:])
list_x = list(m1)
list_y = list(m2)
pyplot.plot(list_x, list_y, label="Метка")
pyplot.show()

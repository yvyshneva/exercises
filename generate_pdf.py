from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet

report = SimpleDocTemplate("/tmp/report.pdf")

styles = getSampleStyleSheet()

report_title = Paragraph("A Complete Inventory of My Fruit", styles["h1"])
report.build([report_title])

############# DATA ################
fruit = {
  "elderberries": 1,
  "figs": 1,
  "apples": 2,
  "durians": 3,
  "bananas": 5,
  "cherries": 8,
  "grapes": 13
}
table_data = []
for k, v in fruit.items():
  table_data.append([k, v])
  
report_table = Table(data=table_data)
report.build([report_title, report_table])

############ TABLE ###################
from reportlab.lib import colors

table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]
report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
report.build([report_title, report_table])

############# GRAPHICS #################
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie

report_pie = Pie(width=3*inch, height=3*inch)

report_pie.data = []
report_pie.labels = []
for fruit_name in sorted(fruit):
  report_pie.data.append(fruit[fruit_name])
  report_pie.labels.append(fruit_name)

print(report_pie.data)
# [2, 5, 8, 3, 1, 1, 13]
print(report_pie.labels)
# ['apples', 'bananas', 'cherries', 'durians', 'elderberries', 'figs', 'grapes']

report_chart = Drawing()
report_chart.add(report_pie)

report.build([report_title, report_table, report_chart])

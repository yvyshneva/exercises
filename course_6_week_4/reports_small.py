#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors


def generate_report(filename, title, data):
  table_data = []
  for k, v in data.items():
    table_data.append([k, v])
  report_table = Table(data=table_data)
  styles = getSampleStyleSheet()
  report_title = Paragraph(title, styles["h1"])
  report.build([report_title, report_table])

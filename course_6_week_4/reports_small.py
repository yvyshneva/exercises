#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(filename, title, data):
  report = SimpleDocTemplate(filename)

  styles = getSampleStyleSheet()
  report_title = Paragraph(title, styles["h1"])
  report_body = Paragraph(data, styles['BodyText'])
  report.build([report_title, report_body])

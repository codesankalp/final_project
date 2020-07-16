#!/usr/bin/env python3
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from datetime import date
import glob
import os


def generate_report(attachment, title, paragraph):
	styles = getSampleStyleSheet()
	report = SimpleDocTemplate("{}".format(attachment))
	report_title = Paragraph(title,styles["h1"])
	nls = []
	for i in paragraph:
		name, weight = i
		report_endline = Paragraph("\n",styles["BodyText"])
		report_name = Paragraph(name,styles["BodyText"])
		report_weight =Paragraph(weight,styles["BodyText"])
		nls.append(report_endline)
		nls.append(report_name)
		nls.append(report_weight)
	# print(nls)
	final_ls = []
	final_ls.append(report_title)
	for i in nls:
		final_ls.append(i)
	print(final_ls)
	report.build(final_ls)

if  __name__ == "__main__":
	generate_report()

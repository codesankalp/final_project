#!/usr/bin/env python3
from datetime import date
import glob
import os
import reports
import emails

def mail():
  data = []
  report_title = "Processed Update on {}".format(date.today())
  for f in glob.glob(os.getcwd()+"/supplier-data/descriptions/*.txt"):
    ls = []
    for line in open(f):
        line = line.strip()
        ls.append(line)
    report_name = "name: {}".format(ls[0])
    report_weight = "weight: {}".format(ls[1])
    data.append([report_name,report_weight])
  return report_title,data

if __name__ == "__main__":
  report_title,data = mail()
  print(data)
  reports.generate_report("/tmp/processed.pdf", title=report_title, paragraph=data)
  message = emails.generate_email('automation@example.com','student-02-ed69dc9ae9d8@example.com','Upload Completed - Online Fruit Store','All fruits are uploaded to our website successfully. A detailed list is attached to this email','/tmp/processed.pdf')
  emails.send_email(message)

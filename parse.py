import matplotlib.pyplot as plt
import csv
import os
from pdf_parser import get_data_from_pdf
from pdf_parser import get_details

def parse(export=None):
  if export:
    if export == 'csv':
      with open('result.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
        fieldnames = ['name', 'gpa']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for x in os.listdir(path=r'.{}pdfs'.format(os.sep)):
          try:
            writer.writerow(get_details(get_data_from_pdf(x)))
          except IndexError:
            print ('Index out of range')
          except ValueError:
            print ('Value error')
  else:
      gpas = []
      for x in os.listdir(path=r'.{}pdfs'.format(os.sep)):
        try:
          gpas.append(float(get_details(get_data_from_pdf(x))['gpa']))
        except IndexError:
          print ('Index out of range')
        except ValueError:
          print ('Value error')
      gpas.sort(reverse=True)
      plt.figure(figsize=(10,5))
      x = range(1, len(gpas)+1)
      plt.plot(x, gpas, 'r--')
      plt.savefig('result.jpg')

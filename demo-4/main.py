import csv

def hitung_karyawan(input_file, output_file):
  """
  Fungsi untuk menghitung jumlah karyawan per perusahaan.

  Args:
    input_file: Path ke file CSV input (misalnya: 'input.csv').
    output_file: Path ke file CSV output (misalnya: 'output.csv').
  """
  company_counts = {}
  with open(input_file, 'r', newline='') as infile:
    reader = csv.reader(infile)
    next(reader)  # Skip header row
    for row in reader:
      company = row[2]
      if company in company_counts:
        company_counts[company] += 1
      else:
        company_counts[company] = 1

  with open(output_file, 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['Company', 'Employee Count'])  # Tulis header
    for company, count in company_counts.items():
      writer.writerow([company, count])

# Jalankan fungsi
hitung_karyawan('input.csv', 'output.csv')

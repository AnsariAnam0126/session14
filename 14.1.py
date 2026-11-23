# 14 task //1
# f = open("upi_log.txt", "w", encoding="utf-8")
# f.write("TXN1,10/11/2026,Chaiwala,50,SUCCESS\n")
# f.write("TXN2,10/11/2026,Zomato,250,SUCCESS\n")
# f.write("TXN3,11/11/2026,Swiggy,300,FAILED\n")
# f.write("TXN4,11/11/2026,Metro,40,SUCCESS\n")
# f.write("TXN5,12/11/2026,Amazon,500,SUCCESS\n")
# f.write("TXN6,12/11/2026,Chaiwala,30,SUCCESS\n")
# f.write("TXN7,13/11/2026,Flipkart,700,FAILED\n")
# f.write("TXN8,13/11/2026,Zomato,150,SUCCESS\n")
# f.write("TXN9,14/11/2026,Uber,120,SUCCESS\n")
# f.write("TXN10,14/11/2026,Amazon,200,SUCCESS\n")
# f.close()

# f = open("upi_log.txt", "a", encoding="utf-8")
# f.write("TXN11,15/11/2026,Swiggy,400,SUCCESS\n")
# f.write("TXN12,15/11/2026,Uber,180,SUCCESS\n")
# f.close()

# with open("upi_log.txt", "r", encoding="utf-8") as f:
#   lines = f.readlines()
#   print("Total lines:", len(lines))
# PS C:\Users\ANSARI ANAM\AppData\Local\Programs\Microsoft VS Code> & 'C:\Program Files\Python314\python.exe' '"c:/tops/session 1/14.1.py"'
# Total lines: 12

#14.2 //task 2
# import csv

# header = ["txn_id", "date", "payee", "amount_inr", "status"]
# rows = [
#     ["TXN1001", "10/11/2026", "Chai Point", 45.0, "SUCCESS"],
#     ["TXN1002", "10/11/2026", "Swiggy Instamart", 320.5, "SUCCESS"],
#     ["TXN1003", "11/11/2026", "Metro Card Recharge", 200.0, "FAILED"],
#     ["TXN1004", "11/11/2026", "Zomato", 480.0, "SUCCESS"],
#     ["TXN1005", "12/11/2026", "Airtel Prepaid", 299.0, "SUCCESS"],
#     ["TXN1006", "12/11/2026", "Apollo Pharmacy", 150.75, "SUCCESS"],
#     ["TXN1007", "13/11/2026", "BookMyShow", 650.0, "FAILED"],
#     ["TXN1008", "13/11/2026", "Chai Point", 60.0, "SUCCESS"],
#     ["TXN1009", "14/11/2026", "Uber India", 185.0, "SUCCESS"],
#     ["TXN1010", "14/11/2026", "Zomato", 310.0, "SUCCESS"],
#     ["TXN1011", "15/11/2026", "Swiggy Instamart", 540.0, "SUCCESS"],
#     ["TXN1012", "15/11/2026", "Metro Card Recharge", 200.0, "SUCCESS"],
# ]


# with open("upi_payments.csv", "w", newline="", encoding="utf-8") as file:
#   writer = csv.writer(file)
#   writer.writerow(header)
#   writer.writerows(rows)

# total_success_amount = 0.0

# with open("upi_payments.csv", "r", encoding="utf-8") as file:
#   reader = csv.DictReader(file)
#   for row in reader:
#     if row["status"] == "SUCCESS":
#       total_success_amount += float(row["amount_inr"])

# print("Total amount_inr for SUCCESS rows:", total_success_amount)

# Total amount_inr for SUCCESS rows: 2590.25
# PS C:\Users\ANSARI ANAM\AppData\Local\Programs\Microsoft VS Code>

#14.3 task //3
# import csv
# import json

# payee_summary = {}

# with open("upi_payments.csv", "r", encoding="utf-8") as file:
#   reader = csv.DictReader(file)
#   for row in reader:
#     if row["status"] == "SUCCESS":
#       payee = row["payee"]
#       amount = float(row["amount_inr"])
      
#       payee_summary[payee] = payee_summary.get(payee, 0.0) + amount

# with open("payee_summary.json", "w", encoding="utf-8") as file:
#   json.dump(payee_summary, file, indent=2)


# with open("payee_summary.json", "r", encoding="utf-8") as file:
#   loaded_summary = json.load(file)

# top_payee = max(loaded_summary, key=loaded_summary.get)
# print(
#     f"Payee with highest total: {top_payee} (INR {loaded_summary[top_payee]})"
# )
# Payee with highest total: Swiggy Instamart (INR 860.5)
# PS C:\Users\ANSARI ANAM\AppData\Local\Programs\Microsoft VS Code> 

from pathlib import Path


output_dir = Path("upi_output")
output_dir.mkdir(exist_ok=True)


files_to_copy = ["upi_log.txt", "upi_payments.csv", "payee_summary.json"]

for filename in files_to_copy:
  source_path = Path(filename)
  dest_path = output_dir / filename
  
  dest_path.write_text(
      source_path.read_text(encoding="utf-8"), encoding="utf-8"
  )


print("--- File Checks inside upi_output ---")
for filename in files_to_copy:
  file_path = output_dir / filename
  exists = file_path.exists()
  size = file_path.stat().st_size
  print(f"{file_path}: Exists = {exists}, Size = {size} bytes")

# 4. List all CSV files in 'upi_output' using glob('*.csv')
csv_files = list(output_dir.glob("*.csv"))
print("\nCSV files found in upi_output:", [f.name for f in csv_files])

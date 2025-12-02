import csv

file="E:\\python\\Scores.csv"
data = [("Hanzlla",185),("Muneeb",199),("Awais",167)]

#Writing a csv file
writer = csv.writer(open(file,"w", newline=''))
for row in data:
    writer.writerow(row)

#reading a csv file
reader = csv.reader(open(file,"r"))
for row in reader:
    print(row)
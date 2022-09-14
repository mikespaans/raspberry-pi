import csv

# link van de dataset
# http://archive.ics.uci.edu/ml/datasets/Gas+sensors+for+home+activity+monitoring
# dataset .dat omzetten naar .csv-formaat

with open("/home/mike/Downloads/JSON/HT_Sensor_dataset.dat") as dat_file, open("file.csv", "w") as csv_file:
    csv_writer = csv.writer(csv_file)


    for line in dat_file:
        row = [field.strip() for field in line.split(" ")]
        if len(row) == 13:
            csv_writer.writerow(row)


print ("omzetting naar file.csv is gereed")
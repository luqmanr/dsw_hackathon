import csv

type_dict = {
    "ROAD_CLOSED_EVENT":1,
    "JAM_HEAVY_TRAFFIC":2,
    "HAZARD_ON_ROAD_POT_HOLE":3
}

new_csv = []
with open("./data/alerts.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for index,row in enumerate(csv_reader):
        if index == 0:
            row.insert(14, "type_num")
            new_csv.append(row)
        subtype = row[13]
        if subtype in type_dict:
            row.insert(14, type_dict[subtype])
            new_csv.append(row)

with open("./data/output_test.csv", mode="w") as csv_output:
    csv_writer = csv.writer(csv_output, delimiter=",")
    for row in new_csv:
        csv_writer.writerow(row)

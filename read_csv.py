import csv

with open("./data/from_ato/test_none.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row_index,row in enumerate(csv_reader):
        print(row)
        # if row_index == 0:
        #     row.insert(14, "type_num")
        #     # for col_index,header in enumerate(row):
        #     #     print("%s = %s" % (col_index, header))
        # if row[19] == None:
        #     print("ADA YANG NULL NIH DI ROW = ", row_index)
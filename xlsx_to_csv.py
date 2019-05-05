#!/usr/bin/env python3
import csv

import xlrd


def read_excel(source, target):
    l = []
    # 打开文件
    workbook = xlrd.open_workbook(source)

    sheet = workbook.sheet_by_index(0)

    r = sheet.get_rows()
    for row in r:
        r = []
        for c in row:
            r.append(c.value)
        l.append(r)
    write_to_csv(target, l)


def write_to_csv(filename, rows):
    print("--------write_to_csv---------")
    with open(filename, 'w+', newline='')as f:
        csv_write = csv.writer(f, dialect='excel', delimiter="|")
        csv_write.writerows(rows)


if __name__ == '__main__':
    read_excel('Shop.xlsx', "abc.csv")
    print("f**k finish")

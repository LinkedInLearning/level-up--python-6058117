import csv

def merge_csv(csv_list, output_path):
    # 构建包含所有字段名的列表
    fieldnames = []
    for file in csv_list:
        with open(file, 'r', encoding='utf-8') as input_csv:
            field = csv.DictReader(input_csv).fieldnames
            fieldnames.extend(f for f in field if f not in fieldnames)

    # 根据字段名将数据写入输出文件
    with open(output_path, 'w', encoding='utf-8', newline='') as output_csv:
        writer = csv.DictWriter(output_csv, fieldnames=fieldnames)
        writer.writeheader()
        for file in csv_list:
            with open(file, 'r', encoding='utf-8') as input_csv:
                reader = csv.DictReader(input_csv)
                for row in reader:
                    writer.writerow(row)


# 解决方案视频中使用的命令，仅供参考
# if __name__ == '__main__':
#     merge_csv(['class1.csv', 'class2.csv'], 'all_students.csv')


# -*- coding:utf-8 -*-
# __author__ = majing

table_name = 'sql_metrics'
sql = 'insert into sql_metrics(table_id, metric_name,verbose_name,metric_type,expression,description,created_by_fk) ' \
      'VALUES (%s, "total_entry","COUNT(*)", "count", "COUNT(*)", "查询表中数据总条数专用字段，勿删,勿改",203);'

file_name = 'tab_id'
def get_table_id(file_name):
    data = []
    with open(file_name) as f:
        for line in f.readlines():
            data.append(int(line.strip()))
    print("total table: %s" % len(data))
    return data


def write_data(file_name):
    data = get_table_id(file_name)
    file = open('data.sql', 'w+')
    count = 0
    for table_id in data:
        file.write(sql % table_id + '\n')
        count += 1

    file.write("################# total %s" % count)

if __name__ == "__main__":
    write_data(file_name)

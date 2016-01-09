# -*- coding:utf-8 -*-
"""
Id: 0
ASIN: 0771044445
discontinued product

Id: 1
ASIN: 0827229534
title: Patterns of Preaching: A Sermon Sampler
group: Book
salesrank: 396585
similar: 5 0804215715 156101074X 0687023955 0687074231 082721619X
categories: 2
|Books[283155]|Subjects[1000]|Religion & Spirituality[22]|Christianity[12290]|Clergy[12360]|Preaching[12368]
|Books[283155]|Subjects[1000]|Religion & Spirituality[22]|Christianity[12290]|Clergy[12360]|Sermons[12370]
reviews: total: 2 downloaded: 2 avg rating: 5
2000-7-28 cutomer: A2JW67OY8U6HHK rating: 5 votes: 10 helpful: 9
2003-12-14 cutomer: A2VE83MZF98ITY rating: 5 votes: 6 helpful: 5

Id: 2
ASIN: 0738700797
title: Candlemas: Feast of Flames
group: Book
salesrank: 168596
similar: 5 0738700827 1567184960 1567182836 0738700525 0738700940
categories: 2
|Books[283155]|Subjects[1000]|Religion & Spirituality[22]|Earth-Based Religions[12472]|Wicca[12484]
|Books[283155]|Subjects[1000]|Religion & Spirituality[22]|Earth-Based Religions[12472]|Witchcraft[12486]
reviews: total: 12 downloaded: 12 avg rating: 4.5
2001-12-16 cutomer: A11NCO6YTE4BTJ rating: 5 votes: 5 helpful: 4
2002-1-7 cutomer: A9CQ3PLRNIR83 rating: 4 votes: 5 helpful: 5
2002-1-24 cutomer: A13SG9ACZ9O5IM rating: 5 votes: 8 helpful: 8
2002-1-28 cutomer: A1BDAI6VEYMAZA rating: 5 votes: 4 helpful: 4
原数据格式如上，存在m.txt中，我想得到的格式如下：
Id: 1 cutomer: A2JW67OY8U6HHK rating: 5 votes: 10 helpful: 9
Id: 1 cutomer: A2VE83MZF98ITY rating: 5 votes: 6 helpful: 5
Id: 2 cutomer: A11NCO6YTE4BTJ rating: 5 votes: 5 helpful: 4
Id: 2 cutomer: A9CQ3PLRNIR83 rating: 4 votes: 5 helpful: 5
Id: 2 cutomer: A13SG9ACZ9O5IM rating: 5 votes: 8 helpful: 8
Id: 2 cutomer: A1BDAI6VEYMAZA rating: 5 votes: 4 helpful: 4
"""

file_info={}
count = 0
with open('test_1.txt') as f:
    for line in f:
        if line.startswith('Id'):
            file_keys = 'Id'+str(count)
            file_info[file_keys] = []
            count += 1
            continue
        if not line or line == '\n' or '|' in line:
            continue

        line_info = {}
        key, value = line.split(' ', 1)
        line_info[key] = value
        file_info[file_keys].append(line_info)

print "file_info:",file_info

res_info = {}
for keys,item_list in file_info.items():
    res_info[keys] = []
    for item in item_list:
        if item.keys()[0].startswith('20'):
            res_info[keys].append(item.values()[0])
print "res_info:",res_info


with open('m.txt','w') as fm:
    for key, values in res_info.items():
        for item in values:
            fm.write(key+'  '+ item)
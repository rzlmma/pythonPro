# -*- coding:utf-8 -*-
# __author__ = majing
"""
处理文本文件
"""
data = [[u'BK_10300000245618',u'BKC_10300008036390',u'U5 Riding the Roller Coaster'],
        [u'BK_10300000336398',u'BKC_10300014237430',u'BKC_10300014238339',u'L19 Red, Green'],
        [u'BK_10300000339217',u'BKC_10300014461342',u'BKC_10300014465371',u'L14 Rice and Meat'],
        [u'BK_10300000361771',u'BKC_10300015758573',u'BKC_10300015769924',u'L10 Red, Yellow, Blue, Green'],
        [u'BK_10300000362178',u'BKC_10300015860468',u'BKC_10300015871643',u'L10 Rain and sun'],
        [u'BK_10300003116449',u'BKC_10300199715889',u'U3 Redrock Bay Sports Club'],
        [u'BK_10300000458145',u'BKC_10300021783015',u'U3 Restaurant'],
        [u'BK_10300002554542',u'BKC_10300133566932',u'M5 Relatives'],
        [u'BK_10300001807246',u'BKC_10300105893332',u'U2 Room'],
        [u'BK_10300000637070',u'BKC_10300033951930',u'U1 Remember the rules'],
        [u'BK_10300001693957',u'BKC_10300095343166',u'M2 Relationships'],
        [u'BK_10300003117229',u'BKC_10300199775472',u'M2 Relationships'],
        [u'BK_10300000741853',u'BKC_10300041293335',u'M2 Relationships'],
        [u'BK_10300000742898',u'BKC_10300041381445',u'M2 Relationships'],
        [u'BK_10300000763495',u'BKC_10300042326183',u'U4 Road safety'],
        [u'BK_10300002662503',u'BKC_10300141795745',u'BKC_10300141800215',u'U1 Rules in the park'],
        [u'BK_10300001708093',u'BKC_10300096442126',u'BKC_10300096449742',u'U2 Rules in fun places'],
        [u'BK_10300002664970',u'BKC_10300142118022',u'M1 Relationships'],
        [u'BK_10300001678757',u'BKC_10300094465122',u'M1 Relationships'],
        [u'BK_10300001678757',u'BKC_10300094508420',u'BKC_10300094509790',u'U7 Ricky learns a lesson'],
        [u'BK_10300002670235',u'BKC_10300142370208',u'M3 Relationships'],
        [u'BK_10300001683419',u'BKC_10300094725915',u'M2 Relationships'],
        [u'BK_10300001705822',u'BKC_10300096292152',u'M1 Relationships'],
        [u'BK_10300002671562',u'BKC_10300142890493',u'M3 Relationships'],
        [u'BK_10300002642592',u'BKC_10300139569384',u'U5 Reuse and recycle']
        ]

def parase_data(pdata):
    book_ids = [item[0] for item in pdata]
    module_ids = [item[1] for item in pdata]
    unit_ids = [item[2] for item in pdata if item[2].startswith("BKC")]

    print("book_ids: ", list(set(book_ids)))
    print("module_ids: ", list(set(module_ids)))
    print("unit_ids: ", list(set(unit_ids)))

if __name__ == "__main__":
    parase_data(data)

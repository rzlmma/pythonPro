# -*- coding:utf-8 -*-
# __author__ = majing

"""
合并多个execl
"""
import os
import sys
import pandas as pd
import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


# EXECL_DIRS = ["xueqian", "xiaoyu", "xiaoying", "xiaoshu"]
EXECL_DIRS = ["xueqian"]
EXECL_FIELS_MAP = {"xueqian": "学前包含图片的题目", "xiaoyu": "小语包含图片的题目",
                       "xiaoying": "小英包含图片的题目", "xiaoshu": "小数包含图片的题目"}


def combine_execl_files():
    """
    组合execl
    :return: 
    """
    def deal_url(val):
        if not val.startswith('"'):
            val = '"'+val+'"'
        return val

    for item in EXECL_DIRS:
        dfs = []
        print("begin to deal %s" % item)
        start_time = datetime.datetime.now()
        path_dir = os.path.join(BASE_DIR, 'tools/%s/'% item)
        files = os.listdir(path_dir)
        for file in files:
            file_path = os.path.join(path_dir, file)
            if '.DS_Store' in file_path:
                continue
            try:
                df = pd.read_excel(file_path)
                if not df.empty:
                    df['图片url'] = df['图片url'].apply(deal_url)
                    dfs.append(df)
            except Exception as exc:
                print("error file_path: %s     error:%s" % (file_path, str(exc)))

        print("total df number: %s" % len(dfs))
        new_df = pd.concat(dfs, ignore_index=True)

        data = new_df['题目ID']
        print("item:%s   before count:%s" % (item, len(data)))

        data = data.drop_duplicates()
        print("item:%s    count:%s" % (item, len(data)))


        # new_df = new_df.sort_values(by=['图片url'])
        # print("total rows: %s   total cost time:%s " % (len(new_df), datetime.datetime.now()-start_time))
        #
        # df_cnt = len(new_df)
        # step = 500000
        # numbers = int(df_cnt/step) + 1
        # for i in range(1, numbers+1):
        #     start_time_2 = datetime.datetime.now()
        #     start = (i-1) * step
        #     end = i * step
        #     print("start:%s   end:%s " % (start, end))
        #     sub_df = new_df[start:end]
        #     a_file_name = os.path.join(BASE_DIR, 'tools/%s_%s.xlsx' % (EXECL_FIELS_MAP.get(item), i))
        #     sub_df.to_excel(a_file_name, index=False, encoding='utf8')
        #     print("write data to excel success !!!   cost time: %s" % (datetime.datetime.now() - start_time_2))


if __name__ == "__main__":
    combine_execl_files()
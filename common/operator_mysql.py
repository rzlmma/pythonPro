# -*- coding:utf-8 -*-
# __author__ = majing
"""
操作mysql
"""
import os
import logging
import MySQLdb
import copy
from logging import FileHandler

LOG_FORMATTER = logging.Formatter('%(asctime)s  %(filename)s : %(levelname)s [%(funcName)s]:%(lineno)s  %(message)s')
APS_LOG_FILE = os.path.join(os.getcwd(), 'contab.log')
logger = logging.getLogger('contab')
logger.setLevel('INFO')
handler = FileHandler(APS_LOG_FILE)
handler.setFormatter(LOG_FORMATTER)
logger.addHandler(handler)

DB_MAPS = {"tsm_operator": ['ins_id', 'tsm_email_account', 'tsm_own_department', 'tsm_own_zones', 'tsm_own_branch_office',
            'tsm_post_rank'],
           "operator": ['email_account', 'own_department', 'own_zones', 'own_branch_office', 'post_rank', 'post_name'],

           # 远程表
           'bi_tsm_ins_index':['ins_id', 'tsm_email_account', 'tsm_own_department', 'tsm_own_zones',
                                   'tsm_own_branch_office', 'tsm_post_rank'],
           'tmp_customer_success_organization':['email_account', 'own_department', 'own_zones', 'own_branch_office',
                                                 'post_rank', 'post_name']
           }

REMOTE_TAB = ['bi_tsm_ins_index', 'tmp_customer_success_organization']
LOCAL_TAB = ['tsm_operator', "operator"]


class RemoteDB:
    host = ''
    user = ''
    password = ''
    db = ''


class LocalDB:
    host = ''
    user = ''
    password = ''
    db = ''


class TestDB:
    host = '127.0.0.1'
    user = 'root'
    password = '123456'
    db = ''


class MysqlConn(object):
    def __init__(self, db_class):
        self.host = db_class.host
        self.user = db_class.user
        self.password = db_class.password
        self.db = db_class.db
        self.cursor = self.get_cursor()

    def connect(self):
        try:
            self.conn = MySQLdb.Connect(host=self.host, user=self.user, passwd=self.password, db=self.db)
        except Exception as exc:
            logging.error(str(exc))
            self.conn = None

    def get_cursor(self):
        self.connect()
        if self.conn:
            cursor = self.conn.cursor()
        else:
            cursor = None
        return cursor

    def get_query_sql(self, tab_name, cols):
        """
        获取读取数据的sql
        """
        p_str = ''
        last_field = cols.pop()
        for col in cols:
            p_str += '%s, ' % col

        p_str += '%s' % last_field
        sql = 'select %s from %s ;' % (p_str, tab_name)
        logger.info("获取读取数据的sql===> sql:%s\n" % sql)
        return sql

    def get_insert_sql(self, tab_name, cols):
        """
        获取读取数据的sql
        """
        p_str = ''
        val_str = ''
        last_field = cols.pop()
        for col in cols:
            p_str += '%s, ' % col
            val_str += '%s, '

        p_str += '%s' % last_field
        val_str += '%s '

        sql = 'insert into %s(%s) values(%s) ;' % (tab_name, p_str, val_str)
        logger.info("获取插入数据的sql===> sql:%s\n" % sql)
        return sql

    def truncate(self, tab_name):
        try:
            sql = 'truncate %s' % tab_name
            self.cursor.execute(sql)
        except Exception as exc:
            logger.error(str(exc))
        else:
            logger.info("truncate the table %s success!!!" % tab_name)

    def fetch_data(self, tab_name):
        """
        获取数据
        """
        try:
            fields = DB_MAPS.get(tab_name)
            sql = self.get_query_sql(tab_name, copy.copy(fields))
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            logger.info("表[%s] 共有 %s 条数据" % (tab_name, len(data)))
        except Exception as exc:
            data = []
            logger.error("表[%s]获取数据失败: %s" % (tab_name, str(exc)))
        else:
            logger.error("表[%s]获取数据成功！！！" % tab_name)
        return data

    def insert_data(self, tab_name, data):
        try:
            self.truncate(tab_name)

            fields = DB_MAPS.get(tab_name)
            sql = self.get_insert_sql(tab_name, fields)
            self.cursor.executemany(sql, data)
        except Exception as exc:
            logger.error("表[%s]插入数据失败：%s" % (tab_name, str(exc)))
        else:
            logger.info("表[%s]插入数据成功！！！！" % tab_name)

    def close(self):
        self.cursor.close()
        self.conn.commit()
        self.conn.close()



class SyncData(object):
    def __init__(self, remote_class, local_class):
        self.remote_class = remote_class
        self.local_class = local_class

    def sync_data_to_local(self):
        for re_tab, lo_tab in zip(REMOTE_TAB, LOCAL_TAB):
            logger.info("sync table: remote_table:%s   local_table:%s" % (re_tab, lo_tab))
            data = self.remote_class.fetch_data(re_tab)
            self.local_class.insert_data(lo_tab, data)
            logger.info("synce remote table [%s] to local table [%s] success !!!\n\n" % (re_tab, lo_tab))

        self.remote_class.close()

        self.local_class.close()


if __name__ == '__main__':
    remote_cls = MysqlConn(RemoteDB)
    local_cls = MysqlConn(TestDB)

    sy = SyncData(remote_cls, local_cls)
    sy.sync_data_to_local()

















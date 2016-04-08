# -*- coding: UTF-8 -*-
__author__ = 'xuwen'

from sqlalchemy import create_engine, MetaData, Table, Column
from sqlalchemy.orm import sessionmaker, mapper
from decimal import *
import relatedTime
from sqlalchemy.dialects.mysql import \
        BIGINT, BINARY, BIT, BLOB, BOOLEAN, CHAR, DATE, \
        DATETIME, DECIMAL, DECIMAL, DOUBLE, ENUM, FLOAT, INTEGER, \
        LONGBLOB, LONGTEXT, MEDIUMBLOB, MEDIUMINT, MEDIUMTEXT, NCHAR, \
        NUMERIC, NVARCHAR, REAL, SET, SMALLINT, TEXT, TIME, TIMESTAMP, \
        TINYBLOB, TINYINT, TINYTEXT, VARBINARY, VARCHAR, YEAR
import sys
import capp
import Data



def db_session():
    db_config = {
        'host': '10.10.13.39',
        'port':3306,
        'user': 'crm',
        'passwd': 'crm@2015',
        'db':'crm',
        'charset':'utf8'
        }
    engine = create_engine('mysql+pymysql://%s:%s@%s:%s/%s?charset=%s'%(db_config['user'],
                                                                        db_config['passwd'],
                                                                        db_config['host'],
                                                                        db_config['port'],
                                                                        db_config['db'],
                                                                        db_config['charset']), echo=True)
    DB_Session = sessionmaker(bind=engine)
    session = DB_Session()
    return session

# def db_session():
#     db_config = {
#         'host': '10.10.87.38',
#         'port':3306,
#         'user': 'crm',
#         'passwd': 'crm@2015',
#         'db':'crm',
#         'charset':'utf8'
#         }
#     engine = create_engine('mysql+pymysql://%s:%s@%s:%s/%s?charset=%s'%(db_config['user'],
#                                                                         db_config['passwd'],
#                                                                         db_config['host'],
#                                                                         db_config['port'],
#                                                                         db_config['db'],
#                                                                         db_config['charset']), echo=True)
#     DB_Session = sessionmaker(bind=engine)
#     session = DB_Session()
#     return session

#删除Capp用户
def delete_cuser(phone):
    session = db_session()
    cid = session.execute("select * from c_user where loginmobile = \'" + str(phone) + "\'").first().id
    session.execute("delete from c_self_stock where cid = " + str(cid))
    session.commit()
    session.execute("delete from c_user_belong_log where c_user_id = \'" + str(cid) + "\'")
    session.commit()
    session.execute("delete from portfolios where owner = 'imaster_" + str(cid) + "\'")
    session.commit()
    session.execute("delete from portfolio_comments where symbol in (select symbol from portfolios where owner = 'imaster_" + str(cid) + "\')")
    session.commit()
    session.execute("delete from portfolio_favourites where symbol in (select symbol from portfolios where owner = 'imaster_" + str(cid) + "\')")
    session.commit()
    session.execute("delete from portfolio_holdings where symbol in (select symbol from portfolios where owner = 'imaster_" + str(cid) + "\')")
    session.commit()
    session.execute("delete from portfolio_performance where symbol in (select symbol from portfolios where owner = 'imaster_" + str(cid) + "\')")
    session.commit()
    session.execute("delete from portfolio_rebalancings where symbol in (select symbol from portfolios where owner = 'imaster_" + str(cid) + "\')")
    session.commit()
    session.execute("delete from portfolio_reference where symbol in (select symbol from portfolios where owner = 'imaster_" + str(cid) + "\')")
    session.commit()
    session.execute("delete from rebalancings where symbol in (select symbol from portfolios where owner = 'imaster_" + str(cid) + "\')")
    session.commit()
    session.execute("delete from trade_fund_account where c_user_id = (select id from c_user where loginmobile = " + str(phone) + ")")
    session.commit()
    session.execute("delete from c_user where loginmobile = " + str(phone))
    session.commit()
    session.execute("delete from sd_customer where mobileno = " + str(phone))
    session.commit()
    session.close()

#获取Capp用户注册状态
def imaster_info(phone):
    session = db_session()
    result = session.execute("select * from c_user where loginmobile = '" + str(phone) + "\'").fetchall()
    return result

#添加Capp用户
def insert_cuser(phone):
    session = db_session()
    session.execute("delete from c_user where loginmobile = \'" + str(phone) + "\'")
    session.commit()
    session.execute("INSERT INTO c_user VALUES (NULL, '6b4f9f85012b304979c94" + str(phone) + "\', '2015-09-10 10:59:23', '34f85ca80ec353d3052b8a2d3973a0c5', '0', \'" + str(phone) + "\', '', '', '1', '1977-07-17', '', '', '投资大师" + str(phone) + "\', '401', '2015-09-14 10:45:38', '1', '0', '0', '1012', '河北省张家口市万全县孔家庄镇工业街南万兴小区0号楼1单元202室', '2015-09-14 10:45:38', '2015-10-29 17:20:32', '', '1', '', '1', '', '', '', '')")
    session.commit()
    cuser = session.execute("select * from c_user where loginmobile = " + str(phone)).first()
    if(cuser != None):
        session.execute("update c_user set client_id = 'imaster_" + str(cuser.id) + "\' where loginmobile = \'" + str(phone) + "\'")
        session.commit()
    session.execute("delete from sd_customer where fund_account = \'" + str(phone) + "\'")
    session.commit()
    session.execute("INSERT INTO sd_customer VALUES (NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '0811', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, \'" + str(phone) + "\', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, \'" + str(phone) + "\', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '0', NULL, NULL, NULL, NULL, NULL)")
    session.commit()
    cuser_id = session.execute("select * from c_user where loginmobile = \'" + str(phone) + "\'").first().id
    session.execute("delete from trade_fund_account where c_user_id = \'" + str(cuser_id) + "\' or cust_id = \'" + str(phone) + "\'")
    session.commit()
    session.execute("INSERT INTO trade_fund_account VALUES (NULL, \'" + str(cuser_id) + "\', \'" + str(phone) + "\', \'" + str(phone) + "\', '0.00015000', '0.00000', '投资大师" + str(phone) + "\', '', '2008-10-13', '2018-10-13', 'c', '43062419900818361X', '00', '156', '长沙市开福区四方坪红色渔业队1号', '401', '101963', 'visitsurvey', '0', '2015-08-21 18:18:36', '2015-09-21 07:01:04')")
    session.commit()
    session.close()


if __name__ == '__main__':
    delete_cuser(18001361256)
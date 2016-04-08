# -*- coding: UTF-8 -*-
__author__ = 'xuwen'

import urllib
import dataBase
import globalData
from pyexcel_xls import XLBook

#产品列表: 410627
def get_product():
    params = urllib.urlencode({
        'appType': '12',
        'appVer': 'V1.1.4.01',
        'custid': '81106500034',
        'deviceCode': 'e3e1f6db621de8052d6cce21e339f9c',
        'deviceType': 'IOS',
        'envType': '1',
        'fundid': '81106500034',
        'mobilephone': '13300000002',
    })
    response = urllib.urlopen("http://t.c.jzsec.com/loan/f410627",params).read()
    return response

#权限: 410332
def get_authorization():
    params = urllib.urlencode({
        "deviceCode": "e3e1f6db621de805f2d6cce21e339f9c",
        "appVer": "V1.1.4.01",
        "custid": "81106500034",
        "fundid": "81106500034",
        "deviceType": "IOS",
        "userId": "2",
        "trdpwd": "Nyozp83o9fsM3lYFf1HHduXsXAvNyw3mm6TrfVAIPIP1aW8X3vXvqT3u-aIev8jA7wyskDn1lqTf0QxkXngGPwG6sC1rY7xT3lMqVUGKdVMmnmSjx2iUJknOOzULPUuxc8NyM7XxZtXR-5UiJC1gspj7YzrN016V8YD3UYaj4X8",
        "token": "877ca3427255f226e360fa4e29b06700",
        "mobilephone": "13300000002",
        "appType": "12",
        "envType": "1"
    })
    response = urllib.urlopen("http://t.c.jzsec.com/loan/f410332",params).read()
    return response

#额度: 410624
def get_limit():
    params = urllib.urlencode({
        "deviceCode": "e3e1f6db621de805f2d6cce21e339f9c",
        "appVer": "V1.1.4.01",
        "custid": "81106500034",
        "fundid": "81106500034",
        "deviceType": "IOS",
        "userId": "2",
        "trdpwd": "ZtKJ5RJyjago-1z52kXs8dIwGLUYe90sKWjQsylROVZAGA6f9a39zcDXckbbcESEWIhzFwkcBFOBOmbHVt_moFk511aJX0myr_z9or90UoOz6KsxLD7lAIz6ayP-ByRdg1YxgCDyVNDIXI7T_fQx40UFbMlisFI7M_AHww44Ln8",
        "token": "877ca3427255f226e360fa4e29b06700",
        "mobilephone": "13300000002",
        "appType": "12",
        "envType": "1"
    })
    response = urllib.urlopen("http://t.c.jzsec.com/loan/f410624",params).read()
    return response


#质押合约: 410625
def get_contract():
    params = urllib.urlencode({
       	"deviceCode": "e3e1f6db621de805f2d6cce21e339f9c",
        "appVer": "V1.1.4.01",
        "custid": "81106500034",
        "fundid": "81106500034",
        "deviceType": "IOS",
        "userId": "2",
        "trdpwd": "HXCp87ChKFVsFgvWpzv-_SZq57cLZMZkqiZ6ON4BfJywXZrAxUz4RMvBVqbJLJA7AhZgB5Ytogsympo-_c4k3H5s72qXTD42pEMzxrxx63RNlKycFFgG41D5EV84x7HJJ-snqx2if9Tbn5UxhjgCD3UzFVnBFXWj0q2TwoMctuI",
        "token": "877ca3427255f226e360fa4e29b06700",
        "mobilephone": "13300000002",
        "appType": "12",
        "envType": "1"
    })
    response = urllib.urlopen("http://t.c.jzsec.com/loan/f410625", params).read()
    return response

#最大可贷金额查询: 410641
def get_number_limit():
    params = urllib.urlencode({
       	"mobilephone": "13300000003",
        "market": "0",
        "stkcode": "000004",
        "producttype": "1",
        "fundid": "81106500011",
        "appVer": "V1.1.4.01",
        "deviceType": "IOS",
        "appType": "12",
        "custid": "81106500011",
        "token": "e02b5568fc2df50458aa8ca9149019ac",
        "envType": "1",
        "secuid": "0059214898",
        "userId": "3",
        "orderqty": "10000000000",
        "trdpwd": "ekLRvde0RoDquKgnidUOQ97IM0iMacfaWSlh1jScsli-Zkq6Fkxz2bNcHpYn4R9hTX2b5gTQokf-EsQF41LtHtruDRk4IB1JA8fBp2vCSrIx77Rf_oOK_H4fZsiwmmjQgEVTOW_dLcwL-2uTzTjjkixkIHR_3bciXw2ys1G_0Qo",
        "ghdays": "366",
        "deviceCode": "e3e1f6db621de805f2d6cce21e339f9c"
    })
    response = urllib.urlopen("http://t.c.jzsec.com/loan/f410641", params).read()
    return response


#获取业务申请单: contracthistory
def get_contracthistory():
    params = urllib.urlencode({
        "mobilephone": "13300000003",
        "gpzysno": "201509090B3000010",
        "fundid": "81106500011",
        "appVer": "V1.1.4.01",
        "deviceType": "IOS",
        "custid": "81106500011",
        "userId": "3",
        "appType": "12",
        "envType": "1",
        "token": "e02b5568fc2df50458aa8ca9149019ac",
        "trdpwd": "nrQACXwBW7hNhEy1Sg2H5NlN7jNO2iE1bSzevhraq9yJneUi1D8PV7LFIflYBvMcg3S7qpr9vV-lb3j_LoSFpbloyss2DRLSvDrpI50iFdoVvLzI0IoVnWuQyK0clBOUpUalLMVOjm50bLTbXUNDEf5yWrArVSzPsp8p1Pn0wpk",
        "deviceCode": "e3e1f6db621de805f2d6cce21e339f9c"
    })
    response = urllib.urlopen("http://t.c.jzsec.com/loan/contracthistory", params).read()
    return response

#股票质押债务合约明细查询: 410626
def get_contract_details():
    params = urllib.urlencode({
        "mobilephone": "13300000003",
        "market": "0",
        "gpzysno": "201509090B3000004",
        "producttype": "0",
        "fundid": "81106500011",
        "appVer": "V1.1.4.01",
        "deviceType": "IOS",
        "appType": "12",
        "custid": "81106500011",
        "token": "e02b5568fc2df50458aa8ca9149019ac",
        "envType": "1",
        "userId": "3",
        "busikind": "1",
        "trdpwd": "Av1IxyI8MR_ugi0rWgK0njXaLie9Vb86qMiIM3erNfanrX_YAby5h7D80Ca_BMI8PNZlXqi8ClCgk9OrM-47lMkaJ1TFo4_XFs8zMoTbHHeAMGMIVhHMpqJN3IiPzGEhHCiXBtecTAFNtFj9j8W1FLkZKr78ygPw7huwfRo8ctA",
        "ghdays": "366",
        "deviceCode": "e3e1f6db621de805f2d6cce21e339f9c"
    })
    response = urllib.urlopen("http://t.c.jzsec.com/loan/f410626", params).read()
    return response


#金易贷可质押证券持仓查询: 410642
def get_keep_stock():
    params = urllib.urlencode({
        "deviceCode": "e3e1f6db621de805f2d6cce21e339f9c",
        "appVer": "V1.1.4.01",
        "custid": "81106500011",
        "fundid": "81106500011",
        "deviceType": "IOS",
        "userId": "3",
        "trdpwd": "cCNvNYrKeELPw-vfQEEgy9WTCar5oZrqw3rZ5Y1CUY6Ks0mB2uipQN4X34v7JuJ_57iuPfSsZfD1EMlg7Ri7GaV2LKULxCDxmEq6Ip3trHY6L1F-AzVjTGN_CqoHKC_f5PJnm8ysLfps2k4uFA5oHOVeezA7eOkrkA4LvWlwmO4",
        "token": "e02b5568fc2df50458aa8ca9149019ac",
        "mobilephone": "13300000003",
        "appType": "12",
        "envType": "1"
    })
    response = urllib.urlopen("http://t.c.jzsec.com/loan/f410642", params).read()
    return response


#股票质押: 410629
def pledge():
    params = urllib.urlencode({
        "funduse": "",
        "mobilephone": "13300000002",
        "market": "0",
        "stkcode": "000001",
        "producttype": "1",
        "fundid": "81106500034",
        "appVer": "V1.1.4.01",
        "deviceType": "IOS",
        "appType": "12",
        "orderamt": "5006.00",
        "token": "868f294aa44953016c5c7f0e58f0065c",
        "envType": "1",
        "secuid": "0060630008",
        "custid": "81106500034",
        "userId": "2",
        "orderqty": "900",
        "trdpwd": "D-ectHlgxVwVmjb_-jxhQBkSEHKJqMo3PS6hHsFNVRZLAtPvbJsK8WrQ98A77Vn0dcb-szxkl-32BnxzLio0g4aisr1fRJRpEOoPC-JL3-b6UitliHPf6_zZbzgvHL6w-1oFmOHKG28ACQf4JWvbLFvkEJhnyT9zJiBTqEd_Ktc",
        "ghdays": "366",
        "deviceCode": "e3e1f6db621de805f2d6cce21e339f9c"
    })
    response = urllib.urlopen("http://t.c.jzsec.com/loan/f410629", params).read()
    return response

#补充质押: 410630
def add_pledge():
    params = urllib.urlencode({
        "mobilephone": "13300000002",
        "market": "0",
        "stkcode": "000001",
        "gpzysno": "201508280B3000040",
        "fundid": "81106500034",
        "appVer": "V1.1.4.01",
        "deviceType": "IOS",
        "appType": "12",
        "custid": "81106500034",
        "token": "868f294aa44953016c5c7f0e58f0065c",
        "envType": "1",
        "secuid": "0060630008",
        "userId": "2",
        "orderqty": "100",
        "trdpwd": "SinBqYKdzBQk9rTsalGYPYVbDuj3EgOkQHzDVAxIPsxpXFf1g5mnMwYJdTPO-yIMRmBrw9W4y7f_abF0aOIHsIZrCP9KztqNN_yIcz1D12hEZQCIiPUCqGSHZ3GsiJ4bVXchOyBpuGugkfBwxkGZDAE5F8W52V1x6yB2jLZzZV0",
        "deviceCode": "e3e1f6db621de805f2d6cce21e339f9c"
    })
    response = urllib.urlopen("http://t.c.jzsec.com/loan/f410630", params).read()
    return response


#还款: 410636
def return_money():
    params = urllib.urlencode({
        "mobilephone": "13300000002",
        "gpzysno": "201509020B3000007",
        "fundid": "81106500034",
        "appVer": "V1.1.4.01",
        "deviceType": "IOS",
        "custid": "81106500034",
        "userId": "2",
        "appType": "12",
        "envType": "1",
        "token": "868f294aa44953016c5c7f0e58f0065c",
        "trdpwd": "DrLnBde0hZJFJvkzZhvtDr_GK1srmCBveoAeBNfuPUYOANavuWpt7hhjlhJTQDyZ_g7DnyqGo5bAhtjhWamOGo-OVrxpI2QXs8YM0SxB4ypvucrAkUNFO2IjfbDaYAa-JOxsXxvSWyRL3WbZTVwFC_XpUEi1oim82xW4gcqZRAs",
        "deviceCode": "e3e1f6db621de805f2d6cce21e339f9c"
    })
    response = urllib.urlopen("http://t.c.jzsec.com/loan/f410636", params).read()

def cuser_info(phone):
    session = dataBase.db_session()
    cuser = session.execute("select * from c_user WHERE loginmobile = " + str(phone)).first()
    trade_fund_account = session.execute("select * from trade_fund_account where c_user_id = " + str(cuser.id)).first()
    sd_customer = session.execute("select * from sd_customer WHERE mobileno = " + str(phone)).first()
    print "Status:"
    print cuser.status
    print "\nCuser Info:"
    print cuser
    print "\nTrade Fund Account:"
    print trade_fund_account
    print "\nSD Customer:"
    print sd_customer
    session.close()
    # return cuser.status, cuser, trade_fund_account, sd_customer





def add_user():
    file_path = globalData.PATH + '/TestData/CappData.xlsx'
    workbook = XLBook(file_path)
    test_data = dict(workbook.sheets())
    worksheet = test_data.get("capp")
    nrows = len(worksheet)
    mobile = []
    cust_id = []
    for i in range(0, nrows):
        mobile.append(str(worksheet[i][0]).split(".")[0])
        cust_id.append(str(worksheet[i][1]).split(".")[0])
    # print mobile[1]
    # print cust_id[1]
    session = dataBase.db_session()
    for i in range(0, len(mobile)):
        session.execute("delete from c_user where loginmobile = \'" + mobile[i] + "\'")
        session.commit()
        session.execute("INSERT INTO c_user VALUES (NULL, '6b4f9f85012b304979c94" + mobile[i] + "\', '2015-09-10 10:59:23', '34f85ca80ec353d3052b8a2d3973a0c5', '0', \'" + mobile[i] + "\', '', '', '1', '1977-07-17', '', '', '投资大师" + mobile[i] + "\', '401', '2015-09-14 10:45:38', '1', '0', '0', '1012', '河北省张家口市万全县孔家庄镇工业街南万兴小区0号楼1单元202室', '2015-09-14 10:45:38', '2015-10-29 17:20:32', '', '1', '', '1', '', '', '', '')")
        # session.execute("INSERT INTO c_user VALUES (NULL, '6b4f9f85012b304979c94" + mobile[i] + "\', '2015-09-10 10:59:23', '34f85ca80ec353d3052b8a2d3973a0c5', '0', \'" + mobile[i] + "\', '', '', '1', '1977-07-17', '', '', '投资大师" + mobile[i] + "\', '401', '2015-09-14 10:45:38', '1', '0', '0', '1012', '河北省张家口市万全县孔家庄镇工业街南万兴小区0号楼1单元202室', '2015-09-14 10:45:38', '2015-10-29 17:20:32')")
        session.commit()
        cuser = session.execute("select * from c_user where loginmobile = " + mobile[i]).first()
        if(cuser != None):
            session.execute("update c_user set client_id = 'imaster_" + str(cuser.id) + "\' where loginmobile = \'" + mobile[i] + "\'")
            session.commit()
        session.execute("delete from sd_customer where fund_account = \'" + cust_id[i] + "\'")
        session.commit()
        session.execute("INSERT INTO sd_customer VALUES (NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '0811', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, \'" + cust_id[i] + "\', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, \'" + mobile[i] + "\', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '0', NULL, NULL, NULL, NULL, NULL)")
        session.commit()
        cuser_id = session.execute("select * from c_user where loginmobile = \'" + mobile[i] + "\'").first().id
        session.execute("delete from trade_fund_account where c_user_id = \'" + str(cuser_id) + "\' or cust_id = \'" + cust_id[i] + "\'")
        session.commit()
        session.execute("INSERT INTO trade_fund_account VALUES (NULL, \'" + str(cuser_id) + "\', \'" + cust_id[i] + "\', \'" + mobile[i] + "\', '0.00015000', '0.00000', '投资大师" + mobile[i] + "\', '', '2008-10-13', '2018-10-13', 'c', '43062419900818361X', '00', '156', '长沙市开福区四方坪红色渔业队1号', '401', '101963', 'visitsurvey', '0', '2015-08-21 18:18:36', '2015-09-21 07:01:04')")
        session.commit()
    session.close()


def delete_portfolios(phone):
    session = dataBase.db_session()
    session.execute("delete from portfolios where owner = (select client_id from c_user where loginmobile = \'"+ str(phone) + "\')")
    session.commit()

def add_portfolios(phone, i):
    session = dataBase.db_session()
    client_id = session.execute("select * from c_user where loginmobile = \'" + str(phone) + "\'").first().client_id
    for i in range(0, i):
        k = i
        symbol = make_symbol(k)
        while(not session.execute("select * from portfolios where symbol = \'" + symbol + "\'").fetchall()):
            k = k + 1
            symbol = make_symbol(k)
        session.execute("INSERT INTO portfolios VALUES (\'" + symbol +"\', '组合" + str(i) + "\', \'" + client_id + "\', '0.0000', '0.0000', '0.0000', '0.0000', '0.0000', '0.000000', '100.00', '1.0000', '0.0000', '2016-01-05 17:28:32', '2016-01-05 17:36:19', NULL, NULL, NULL, NULL, 'cn', NULL, NULL, NULL, NULL, NULL, '1', NULL, '0', '0', NULL, NULL, NULL, NULL, NULL, '843', '843', NULL)")
        session.commit()
    session.close()

def make_symbol(i):
    symbol = chr(i + 65) + chr(i + 66) + chr(i + 67) + '188'
    return symbol


def add_portfolios_holdings(phone, i):
    file_path = globalData.PATH + '/TestData/CappData.xlsx'
    workbook = XLBook(file_path)
    test_data = dict(workbook.sheets())
    worksheet = test_data.get("portfolio_holdings")
    nrows = len(worksheet)
    stock_market = []
    stock_symbol = []
    stock_name = []
    volume = []
    yd_volume = []
    today_profit = []
    total_profit = []
    net_value = []
    for i in range(0, nrows):
        stock_market.append(str(worksheet[i][0]))
        stock_symbol.append(str(worksheet[i][1]))
        stock_name.append(str(worksheet[i][2]))
        volume.append(str(worksheet[i][3]))
        yd_volume.append(str(worksheet[i][4]))
        today_profit.append(str(worksheet[i][5]))
        total_profit.append(str(worksheet[i][6]))
        net_value.append(str(worksheet[i][7]))
    session = dataBase.db_session()
    client_id = session.execute("select * from c_user where loginmobile = \'" + str(phone) + "\'").first().client_id
    portfolio = session.execute("select * from portfolios where owner = \'" + str(client_id) + "\'").first().symbol
    session.execute("delete from portfolio_holdings where symbol = \'" + str(portfolio) + "\'")
    session.commit()
    for i in range(0, i):
        session.execute("INSERT INTO portfolio_holdings VALUES (NULL, \'" + str(portfolio) + "\', \'" + str(stock_market) + "\', \'" + str(stock_symbol) + "\', \'" + str(stock_name) + "\', \'" + str(volume) + "\', \'" + str(yd_volume) + "\', \'" + str(today_profit) + "\', \'" + str(total_profit) + "\', \'" + str(net_value) + "\', '1', NULL, NULL, NULL, NULL, NULL, '2016-01-04 09:30:01', '2016-01-04 20:01:01')")
        session.commit()
    session.close()



if __name__ == '__main__':
    # print get_product()
    # print get_authorization()
    # print get_limit()
    # print get_contract()
    # print get_contract_details()
    # print get_number_limit()
    # print get_contracthistory()
    # cuser_info(18910848077)
    # delete_cuser(18001284533)
    # delete_cuser(15501253283)
    add_user()
    # add_portfolios(18001284533, 1)
    # add_portfolios_holdings(18001284533, 1)
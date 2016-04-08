# -*- coding: utf-8 -*-
import xlsxwriter
from CommonMethods import globalData, relatedTime
import os


def generateReport():
    time = relatedTime.reporttime()
    file = globalData.PATH + '/TestResult/TestReport_'+ str(time) + '.xlsx'
    workbook = xlsxwriter.Workbook(file)

    for i in range(0, len(globalData.EXECUTED)):
        moudle = globalData.EXECUTED[i]
        #新建工作表
        report = workbook.add_worksheet(moudle)


        #设置工作表单元格的宽高
        report.set_column('A:Z', 30)
        for i in range(1, 100):
            report.set_row(i, 20)




        title_format = workbook.add_format({
            'bold': 2,
            'border': 1,
            'align': 'center',
            'valign': 'vcenter',
            'font_name': u'黑体',
            'font_size': 20})


        table_format = workbook.add_format({
            'bold': 0,
            'border': 0,
            'align': 'center',
            'valign': 'vcenter',
            'font_name': u'黑体',
            'font_size': 11})

        result = []

        for i in range(0, len(globalData.RESULT)):
            if(globalData.RESULT[i][0] == str(moudle)):
                result.append(globalData.RESULT[i][2])

        data = []

        for i in range(0, len(globalData.TESTDATA.get(moudle))):
            data.append([globalData.TESTDATA.get(moudle)[i], result[i]])

        header = []
        for i in range(0, len(globalData.TESTDATA.get(moudle)[0])):
            header.append({'header': globalData.TESTDATA.get(moudle)[0][i], 'format': title_format})

        # title = {
        #     'name': u'开户视频接入',
        #     'name_font': {'size': 14, 'bold': True},
        #     'num_font':  {'黑体': True },
        # }
        for i in range(65, 65 + len(globalData.TESTDATA.get(moudle)[0])):
            report.write(str(i) + '1', globalData.TESTDATA.get(moudle)[0][i], title_format )
        # report.write('A2', 'Start', title_format)
        # report.write('B2', 'End', title_format)
        # report.write('C2', 'Total', title_format)
        # report.write('D2', 'Init', title_format)
        # report.write('E2', 'Reuslt', title_format)
        for i in range(0, len(data)):
            report.write_row('A' + str(i + 2), data[i])
        # report.write_row('B2', data[1])
        # report.write_row('C2', data[2])
        # report.write_row('D2', data[3])
        # report.write_row('E2', data[4])


        # report.merge_range('A1:E1', u'开户视频接入', title_format)


    workbook.close()


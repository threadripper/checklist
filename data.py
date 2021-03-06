# -*- encoding: utf-8 -*-
import xlwt  # 需要的模块
import xlrd
from xlutils.copy import copy
from goto import with_goto
import re
import os.path

def txt_2_xls(filename, xlsname):
    """
    :文本转换成xls的函数
    :param filename txt文本文件名称、
    :param xlsname 表示转换后的excel文件名
    """
    try:
        fopen = open(filename , 'r')
        xls = xlwt.Workbook()
        # 生成excel的方法，声明excel
        sheet = xls.add_sheet('sheet1', cell_overwrite_ok=True)
        x = 0
        for line in fopen:
            #预处理 ：去掉空行
            if line == '\n':
                continue
            #end
            #预处理 ：将等号替换为空格
            if '=' in line:
                line = re.sub('=', ' ', line)
            #end
            for i in range(len(line.split())): #以空格作为关键字的区分
                item = line.split()[i]
                # 对数据进行筛选
                # 去掉以#开头的注释行
                if '#' in item :
                    if i == 0 :
                        x -= 1
                        break
                    else :
                        break
                #en
                if i//256 :
                    sheet.write(x+i//256 ,i%256, item)  #如果超过256个数据，那就另起一行
                else :
                    #sheet.write(x, i, item, xlwt.easyxf('pattern: pattern solid, fore_colour red;'))
                    #https://www.crifan.com/python_xlwt_set_cell_background_color/
                    sheet.write(x, i, item)  # x单元格经度，i 单元格纬度 注意 i 不能大于256
            x += len(line.split())//256 + 1  # excel另起一行加上超过256个数据额外消耗的行数
        fopen.close()
        xls.save(xlsname)  # 保存xls文件
    except:
        raise

def xls_Prcfig_txt(xls_name,file_name):
    """
    :文本转换成xls的函数
    :param filename txt文本文件名称、
    :param xlsname 表示转换后的excel文件名
    """
    try:
        fopen = open(file_name, "w")
        data = xlrd.open_workbook(xls_name)
        table = data.sheets()[0]
        nrows = table.nrows
        ncols = table.ncols

        for nrow in range(0, nrows):
            print(nrow)
            for ncol in range(0, ncols):
                cell_value = table.cell(nrow, ncol).value
                if cell_value == "":
                    fopen.write("\n")
                    break
                if ncol == 0:
                    fopen.write(cell_value)
                    fopen.write(" = ")
                else:
                    fopen.write(cell_value)
                    fopen.write(" ")
            print(ncol)
    except:
        raise


def xls_Prcfig_xls(from_xls, to_xls):
    """
    :xls转换成xls的函数
    :param from_xls xls文件名称、
    :param to_xls 表示转换后的excel文件名
    #https://blog.csdn.net/qq_16645423/article/details/79466958
    """
    try:
        data = xlrd.open_workbook(from_xls)
        table = data.sheets()[2] #获取表单
        nrows = table.nrows  # 获取行数
        ncols = table.ncols #获取列数

        xls = xlwt.Workbook()
        sheet = xls.add_sheet('sheet1')
        for nrow in range(0, nrows):
            for ncol in range(0, ncols):
                cell = table.cell(nrow, ncol).value
                sheet.write(nrow, ncol, cell)
        xls.save(to_xls)  # 保存xls文件

    except:
        raise
@with_goto
def xls_Prcfig_xls_for_memory(from_xls, to_xls):
    """
    :xls转换成xls的函数
    :param from_xls xls文件名称、
    :param to_xls 表示转换后的excel文件名
    #https://blog.csdn.net/qq_16645423/article/details/79466958
    """
    try:
        if os.path.isfile(to_xls):
            pass
        else:
            data = xlrd.open_workbook(from_xls)
            len_copy = len(data.sheets())
            xls = xlwt.Workbook()
            for copy_sheet in range(0, len_copy):
                table = data.sheets()[copy_sheet] #获取表单
                nrows = table.nrows  # 获取行数
                ncols = table.ncols #获取列数
                sheet = xls.add_sheet("sheet%d"%(copy_sheet))
                for nrow in range(0, nrows):
                    for ncol in range(0, ncols):
                        cell = table.cell(nrow, ncol).value
                        sheet.write(nrow, ncol, cell)
            xls.save(to_xls)  # 保存xls文件

        xls = xlrd.open_workbook(to_xls)
        new_xls = copy(xls)

        data = xlrd.open_workbook(from_xls, "r+")
        nsheets = len(data.sheets())
        for nsheet in range(0, nsheets):#获取等待拷贝的表格sheet数量
            print(nsheets)
            table = data.sheets()[nsheet] #获取表单，待拷贝的sheet
            nrows = table.nrows  # 获取行数，表示即将拷贝的行
            print("nrows:%d" % (nrows))
            ncols = table.ncols  # 获取列数，表示即将拷贝的列
            print("ncols:%d" % (ncols))
            print("nrows:%d"%(nrows))
            xtable = xls.sheets()[nsheet]#正在执行的sheet
            print(xtable.name)
            xrows = xtable.nrows #获取原始表格的行数
            print("xrows:%d" % (xrows))
            x_w_sheet = new_xls.get_sheet(xtable.name)#选择写入对象sheet
            nrow = 0
            ncol = 0
            row_add = 0
            cell = table.cell(nrow, ncol).value  # 待拷贝的sheet里面的当前单元的值
            for nrow in range(0, nrows): #待拷贝的行循环
                print(nrow)
                for xrow in range(0, xrows):
                    print("xrow:%d" % (xrow))
                    value_nrow_hw = table.cell(nrow, 1).value
                    if len(value_nrow_hw) == 0:  # 如果待拷贝的这个行是空的，就跳过
                        goto.next
                    if table.cell(nrow, 1).value == xtable.cell(xrow, 1).value:
                        print("meet")
                        goto.next
                    else:
                        print("not meet")
                        if xrow == xrows-1 :
                            for ncol in range(0, ncols):  # 待拷贝的列循环
                                cell = table.cell(nrow, ncol).value
                                x_w_sheet.write(row_add + xrows, ncol, cell)
                            row_add += 1
                label .next
            #if cell != "END" and table.cell(nrow, 0).value != "END":
            #    x_w_sheet.write(row_add+xrows, 0, "END")
        new_xls.save(to_xls)  # 保存xls文件

    except:
       raise

def proc_xls(xls_hw, xls_Prcfig, result):
    """
    :xls处理的函数
    :param xls_hw, xls_Prcfig 待处理xls文件名称、
    :param result 表示处理后的excel文件名
    #https://blog.csdn.net/qq_16645423/article/details/79466958
    """
    try:
        print("ok")
        data_hw = xlrd.open_workbook(xls_hw)
        table_hw = data_hw.sheets()[0]  # 获取表单
        nrows_hw = table_hw.nrows  # 获取行数
        ncols_hw = table_hw.ncols #获取列数

        data_Prcfig = xlrd.open_workbook(xls_Prcfig)
        table_Prcfig = data_Prcfig.sheets()[0]  # 获取表单
        nrows_Prcfig = table_Prcfig.nrows  # 获取行数
        ncols_Prcfig = table_Prcfig.ncols

        xls = xlwt.Workbook()
        sheet = xls.add_sheet('sheet1', cell_overwrite_ok=True) # Attempt to overwrite cell
        overwrite = 0
        for nrow_hw in range(0, nrows_hw):

            cell_hw = table_hw.cell(nrow_hw, 0).value
            if cell_hw == '主板PCB' :
                key_words_pcb = re.findall('\d+', table_hw.cell(nrow_hw, 3).value) #python 正则表达式 re findall 方法能够以列表的形式返回能匹配的子串
                overwrite = 0
                for nrow_Prcfig in range(0, nrows_Prcfig):
                    cell_Prcfig_1 = table_Prcfig.cell(nrow_Prcfig, 1).value
                    cell_Prcfig_0 = table_Prcfig.cell(nrow_Prcfig, 0).value
                    if key_words_pcb[0] in cell_Prcfig_1:
                        if overwrite :
                            sheet.write(overwrite, 1, cell_Prcfig_0)
                            sheet.write(overwrite, 2, cell_Prcfig_1)
                        else :
                            sheet.write(overwrite, 0, cell_hw)
                            sheet.write(overwrite, 1, cell_Prcfig_0)
                            sheet.write(overwrite, 2, cell_Prcfig_1)
                        overwrite += 1
                    #else:
                        #print("nok")
                print(overwrite)

            if cell_hw == 'CPU' :
                sheet.write(overwrite, 0, cell_hw)
                key_words_cpu = re.findall('\d+', table_hw.cell(nrow_hw, 2).value) #匹配cell_hw中的数字

                for nrow_Prcfig in range(0, nrows_Prcfig):
                    cell_Prcfig_1 = table_Prcfig.cell(nrow_Prcfig, 1).value
                    cell_Prcfig_0 = table_Prcfig.cell(nrow_Prcfig, 0).value
                    if key_words_cpu[0] in cell_Prcfig_1:
                        if overwrite :
                            sheet.write(overwrite, 1, cell_Prcfig_0)
                            sheet.write(overwrite, 2, cell_Prcfig_1)
                        else :
                            sheet.write(overwrite, 1, cell_Prcfig_0)
                            sheet.write(overwrite, 2, cell_Prcfig_1)
                        overwrite += 1
                    #else:
                        #print("nok")
                print(overwrite)


            if cell_hw == 'FLASH' :
                sheet.write(overwrite, 0, cell_hw)
                key_words_flash = table_hw.cell(nrow_hw, 2).value
                print(key_words_flash)
                for nrow_Prcfig in range(0, nrows_Prcfig):
                    cell_Prcfig_1 = table_Prcfig.cell(nrow_Prcfig, 1).value
                    cell_Prcfig_0 = table_Prcfig.cell(nrow_Prcfig, 0).value
                    if "sagereal_memory_flash" in cell_Prcfig_0:
                        fopen = open("memory/%s/custom_MemoryDevice.h"%(cell_Prcfig_1), 'r+')

                        fopen.close()
                    else:
                        print("notmeet")
                print(overwrite)

        xls.save(result)  # 保存xls文件

    except:
        raise #显示错误信息


if __name__ == "__main__":
    filename = "VP531_H5313_common/ProjectConfig.mk"
    xlsname = "test.xlsx"
    #txt_2_xls(filename, xlsname)
    xls_name = "test.xlsx"
    file_name = "trans_file"
    #xls_Prcfig_txt(xls_name,file_name)
    #from_xls = "VP531E_AH5313_配置M_硬件配置表&任务表-ME84 GD B2&5+汉天下-20180911.xls"
    from_xls = "MemoryDeviceList_MT6580_2.xls"
    to_xls = "all_memory.xlsx"
#    xls_Prcfig_xls_for_memory(from_xls, to_xls)
    xls_hw = "test2.xlsx"
    xls_Prcfig = "test.xlsx"
    result = "result.xlsx"
    proc_xls(xls_hw, xls_Prcfig, result)



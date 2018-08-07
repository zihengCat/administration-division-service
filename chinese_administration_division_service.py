# -*- coding:utf-8 -*-
# `OS`模块 => 文件路径
import os
# `json`模块 => JSON 数据解析
import json
# 行政区划信息服务类
class AdministrationDivisionService(object):
    # 类初始化函数(无参)
    def __init__(self):
        # JSON数据 => Dict
        f1_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                  'db/location.min.json')
        f2_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                  'db/list.json')
        with open(f1_path, 'rt') as f1, open(f2_path, 'rt') as f2:
            self.location_dict = json.loads(f1.read())
            d = json.loads(f2.read())
            self.location_dict_r = dict(zip(d.values(), d.keys()))
            # for `DEBUG` Mode
            #print(self.location_dict_r)
        # 特殊城市列表 => 北京，天津，上海，重庆，香港，澳门
        self.sp_cities = ['110000', # 北京市
                          '120000', # 天津市
                          '310000', # 上海市
                          '500000', # 重庆市
                          '810000', # 香港特别行政区
                          '820000', # 澳门特别行政区
        ]
    # 对外接口API：parseString()
    # 接受参数：省市区字符串（`str`）
    # 正确返回：6位行政区划代码（`str`）
    # 错误返回：`None`
    def parseString(self, string_str):
        try:
            return self.location_dict_r.get(string_str)
        except Exception as e:
            # for `DEBUG` Mode
            #print(e)
            # 出错返回`None`
            return None
    # 对外接口API：parseCode()
    # 接受参数：6位行政区划代码（`str`）
    # 正确返回：省市区字符串（`sep`分隔，默认`;`）
    # 错误返回：`None`
    def parseCode(self, code_str, sep = ';'):
        try:
            # 验证输入参数的合法性
            if(type(code_str) != type("str") or len(code_str) != 6):
                raise("Error: input argument does not fit")
            # 确认参数类型
            code_type = self.__checkCodeType(code_str)
            # 分割参数
            code_part_12 = code_str[0: 2]
            code_part_34 = code_str[2: 4]
            code_part_56 = code_str[4: 6]
            #print(code_part_12, code_part_34, code_part_56)
            '''
            if(code_type == 1):
                # 搜索目标：省/直辖市/特别行政区
                json_part1 = self.location_dict
                # 返回值第1部分：省/直辖市/特别行政区
                ret_part1 = json_part1.get(code_part_12 + '0000').get('name')
                return ret_part1 + sep + sep
            '''
            if(code_type == 1 or code_type == 2):
                # 搜索目标：省/直辖市/特别行政区
                json_part1 = self.location_dict
                #print(json_part1)
                # 搜索目标：地级市
                json_part2 = json_part1.get(code_part_12 + '0000').get('cities')
                #print(json_part2)
                # 返回值第1部分：省/直辖市/特别行政区
                ret_part1 = json_part1.get(code_part_12 + '0000').get('name')
                # 返回值第2部分：地级市
                if(code_part_12 + '0000' in self.sp_cities):
                    ret_part2 = json_part2.get(code_part_12 + '00' + '00').get('name')
                else:
                    ret_part2 = json_part2.get(code_part_12 + code_part_34 + '00').get('name')
                return ret_part1 + sep + ret_part2 + sep
            elif(code_type == 3):
                # 搜索目标：省/直辖市/特别行政区
                json_part1 = self.location_dict
                #print(json_part1)
                # 搜索目标：地级市
                json_part2 = json_part1.get(code_part_12 + '0000').get('cities')
                #print(json_part2)
                # 搜索目标：市辖区
                # 对特殊城市作特殊处理
                if(code_part_12 + '0000' in self.sp_cities):
                    json_part3 = json_part2.get(code_part_12 + '00' + '00').get('districts')
                else:
                    json_part3 = json_part2.get(code_part_12 + code_part_34 + '00').get('districts')
                #print(json_part3)
                # 返回值第1部分：省/直辖市/特别行政区
                ret_part1 = json_part1.get(code_part_12 + '0000').get('name')
                # 返回值第2部分：地级市
                if(code_part_12 + '0000' in self.sp_cities):
                    ret_part2 = json_part2.get(code_part_12 + '00' + '00').get('name')
                else:
                    ret_part2 = json_part2.get(code_part_12 + code_part_34 + '00').get('name')
                # 返回值第3部分：市辖区
                ret_part3 = json_part3.get(code_part_12 + code_part_34 + code_part_56)
                # 返回值：`sep`分隔
                return ret_part1 + sep + ret_part2 + sep + ret_part3
            else:
                # 不明的行政区划类型
                raise("Error: unknow code type")
        except:
            # 出错返回`None`
            return None
    # 内部功能函数：确认行政区划字符串类型
    def __checkStringType(self, string_str, sep = ';'):
        pass
    # 内部功能函数：确认行政区划代码类型
    def __checkCodeType(self, code_str):
        if(code_str[2:6] == '0000'):
            # Flag: 省/直辖市/特别行政区
            return 1
        elif(code_str[4:6] == '00'):
            # Flag: 地级市
            return 2
        else:
            # Flag: 市辖区
            return 3

if __name__ == '__main__':
    # 测试用例参看`main.py`
    pass

# Chinese Administration Division Service

[![Build Status](https://travis-ci.com/zihengCat/chinese-administration-division-service.svg?branch=master)](https://travis-ci.com/zihengCat/chinese-administration-division-service)

中华人民共和国行政区划数据服务模块「`Python`模块」。

An Chinese Administration Division Service Module for `Python`.

# Usage（使用说明）

此模块**同时兼容`Python2`与`Python3`，且无「第三方」依赖项**。

1. 导入模块
2. 初始化类实例
3. 调用解析方法

| API                   | 说明           |
| --------------------- | -------------- |
| `parseCode(code_str, [sep = ';'])` | 接受参数：行政区划代码（6位字符串），正确返回：省市区字符串（默认`;`分隔），错误返回：`None` |

> 表：模块`API`接口表

```python
# 1. 导入模块「可以使用`as`简化书写」
import chinese_administration_division_service as cads

# 2. 创建类实例
c = cads.AdministrationDivisionService()

# 3. 调用解析方法
i = c.parseCode('130529')
print(i)
```
> 代码清单：示例代码「详见`main.py`」

# Data Source（数据来源）

- [中国行政区划信息 - 区划代码数据库（GB/T 2260）](https://github.com/JasonBoy/china-location)

- [中华人民共和国行政区划数据【省、市、区县、乡镇街道】中国省市区镇三级四级联动地址数据（GB/T 2260）](https://github.com/mumuy/data_location)

> 更新时间: 2018-05-24

# License（许可协议）

[MIT](./LICENSE)


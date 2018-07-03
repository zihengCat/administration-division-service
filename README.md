# Administration Division Service

火石 - 行政区划信息服务模块

An Chinese Administration Division Service Module for **hsmap**.

# Usage（使用说明）

此模块**同时兼容`Python2`与`Python3`，且无第三方依赖项**。

1. 导入模块
2. 初始化类实例
3. 调用解析方法

| API                   | 说明           |
| --------------------- | -------------- |
| `parseCode(code_str)` | 接受行政区划代码（6位字符串），返回省市区字符串（`;`分隔），出错返回`None` |

> 表：模块API接口表

```python
# -*- coding:utf-8 -*-

# 导入模块（使用`as`可简化书写）
import administration_division_service as ads

# 创建类实例
c = ads.Administration_division_service()

# 测试用例

# 正确情况 =>
print(c.parseCode('130529'))
print(c.parseCode('130432'))
print(c.parseCode('110105'))
print(c.parseCode('130825'))
print(c.parseCode('810107'))
print(c.parseCode('710101'))
print(c.parseCode('540223'))

# 错误情况 =>

## 参数不匹配
print(c.parseCode(123))
print(c.parseCode('hello'))
print(c.parseCode('130825123'))
print(c.parseCode('1235'))

## 不存在的区划代码
print(c.parseCode('123456'))
print(c.parseCode('123123'))
```
> 代码清单：示例代码（详见`main.py`）

# Data Source（数据源）

- [中国行政区划信息 - 区划代码数据库（GB/T 2260）](https://github.com/JasonBoy/china-location)

> 更新时间: 2018-05-24


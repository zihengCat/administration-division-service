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
| `parseCode(code_str, [sep = ';'])` | 接受参数：行政区划代码（6位字符串），正确返回：省市区字符串（`;`分隔），错误返回：`None` |

> 表：模块`API`接口表

```python
# -*- coding:utf-8 -*-

# 1. 导入模块（使用`as`可简化书写）
import administration_division_service as ads

# 2. 创建类实例
c = ads.Administration_division_service()

# 3. 调用解析方法
print(c.parseCode('130529'))
```
> 代码清单：示例代码（详见`main.py`）

# Data Source（数据源）

- [中国行政区划信息 - 区划代码数据库（GB/T 2260）](https://github.com/JasonBoy/china-location)

> 更新时间: 2018-05-24

# Author（维护人）

子恒：lvzh@hsmap.cn

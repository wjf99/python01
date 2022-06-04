# 使用loguru模块 操作日志
'''
功能：
1、可以格式化日志
2、着色（不同的颜色）
3、生成到文件
4、显示不同的日志级别
5、只使用一个对象（非常方便）
'''

# 1、下载安装 pip install loguru
# 2、导包：可以使用logger的所有方法
from loguru import logger
# 打印一条普通日志
logger.info("hello")

# 其他日志模块打印(颜色用来区分日志级别）
# degug：调试日志
logger.debug("debug日志")
# warning: 警告日志
logger.warning("warning日志")
# success: 成功日志
logger.success("success日志")
# error :错误日志
logger.error("错误日志")

# 输出到文件 add()方法
#logger.add("file.log",level="DEBUG")

# 格式化 这里面的格式level 会打印包括该级别以及该级别以上的级别
#logger.add("file.log",format="{time} | {level} | {message} | {line}",level="DEBUG")
logger.add("file.log",format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message} | {line}",level="DEBUG")
# logger.add("file.log",level="DEBUG")
# degug：调试日志
logger.debug("debug日志")
# warning: 警告日志
logger.warning("warning日志")

# 对日志进行传入参数的格式化
logger.info("我的名字叫{}","张三")
logger.info("我的名字叫{}",format("张三"))
# 文件保存（了解）
# 按照时间段保存文件
# 文件过多切割

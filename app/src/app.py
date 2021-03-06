# -*- coding: utf-8 -*-
from logging import getLogger, config, StreamHandler, DEBUG
import os

import sys
sys.path.append('./')
from logutil import LogUtil
from importenv import ImportEnvKeyEnum
import importenv as setting
from data import User

PYTHON_APP_HOME = os.getenv('PYTHON_APP_HOME')
logger = getLogger(__name__)
log_conf = LogUtil.get_log_conf(PYTHON_APP_HOME + '/config/log_config.json')
config.dictConfig(log_conf)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

if __name__ == '__main__':
  data = User(name = 'hoge', age = 20)
  logger.info(data)
  logger.info('name : %s' % data.name)
  logger.info('age : %d' % data.age)

  data2 = User(name = 'hoge', age = 20)
  logger.info(data == data2)
  
  data3 = User(name = 'piyo', age = 20)
  logger.info(data == data3)
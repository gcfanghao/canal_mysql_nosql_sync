#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# redis
redis_host = '127.0.0.1'
redis_port = 6379

# rabbitmq connect
rabbitmq_host = '127.0.0.1'
rabbitmq_port = 5672
# rabbitmq 远程访问禁止使用 guest账号
rabbitmq_user = 'test'    
rabbitmq_pass = '123456'
rabbitmq_queue_name = 'binlog_test'


#binlog_dir = '/Users/liukelin/Desktop/canal-otter-mycat-cobar/canal_object/data' # 文件路径
#binlog_file = '' # 开始文件
#binlog_prefix = 'binlog_' # 文件前缀


# 指定保存到redis的key，指定每个db-table的 key
redis_cache_map = {
    # db
	'test':{  
	        # table      
			'users':'uid',  # 
		  }
}



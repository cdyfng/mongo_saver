## save kline into mongodb 

### 框架依赖
- 运行环境
	- python 3.5.3 或以上版本

- 依赖python三方包
	- aiohttp>=3.2.1
	- aioamqp>=0.13.0
	- motor>=2.0.0 (可选)

- RabbitMQ服务器
    - 事件发布、订阅

- MongoDB数据库(可选)
    - 数据存储



- 运行
```text
python main.py config.json
```

- 存储数据到mongodb
	- 数据库启动
	```text
	./bin/mongod --dbpath=./db2
	```
	- create user&password
	```text
	db.createUser({user:"anna",pwd:"beauty",roles:[{role: "userAdminAnyDatabase", db: "admin"}, "readWriteAnyDatabase"]})
	```
	- into terminal 
	```text
	./bin/mongo 127.0.0.1:27017
	use okex_swap
	db.kline_BTCUSDTSWAP.find()
	db.kline_BTCUSDTSWAP.find().count()
	```


	
	
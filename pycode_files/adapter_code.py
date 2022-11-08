import sqlite3


class AdapterDB:
	def __init__(self, name_db):
		self.name_db = name_db
		self.connection = sqlite3.connect(self.name_db)
		self.cur = self.connection.cursor()
	
	def add_result(self, expression, result):
		self.sql = f"insert into results (expression, iserror, result) values ('{expression}', 0, {result})"
		self.cur.execute(self.sql)
		self.connection.commit()
	
	def add_error(self, expression, error):
		self.sql = f"insert into results (expression, iserror, result) values ('{expression}', 1, 'error')"
		self.cur.execute(self.sql)
		self.sql = f"insert into errors (expression, error) values ('{expression}', '{error}')"
		self.cur.execute(self.sql)
		self.connection.commit()
	
	def close_db(self):
		self.connection.close()


# adapter = AdapterDB('../results.db')
#
# try:
# 	string = '1/0'
# 	adapter.add_result(string, eval(string))
# except Exception as e:
# 	adapter.add_error(string, e)
# adapter.close_db()
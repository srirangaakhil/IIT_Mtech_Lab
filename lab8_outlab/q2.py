import getpass
import requests
from bs4 import BeautifulSoup
from datetime import datetime, date
import re
import sqlite3
from sqlite3 import Error


class CS699:
	moodle_auth_url = 'https://moodle.iitb.ac.in/login/index.php'
	sl_lab_url = 'https://moodle.iitb.ac.in/mod/forum/view.php?id=80239'


	def __init__(self):
		db_file = 'CS699_DB'
		""" create a database connection to a SQLite database and create table"""
		self.conn = None
		try:
			self.conn = sqlite3.connect(db_file)
			if self.conn is not None:
				create_table_cmd = """ CREATE TABLE IF NOT EXISTS ANNOUNCEMENT_INFO (
													Topic text NOT NULL,
													Comment text NOT NULL,
													Topic_Date date NOT NULL
												);"""
				self.conn.execute(create_table_cmd)
		except Error as e:
			print("Error creating connection/table.")
			print(e)
		

	def login(self, cred):
		self.session = requests.Session()
		try:
			self.session.post(url = CS699.moodle_auth_url, data = cred)
		except ConnectionError as ce:
			print('Error contacting moodle.')
			print(ce)


	def logout(self):
		if self.session is not None:
			self.session.get(self.logout_url)


	def populate_table(self):
		if self.session is None:
			print('session missing')
			return
		soup = BeautifulSoup(self.session.get(CS699.sl_lab_url).text, 'html5lib')
		self.logout_url = soup.find('a', attrs={'data-title': 'logout,moodle'}).get('href')
		rows = soup.find_all('tr', class_='discussion')
		for row in rows:
			author_name = row.find('td', class_='author').text
			if author_name == 'Diptesh Kanojia':
				topic_col = row.select('td.topic.starter')[0] #CSS Selector
				topic_url = topic_col.find('a').get('href')
				topic_name = topic_col.text
				topic_page = BeautifulSoup(self.session.get(topic_url).text, 'html5lib')
				parent = topic_page.select('div.forumpost.clearfix.firstpost.starter')[0]
				comment = parent.find('div', class_='content').text
				topic_date = datetime.strptime(re.sub('.* - .*day, ', '', parent.find('div', class_='author').text), '%d %B %Y, %I:%M %p')
				try:
					with self.conn:
						self.conn.execute("insert into ANNOUNCEMENT_INFO values (?, ?, ?)", (topic_name, comment, topic_date))
				except:
					print("couldn't add Topic:", topic)
		self.conn.commit()


	def print_table(self):
		cur = self.conn.cursor()
		cur.execute("select * from ANNOUNCEMENT_INFO;")
	 
		rows = cur.fetchall()
	 
		for row in rows:
			print(row)


	def __del__(self):
		self.conn.close()

if __name__ == '__main__':
	cred = { 'username': getpass.getpass(prompt='Enter ldap Username:-', stream=None),
			 'password': getpass.getpass(prompt='Enter ldap Password:-', stream=None)
	}
	foo = CS699()
	foo.login(cred)
	foo.populate_table()
	foo.print_table()
	foo.logout
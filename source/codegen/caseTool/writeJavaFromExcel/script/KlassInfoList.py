# -*- coding: utf-8 -*-
'''애는 뭐하는 얘나? 음 뭐냐면
일단은 말야.....
액셀을 읽어서 테이블의 리스트를 만드는애다.
'''
# start
class KlassInfoList:
	def __init__(self):
		self.klassList = []
	def setKlassList(self, klassList):
		self.klassList = klassList
	def getKlassList(self):
		return self.klassList

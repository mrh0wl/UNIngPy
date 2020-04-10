
from __future__ import print_function

import os
import sys
import requests
from bs4 import BeautifulSoup


class uniarticles(object):
	"""UNI ARTICULOS API"""
	def __init__(self, verbose=False, session=None):
		self.verbose = verbose
		if not session:
			self.session = requests.Session()
		else:
			self.session = session

	def retrieve_results(self, article, limit):
		url = 'http://archivodenoticias.uni.edu.ni/Articulo/'
		res = []
		for i in range(limit):
			divs = article[i].findAll('div', {'class': 'col-lg-13 col-md-15 col-sm-16 col-xs-16'})[0]
			ps = divs.find('p')
			ases = str(divs.find('a')).split('<h2>')[1].split('</h2>')[0]
			date = divs.find('span').text
			link =  [a['href'].split('Articulo/')[1] for a in divs.findAll('a', href=True) if a.text]
			redirect = ''.join(link[:1])
			data = {'title': ases,
					'date': date,
					'preview': (ps.text).encode('ascii', 'ignore'),
					'redirect': url+redirect}
			res.append(data)
		return res

	def ExceptionHandler(self, message, response, exception, warn, function, *args, **kwargs):
		difflib, exceptWarn, error, warnMessage, callback = [],[],[],[],[]
		warns = []

		try:
			return function(*args, **kwargs)
		except exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			x = str((exc_type, fname, exc_tb.tb_lineno)).split("'")[1]
			count = len(x.split("."))
		
			for i in range(10):
				for l in args:
					try:
						if l in str(e):
							z = str(e).split(l+"'"+"\n")[i]
						else:
							z = str(e).split(":")[i]
						if z not in warns:
							warns.append(z.lstrip(' '))
					except:
						pass

			try:
				truefalse = "Default Python Library" if 'exceptions' in x.split('.')[0] else x.split('.')[0] 
				difflib = "Default Python Library" if x.split('.')[0] is False and x.split('.')[1] is False else truefalse
				exceptWarn = x.split('.')[count-2]
				error = x.split('.')[count-1]
				if "bool" in str(type(warn)):
					raise TypeError
				else:
					warn = warn
				if warn == 'AllWarnings':
					warnMessage = warns
				else:
					warnMessage = warns[warn]
			except TypeError:
				t = str(type(warn)).split('<type ')[1].replace(">", '') if sys.version_info[0] is 2 else str(type(warn)).split('<class ')[1].replace(">", '')
				print ("The value of 'warn' must be an integer not %s" % t)
				sys.exit()
			except IndexError:
				pass

			info = {}
			info = {'lib': difflib,
					'exception': exceptWarn,
					'error': error,
					'warning': warnMessage}

			if info not in callback and difflib != None and exceptWarn != None and error != None and warnMessage != None and response == False:
				callback.append(info)
				return callback

			if response == True:
				message = message + str(info['warning'])
				return message

	def urlIndex(self, limit):
		counter = []
		urlist = []

		for l in range(limit)[::10]:
			counter.append(l)
			if l in counter:
				uni_url = 'https://archivodenoticias.uni.edu.ni/Articulo/Pagina/' +str(len(counter))
				urlist.append(uni_url)
		return urlist

	def search(self, limit=10):
		uni_url = self.urlIndex(limit)
		pageDelimiter = [10]
		pageDelimiter = pageDelimiter*(limit//10)
		limitResidue = limit%10
		results = []
		for i in range(0,len(uni_url)):
			res = {}
			value = pageDelimiter.pop(-1) if len(pageDelimiter) is not 0 else limitResidue
			requests.packages.urllib3.disable_warnings()
			req = self.ExceptionHandler("Ha ocurrido un error: ", True, Exception, 1, self.session.get, uni_url[i], verify=True)
			try:
				soup = BeautifulSoup(req.content, 'html.parser')
				articles = soup.findAll('article')
				res = self.retrieve_results(articles, limit=value)
				results.extend(res)
			except:
				print(req + " because" + self.ExceptionHandler(" ", True, Exception, 3, self.session.get, uni_url[i], verify=True).split("]")[0])
		return results
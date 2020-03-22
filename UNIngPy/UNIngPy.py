
from __future__ import print_function

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
					'preview': ps.text,
					'redirect': url+redirect}
			res.append(data)
		return res

	def urlIndex(self, limit):
		counter = []
		urlist = []
		for l in range(limit)[::10]:
			counter.append(l)
			if l in counter:
				uni_url = 'http://archivodenoticias.uni.edu.ni/Articulo/Pagina/'+str(len(counter))
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
			req = self.session.get(uni_url[i])
			soup = BeautifulSoup(req.content, 'html.parser')
			articles = soup.findAll('article')
			res = self.retrieve_results(articles, limit=value)
			results.extend(res)
		return results
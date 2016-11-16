# -*- coding: utf-8 *-*
from urllib.request import urlopen
import classifier as c

def application(environ, start_response):
	request = str(environ['REQUEST_URI']).split("?")
	acidez = request[1]
	ph = request[2]
	alcohol = request[3]
	output = c.predict(acidez, ph, alcohol)

	response_headers = [('Content-type', 'text/plain'),
	('Content-Length', str(len(output)))]
	status = '200 OK'
	start_response(status, response_headers)

	return [bytes(output, 'utf-8')]



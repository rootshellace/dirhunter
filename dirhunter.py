#!/usr/bin/python3

import argparse
import re
import sys
import requests
import http
import colors


def get_arguments():

	parser_description = '''
	dirhunter by rootshellace

	This is a tool used to brute force URLs for subpages.

	You need to pass 2 arguments, the URL to be scanned and 
	the file which contains the subpages to check.

	In case you need to access the page using a different port
	from the standard one, just append :[PORT] at the end of 
	the URL, replacing [PORT] with the number of the needed port.
	'''

	parser = argparse.ArgumentParser(description=parser_description, 
									formatter_class=argparse.RawDescriptionHelpFormatter)
	parser.add_argument('-u', '--url', metavar="URL", type=str, help="URL to scan", required=True)
	parser.add_argument('-w', '--wordlist', metavar="WORDLIST", type=argparse.FileType('r', encoding='UTF-8'), 
						help="File containing list of subpaths to check", required=True)
	args = parser.parse_args()
	url_regex = "^https?:\/\/(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}(:[0-9]{1,5})?(\/[a-zA-Z0-9@:%.\#~=+-_]*)*$"

	if not re.match(url_regex, args.url):
		print("Invalid URL!")
		parser.print_help()
		sys.exit()

	return args.url, args.wordlist.name


def create_urls_to_scan(main_url, subpages_list):

	urls_to_scan = []

	subpages_content = open(subpages_list, 'r')

	for subpage in subpages_content:
		
		if main_url[-1] == '/':
			url = main_url + subpage.strip()
		else:
			url = main_url + '/' + subpage.strip()
		urls_to_scan.append(url)

	subpages_content.close()

	return urls_to_scan


def scan_urls(urls_to_scan):

	for url in urls_to_scan:
		
		url_request = requests.get(url)
		msg = "-> " + http.HTTPStatus(url_request.status_code).phrase + " (Status : " + str(url_request.status_code) + ")"

		if url_request.status_code == 200:
			print("[•]", url, colors.green.format(msg))
		else:
			print("[•]", url, colors.red.format(msg))


def show_header(main_url, subpages_list):

	print(colors.yellow.format("dirhunter - scan URLs for subpages"))
	print(colors.purple.format("=" * 70))
	print(colors.blue.format("[*] URL".ljust(15)), ":", str(main_url))
	print(colors.blue.format("[*] Wordlist".ljust(15)), ":", str(subpages_list))
	print(colors.purple.format("=" * 70))


if __name__ == "__main__":

	main_url, subpages_list = get_arguments()
	urls_to_scan = create_urls_to_scan(main_url, subpages_list)
	show_header(main_url, subpages_list)
	scan_urls(urls_to_scan)
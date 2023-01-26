#!/usr/bin/python3

import argparse
import re
import sys
import requests
import http
import cfg
import colors


def get_arguments():

	parser = argparse.ArgumentParser(description=cfg.parser_description, 
									formatter_class=argparse.RawDescriptionHelpFormatter)
	parser.add_argument(cfg.url_short_opt, cfg.url_long_opt, metavar=cfg.url_metavar, type=str, 
						help=cfg.url_help, required=True)
	parser.add_argument(cfg.wordlist_short_opt, cfg.wordlist_long_opt, metavar=cfg.wordlist_metavar, 
						type=argparse.FileType(cfg.file_read_mode, encoding=cfg.encd_utf8), 
						help=cfg.wordlist_help, required=True)
	args = parser.parse_args()

	if not re.match(cfg.url_regex, args.url):
		
		print(cfg.invalid_url_error_msg)
		parser.print_help()
		sys.exit()

	return args.url, args.wordlist.name


def create_urls_to_scan(main_url, subpages_list):

	urls_to_scan = []
	subpages_content = open(subpages_list, cfg.file_read_mode)

	for subpage in subpages_content:
		
		if main_url[-1] == cfg.url_join_char:
			
			url = main_url + subpage.strip()
		
		else:
		
			url = main_url + cfg.url_join_char + subpage.strip()
		
		urls_to_scan.append(url)

	subpages_content.close()

	return urls_to_scan


def scan_urls(urls_to_scan):

	for url in urls_to_scan:
		
		url_request = requests.get(url)
		msg = cfg.url_output_msg_template.replace(cfg.url_status_desc_var, 
												http.HTTPStatus(url_request.status_code).phrase)
		msg = msg.replace(cfg.url_status_code_var, str(url_request.status_code))

		if url_request.status_code == cfg.http_code_ok:

			print(cfg.bullet_char, url, colors.green.format(msg))

		elif url_request.status_code != cfg.http_code_not_found:
			
			print(cfg.bullet_char, url, colors.yellow.format(msg))


def show_header(main_url, subpages_list):

	print(colors.yellow.format(cfg.output_line))
	print(colors.blue.format(cfg.output_header.center(cfg.output_line_length)))
	print(colors.yellow.format(cfg.output_line))
	print(colors.red.format(cfg.output_url.ljust(cfg.output_ljust)), cfg.output_var_sep, 
			str(main_url))
	print(colors.red.format(cfg.output_wordlist.ljust(cfg.output_ljust)), cfg.output_var_sep, 
			str(subpages_list))
	print(colors.red.format(cfg.output_omit_sts_cd.ljust(cfg.output_ljust)), cfg.output_var_sep, 
			str(cfg.http_code_not_found))
	print(colors.yellow.format(cfg.output_line))
	print(colors.purple.format(cfg.output_start_scan_msg.center(cfg.output_line_length)))
	print(colors.yellow.format(cfg.output_line))


def show_footer():

	print(colors.yellow.format(cfg.output_line))
	print(colors.purple.format(cfg.output_end_scan_msg.center(cfg.output_line_length)))
	print(colors.yellow.format(cfg.output_line))

def close_program(exc):

	print(cfg.output_error_msg, str(exc))
	print(cfg.output_exit_msg)
	sys.exit()


if __name__ == "__main__":

	try:
		main_url, subpages_list = get_arguments()
		urls_to_scan = create_urls_to_scan(main_url, subpages_list)
		show_header(main_url, subpages_list)
		scan_urls(urls_to_scan)
		show_footer()
	except Exception as exc:
		close_program(exc)



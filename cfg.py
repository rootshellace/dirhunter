#!/usr/bin/python3


### Argument parser configuration

parser_description = '''
	dirhunter by rootshellace

	This is a tool used to brute force URLs for subpages.

	You need to pass 2 arguments, the URL to be scanned and 
	the file which contains the subpages to check.

	In case you need to access the page using a different port
	from the standard one, just append :[PORT] at the end of 
	the URL, replacing [PORT] with the number of the needed port.
	'''
url_short_opt = '-u'
url_long_opt = '--url'
url_metavar = "URL"
url_help = "URL to scan"
wordlist_short_opt = '-w'
wordlist_long_opt = '--wordlist'
wordlist_metavar = "WORDLIST"
wordlist_help = "File containing list of subpaths to check"
file_read_mode = 'r'
encd_utf8 = 'UTF-8'


### URL - validate and create configuration

url_regex = "^https?:\/\/(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}(:[0-9]{1,5})?(\/[a-zA-Z0-9@:%.\#~=+-_]*)*$"
invalid_url_error_msg = "Invalid URL!"
url_join_char = '/'


### URL scan output configuration

url_status_desc_var = "HTTP_STATUS_DESC"
url_status_code_var = "HTTP_STATUS_CODE"
url_output_msg_template = "-> HTTP_STATUS_DESC (Status : HTTP_STATUS_CODE)"
http_code_ok = 200
http_code_not_found = 404


### Output header configuration

bullet_char = "[•]"
output_header = "dirhunter by rootshellace - scan URLs for subpages"
output_start_scan_msg = "Started scanning..."
output_end_scan_msg = "Scan complete!"
output_error_msg = "Error encountered:"
output_exit_msg = "The script will end!"
output_line_char = "="
output_line_length = 70
output_line = output_line_char * output_line_length
output_var_sep = ":"
output_url = "[+] URL"
output_wordlist = "[+] Wordlist"
output_omit_sts_cd = "[+] Omitted status code"
output_ljust = 25

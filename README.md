# dirhunter by rootshellace

This is a Python tool that can be used in pentesting for enumeration. It scans a website for subpages.

## Usage

There are 2 arguments required by this script, both mandatory:

- URL of target website
- text file containing directories to scan

If you run it without any arguments (or only one), it will show an error message saying which of them is missing.

```
usage: dirhunter.py [-h] -u URL -w WORDLIST
dirhunter.py: error: the following arguments are required: -u/--url, -w/--wordlist
```

To see the help message, just execute the script with *-h* argument.
```bash
./dirhunter.py -h
```
It will display the full message, just like below:
```
usage: dirhunter.py [-h] -u URL -w WORDLIST

	dirhunter by rootshellace

	This is a tool used to brute force URLs for subpages.

	You need to pass 2 arguments, the URL to be scanned and 
	the file which contains the subpages to check.

	In case you need to access the page using a different port
	from the standard one, just append :[PORT] at the end of 
	the URL, replacing [PORT] with the number of the needed port.
	

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     URL to scan
  -w WORDLIST, --wordlist WORDLIST
                        File containing list of subpaths to check
```
## Arguments

* **URL**

This URL must be valid, otherwise it will throw an error message and print the help message. In case the web server has to be accessed on a different port, just add :[PORT] at the end of the URL, replacing [PORT] with the corresponding number.

* **Directory list**

This file needs to be present on your local hard drive and the path provided as argument must be valid. 

## Prerequisites

First, you must have Python 3 installed. I have tested the tool on Python 3.9.2 version. 
I have also used a couple of modules : *argparse*, *re*, *sys*, *requests*, *http*. Also, the other 2 files, *colors.py* and *cfg.py*, must be placed in the same directory with our main script.

All of them are default Python modules (or they should be), except *requests*. This one must be installed separately. Using pip3, just run this command:

```
pip3 install requests
```

In case any of the earlier mentioned modules is missing on your side, just run the same command as above, replacing *requests* with the name of your missing module.
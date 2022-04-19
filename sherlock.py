#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import requests
import argparse
import os
import time
import sys


G = '\033[92m'
Y = '\033[93m'
R = '\033[91m'
W = '\033[0m'


def banner():
	print("                                                       ______              ")
	print("                                                    .-'      `-.           ")
	print("                                                  .'            `.         ")
	print("                                                 /                \        ")
	print("                                                ;                 ;`       ")
	print("                                                |                 |;       ")
	print("      _               _            _            ;                 ;|       ")
	print("     | |             | |          | |           '\               / ;       ")
	print("  ___| |__   ___ _ __| | ___   ___| | __         \`.           .' /        ")
	print(" / __| '_ \ / _ \ '__| |/ _ \ / __| |/ /          `.`-._____.-' .'         ")
	print(" \__ \ | | |  __/ |  | | (_) | (__|   <             / /`_____.-'           ")
	print(" |___/_| |_|\___|_|  |_|\___/ \___|_|\_\           / / /                   ")
	print("                                                  / / /                    ")
	print(" Version 1.0 - subdomain's finder tool           / / /                     ")
	print("         Made by BBND                           / / /                      ")
	print("                                               / / /                       ")
	print("                                              / / /                        ")
	print("                                             / / /                         ")
	print("                                             \/_/                          ")



def menu():
    print("Usage : This tool is a python script used to get all subdomains from a https url without brute forcing.")
    print("------------------------------------------------------------------------\n")
    print('Options : ')
    print(' -d [URL] ,--domain [URL]			Set an url to get all subdomains. \n')
    print(' -o [file] ,--output [file]		Set the output file to save results (optional) \n')
    print('	-h , --help						Show documentation. \n')
    print("------------------------------------------------------------------------\n")

def anim():
    array = ['[]']
    for i in range(1, 61):
        text = ''
        for j in range(i):
            text = text + '#'
        array.append('[' + R + text + W + ']')
    return array


def loading():
	animation = anim()
	for i in range(1, 61):
		time.sleep(0.1)
		sys.stdout.write("\r" + "Loading : " + animation[i % len(animation)] + ' ' + str(int(round(i * 5 / 3))) + '%')
		sys.stdout.flush()

def search(url, output=None):
	# Clean the url
	url = re.sub('.*www\.','',url,1).split('/')[0].strip()
	subdomains = []

	r =  requests.get("https://crt.sh/?q="+url+"&output=json")
	
	if r.status_code != 200:
		print(R + "[X] Information not available!" + W) 
		exit(1)

	print(G + "\n[!] ---- TARGET: {d} ---- [!] {w} \n".format(d=url,w=W))

	loading()

	print("\n")

	for (key,value) in enumerate(r.json()) :
		for element in value['name_value'].split('\n') :
			subdomains.append(element)

	subdomains = set(sorted(subdomains))

	for subdomain in subdomains :		
			print(R + "[ + ] " + W + subdomain)
			if output is not None : 
				with open(output,"a") as f:
					f.write(subdomain + '\n')
					f.close()
	print("\n")


if __name__ == '__main__':
	os.system("clear")
	banner()
	menu()

	parsing = argparse.ArgumentParser(description="This tool is a python script used to get all subdomains from a https url without brute forcing.")

	parsing.add_argument('-d', '--domain', dest='url_subdomain', help='Set an url to get all subdomains.')
	parsing.add_argument('-o', '--output', dest='output', help='Set the output file to save results (optional)')
	args = parsing.parse_args()
	
	url_subdomain = args.url_subdomain
	url_output = args.output

	if url_subdomain is not None:
		if url_output is None :
			search(url_subdomain)
		else :
			search(url_subdomain, url_output)
	else :
		pass
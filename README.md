# SherlockTool
This tool allows you to display all the website subdomains without using the brute force method. 

⛔If the tool is used for malicious purposes, we will not be liable.⛔

## About the tool

- **Subdomain finder: extract all subdomains from crt service**

## Install

```sh
$ git clone https://github.com/BBND/SherlockTool
$ cd SherlockTool
```

## How it works ?

| Argument | Description |
| ------ | ------ |
| -h, --help | Show documentation. |
| -d [URL] ,--domain [URL] | Set an url to get all subdomains. |
| -o [file] ,--output [file]  | Set the output file to save results (optional) |

## Usage Examples

```sh
$ python  sherlock.py --domain www.google.com
```

```sh
$ python  sherlock.py --domain www.google.com --output resultats.txt
```

## Author
[BBND](https://www.bbnd.eu)


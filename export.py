#! encoding: utf8

from sys import argv
from bs4 import BeautifulSoup

inFile = argv[1]
outFile = inFile.replace('html', 'txt')
soup = BeautifulSoup(open(inFile), 'html5')

with open(outFile, 'w') as f:
    for tag in soup.find_all('font'):
        if tag.div:
            f.write('\n')
        else:
            f.write(tag.string.encode('utf8'))

"""wcount.py: count words from an Internet file.
__author__ ="陈新杨"
__pkuid__  ="1800011830"
__email__  ="1800011830@pku.edu.cn"
"""

import sys
import re
from urllib.request import urlopen
from collections import Counter

def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line.
    """
    result = Counter(lines)
    for i in range(topn):
	    print(result.most_common(topn)[i][0]+\
        " "*(12-len(result.most_common(topn)[i][0]))+\
        str(result.most_common(topn)[i][1])+'\n')


if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)
    
    if len(sys.argv) == 3:
        topn = int(sys.argv[2])###判断是否输入了所求的单词个数

    if len(sys.argv) > 1:
        doc = urlopen(sys.argv[1])
        docstr = doc.read()
        jstr = docstr.decode()
        lines = re.findall(r'\w+',str.lower(jstr)) 
        
    print(wcount(lines,topn))


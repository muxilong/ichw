
"""wcount.py: count words from an Internet file.

__author__ = "Zhangsan"
__pkuid__  = "1600012345"
__email__  = "zhangsan@pku.edu.cn"
"""

import sys
from urllib.request import urlopen
from urllib import request
from urllib import error
import string

dic = dict()                                           #建一个空字典用来计数
def convert(line):                                     #函数的作用是，处理一行的字节流，转化为列表
    sen = line.decode('UTF-8-sig')                              #解码  
    sen = sen.lower()
    for i in range(len(sen)):
        if sen[i] in string.punctuation and sen[i] != '-':      #处理标点
            if sen[i] != "'" or sen[i+1] != 's':                #保留‘s
                sen = sen.replace(sen[i],' ')
    t = sen.split()
    return t
def count(alist):                    #对convert函数得到的列表进行计数，存到字典中
    global dic
    for element in alist:
        dic[element] = dic.get(element,0) + 1
    return dic    

def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """
                                        #对字典进行排序，按顺序输出单词和单词频率
    global dic
    for line in lines:                  #一行一行地计数
        dic = count(convert(line))
    sorted_list = sorted(dic.items(),key = lambda t:t[1])    #排序   
    
    inf = min(topn,len(dic))        #选择其中的小的，为了在topn很大时，输出全部的单词  
    
    for i in range(inf):
        print(sorted_list[-i-1][0],end = '\t')
        if len(sorted_list[-i-1][0]) <= 7:
            print(' ',end = '\t')
        print(sorted_list[-i-1][1],end = '\t\n')
        #这样的输出，保证单词和单词的频率对齐    
    pass
def main():
    try:
        response = request.urlopen(sys.argv[1])
    except error.HTTPError as e:
        print('HTTPError 异常错误 ')
        print('reason:'+str(e.reason), 'code:'+str(e.code), 'headers:'+str(e.headers), sep='\n')
    except error.URLError as e:
        print('URLError 异常错误 ')
        print('reason:'+str(e.reason))
    else:
        print('Request Successfully')
                                            # 判断遇到的URLError HttpError        
    fin = urlopen(sys.argv[1])
    fin_ = fin.readlines()                  # 一行一行读入文件
    
    if len(sys.argv) == 2:
        wcount(fin_,10)                     # 如果没输入参数，输出前10个
    else:
        wcount(fin_,int(sys.argv[2]))


if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)
    else:
        main()

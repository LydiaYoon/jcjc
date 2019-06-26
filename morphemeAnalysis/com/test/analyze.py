# -*- coding:utf-8 -*-
import os
import pymongo
import cx_Oracle

from collections import Counter

from konlpy.corpus import kolaw
from konlpy.tag import Komoran
from konlpy.tag import Hannanum
from konlpy.utils import concordance, pprint


# oracle의 쿼리 결과를 Dict로 받기위한 메서드
def makeDictFactory(cursor):
    columnNames = [d[0] for d in cursor.description]
    def createRow(*args):
        return dict(zip(columnNames, args))
    return createRow


class konlpy():
    os.environ["NLS_LANG"] = ".AL32UTF8" # UTF-8 : .AL32UTF8, CP949 : .KO16MSWIN949
    con = pymongo.MongoClient("localhost", 27017)['jcjc']
    conn = cx_Oracle.connect('bigdata/admin1234@localhost:1521/xe') # oracle 서버와 연결 (connection 맺기)
    
    # userdic : 단어 추출에서 제외할 목록들이 들어갈 단어사전
    komoran = Komoran(userdic='C:\\Project\\morphemeAnalysis\\com\\test\\user_dic.txt')
    hannanum = Hannanum()
    
    def analyze(self):
        count = 0
        for item in self.con['billInfo'].find().limit(5): 
            count += 1
            billid = item.get('billid')
            billname = item.get('billname')
            summary = item.get('summary') 
            
            # komoran은 빈줄이 있으면 에러가 남
            summary = summary.replace("\r", "").replace("\n", " ").replace("\t", " ")
            summary = summary.replace("？", "ㆍ").replace(",", "")
            
            print(count, "번째")
            print(billname)
            print(summary)
#             print(item.get('summary').replace("\n", " ").replace("？", "ㆍ"))
            
            nouns = self.komoran.nouns(summary)
            
#             cnt = Counter(nouns)
#             pprint(cnt.most_common(10))
            print(nouns)
            print("==========================================================")


if __name__ == '__main__':
    obj = konlpy()
    obj.analyze()
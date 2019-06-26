# -*- coding:utf-8 -*-
from pymongo import MongoClient
import cx_Oracle
import os
from collections import defaultdict


def input():
    
    os.environ["NLS_LANG"] = ".AL32UTF8" # UTF-8 : .AL32UTF8, CP949 : .KO16MSWIN949
    
    conn = cx_Oracle.connect('bigdata/admin1234@localhost:1521/xe') # oracle 서버와 연결 (connection 맺기)
    print(conn.version) # connection 확인
    db = conn.cursor() # cursor 객체 얻어오기
    
    # mongoDB 연결
    mongo = pyMongo()
    items = mongo.find_info()

    # politicianInfo insert
    sql_insert = """insert into politician
    (politician_no, politician_num, 
    politician_kor_name, politician_hj_name, politician_eng_name,
    reele_gbn_name, orig_name, politician_jpg_link)
    values(
    :politician_no, :politician_num, 
    :politician_kor_name, :politician_hj_name, :politician_eng_name, 
    :reele_gbn_name, :orig_name, :politician_jpg_link)"""

    for item in items:
        db.execute(sql_insert, 
                   politician_no = item['deptcd'], 
                   politician_num = item['num'],
                   politician_kor_name = item['empnm'], 
                   politician_hj_name = item['hjnm'],  
                   politician_eng_name = item['engnm'], 
                   reele_gbn_name = item['reelegbnnm'], 
                   orig_name = item['orignm'], 
                   politician_jpg_link = item['jpglink']
                   )

        detail_items = mongo.find_detail(item['deptcd'], item['num'])
        for detail_item in detail_items:
        
            row = {} # Dict 객체 생성
            row['deptcd'] = item['deptcd']
            row['num'] = item['num']
            row['bth_date'] = detail_item['bthdate']
            row['poly_name'] = detail_item['polynm']
            
            if 'shrtnm' in detail_item:
                row['shrt_name'] = detail_item['shrtnm']
            else:
                row['shrt_name'] = ''
            
            if 'electionnum' in detail_item:
                row['election_name'] = detail_item['electionnum']
            else:
                row['election_name'] = ''
                
            if 'assemtel' in detail_item:
                row['assem_tel'] = detail_item['assemtel']
            else:
                row['assem_tel'] = ''
                
            if 'assemhomep' in detail_item:
                row['assem_homep'] = detail_item['assemhomep']
            else:
                row['assem_homep'] = ''
            
            if 'assememail' in detail_item:
                row['assem_email'] = detail_item['assememail']
            else:
                row['assem_email'] = ''
            
            if 'hbbycd' in detail_item:
                row['hbby_cd'] = detail_item['hbbycd']
            else:
                row['hbby_cd'] = ''
                
            if 'examcd' in detail_item:
                row['exam_cd'] = detail_item['examcd']
            else:
                row['exam_cd'] = ''
        
        # politicianDetail update
        sql_update = """update politician
        set 
        bth_date = to_date(:bth_date, 'YYYYMMDD'),
        poly_name = :poly_name, 
        shrt_name = :shrt_name, 
        election_name = :election_name,
        assem_tel = :assem_tel,
        assem_homep = :assem_homep,
        assem_email = :assem_email,
        hbby_cd = :hbby_cd,
        exam_cd = :exam_cd
        where
        politician_no = :politician_no
        and
        politician_num = :politician_num"""
        
        db.execute(sql_update, 
                   bth_date = row['bth_date'], 
                   poly_name = row['poly_name'],
                   shrt_name = row['shrt_name'], 
                   election_name = row['election_name'],  
                   assem_tel = row['assem_tel'], 
                   assem_homep = row['assem_homep'], 
                   assem_email = row['assem_email'], 
                   hbby_cd = row['hbby_cd'],
                   exam_cd = row['exam_cd'],
                   politician_no = row['deptcd'],
                   politician_num = row['num']
                   )
 
    print("입력 완료!")
    conn.commit()
    
#     politicianInfo insert 결과 조회
    db.execute("SELECT * FROM politician")
    for i in db:
        print(i)
      
    db.close() # cursor 객체 닫기
    conn.close() # oracle 서버와 연결 끊기



class pyMongo(object):
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client['jcjc']
        
    def find_info(self):
        res = self.db.politicianInfo.find()
        return res
    
    def find_detail(self, deptcd, num):
        res = self.db.politicianDetail.find({"deptcd":deptcd, "num":num})
        return res

if __name__ == '__main__':
    input()
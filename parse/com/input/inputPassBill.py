# -*- coding:utf-8 -*-

import os
import cx_Oracle
from pymongo import MongoClient
import pymongo


class inputBill():
    os.environ["NLS_LANG"] = ".AL32UTF8" # UTF-8 : .AL32UTF8, CP949 : .KO16MSWIN949
    con = pymongo.MongoClient("localhost", 27017)['jcjc'] # mongoDB Client Connection
    conn = cx_Oracle.connect('bigdata/admin1234@localhost:1521/xe') # cx_Oracle Connection
    
    def input(self):
        
        print(self.conn.version) # cx_Oracle connection 확인
        oracle = self.conn.cursor() # cx_Oracle cursor 객체 얻어오기
        
        count = 0
             
        # passBill insert
        items = self.con['passBill'].find()
             
        # passBill query
        sql_insert = """insert into bill
        (bill_no, bill_name,
        politician_no, proposer, proposer_hj, proposer_kind,
        propose_dt, submit_dt, committee_name,
        proc_dt, general_result, 
        summary)
        values(
        :bill_no, :bill_name,
        :politician_no, :proposer, 
        :proposer_hj, :proposer_kind,
        to_date(:propose_dt, 'YYYY-MM-DD'), 
        to_date(:submit_dt, 'YYYY-MM-DD'), 
        :committee_name,
        to_date(:proc_dt, 'YYYY-MM-DD'), 
        :general_result,
        :summary)"""
          
        for item in items:
            print("item :\t", item)
            count += 1
             
            row = {} # Dict 객체 생성
            row['bill_no'] = item['billno']
            row['bill_name'] = item['billname']
            row['proposer'] = item['proposer']
            row['proposer_kind'] = item['proposerkind']
            row['propose_dt'] = item['proposedt']
            row['proc_dt'] = item['procdt']
            row['general_result'] = item['generalresult']
     
            if 'submitdt' in item:
                row['submit_dt'] = item['submitdt']
            else:
                row['submit_dt'] = ''
              
            if 'committeename' in item:
                row['committee_name'] = item['committeename']
            else:
                row['committee_name'] = ''
             
             
            # summary
            for info_item in self.con['billInfo'].find({"billno" : row['bill_no']}): 
                if 'summary' in info_item:
                    row['summary'] = info_item['summary']
                else:
                    row['summary'] = ''
                    
            
            # politician_no
            # mongoDB에 찾는 정치인 정보가 없을 수 있기 때문에 정치인번호와 한자이름을 None으로 초기화
            row['politician_no'] = '' 
            row['proposer_hj'] = ''
            
            index = row['proposer'].find('의원') # 제안자 컬럼에서 '의원'문자열의 인덱스 위치를 찾아서 저장 
            if row['proposer_kind'] == '의원' and index > -1: # 제안자 분류가 '의원'이고 제안자 컬럼에 '의원'문자열이 있을 경우
                kor_name = row['proposer'][:index] # 0번째 인덱스부터 '의원'문자열 앞까지 잘라서 저장
                if kor_name != '김성태' and kor_name != '최경환': # 동명이인(김성태, 최경환) 별도 처리하기 위해 제외
                    for no_item in self.con['politicianInfo'].find({"empnm": kor_name}):
                            print(no_item['deptcd'], no_item['empnm'], no_item['hjnm'])
                            row['politician_no'] = no_item['deptcd']
                            row['proposer'] = no_item['empnm']
                            row['proposer_hj'] = no_item['hjnm']
                    
            print("row :\t", row)

            # passBill execute
            oracle.execute(sql_insert,
                       bill_no = row['bill_no'],
                       bill_name = row['bill_name'],
                       politician_no = row['politician_no'],
                       proposer = row['proposer'],
                       proposer_hj = row['proposer_hj'],
                       proposer_kind = row['proposer_kind'],
                       propose_dt = row['propose_dt'],
                       submit_dt = row['submit_dt'],
                       committee_name = row['committee_name'],
                       proc_dt = row['proc_dt'],
                       general_result = row['general_result'] ,
                       summary = row['summary']                          
                       )
            print(count, "\tpassBill insert\t")
            print("===========================================================================") 
             
                 
        print("passBill 입력 완료!")
        self.conn.commit()
        

if __name__ == '__main__':
    obj = inputBill()
    obj.input()
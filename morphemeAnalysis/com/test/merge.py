# -*- coding:utf-8 -*-
import os
import pymongo
import pandas as pd


class merge():
    os.environ["NLS_LANG"] = ".AL32UTF8" # UTF-8 : .AL32UTF8, CP949 : .KO16MSWIN949
    con = pymongo.MongoClient("localhost", 27017)['jcjc'] 
    
    def merge(self):
        
        for item in self.con['billAnalysis'].find():
            
            df = pd.DataFrame()
        
        
        
if __name__ == '__main__':
    obj = merge()
    obj.merge()
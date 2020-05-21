import requests 
import zipfile
from datetime import date,timedelta
import pandas as pd
import csv

class nseindia:

    def find_symbol(self,symbol):
        #df = pd.read_csv("files/cm"+str(date)+"bhav.csv")
        #print(df)
        #print(df['SYMBOL'])
        weekend = set([5, 6])
       
        count=0
        for i in range(1,31):
            try:
            
                delta_date = date(2020,4,15) + timedelta(days=i)
                    #print(delta_date.weekday())
                    
                if delta_date.weekday() not in weekend:
                        #print("in")
                    date_str1=date.strftime(delta_date,'%d %b %Y')
                    #date_str.append(date_str1)
                    split_date=date_str1.split(" ")
                    #print(split_date)
                    #print(split_date[0])
                
                    df = pd.read_csv("files/cm"+str(split_date[0])+str(split_date[1].upper())+str(split_date[2])+"bhav.csv")
                    if count == 0 :
                        #print("count=0")
                        df1=pd.DataFrame(df[df['SYMBOL']==symbol])
                        #print(df1)
                        count=count+1
                        #print(count)
                    else:    
                        #print("count not 0")
                        df1=df1.append(df[df['SYMBOL']==symbol],ignore_index=True)
                    #print(df1)
            except:
                continue        
                    
                    
             
        print(df1[['SYMBOL','SERIES','OPEN','HIGH','LOW','CLOSE','LAST','PREVCLOSE','TOTTRDQTY','TIMESTAMP']]) 
        df2=pd.DataFrame(df1[['SYMBOL','SERIES','OPEN','HIGH','LOW','CLOSE','LAST','PREVCLOSE','TOTTRDQTY','TIMESTAMP']])
        print(df2)
        return df2        


        
    def symbol():
        df = pd.read_csv("files/cm02MAR2020bhav.csv")
        #print(df)
        #print(df['SYMBOL'])
        symbols=[]
        for i in df['SYMBOL']:
            symbols.append(i)

        return symbols

    def data():
        weekend = set([5, 6])
        count=0
        date_str=[]
        for i in range(1,31):
            try:
                count =count+1
                delta_date = date(2020,4,15) + timedelta(days=i)
                #print(delta_date.weekday())
                
                if delta_date.weekday() not in weekend:
                    #print("in")
                    date_str1=date.strftime(delta_date,'%d %b %Y')
                    date_str.append(date_str1)
                    split_date=date_str1.split(" ")
                    #print(split_date)
                    url = "https://archives.nseindia.com/content/historical/EQUITIES/2020/"+str(split_date[1].upper())+"/cm"+str(split_date[0])+str(split_date[1].upper())+str(split_date[2])+"bhav.csv.zip"
                    r = requests.get(url) 
                    with open("cm"+str(split_date[0])+str(split_date[1].upper())+str(split_date[2])+"bhav.csv.zip",'wb') as f: 
                
                
                        f.write(r.content) 


                    with zipfile.ZipFile("cm"+str(split_date[0])+str(split_date[1].upper())+str(split_date[2])+"bhav.csv.zip", 'r') as zip_ref:
                        zip_ref.extractall("files/")  
                    
            except:
                continue  
        return date_str

#dates=nseindia.symbol()    
#print(dates)

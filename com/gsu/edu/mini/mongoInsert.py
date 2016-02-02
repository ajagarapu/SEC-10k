'''
Created on Jan 29, 2016

@author: Ashwin
'''
import pymongo
from os.path import dirname
import os
from os import getcwd
import glob
# Connection to Mongo DB
conn = pymongo.MongoClient()
print("Connected successfully!!!")
db = conn.miniproject

mypath=dirname(getcwd())+"\\data"
#file = open(mypath+"\\0000021344_COCA COLA CO\\10-K\\0000021344-12-000007_0000021344_COCA COLA CO_10-K\\html\\2012_10-K_0000021344-12-000007_a20111231ex-311.htm",'r')
readtxt = ''
#print(glob.glob(os.path.join(mypath+"\\0000021344_COCA COLA CO\\10-K\\0000021344-12-000007_0000021344_COCA COLA CO_10-K\\html",'*',"*-k.htm")))
#print(mypath)
#print(os.path.abspath(os.path.curdir)) 
#print(os.listdir(mypath+"\\0000021344_COCA COLA CO\\10-K\\0000021344-12-000007_0000021344_COCA COLA CO_10-K\\html")) 

'''
This is for Coca Cola Year 2008
'''
for filename in glob.iglob(mypath+"\\0000021344_COCA COLA CO\\10-K\\0001047469-09-001875_0000021344_COCA COLA CO_10-K\\html\\*-k.htm"):
    file = open(filename,'r')
    readtxt = file.read()
    file.close()
exhibit=[]
for filename in glob.iglob(mypath+"\\0000021344_COCA COLA CO\\10-K\\0001047469-09-001875_0000021344_COCA COLA CO_10-K\\html\\*ex-*.htm"):
    file = open(filename,'r')
    exhibit.append(file.read())
    file.close()
        
result = db.sec10k.insert_one(
                          {"company" : {"name":"Coca Cola",
                                        "secIdentifier":"001-02217",
                                        "address":{
                                                   "street1:":"One Coca-Cola Plaza",
                                                   "city":"Atlanta",
                                                   "state":"GA",
                                                   "zip":"30313",
                                                   "BUSINESS PHONE":"404-676-2121"
                                                   }
                                        },
                           "year":"2008",
                           "form10k":readtxt,
                           "exhibit":exhibit,
                           "financialData":{
                                           "costofgoodssold":11374,
                                           "inventories":2187,
                                           "totalassets":40519,
                                           "totalcurrentliabilities":12988,
                                           "longtermdebt":2781,
                                           "operationalincome":8446,
                                           "revenues":31944,
                                           "grossprofit":20570
                                           }
                           }
                          )

'''
This is for Coca Cola Year 2009
'''
for filename in glob.iglob(mypath+"\\0000021344_COCA COLA CO\\10-K\\0001047469-10-001476_0000021344_COCA COLA CO_10-K\\html\\*-k.htm"):
    file = open(filename,'r')
    readtxt = file.read()
    file.close()
exhibit=[]
for filename in glob.iglob(mypath+"\\0000021344_COCA COLA CO\\10-K\\0001047469-10-001476_0000021344_COCA COLA CO_10-K\\html\\*ex-*.htm"):
    file = open(filename,'r')
    exhibit.append(file.read())
    file.close()
        
result = db.sec10k.insert_one(
                          {"company" : {"name":"Coca Cola",
                                        "secIdentifier":"001-02217",
                                        "address":{
                                                   "street1:":"One Coca-Cola Plaza",
                                                   "city":"Atlanta",
                                                   "state":"GA",
                                                   "zip":"30313",
                                                   "BUSINESS PHONE":"404-676-2121"
                                                   }
                                        },
                           "year":"2009",
                           "form10k":readtxt,
                           "exhibit":exhibit,
                           "financialData":{
                                           "costofgoodssold":11088,
                                           "inventories":2354,
                                           "totalassets":48671,
                                           "totalcurrentliabilities":13721,
                                           "longtermdebt":5059,
                                           "operationalincome":8231,
                                           "revenues":30990,
                                           "grossprofit":19902
                                           }
                           }
                          )
'''
This is for Coca Cola Year 2010
'''
for filename in glob.iglob(mypath+"\\0000021344_COCA COLA CO\\10-K\\0001047469-11-001506_0000021344_COCA COLA CO_10-K\\html\\*-k.htm"):
    file = open(filename,'r')
    readtxt = file.read()
    file.close()
exhibit=[]
for filename in glob.iglob(mypath+"\\0000021344_COCA COLA CO\\10-K\\0001047469-11-001506_0000021344_COCA COLA CO_10-K\\html\\*ex-*.htm"):
    file = open(filename,'r')
    exhibit.append(file.read())
    file.close()
        
result = db.sec10k.insert_one(
                          {"company" : {"name":"Coca Cola",
                                        "secIdentifier":"001-02217",
                                        "address":{
                                                   "street1:":"One Coca-Cola Plaza",
                                                   "city":"Atlanta",
                                                   "state":"GA",
                                                   "zip":"30313",
                                                   "BUSINESS PHONE":"404-676-2121"
                                                   }
                                        },
                           "year":"2010",
                           "form10k":readtxt,
                           "exhibit":exhibit,
                           "financialData":{
                                           "costofgoodssold":12693,
                                           "inventories":2650,
                                           "totalassets":72921,
                                           "totalcurrentliabilities":18508,
                                           "longtermdebt":14041,
                                           "operationalincome":8413,
                                           "revenues":35119,
                                           "grossprofit":22426
                                           }
                           }
                          )

'''
This is for Coca Cola Year 2011
'''
for filename in glob.iglob(mypath+"\\0000021344_COCA COLA CO\\10-K\\0000021344-12-000007_0000021344_COCA COLA CO_10-K\\html\\*-k.htm"):
    file = open(filename,'r')
    readtxt = file.read()
    file.close()
exhibit=[]
for filename in glob.iglob(mypath+"\\0000021344_COCA COLA CO\\10-K\\0000021344-12-000007_0000021344_COCA COLA CO_10-K\\html\\*ex-*.htm"):
    file = open(filename,'r')
    exhibit.append(file.read())
    file.close()
        
db.sec10k.insert_one(
                          {"company" : {"name":"Coca Cola",
                                        "secIdentifier":"001-02217",
                                        "address":{
                                                   "street1:":"One Coca-Cola Plaza",
                                                   "city":"Atlanta",
                                                   "state":"GA",
                                                   "zip":"30313",
                                                   "BUSINESS PHONE":"404-676-2121"
                                                   }
                                        },
                           "year":"2011",
                           "form10k":readtxt,
                           "exhibit":exhibit,
                           "financialData":{
                                           "costofgoodssold":18215,
                                           "inventories":3092,
                                           "totalassets":79974,
                                           "totalcurrentliabilities":24283,
                                           "longtermdebt":13656,
                                           "operationalincome":10173,
                                           "revenues":46542,
                                           "grossprofit":28327
                                           }
                           }
                          )
'''
This is for Coca Cola Year 2012
'''
for filename in glob.iglob(mypath+"\\0000021344_COCA COLA CO\\10-K\\0000021344-13-000007_0000021344_COCA COLA CO_10-K\\html\\*-k.htm"):
    file = open(filename,'r')
    readtxt = file.read()
    file.close()
exhibit=[]
for filename in glob.iglob(mypath+"\\0000021344_COCA COLA CO\\10-K\\0000021344-13-000007_0000021344_COCA COLA CO_10-K\\html\\*ex-*.htm"):
    file = open(filename,'r')
    exhibit.append(file.read())
    file.close()
        
result = db.sec10k.insert_one(
                          {"company" : {"name":"Coca Cola",
                                        "secIdentifier":"001-02217",
                                        "address":{
                                                   "street1:":"One Coca-Cola Plaza",
                                                   "city":"Atlanta",
                                                   "state":"GA",
                                                   "zip":"30313",
                                                   "BUSINESS PHONE":"404-676-2121"
                                                   }
                                        },
                           "year":"2012",
                           "form10k":readtxt,
                           "exhibit":exhibit,
                           "financialData":{
                                           "costofgoodssold":19053,
                                           "inventories":3264,
                                           "totalassets":86174,
                                           "totalcurrentliabilities":27821,
                                           "longtermdebt":14736,
                                           "operationalincome":10779,
                                           "revenues":48017,
                                           "grossprofit":28964
                                           }
                           }
                          )
'''
This is for Coca Cola Year 2013
'''
for filename in glob.iglob(mypath+"\\0000021344_COCA COLA CO\\10-K\\0000021344-14-000008_0000021344_COCA COLA CO_10-K\\html\\*-k.htm"):
    file = open(filename,'r')
    readtxt = file.read()
    file.close()
exhibit=[]
for filename in glob.iglob(mypath+"\\0000021344_COCA COLA CO\\10-K\\0000021344-14-000008_0000021344_COCA COLA CO_10-K\\html\\*ex-*.htm"):
    file = open(filename,'r')
    exhibit.append(file.read())
    file.close()
        
result = db.sec10k.insert_one(
                          {"company" : {"name":"Coca Cola",
                                        "secIdentifier":"001-02217",
                                        "address":{
                                                   "street1:":"One Coca-Cola Plaza",
                                                   "city":"Atlanta",
                                                   "state":"GA",
                                                   "zip":"30313",
                                                   "BUSINESS PHONE":"404-676-2121"
                                                   }
                                        },
                           "year":"2013",
                           "form10k":readtxt,
                           "exhibit":exhibit,
                           "financialData":{
                                           "costofgoodssold":18421,
                                           "inventories":3277,
                                           "totalassets":90055,
                                           "totalcurrentliabilities":27811,
                                           "longtermdebt":19154,
                                           "operationalincome":10228,
                                           "revenues":46854,
                                           "grossprofit":28433
                                           }
                           }
                          )

'''
This is for Coca Cola Year 2014
'''
for filename in glob.iglob(mypath+"\\0000021344_COCA COLA CO\\10-K\\0000021344-15-000005_0000021344_COCA COLA CO_10-K\\html\\*-k.htm"):
    file = open(filename,'r')
    readtxt = file.read()
    file.close()
exhibit=[]
for filename in glob.iglob(mypath+"\\0000021344_COCA COLA CO\\10-K\\0000021344-15-000005_0000021344_COCA COLA CO_10-K\\html\\*ex-*.htm"):
    file = open(filename,'r')
    exhibit.append(file.read())
    file.close()
        
result = db.sec10k.insert_one(
                          {"company" : {"name":"Coca Cola",
                                        "secIdentifier":"001-02217",
                                        "address":{
                                                   "street1:":"One Coca-Cola Plaza",
                                                   "city":"Atlanta",
                                                   "state":"GA",
                                                   "zip":"30313",
                                                   "BUSINESS PHONE":"404-676-2121"
                                                   }
                                        },
                           "year":"2014",
                           "form10k":readtxt,
                           "exhibit":exhibit,
                           "financialData":{
                                           "costofgoodssold":17889,
                                           "inventories":3100,
                                           "totalassets":92023,
                                           "totalcurrentliabilities":32374,
                                           "longtermdebt":19063,
                                           "operationalincome":9708,
                                           "revenues":45998,
                                           "grossprofit":28109
                                           }
                           }
                          )

'''
This is for DUPONT E I DE NEMOURS & CO Year 2008
'''
for filename in glob.iglob(mypath+"\\0000030554_DUPONT E I DE NEMOURS & CO\\10-K\\0000893220-09-000276_0000030554_DUPONT E I DE NEMOURS & CO_10-K\\html\\*e10vk.htm"):
    file = open(filename,'r')
    readtxt = file.read()
    file.close()
exhibit=[]
for filename in glob.iglob(mypath+"\\0000030554_DUPONT E I DE NEMOURS & CO\\10-K\\0000893220-09-000276_0000030554_DUPONT E I DE NEMOURS & CO_10-K\\html\\*xev*.htm"):
    file = open(filename,'r')
    exhibit.append(file.read())
    file.close()
        
result = db.sec10k.insert_one(
                          {"company" : {"name":"DUPONT E I DE NEMOURS & CO",
                                        "secIdentifier":"001-00815",
                                        "address":{
                                                   "street1:":"1007 MARKET ST",
                                                   "city":"WILMINGTON",
                                                   "state":"DE",
                                                   "zip":"19898",
                                                   "BUSINESS PHONE":"302-774-1000"
                                                   }
                                        },
                           "year":"2008",
                           "form10k":readtxt,
                           "exhibit":exhibit,
                           "financialData":{
                                           "costofgoodssold":24083,
                                           "inventories":5681,
                                           "totalassets":36209,
                                           "totalcurrentliabilities":9710,
                                           "longtermdebt":7638,
                                           "operationalincome":2391,
                                           "revenues":31836,
                                           "grossprofit":8288
                                           }
                           }
                          )
'''
This is for DUPONT E I DE NEMOURS & CO Year 2009
'''
for filename in glob.iglob(mypath+"\\0000030554_DUPONT E I DE NEMOURS & CO\\10-K\\0001047469-10-000954_0000030554_DUPONT E I DE NEMOURS & CO_10-K\\html\\*z10-k.htm"):
    file = open(filename,'r')
    readtxt = file.read()
    file.close()
exhibit=[]
for filename in glob.iglob(mypath+"\\0000030554_DUPONT E I DE NEMOURS & CO\\10-K\\0001047469-10-000954_0000030554_DUPONT E I DE NEMOURS & CO_10-K\\html\\*zex-*.htm"):
    file = open(filename,'r')
    exhibit.append(file.read())
    file.close()
        
result = db.sec10k.insert_one(
                          {"company" : {"name":"DUPONT E I DE NEMOURS & CO",
                                        "secIdentifier":"001-00815",
                                        "address":{
                                                   "street1:":"1007 MARKET ST",
                                                   "city":"WILMINGTON",
                                                   "state":"DE",
                                                   "zip":"19898",
                                                   "BUSINESS PHONE":"302-774-1000"
                                                   }
                                        },
                           "year":"2009",
                           "form10k":readtxt,
                           "exhibit":exhibit,
                           "financialData":{
                                           "costofgoodssold":19708,
                                           "inventories":5380,
                                           "totalassets":38185,
                                           "totalcurrentliabilities":9390,
                                           "longtermdebt":9528,
                                           "operationalincome":2802,
                                           "revenues":27328,
                                           "grossprofit":7620
                                           }
                           }
                          )
'''
This is for DUPONT E I DE NEMOURS & CO Year 2010
'''
for filename in glob.iglob(mypath+"\\0000030554_DUPONT E I DE NEMOURS & CO\\10-K\\0001047469-11-000602_0000030554_DUPONT E I DE NEMOURS & CO_10-K\\html\\*z10-k.htm"):
    file = open(filename,'r')
    readtxt = file.read()
    file.close()
exhibit=[]
for filename in glob.iglob(mypath+"\\0000030554_DUPONT E I DE NEMOURS & CO\\10-K\\0001047469-11-000602_0000030554_DUPONT E I DE NEMOURS & CO_10-K\\html\\*zex-*.htm"):
    file = open(filename,'r')
    exhibit.append(file.read())
    file.close()
        
result = db.sec10k.insert_one(
                          {"company" : {"name":"DUPONT E I DE NEMOURS & CO",
                                        "secIdentifier":"001-00815",
                                        "address":{
                                                   "street1:":"1007 MARKET ST",
                                                   "city":"WILMINGTON",
                                                   "state":"DE",
                                                   "zip":"19898",
                                                   "BUSINESS PHONE":"302-774-1000"
                                                   }
                                        },
                           "year":"2010",
                           "form10k":readtxt,
                           "exhibit":exhibit,
                           "financialData":{
                                           "costofgoodssold":23146,
                                           "inventories":5967,
                                           "totalassets":40410,
                                           "totalcurrentliabilities":9389,
                                           "longtermdebt":10137,
                                           "operationalincome":4267,
                                           "revenues":32733,
                                           "grossprofit":9587
                                           }
                           }
                          )

'''
This is for DUPONT E I DE NEMOURS & CO Year 2011
'''
for filename in glob.iglob(mypath+"\\0000030554_DUPONT E I DE NEMOURS & CO\\10-K\\0000030554-12-000005_0000030554_DUPONT E I DE NEMOURS & CO_10-K\\html\\*x10k.htm"):
    file = open(filename,'r')
    readtxt = file.read()
    file.close()
exhibit=[]
for filename in glob.iglob(mypath+"\\0000030554_DUPONT E I DE NEMOURS & CO\\10-K\\0000030554-12-000005_0000030554_DUPONT E I DE NEMOURS & CO_10-K\\html\\*xex*.htm"):
    file = open(filename,'r')
    exhibit.append(file.read())
    file.close()
        
result = db.sec10k.insert_one(
                          {"company" : {"name":"DUPONT E I DE NEMOURS & CO",
                                        "secIdentifier":"001-00815",
                                        "address":{
                                                   "street1:":"1007 MARKET ST",
                                                   "city":"WILMINGTON",
                                                   "state":"DE",
                                                   "zip":"19898",
                                                   "BUSINESS PHONE":"302-774-1000"
                                                   }
                                        },
                           "year":"2011",
                           "form10k":readtxt,
                           "exhibit":exhibit,
                           "financialData":{
                                           "costofgoodssold":24874,
                                           "inventories":7195,
                                           "totalassets":48492,
                                           "totalcurrentliabilities":11185,
                                           "longtermdebt":11736,
                                           "operationalincome":4281,
                                           "revenues":34423,
                                           "grossprofit":9549
                                           }
                           }
                          )
'''
This is for DUPONT E I DE NEMOURS & CO Year 2012
'''
for filename in glob.iglob(mypath+"\\0000030554_DUPONT E I DE NEMOURS & CO\\10-K\\0000030554-13-000006_0000030554_DUPONT E I DE NEMOURS & CO_10-K\\html\\*x10k.htm"):
    file = open(filename,'r')
    readtxt = file.read()
    file.close()
exhibit=[]
for filename in glob.iglob(mypath+"\\0000030554_DUPONT E I DE NEMOURS & CO\\10-K\\0000030554-13-000006_0000030554_DUPONT E I DE NEMOURS & CO_10-K\\html\\*xex*.htm"):
    file = open(filename,'r')
    exhibit.append(file.read())
    file.close()
        
result = db.sec10k.insert_one(
                          {"company" : {"name":"DUPONT E I DE NEMOURS & CO",
                                        "secIdentifier":"001-00815",
                                        "address":{
                                                   "street1:":"1007 MARKET ST",
                                                   "city":"WILMINGTON",
                                                   "state":"DE",
                                                   "zip":"19898",
                                                   "BUSINESS PHONE":"302-774-1000"
                                                   }
                                        },
                           "year":"2012",
                           "form10k":readtxt,
                           "exhibit":exhibit,
                           "financialData":{
                                           "costofgoodssold":21538,
                                           "inventories":7565,
                                           "totalassets":48492,
                                           "totalcurrentliabilities":11185,
                                           "longtermdebt":10465,
                                           "operationalincome":4281,
                                           "revenues":34423,
                                           "grossprofit":9549
                                           }
                           }
                          )
'''
This is for DUPONT E I DE NEMOURS & CO Year 2013
'''
for filename in glob.iglob(mypath+"\\0000030554_DUPONT E I DE NEMOURS & CO\\10-K\\0000030554-14-000002_0000030554_DUPONT E I DE NEMOURS & CO_10-K\\html\\*x10k.htm"):
    file = open(filename,'r')
    readtxt = file.read()
    file.close()
exhibit=[]
for filename in glob.iglob(mypath+"\\0000030554_DUPONT E I DE NEMOURS & CO\\10-K\\0000030554-14-000002_0000030554_DUPONT E I DE NEMOURS & CO_10-K\\html\\*xex*.htm"):
    file = open(filename,'r')
    exhibit.append(file.read())
    file.close()
        
result = db.sec10k.insert_one(
                          {"company" : {"name":"DUPONT E I DE NEMOURS & CO",
                                        "secIdentifier":"001-00815",
                                        "address":{
                                                   "street1:":"1007 MARKET ST",
                                                   "city":"WILMINGTON",
                                                   "state":"DE",
                                                   "zip":"19898",
                                                   "BUSINESS PHONE":"302-774-1000"
                                                   }
                                        },
                           "year":"2013",
                           "form10k":readtxt,
                           "exhibit":exhibit,
                           "financialData":{
                                           "costofgoodssold":21538,
                                           "inventories":7565,
                                           "totalassets":49859,
                                           "totalcurrentliabilities":13552,
                                           "longtermdebt":10741,
                                           "operationalincome":3937,
                                           "revenues":36144,
                                           "grossprofit":13597
                                           }
                           }
                          )
'''
This is for DUPONT E I DE NEMOURS & CO Year 2014
'''
for filename in glob.iglob(mypath+"\\0000030554_DUPONT E I DE NEMOURS & CO\\10-K\\0000030554-15-000004_0000030554_DUPONT E I DE NEMOURS & CO_10-K\\html\\*x10k.htm"):
    file = open(filename,'r')
    readtxt = file.read()
    file.close()
exhibit=[]
for filename in glob.iglob(mypath+"\\0000030554_DUPONT E I DE NEMOURS & CO\\10-K\\0000030554-15-000004_0000030554_DUPONT E I DE NEMOURS & CO_10-K\\html\\*xex*.htm"):
    file = open(filename,'r')
    exhibit.append(file.read())
    file.close()
        
result = db.sec10k.insert_one(
                          {"company" : {"name":"DUPONT E I DE NEMOURS & CO",
                                        "secIdentifier":"001-00815",
                                        "address":{
                                                   "street1:":"1007 MARKET ST",
                                                   "city":"WILMINGTON",
                                                   "state":"DE",
                                                   "zip":"19898",
                                                   "BUSINESS PHONE":"302-774-1000"
                                                   }
                                        },
                           "year":"2014",
                           "form10k":readtxt,
                           "exhibit":exhibit,
                           "financialData":{
                                           "costofgoodssold":21703,
                                           "inventories":7841,
                                           "totalassets":49876,
                                           "totalcurrentliabilities":12640,
                                           "longtermdebt":9271,
                                           "operationalincome":5368,
                                           "revenues":36046,
                                           "grossprofit":14343
                                           }
                           }
                          )
'''
This is for EXXON MOBIL CORP Year 2008
'''
for filename in glob.iglob(mypath+"\\0000034088_XXON MOBIL CORP\\10-K\\0001193125-09-040966_0000034088_XXON MOBIL CORP_10-K\\html\\*_d10k.htm"):
    file = open(filename,'r')
    readtxt = file.read()
    file.close()
exhibit=[]
for filename in glob.iglob(mypath+"\\0000034088_XXON MOBIL CORP\\10-K\\0001193125-09-040966_0000034088_XXON MOBIL CORP_10-K\\html\\*_dex*.htm"):
    file = open(filename,'r')
    exhibit.append(file.read())
    file.close()
for filename in glob.iglob(mypath+"\\0000034088_XXON MOBIL CORP\\10-K\\0001193125-09-040966_0000034088_XXON MOBIL CORP_10-K\\html\\*filename19.htm"):
    file = open(filename,'r')
    exhibit.append(file.read())
    file.close()
            
result = db.sec10k.insert_one(
                          {"company" : {"name":"EXXON MOBIL CORP",
                                        "secIdentifier":"001-02256",
                                        "address":{
                                                   "street1:":"5959 LAS COLINAS BLVD",
                                                   "city":"IRVING",
                                                   "state":"TX",
                                                   "zip":"75039-2298",
                                                   "BUSINESS PHONE":"972-444-1000"
                                                   }
                                        }, 
                           "year":"2008",
                           "form10k":readtxt,
                           "exhibit":exhibit,
                           "financialData":{
                                           "costofgoodssold":287359,
                                           "inventories":11646,
                                           "totalassets":228052,
                                           "totalcurrentliabilities":49100,
                                           "longtermdebt":7025,
                                           "operationalincome":83397,
                                           "revenues":477359,
                                           "grossprofit":190000
                                           }
                           }
                          )
'''
This is for EXXON MOBIL CORP Year 2009
'''
for filename in glob.iglob(mypath+"\\0000034088_XXON MOBIL CORP\\10-K\\0001193125-10-042929_0000034088_XXON MOBIL CORP_10-K\\html\\*_d10k.htm"):
    file = open(filename,'r')
    readtxt = file.read()
    file.close()
exhibit=[]
for filename in glob.iglob(mypath+"\\0000034088_XXON MOBIL CORP\\10-K\\0001193125-10-042929_0000034088_XXON MOBIL CORP_10-K\\html\\*_dex*.htm"):
    file = open(filename,'r')
    exhibit.append(file.read())
    file.close()
for filename in glob.iglob(mypath+"\\0000034088_XXON MOBIL CORP\\10-K\\0001193125-10-042929_0000034088_XXON MOBIL CORP_10-K\\html\\*filename39.htm"):
    file = open(filename,'r')
    exhibit.append(file.read())
    file.close()
            
result = db.sec10k.insert_one(
                          {"company" : {"name":"EXXON MOBIL CORP",
                                        "secIdentifier":"001-02256",
                                        "address":{
                                                   "street1:":"5959 LAS COLINAS BLVD",
                                                   "city":"IRVING",
                                                   "state":"TX",
                                                   "zip":"75039-2298",
                                                   "BUSINESS PHONE":"972-444-1000"
                                                   }
                                        },
                           "year":"2009",
                           "form10k":readtxt,
                           "exhibit":exhibit,
                           "financialData":{
                                           "costofgoodssold":185833,
                                           "inventories":11553,
                                           "totalassets":233323,
                                           "totalcurrentliabilities":52061,
                                           "longtermdebt":7129,
                                           "operationalincome":34777,
                                           "revenues":310586,
                                           "grossprofit":124753
                                           }
                           }
                          )
'''
This is for EXXON MOBIL CORP Year 2010
'''
for filename in glob.iglob(mypath+"\\0000034088_XXON MOBIL CORP\\10-K\\0001193125-11-047394_0000034088_XXON MOBIL CORP_10-K\\html\\*_d10k.htm"):
    file = open(filename,'r')
    readtxt = file.read()
    file.close()
exhibit=[]
for filename in glob.iglob(mypath+"\\0000034088_XXON MOBIL CORP\\10-K\\0001193125-11-047394_0000034088_XXON MOBIL CORP_10-K\\html\\*_dex*.htm"):
    file = open(filename,'r')
    exhibit.append(file.read())
    file.close()
for filename in glob.iglob(mypath+"\\0000034088_XXON MOBIL CORP\\10-K\\0001193125-11-047394_0000034088_XXON MOBIL CORP_10-K\\html\\*filename21.htm"):
    file = open(filename,'r')
    exhibit.append(file.read())
    file.close()
            
result = db.sec10k.insert_one(
                          {"company" : {"name":"EXXON MOBIL CORP",
                                        "secIdentifier":"001-02256",
                                        "address":{
                                                   "street1:":"5959 LAS COLINAS BLVD",
                                                   "city":"IRVING",
                                                   "state":"TX",
                                                   "zip":"75039-2298",
                                                   "BUSINESS PHONE":"972-444-1000"
                                                   }
                                        },
                           "year":"2010",
                           "form10k":readtxt,
                           "exhibit":exhibit,
                           "financialData":{
                                           "costofgoodssold":233751,
                                           "inventories":12976,
                                           "totalassets":302510,
                                           "totalcurrentliabilities":62633,
                                           "longtermdebt":12227,
                                           "operationalincome":52959,
                                           "revenues":383221,
                                           "grossprofit":149470
                                           }
                           }
                          )

'''
This is for EXXON MOBIL CORP Year 2011
'''
for filename in glob.iglob(mypath+"\\0000034088_XXON MOBIL CORP\\10-K\\0001193125-12-078102_0000034088_XXON MOBIL CORP_10-K\\html\\*d10k.htm"):
    file = open(filename,'r')
    readtxt = file.read()
    file.close()
exhibit=[]
for filename in glob.iglob(mypath+"\\0000034088_XXON MOBIL CORP\\10-K\\0001193125-12-078102_0000034088_XXON MOBIL CORP_10-K\\html\\*dex*.htm"):
    file = open(filename,'r')
    exhibit.append(file.read())
    file.close()
for filename in glob.iglob(mypath+"\\0000034088_XXON MOBIL CORP\\10-K\\0001193125-12-078102_0000034088_XXON MOBIL CORP_10-K\\html\\*filename29.htm"):
    file = open(filename,'r')
    exhibit.append(file.read())
    file.close()
            
result = db.sec10k.insert_one(
                          {"company" : {"name":"EXXON MOBIL CORP",
                                        "secIdentifier":"001-02256",
                                        "address":{
                                                   "street1:":"5959 LAS COLINAS BLVD",
                                                   "city":"IRVING",
                                                   "state":"TX",
                                                   "zip":"75039-2298",
                                                   "BUSINESS PHONE":"972-444-1000"
                                                   }
                                        },
                           "year":"2011",
                           "form10ka":readtxt,
                           "exhibit":exhibit,
                           "financialData":{
                                           "costofgoodssold":306802,
                                           "inventories":15024,
                                           "totalassets":331052,
                                           "totalcurrentliabilities":77505,
                                           "longtermdebt":9322,
                                           "operationalincome":73257,
                                           "revenues":486429,
                                           "grossprofit":179627
                                           }
                           }
                          )
'''
This is for EXXON MOBIL CORP Year 2012
'''
for filename in glob.iglob(mypath+"\\0000034088_XXON MOBIL CORP\\10-K\\0000034088-13-000011_0000034088_XXON MOBIL CORP_10-K\\html\\*_xom10k2012.htm"):
    file = open(filename,'r')
    readtxt = file.read()
    file.close()
exhibit=[]
for filename in glob.iglob(mypath+"\\0000034088_XXON MOBIL CORP\\10-K\\0000034088-13-000011_0000034088_XXON MOBIL CORP_10-K\\html\\*_xomexhibit*.htm"):
    file = open(filename,'r')
    exhibit.append(file.read())
    file.close()
for filename in glob.iglob(mypath+"\\0000034088_XXON MOBIL CORP\\10-K\\0000034088-13-000011_0000034088_XXON MOBIL CORP_10-K\\html\\*_xom10iii*.htm"):
    file = open(filename,'r')
    exhibit.append(file.read())
    file.close()
for filename in glob.iglob(mypath+"\\0000034088_XXON MOBIL CORP\\10-K\\0000034088-13-000011_0000034088_XXON MOBIL CORP_10-K\\html\\*_filename25.htm"):
    file = open(filename,'r')
    exhibit.append(file.read())
    file.close()
            
result = db.sec10k.insert_one(
                          {"company" : {"name":"EXXON MOBIL CORP",
                                        "secIdentifier":"001-02256",
                                        "address":{
                                                   "street1:":"5959 LAS COLINAS BLVD",
                                                   "city":"IRVING",
                                                   "state":"TX",
                                                   "zip":"75039-2298",
                                                   "BUSINESS PHONE":"972-444-1000"
                                                   }
                                        },
                           "year":"2012",
                           "form10k":readtxt,
                           "exhibit":exhibit,
                           "financialData":{
                                           "costofgoodssold":302056,
                                           "inventories":14542,
                                           "totalassets":333795,
                                           "totalcurrentliabilities":64139,
                                           "longtermdebt":7928,
                                           "operationalincome":78726,
                                           "revenues":480681,
                                           "grossprofit":178625
                                           }
                           }
                          )
'''
This is for EXXON MOBIL CORP Year 2013
'''
for filename in glob.iglob(mypath+"\\0000034088_XXON MOBIL CORP\\10-K\\0000034088-14-000012_0000034088_XXON MOBIL CORP_10-K\\html\\*_xom10k2013.htm"):
    file = open(filename,'r')
    readtxt = file.read()
    file.close()
exhibit=[]
for filename in glob.iglob(mypath+"\\0000034088_XXON MOBIL CORP\\10-K\\0000034088-14-000012_0000034088_XXON MOBIL CORP_10-K\\html\\*_xomexhibit*.htm"):
    file = open(filename,'r')
    exhibit.append(file.read())
    file.close()
for filename in glob.iglob(mypath+"\\0000034088_XXON MOBIL CORP\\10-K\\0000034088-14-000012_0000034088_XXON MOBIL CORP_10-K\\html\\*_xom10iii*.htm"):
    file = open(filename,'r')
    exhibit.append(file.read())
    file.close()
            
result = db.sec10k.insert_one(
                          {"company" : {"name":"EXXON MOBIL CORP",
                                        "secIdentifier":"001-02256",
                                        "address":{
                                                   "street1:":"5959 LAS COLINAS BLVD",
                                                   "city":"IRVING",
                                                   "state":"TX",
                                                   "zip":"75039-2298",
                                                   "BUSINESS PHONE":"972-444-1000"
                                                   }
                                        },
                           "year":"2013",
                           "form10k":readtxt,
                           "exhibit":exhibit,
                           "financialData":{
                                           "costofgoodssold":284681,
                                           "inventories":16135,
                                           "totalassets":346808,
                                           "totalcurrentliabilities":71724,
                                           "longtermdebt":6891,
                                           "operationalincome":57711,
                                           "revenues":438255,
                                           "grossprofit":153574
                                           }
                           }
                          )
'''
This is for EXXON MOBIL CORP Year 2014
'''
for filename in glob.iglob(mypath+"\\0000034088_XXON MOBIL CORP\\10-K\\0000034088-15-000013_0000034088_XXON MOBIL CORP_10-K\\html\\*_xom10k2014.htm"):
    file = open(filename,'r')
    readtxt = file.read()
    file.close()
exhibit=[]
for filename in glob.iglob(mypath+"\\0000034088_XXON MOBIL CORP\\10-K\\0000034088-15-000013_0000034088_XXON MOBIL CORP_10-K\\html\\*_xomexhibit*.htm"):
    file = open(filename,'r')
    exhibit.append(file.read())
    file.close()
for filename in glob.iglob(mypath+"\\0000034088_XXON MOBIL CORP\\10-K\\0000034088-15-000013_0000034088_XXON MOBIL CORP_10-K\\html\\*_xom10iii*.htm"):
    file = open(filename,'r')
    exhibit.append(file.read())
    file.close()
            
result = db.sec10k.insert_one(
                          {"company" : {"name":"EXXON MOBIL CORP",
                                        "secIdentifier":"001-02256",
                                        "address":{
                                                   "street1:":"5959 LAS COLINAS BLVD",
                                                   "city":"IRVING",
                                                   "state":"TX",
                                                   "zip":"75039-2298",
                                                   "BUSINESS PHONE":"972-444-1000"
                                                   }
                                        },
                           "year":"2014",
                           "form10k":readtxt,
                           "exhibit":exhibit,
                           "financialData":{
                                           "costofgoodssold":266831,
                                           "inventories":16678,
                                           "totalassets":349493,
                                           "totalcurrentliabilities":64633,
                                           "longtermdebt":11653,
                                           "operationalincome":51630,
                                           "revenues":411939,
                                           "grossprofit":145108
                                           }
                           }
                          )

'''
This is for GENERAL ELECTRIC CO Year 2008
'''
for filename in glob.iglob(mypath+"\\0000040545_GENERAL ELECTRIC CO\\10-K\\0000040545-09-000012_0000040545_GENERAL ELECTRIC CO_10-K\\html\\*_frm10k.htm"):
    file = open(filename,'r')
    readtxt = file.read()
    file.close()
exhibit=[]
for filename in glob.iglob(mypath+"\\0000040545_GENERAL ELECTRIC CO\\10-K\\0000040545-09-000012_0000040545_GENERAL ELECTRIC CO_10-K\\html\\*_ex*.htm"):
    file = open(filename,'r')
    exhibit.append(file.read())
    file.close()
            
result = db.sec10k.insert_one(
                          {"company" : {"name":"GENERAL ELECTRIC CO",
                                        "secIdentifier":"001-00035",
                                        "address":{
                                                   "street1:":"3135 EASTON TURNPIKE",
                                                   "city":"FAIRFIELD",
                                                   "state":"CT",
                                                   "zip": "06828",
                                                   "BUSINESS PHONE":"203-373-2211"
                                                   }
                                        },
                           "year":"2008",
                           "form10k":readtxt,
                           "exhibit":exhibit,
                           "financialData":{
                                           "costofgoodssold":83772,
                                           "inventories":13674,
                                           "totalassets":797769,
                                           "totalcurrentliabilities":218976,
                                           "longtermdebt":322847,
                                           "operationalincome":45991,
                                           "revenues":182515,
                                           "grossprofit":98743
                                           }
                           }
                          )
'''
This is for GENERAL ELECTRIC CO Year 2009
'''
for filename in glob.iglob(mypath+"\\0000040545_GENERAL ELECTRIC CO\\10-K\\0000040545-10-000010_0000040545_GENERAL ELECTRIC CO_10-K\\html\\*_frm10k.htm"):
    file = open(filename,'r')
    readtxt = file.read()
    file.close()
exhibit=[]
for filename in glob.iglob(mypath+"\\0000040545_GENERAL ELECTRIC CO\\10-K\\0000040545-10-000010_0000040545_GENERAL ELECTRIC CO_10-K\\html\\*_ex*.htm"):
    file = open(filename,'r')
    exhibit.append(file.read())
    file.close()
            
result = db.sec10k.insert_one(
                          {"company" : {"name":"GENERAL ELECTRIC CO",
                                        "secIdentifier":"001-00035",
                                        "address":{
                                                   "street1:":"3135 EASTON TURNPIKE",
                                                   "city":"FAIRFIELD",
                                                   "state":"CT",
                                                   "zip": "06828",
                                                   "BUSINESS PHONE":"203-373-2211"
                                                   }
                                        },
                           "year":"2009",
                           "form10k":readtxt,
                           "exhibit":exhibit,
                           "financialData":{
                                           "costofgoodssold":75921,
                                           "inventories":11987,
                                           "totalassets":781901,
                                           "totalcurrentliabilities":201582,
                                           "longtermdebt":337631,
                                           "operationalincome":28304,
                                           "revenues":155278,
                                           "grossprofit":79357
                                           }
                           }
                          )
'''
This is for GENERAL ELECTRIC CO Year 2010
'''
for filename in glob.iglob(mypath+"\\0000040545_GENERAL ELECTRIC CO\\10-K\\0001193125-11-047479_0000040545_GENERAL ELECTRIC CO_10-K\\html\\*_d10k.htm"):
    file = open(filename,'r')
    readtxt = file.read()
    file.close()
exhibit=[]
for filename in glob.iglob(mypath+"\\0000040545_GENERAL ELECTRIC CO\\10-K\\0001193125-11-047479_0000040545_GENERAL ELECTRIC CO_10-K\\html\\*_dex*.htm"):
    file = open(filename,'r')
    exhibit.append(file.read())
    file.close()
            
result = db.sec10k.insert_one(
                          {"company" : {"name":"GENERAL ELECTRIC CO",
                                        "secIdentifier":"001-00035",
                                        "address":{
                                                   "street1:":"3135 EASTON TURNPIKE",
                                                   "city":"FAIRFIELD",
                                                   "state":"CT",
                                                   "zip": "06828",
                                                   "BUSINESS PHONE":"203-373-2211"
                                                   }
                                        },
                           "year":"2010",
                           "form10k":readtxt,
                           "exhibit":exhibit,
                           "financialData":{
                                           "costofgoodssold":71713,
                                           "inventories":11526,
                                           "totalassets":747793,
                                           "totalcurrentliabilities":192907,
                                           "longtermdebt":312842,
                                           "operationalincome":29638,
                                           "revenues":149593,
                                           "grossprofit":77880
                                           }
                           }
                          )
'''
This is for GENERAL ELECTRIC CO Year 2011
'''
for filename in glob.iglob(mypath+"\\0000040545_GENERAL ELECTRIC CO\\10-K\\0000040545-12-000016_0000040545_GENERAL ELECTRIC CO_10-K\\html\\*_ge10k.htm"):
    file = open(filename,'r')
    readtxt = file.read()
    file.close()
exhibit=[]
for filename in glob.iglob(mypath+"\\0000040545_GENERAL ELECTRIC CO\\10-K\\0000040545-12-000016_0000040545_GENERAL ELECTRIC CO_10-K\\html\\*exhibit*.htm"):
    file = open(filename,'r')
    exhibit.append(file.read())
    file.close()
            
result = db.sec10k.insert_one(
                          {"company" : {"name":"GENERAL ELECTRIC CO",
                                        "secIdentifier":"001-00035",
                                        "address":{
                                                   "street1:":"3135 EASTON TURNPIKE",
                                                   "city":"FAIRFIELD",
                                                   "state":"CT",
                                                   "zip": "06828",
                                                   "BUSINESS PHONE":"203-373-2211"
                                                   }
                                        },
                           "year":"2011",
                           "form10k":readtxt,
                           "exhibit":exhibit,
                           "financialData":{
                                           "costofgoodssold":68278,
                                           "inventories":13792,
                                           "totalassets":718189,
                                           "totalcurrentliabilities":218581,
                                           "longtermdebt":262003,
                                           "operationalincome":34785,
                                           "revenues":147288,
                                           "grossprofit":79010
                                           }
                           }
                          )
'''
This is for GENERAL ELECTRIC CO Year 2012
'''
for filename in glob.iglob(mypath+"\\0000040545_GENERAL ELECTRIC CO\\10-K\\0000040545-13-000036_0000040545_GENERAL ELECTRIC CO_10-K\\html\\*_geform10k2012.htm"):
    file = open(filename,'r')
    readtxt = file.read()
    file.close()
exhibit=[]
for filename in glob.iglob(mypath+"\\0000040545_GENERAL ELECTRIC CO\\10-K\\0000040545-13-000036_0000040545_GENERAL ELECTRIC CO_10-K\\html\\*_exhibit*.htm"):
    file = open(filename,'r')
    exhibit.append(file.read())
    file.close()
            
result = db.sec10k.insert_one(
                          {"company" : {"name":"GENERAL ELECTRIC CO",
                                        "secIdentifier":"001-00035",
                                        "address":{
                                                   "street1:":"3135 EASTON TURNPIKE",
                                                   "city":"FAIRFIELD",
                                                   "state":"CT",
                                                   "zip": "06828",
                                                   "BUSINESS PHONE":"203-373-2211"
                                                   }
                                        },
                           "year":"2012",
                           "form10k":readtxt,
                           "exhibit":exhibit,
                           "financialData":{
                                           "costofgoodssold":74310,
                                           "inventories":15374,
                                           "totalassets":684999,
                                           "totalcurrentliabilities":181414,
                                           "longtermdebt":258500,
                                           "operationalincome":29788,
                                           "revenues":146684,
                                           "grossprofit":72374
                                           }
                           }
                          )
'''
This is for GENERAL ELECTRIC CO Year 2013
'''
for filename in glob.iglob(mypath+"\\0000040545_GENERAL ELECTRIC CO\\10-K\\0000040554-14-000023_0000040545_GENERAL ELECTRIC CO_10-K\\html\\*_geform10k2013.htm"):
    file = open(filename,'r')
    readtxt = file.read()
    file.close()
exhibit=[]
for filename in glob.iglob(mypath+"\\0000040545_GENERAL ELECTRIC CO\\10-K\\0000040554-14-000023_0000040545_GENERAL ELECTRIC CO_10-K\\html\\*_exhibit*.htm"):
    file = open(filename,'r')
    exhibit.append(file.read())
    file.close()
            
result = db.sec10k.insert_one(
                          {"company" : {"name":"GENERAL ELECTRIC CO",
                                        "secIdentifier":"001-00035",
                                        "address":{
                                                   "street1:":"3135 EASTON TURNPIKE",
                                                   "city":"FAIRFIELD",
                                                   "state":"CT",
                                                   "zip": "06828",
                                                   "BUSINESS PHONE":"203-373-2211"
                                                   }
                                        },
                           "year":"2013",
                           "form10k":readtxt,
                           "exhibit":exhibit,
                           "financialData":{
                                           "costofgoodssold":77141,
                                           "inventories":17325,
                                           "totalassets":656560,
                                           "totalcurrentliabilities":167220,
                                           "longtermdebt":242742,
                                           "operationalincome":26267,
                                           "revenues":146045,
                                           "grossprofit":68904
                                           }
                           }
                          )
'''
This is for GENERAL ELECTRIC CO Year 2014
'''
for filename in glob.iglob(mypath+"\\0000040545_GENERAL ELECTRIC CO\\10-K\\0000040545-15-000030_0000040545_GENERAL ELECTRIC CO_10-K\\html\\*_ge10k2014.htm"):
    file = open(filename,'r')
    readtxt = file.read()
    file.close()
exhibit=[]
for filename in glob.iglob(mypath+"\\0000040545_GENERAL ELECTRIC CO\\10-K\\0000040545-15-000030_0000040545_GENERAL ELECTRIC CO_10-K\\html\\*_ge10k2014ex*.htm"):
    file = open(filename,'r')
    exhibit.append(file.read())
    file.close()
            
result = db.sec10k.insert_one(
                          {"company" : {"name":"GENERAL ELECTRIC CO",
                                        "secIdentifier":"001-00035",
                                        "address":{
                                                   "street1:":"3135 EASTON TURNPIKE",
                                                   "city":"FAIRFIELD",
                                                   "state":"CT",
                                                   "zip": "06828",
                                                   "BUSINESS PHONE":"203-373-2211"
                                                   }
                                        },
                           "year":"2014",
                           "form10k":readtxt,
                           "exhibit":exhibit,
                           "financialData":{
                                           "costofgoodssold":81311,
                                           "inventories":17689,
                                           "totalassets":648349,
                                           "totalcurrentliabilities":163096,
                                           "longtermdebt":222910,
                                           "operationalincome":26711,
                                           "revenues":148589,
                                           "grossprofit":67278
                                           }
                           }
                          )
cursor = db.sec10k.find()
#db.sec10k.ensure_index({'company':1})

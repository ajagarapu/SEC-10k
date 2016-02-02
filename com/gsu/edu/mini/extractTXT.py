'''
Created on Jan 26, 2016

@author: Ashwin
'''
from os.path import dirname
from os import getcwd
import json
from pymongo import MongoClient
import re
from bs4 import BeautifulSoup 
'''data = file.read().strip()
file.close()
header=''
rex = re.compile('<SEC-HEADER>(.*?)')
match = rex.match(data)
print("starts from here")

print(match)

if match:
    print('Match found!!')
    header=match.groups()[0].strip()
print(header)
'''
mypath=dirname(getcwd())+"\\data"
htmtext = """<DOCUMENT>
<TYPE>EX-32
<SEQUENCE>17
<FILENAME>a20111231ex-32.htm
<TEXT>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
    <head>
        <!-- Document created using WebFilings 1 -->
        <!-- Copyright 2008-2012 WebFilings LLC. All Rights Reserved -->
        <title>2011.12.31 Ex-32</title>
    </head>
    <body style="font-family:Times New Roman;font-size:10pt;">
<a name="s934251C0B21B97F1F47D4A392064DD8C"></a><div><div style="line-height:120%;font-size:10pt;"><font style="font-family:inherit;font-size:10pt;"><br></font></div></div><br><div style="line-height:120%;padding-bottom:13px;text-align:right;font-size:10pt;"><font style="font-family:inherit;font-size:10pt;font-weight:bold;">EXHIBIT 32.1</font></div><div style="line-height:120%;text-align:center;font-size:10pt;"><font style="font-family:inherit;font-size:10pt;font-weight:bold;">CERTIFICATION PURSUANT TO</font></div><div style="line-height:120%;text-align:center;font-size:10pt;"><font style="font-family:inherit;font-size:10pt;font-weight:bold;">18 U.S.C. SECTION&#160;1350,</font></div><div style="line-height:120%;text-align:center;font-size:10pt;"><font style="font-family:inherit;font-size:10pt;font-weight:bold;">AS ADOPTED PURSUANT TO</font></div><div style="line-height:120%;text-align:center;font-size:10pt;"><font style="font-family:inherit;font-size:10pt;font-weight:bold;">SECTION&#160;906 OF THE SARBANES&#8209;OXLEY ACT OF&#160;2002</font></div><div style="line-height:120%;text-align:center;font-size:10pt;"><font style="font-family:inherit;font-size:10pt;"><br></font></div><div style="line-height:120%;padding-bottom:13px;text-align:left;font-size:10pt;"><font style="font-family:inherit;font-size:10pt;">In connection with the annual report of The Coca-Cola Company (the &#8220;Company&#8221;) on Form&#160;10-K for the period ended December&#160;31, 2011 (the &#8220;Report&#8221;), I, Muhtar Kent, Chairman of the Board of Directors, Chief Executive Officer and President of the Company and I, Gary P. Fayard, Executive Vice President and Chief Financial Officer of the Company, each certify, pursuant to 18 U.S.C. Section&#160;1350, as adopted pursuant to Section&#160;906 of the Sarbanes&#8209;Oxley Act of 2002, that:</font></div><div style="line-height:120%;padding-bottom:13px;text-align:left;font-size:10pt;"><font style="font-family:inherit;font-size:10pt;">(1)&#160;&#160;&#160;&#160;to my knowledge, the Report fully complies with the requirements of Section&#160;13(a) or 15(d) of the Securities Exchange Act of 1934; and</font></div><div style="line-height:120%;padding-bottom:13px;text-align:left;font-size:10pt;"><font style="font-family:inherit;font-size:10pt;">(2)&#160;&#160;&#160;&#160;the information contained in the Report fairly presents, in all material respects, the financial condition and results of operations of the Company.</font></div><div style="line-height:120%;text-align:center;font-size:10pt;"><div style="padding-left:0px;text-indent:0px;line-height:normal;padding-top:10px;"><table cellpadding="0" cellspacing="0" style="font-family:Times New Roman;font-size:10pt;margin-left:auto;margin-right:auto;width:100%;border-collapse:collapse;text-align:left;"><tr><td colspan="2"></td></tr><tr><td width="56%"></td><td width="44%"></td></tr><tr><td style="vertical-align:bottom;padding-left:2px;padding-top:2px;padding-bottom:2px;padding-right:2px;"><div style="overflow:hidden;font-size:10pt;"><font style="font-family:inherit;font-size:10pt;">&#160;</font></div></td><td style="vertical-align:bottom;border-bottom:1px solid #000000;padding-left:2px;padding-top:2px;padding-bottom:2px;padding-right:2px;"><div style="text-align:left;font-size:10pt;"><font style="font-family:inherit;font-size:10pt;">/s/ Muhtar Kent</font></div></td></tr><tr><td style="vertical-align:bottom;padding-left:2px;padding-top:2px;padding-bottom:2px;padding-right:2px;"><div style="overflow:hidden;font-size:10pt;"><font style="font-family:inherit;font-size:10pt;">&#160;</font></div></td><td style="vertical-align:top;padding-left:2px;padding-top:2px;padding-bottom:2px;padding-right:2px;"><div style="padding-bottom:13px;vertical-align:top;font-size:10pt;"><font style="font-family:inherit;font-size:10pt;vertical-align:top;">Muhtar Kent</font></div><div style="padding-bottom:13px;vertical-align:top;font-size:10pt;"><font style="font-family:inherit;font-size:10pt;"><br></font></div></td></tr><tr><td style="vertical-align:bottom;padding-left:2px;padding-top:2px;padding-bottom:2px;padding-right:2px;"><div style="overflow:hidden;font-size:10pt;"><font style="font-family:inherit;font-size:10pt;">&#160;</font></div></td><td style="vertical-align:top;padding-left:2px;padding-top:2px;padding-bottom:2px;padding-right:2px;"><div style="text-align:left;font-size:10pt;"><font style="font-family:inherit;font-size:10pt;font-style:italic;">Chairman of the Board of Directors, Chief Executive Officer and President</font></div></td></tr><tr><td style="vertical-align:bottom;padding-left:2px;padding-top:2px;padding-bottom:2px;padding-right:2px;"><div style="overflow:hidden;font-size:10pt;"><font style="font-family:inherit;font-size:10pt;">&#160;</font></div></td><td style="vertical-align:bottom;padding-left:2px;padding-top:2px;padding-bottom:2px;padding-right:2px;"><div style="text-align:left;font-size:10pt;"><font style="font-family:inherit;font-size:10pt;">February&#160;23, 2012</font></div></td></tr><tr><td style="vertical-align:bottom;padding-left:2px;padding-top:2px;padding-bottom:2px;padding-right:2px;"><div style="overflow:hidden;font-size:10pt;"><font style="font-family:inherit;font-size:10pt;">&#160;</font></div></td><td style="vertical-align:bottom;border-bottom:1px solid #000000;padding-left:2px;padding-top:2px;padding-bottom:2px;padding-right:2px;"><div style="text-align:left;font-size:10pt;"><font style="font-family:inherit;font-size:10pt;">/s/ Gary P. Fayard</font></div></td></tr><tr><td style="vertical-align:bottom;padding-left:2px;padding-top:2px;padding-bottom:2px;padding-right:2px;"><div style="overflow:hidden;font-size:10pt;"><font style="font-family:inherit;font-size:10pt;">&#160;</font></div></td><td style="vertical-align:bottom;padding-left:2px;padding-top:2px;padding-bottom:2px;padding-right:2px;"><div style="text-align:left;font-size:10pt;"><font style="font-family:inherit;font-size:10pt;">Gary P. Fayard</font></div></td></tr><tr><td style="vertical-align:bottom;padding-left:2px;padding-top:2px;padding-bottom:2px;padding-right:2px;"><div style="overflow:hidden;font-size:10pt;"><font style="font-family:inherit;font-size:10pt;">&#160;</font></div></td><td style="vertical-align:top;padding-left:2px;padding-top:2px;padding-bottom:2px;padding-right:2px;"><div style="text-align:left;font-size:10pt;"><font style="font-family:inherit;font-size:10pt;font-style:italic;">Executive Vice President and Chief Financial Officer</font></div></td></tr><tr><td style="vertical-align:bottom;padding-left:2px;padding-top:2px;padding-bottom:2px;padding-right:2px;"><div style="overflow:hidden;font-size:10pt;"><font style="font-family:inherit;font-size:10pt;">&#160;</font></div></td><td style="vertical-align:bottom;padding-left:2px;padding-top:2px;padding-bottom:2px;padding-right:2px;"><div style="text-align:left;font-size:10pt;"><font style="font-family:inherit;font-size:10pt;">February&#160;23, 2012</font></div></td></tr></table></div></div><div style="line-height:120%;padding-bottom:13px;text-align:left;font-size:10pt;"><font style="font-family:inherit;font-size:10pt;"><br></font></div><div style="line-height:120%;font-size:10pt;"><font style="font-family:inherit;font-size:10pt;"><br></font></div><br><div style="text-align:center;"><div style="line-height:120%;font-size:10pt;"><font style="font-family:inherit;font-size:10pt;"><br></font></div></div>    </body>
</html>
</TEXT>
</DOCUMENT>
"""
client = MongoClient('localhost',27017)
db = client.miniproject.company()

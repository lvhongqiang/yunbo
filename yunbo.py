import requests

while 1:

    url = 'http://p.qiao.baidu.com/cps2//bookmanage/saveBook.action?userId=24226557'
    headers={
    'Host':'p.qiao.baidu.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Referer':'http://www.hdybjy.com/',
    # 'Cookie':'JSESSIONID=172237AC9A03DC19B13E0FE1B0676B35; AWSELB=61C7191310AB05479AEDA95B4CD08C3F745A52AB1C576F7D9C72DB29A946FCF0E458E429D4C4E74477137C35ACD1805C9FCC7C38C0166B0590CA88C6DCA830F0E1A1D15881FCC51A2032A4B19E727D1625DC596FAC; D_SID=159.226.177.234:FSTWIqOfTh/xIiIJ1EEqSU8AVSFrhQaYmsqSLcsh9I8; WT_FPC=id=a8897808-c399-4b5a-8e4b-364bed6934d6:lv=1504707598916:ss=1504705803521; __unam=9a98afa-15e6ef8fcd9-5e0edce6-4; correlationId=af0781d3-5f6f-4254-809f-c68980fe13f4; D_IID=5EB6EF8D-7E79-38B0-8915-91900F0F6841; D_UID=B147A783-1935-33DD-8D24-9F547CF546FA; D_ZID=702649D3-1578-3D45-B050-23B2AE7FF6B9; D_ZUID=6E6382D3-C3D9-33F5-BC3E-C7556CADD8A3; D_HID=FD01AAAF-6055-33BF-BFEF-EF424B3BF3FE; _4c_=dVJNi9swEP0rRQWf0liSJUsO5NBNKd1LKfTQY9GXsahjCVneD5b89x153d2StjmY%2BXjz3sxTntD94CZ0IBxzQRtCMKF4h365xxkdnpCJ5XtXPksa0QENOcf5UNcxhTtvXdpro%2Be9CedaxVjHRY%2Fe1O%2FrMLna%2BPx4rOassjtWMUAwnoKF2IRlygl6fpqX5NJavTndfP%2F487bSSU32rfL105fPlRrjoL4l1%2FuHY1UEIQl2MfnW1sreqck4%2B2F2KpkB7ZCBYdiUdHu%2Bx5DrFO5nl6B0GlI4u3esg2oPlyFKDXOCMNs4rTnlHeulNoYJpdtGcQ64AD6gH36yQAIpLOES7AxFyGafi9RvD6CSXTqXCQgj2IYoBGMwaiw4MHqHLLiNrOvVMmZ02aGHF%2FMl7jiWhEngyOC0bBkuP0Akb7dXQLaXQjHSSsVaQawRDXYNPBvtaacdKeeufKRhgkuOoQMEZZN1nv4px9q2Jf%2BQe%2FHr%2FzOU%2FD0TIV3R0NvQohGrQruhCXtFw%2FUbHP5qV%2BQgd01eHNvO32x7u7LrcCuElADzr6jrftfIy%2BXyDA%3D%3D; _gat_UA-47964423-1=1; _gat_UA-47964423-41=1; _ga=GA1.2.493277962.1504763405; _gid=GA1.2.172928401.1505699847',
    }
    proxies={

    }

    try:

        d = {

        }
        requests.post(url,data=d,headers=headers,proxies=proxies)
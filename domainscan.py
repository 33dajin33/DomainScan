import requests
import re
domain=input("Domain：")
result=[]
head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0'}
match='style="text-decoration:none;">(.*?)</b>'
sum=0
for num in range(0,10):
    url='https://www.baidu.com/s?wd=inurl:{}&pn={}&oq={}&ie=utf-8'.format(domain,num*10,domain) #pn代表爬取个数，100/10=10意思是爬取前10页
    response=requests.get(url,headers=head).content
    #print(url)
    ifmatch=re.findall(match,response.decode())
    count=len(ifmatch)
    sum=count+sum
    for matched in ifmatch:
        matched=matched.replace('<b>','')
        if domain in matched:
            if matched not in result:
                result.append(matched)
print('Lucky!'+str(sum)+'subdomains')
print(result)

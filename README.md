# wiki_spider
爬取维基百科，获取一万五千个城市的人口与面积信息。
1.从文档中获取城市名称，并对名称进行处理（url中带空格request会出错，所以换成 "_"， 对搜索结果无影响。
2.城市名前加上维基百科host,urllib.request+bs4获取网页内容，维基百科对城市的介绍中会有目录项，从中获取人口及面积信息。
3.如果直接https://en.wikipedia/City_name搜寻不到，则在谷歌中搜索此城市，再爬取搜索结果的url，获取第一个带有https://en.wikipedia前缀的url，爬取内容并分析。

# 通过AIP来识别文件名中的人名
from aip import AipNlp

""" 你的 APPID AK SK """
APP_ID = '24942249'
API_KEY = '8YrSBhUOaw9enqqMKcGrG2qW'
SECRET_KEY = 'N4zFNSz2jxB2XA7XBiDBpnWoyQoEZeDP'

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

text = '计算机193_201905010330_方恒'
# 如果出现编码错误，加上
# text = str(text.encode('gbk', 'ignore'), encoding='gbk')

# 分析结果
# print(aipNlp.lexer(text))

# 提取名字
result = []
for i in client.lexer(text)['items']:
	if i['ne'] == 'PER' or i['pos'] == 'nr':
		result.append(i['item'])
print(result)
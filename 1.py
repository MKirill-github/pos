import requests
url = 'https://melbet-156973.top/ru/toto/fifteen'
# url = 'https://melbet-156973.top/ru/toto/fifteen/draw/3538/1'
header = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}
p = requests.get(url, headers=header)
src = p.text
# print(p)
with open('text.html', 'w', encoding='utf-8') as f:
    # print(p)
    f.write(src)


# 123

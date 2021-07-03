from urllib import request

try:
    site = request.urlopen('https://www.python.org/')
except:
    print('\033[31mNão consegui acessar o site python.org\033[m')
else:
    print('\033[32mSite acessado com sucesso\033[m')

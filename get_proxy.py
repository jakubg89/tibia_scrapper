# create proxy list


def headers():
    headers_list = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                                  ' AppleWebKit/537.36 (KHTML, like Gecko)'
                                  ' Chrome/99.0.4844.74 Safari/537.36'}
    return headers_list


def proxy_list():
    temp_list = [
        '139.162.182.54:49165',
        '96.126.124.197:81',
        '80.48.119.28:8080',
        '198.59.191.234:8080',
        '71.86.129.131:8080',
        '185.125.125.157:80'
    ]
    return temp_list


def get_one_proxy():
    pass

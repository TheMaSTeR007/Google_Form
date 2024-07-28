import json
import openpyxl
import requests
from lxml import html, etree

get_url = 'https://docs.google.com/forms/d/e/1FAIpQLSePH4DzukHZsyNJGVbVmWBIrKq4Sn-ZBs3XyGwgSvYJ74fzAg/viewform?usp=sf_link'

resp_get = requests.get(get_url)
print('Response of GET request: ', resp_get.status_code)
resp_text = resp_get.text
parsed_text = html.fromstring(resp_text)
xpath_script = "//script[contains(text(), 'FB_PUBLIC_LOAD_DATA_')]/text()"
js = parsed_text.xpath(xpath_script)
print(js)
data_list = json.loads(js[0].replace('var FB_PUBLIC_LOAD_DATA_ = ', '').replace(';', ''))
print(data_list)
input_data_list = data_list[1][1]
header_list = list()
for i in input_data_list:
    print(f'Data field name: {i[1]}')
    print(f"input_id: {i[4][0][0]}")
    header_list.append(i[1])

print(header_list)

cookies = {
    'S': 'spreadsheet_forms=mhhTjDp4Fx0MpPlXS_5_IUl7nUX3AWb64G1QS2K6dwA',
    'COMPASS': 'spreadsheet_forms=CjIACWuJV8toK6biUCbOx4kw_J7YNds_YbhMIZrLdTNwrFjVYEFEUz36FMvGMJCiJ77y8BDctN60Bho0AAlriVeKTP-FlP33AxOg22Q4jgetjQDIwewLT4FISHKi6_ZbRXIouchNKQjIaReqznRiog==',
    'SID': 'g.a000lwjJf6ZSAEI2rgcIHLSqtZKVtemnkT2tBex0l0aTBIYRDIirZvnS8F-ppcjyuIRAd3GAlgACgYKAc4SARISFQHGX2MikJhlMtrW06iSFwCrvNX7BxoVAUF8yKoiuDts134zPGVwv1_XqIfd0076',
    '__Secure-1PSID': 'g.a000lwjJf6ZSAEI2rgcIHLSqtZKVtemnkT2tBex0l0aTBIYRDIirx_LHi7jBj5I2z_mC_eC3QAACgYKAZgSARISFQHGX2Mi7XJqxo6p2SOH-K5PzND88xoVAUF8yKq5qyRWD3BPun1yy4QomPvp0076',
    '__Secure-3PSID': 'g.a000lwjJf6ZSAEI2rgcIHLSqtZKVtemnkT2tBex0l0aTBIYRDIirKwdZgHXTABmgePd7LBTuYwACgYKAVcSARISFQHGX2MiQLBH9LwvOk22HsnLdZBDPBoVAUF8yKq1m5ESFDqXu32ldMKXcmHZ0076',
    'HSID': 'AgGZjOILM9FKo-74t',
    'SSID': 'AwLgPha26S4Yz6prd',
    'APISID': 'h7QJ_ypit4OOxCtB/A3hAWkKplwaxc9Squ',
    'SAPISID': 'a_VtbE0_0x9QVV5q/AAF7M4rwURXqa4mhF',
    '__Secure-1PAPISID': 'a_VtbE0_0x9QVV5q/AAF7M4rwURXqa4mhF',
    '__Secure-3PAPISID': 'a_VtbE0_0x9QVV5q/AAF7M4rwURXqa4mhF',
    'OSID': 'g.a000lwjJf7l9qrFPBFHGYOwxNBbB6z_d_cA_Td4tDlMQL-YiGGguzecS8pgscQsQCrfDsBFQ-AACgYKAR4SARISFQHGX2MisuPzAUw3cL9UydutgBpipRoVAUF8yKpQJGkukcHLYp_-VFfOKbcz0076',
    '__Secure-OSID': 'g.a000lwjJf7l9qrFPBFHGYOwxNBbB6z_d_cA_Td4tDlMQL-YiGGgu90GVwlOjwXhjLeDxg9xFLQACgYKAYQSARISFQHGX2MiiJ4tLsVBYum2Bb6Bx6ZGghoVAUF8yKrKNEzuXzHYvXURVMqcfm_b0076',
    'SEARCH_SAMESITE': 'CgQIzpsB',
    'AEC': 'AVYB7cor82_5NaL01OrVSa41jEueeqNZoAMO9auGd9xBqACx53zX5CoaPjI',
    '__Secure-1PSIDTS': 'sidts-CjIB4E2dkWRRg1WdDkkKFJZ5H9GVoJ1_dTixbVl3pJL3CZNFaYlPeP6M1a3mMqLBAjkXehAA',
    '__Secure-3PSIDTS': 'sidts-CjIB4E2dkWRRg1WdDkkKFJZ5H9GVoJ1_dTixbVl3pJL3CZNFaYlPeP6M1a3mMqLBAjkXehAA',
    'NID': '515=xQ9tM2J9vO6plky6sZ-I6OYcSOefkqH7rIz0ZLXFx3vu-os0hnZaD75NoQgk96D9fnvx6Mgy8EE4M_WB6vwyokYdDKueN5XmsVcEKn3MiEPEw-wZCfLWo5qhZqbXZlChR1seQF-0LV3WG5QLcpOKEWzwZNzI4JsB4WdOFHjpqQktg_8tIJz2ikVGXI4zyVMba0qwq0c02diF7Y2jCmcWGtUEentDfJ8sY0PD9ochRO-jmjceyBjJ275wkddWjmoUIjlUQrpZ930enfjcBLT3SH94Y-W58TrDgibl_sjkDUL-KRCgEoXkHN3xaF5qQlnbKCV3SDzgejlr8Nn1JLsBxra4T7hGZFudtzxOnp98sK5wyozB7YPQZI94zbAZ3qf5tqp0cDHA5zs0hTIsqdLNr6BpK4hnFYmwU5J9l83-F1bw8c9oI2yPUsBuRG1gXrSRkR-xNpVTw8fRwjnRJap3ItvZv62UWwD7UBHVc2P6zJ4VDy2zy3vukbQsWUddPpibxoqo285AIsecyFD0j73--vUNADg4cVAp_tUb3wcUpyXJ4pV5wu2xNmAT8blGyl61X-cpto0dYY2PXGCiRPXiWnjQDBUIyg__PQwZTHG4nF2m2x851z2W4F8S_n5xPcR1qwwHBUrOpqkoalmKSIipnEhKlLV2SqddLycgxWPmEfp9YLFlzO6K7LJOAyvtyzzJBygngZipeLsva8z0Q-XJL0gCfCH6bt-28ji_EoltyFFl-HQMTacR4zZpbE67E2-Tox584ooRhygklm-oPH8xag8XhD96f7J2--hICdcZvTHXW_l7jUyi5IrNSfUyDGI',
    'SIDCC': 'AKEyXzXn5h-8_wjMF4I-bAsraxkZvIhHHQ9oelrKkcu6jhfMznRFlryEKTP5v5FjBp4GXM5lOS4',
    '__Secure-1PSIDCC': 'AKEyXzVUE3cG9O2KUbS80qGw-E9nMxHX25lVxTIDgIV8xfhSX5V_Rp0WKbwlkmqBa5QS5i1aXQ',
    '__Secure-3PSIDCC': 'AKEyXzUWpwL_aDYspIaAR00eDv7kzk3xWJNVM6Kd3jSWK6sdsTJQVIghLWZ2_LAP2turtcZxEwQ',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'dnt': '1',
    'origin': 'https://docs.google.com',
    'priority': 'u=0, i',
    'referer': 'https://docs.google.com/forms/d/e/1FAIpQLSePH4DzukHZsyNJGVbVmWBIrKq4Sn-ZBs3XyGwgSvYJ74fzAg/viewform?fbzx=1239359535627696286',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version-list': '"Not/A)Brand";v="8.0.0.0", "Chromium";v="126.0.6478.127", "Google Chrome";v="126.0.6478.127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-ch-ua-wow64': '?0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-chrome-connected': 'source=Chrome,id=104970345002812333605,mode=0,enable_account_consistency=false,supervised=false,consistency_enabled_by_default=false',
    'x-client-data': 'CI22yQEIorbJAQipncoBCL7oygEIlaHLAQiTossBCIWgzQEIrJ7OAQinos4BCOGnzgEImqjOAQierM4BCP2szgEIpK7OARj1yc0BGKGdzgEYyZ/OAQ==',
}

wb = openpyxl.load_workbook('g_form_data.xlsx')
sheet = wb.active

print(sheet[3][4].value)
print(type(sheet))
data = {
    f'entry.{51577114}': 'Hey',
    f'entry.{111449395}': 'My paragraph poll ',
    f'entry.{414025721}': 'Dropdown Option 2',
    f'entry.{1710350074}': 'Option 2',
    f'entry.{623583733}': 'Check Option 1'
}

post_url = 'https://docs.google.com/forms/u/0/d/e/1FAIpQLSePH4DzukHZsyNJGVbVmWBIrKq4Sn-ZBs3XyGwgSvYJ74fzAg/formResponse'
# response = requests.post(url=post_url, cookies=cookies, headers=headers, data=data)
# print(response)
# for i in range(25):
#     print(i, 'th request...')

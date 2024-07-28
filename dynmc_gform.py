import json
import requests
from lxml import html
import random

# URL of the Google Form (view form URL)
form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSePH4DzukHZsyNJGVbVmWBIrKq4Sn-ZBs3XyGwgSvYJ74fzAg/viewform?usp=sf_link'

# Send GET request to fetch the form
resp_get = requests.get(form_url)
print('Response of GET request: ', resp_get.status_code)

# Parse the HTML response
resp_text = resp_get.text
parsed_text = html.fromstring(resp_text)

# Extract the script containing the form data
xpath_script = "//script[contains(text(), 'FB_PUBLIC_LOAD_DATA_')]/text()"
js = parsed_text.xpath(xpath_script)

# Parse the JSON data from the script
data_list = json.loads(js[0].replace('var FB_PUBLIC_LOAD_DATA_ = ', '').replace(';', ''))


# Function to generate random data for each field type
def generate_data_for_field(field_type, options=None):
    if field_type == 0:  # Short Answer
        return 'Sample Short Answer'
    elif field_type == 1:  # Paragraph
        return 'Sample Paragraph Answer'
    elif field_type == 2:  # Multiple Choice
        return random.choice(options) if options else 'Option 1'
    elif field_type == 3:  # Dropdown
        return random.choice(options) if options else 'Dropdown Option 1'
    elif field_type == 4:  # Checkboxes
        return random.choice(options) if options else 'Check Option 1'
    elif field_type == 9:  # Date
        return '2024-07-17'
    elif field_type == 10:  # Time
        return '12:34'
    else:
        return 'Sample Answer'


# Parse the form data and construct the payload dynamically
form_data = {}
for field in data_list[1][1]:
    field_id = field[0]
    field_type = field[3]
    field_options = None
    if field[4] and field[4][0] and isinstance(field[4][0], list) and len(field[4][0]) > 1 and field[4][0][1]:
        field_options = [option[0] for option in field[4][0][1] if option and isinstance(option, list) and len(option) > 0]
    form_data[f'entry.{field_id}'] = generate_data_for_field(field_type, field_options)

# URL for form submission
post_url = form_url.replace('/viewform?usp=sf_link', '/formResponse')

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

# Send the POST request with the form data
response = requests.post(post_url, data=form_data)  # , cookies=cookies, headers=headers)
print('Response of POST request: ', response.status_code)
print(response.text)

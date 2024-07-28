import requests
from requests import Session

s = Session()
get_url = 'https://docs.google.com/forms/d/e/1FAIpQLSeN7mNzNn7zmzuUF3vrDECfNBdV6DjZJOLE2aJ8cH0jUGf5mQ/viewform?usp=form_confirm'

resp_get = s.get(get_url)
print('Response of GET request: ', resp_get.status_code)

cookies = {
    'S': 'spreadsheet_forms=CYqLP1LJv3gIQmfKT4aiS-8qhLk82_MyL1LsIAh4zhQ',
    'COMPASS': 'spreadsheet_forms=CjIACWuJV3eORFHnsCcmGTTJJid4wa0vud71G-mZLy-eTQLk1thDeuZfm5HgV-6aM9mObxD-3d20Bho0AAlriVcKKyZ1RVBl15KQyJEQSkmFtEzTDjlvJITFpFXFUVU-lEcDaJ9q7J4BhP83Xj7eHg==',
    '_gid': 'GA1.2-2.1457162311.1721195818',
    '_ga': 'GA1.2-2.1925724488.1721195818',
    '_ga_3WTQFP9ECQ': 'GS1.1-2.1721195817.1.0.1721195819.0.0.0',
    'SEARCH_SAMESITE': 'CgQIyZsB',
    'OSID': 'g.a000lgj1rOOGYzwrCxWMFDAlz1uivgu-QABAg_J6keXRpNc_aXTGq0I9j4JQTMta8V6UVv-ntAACgYKAWASARMSFQHGX2Mi20sCnFJGG4VDvJGXCalhDRoVAUF8yKodcf962PURgVsFUpooa2Lg0076',
    '__Secure-OSID': 'g.a000lgj1rOOGYzwrCxWMFDAlz1uivgu-QABAg_J6keXRpNc_aXTGkHIzgNCKXkJoZEZ_d8_DtAACgYKAVYSARMSFQHGX2MiP21gDEJwDu7QtzsqjMk-FxoVAUF8yKoWK6SaxlLWGUEebwyVLZVQ0076',
    'SID': 'g.a000lgj1rG6t3w-rmejuEdxwm7edq5C60rSBrNH17bvPVkurJ7g11IZt0sOe_gK12Ai-Sf4jWwACgYKAYgSARMSFQHGX2Mi3BW20tEeh7b_ek3lQ2vWSBoVAUF8yKrokFBtud4ACh5kv-Ztmdzf0076',
    '__Secure-1PSID': 'g.a000lgj1rG6t3w-rmejuEdxwm7edq5C60rSBrNH17bvPVkurJ7g15e3O45GMwg6-mTN3wdZ_uwACgYKAdsSARMSFQHGX2MilUets2PbWH5d82-oGXHR4BoVAUF8yKpZhkQVWl0RCd10_N4qHpea0076',
    '__Secure-3PSID': 'g.a000lgj1rG6t3w-rmejuEdxwm7edq5C60rSBrNH17bvPVkurJ7g14NaL_ZcmO5iVQsmQiGoa9AACgYKATkSARMSFQHGX2Mi7pI9mIr0mnS9oRTwO_rQtxoVAUF8yKoZ0EgpQuhgqGX_kw7ckD9j0076',
    'HSID': 'A_q2tB0IflM4YSgQe',
    'SSID': 'Ap5zPYQqKz40oV8BE',
    'APISID': 'Qe29Jps-NE7qFopN/AX0qdLcHofrfgIUW3',
    'SAPISID': 'MRf627AekTGIYv5A/AzYfDZhSApLAIY-F7',
    '__Secure-1PAPISID': 'MRf627AekTGIYv5A/AzYfDZhSApLAIY-F7',
    '__Secure-3PAPISID': 'MRf627AekTGIYv5A/AzYfDZhSApLAIY-F7',
    'AEC': 'AVYB7coys66c2ayk8bzkGM_Z4Isptc6Se5eqqSGkinReHfEBNi44jMwEN-I',
    'COMPASS': 'appsfrontendserver=CgAQwtbdtAYaegAJa4lX9J3du2qc0sidUerIUCz49V2qOIWeBSBbTMe-vT-1j-a6gCxSvR5IkAzHnQ7-_RX7AiZEKGgKESfA1-_8yc9taEYe2dNeNBl0tiB9YlP6qDqjkK2DEVrTSgKTRDRscy6WPRhuBUefmc2VbN2qfnXjEoP5A_hKIAEwAQ',
    '__Secure-1PSIDTS': 'sidts-CjEB4E2dkZjXvucHenoybS3qSU5lqjDuFAgabLKfVN2SzG8ohuNBYsRQ5DofuDGZBIRXEAA',
    '__Secure-3PSIDTS': 'sidts-CjEB4E2dkZjXvucHenoybS3qSU5lqjDuFAgabLKfVN2SzG8ohuNBYsRQ5DofuDGZBIRXEAA',
    'OTZ': '7648197_34_34__34_',
    'NID': '515=kHM5htqF_2F-tMcKQkHGWHqzgfe0dLxAQkjKZmfNKciO3Ccg4Uhj3FL9RCVeeJ7kvotyuthyDDZc7h3p0UkEmPimO4GeRaZO5nyN7PCO8nVwRWrh7UtdG3xyUYaZrh1AJPYah7kF5WtP97bJ5AQEVwJsKEDC282YDasUcUR9BiD76r848p3vRzCXKD-xR4b-ZZfiqHYIMr1nqdo7C89XygDjUGxkQQGfHV9wt4lGgQhPYBrQYZUs5rYgjH5CbE3MuYD35Q6wTXlgkBtVoMohY5QP4h66fBNwQEflbGopLv3v4P30FlfsUog5pxzQq9yisSpnmiBBciz-EBge-CSJCz0hwqz111BMYze6Ml2sqzY-TmJ1ZGQY_hYGfHyuG2wlPeKJ0RTWhei50EqXB6h4E5yUHXC-aHAmiZx586HoXaUXjDvea0D_mojBYZNSeMKD0rQ4lUOPp-_uaxoY9KVdPMOQ4n36yHNV_gXUVm6uHUvzqn4dx7VMlRf8_DQxtTk9P1G9qDoZje_phAHUVRRshHlo9q6Kyjtsmi8bajYCXcDEncg4i6DWR8w8gIx8WfKdEHRu1hgkR33UFiHW6VpQ2o4pzDdmCmlneZaC5mlI99LS0DcKgIUgG02m_Vy35mvEhSfNacE1rqkCQGmJLwOhrQrM_MDTVhfjl5-EqD957kp9UlbJtlo5Afg2sQ5xdHg1cu6zjISbkVSgnuAQKeC_EXZZSnkgDs10NAMNxJkbkLiEbd0RqH5ObelAsM0KHQ',
    'SIDCC': 'AKEyXzWvKQrruXKAdmwehhbNM4pXxMNLO_jrblTYaoc6cYIRBVwWmp1Yt7GrPaw2l2-cVbbvPKg',
    '__Secure-1PSIDCC': 'AKEyXzU5WA6hUZ5vkrmegK13ZzwdcwUxVokeHnUV3FqrtT0oHu43CQI3GUUxvCP7lzs1k10zRg',
    '__Secure-3PSIDCC': 'AKEyXzXiE8jvhxeBjwebPGRkcOn-eiBmJiQQu9crJTnDhalPP4QbZ0rQSWl69tDcJ00xzDEEA4I',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'S=spreadsheet_forms=CYqLP1LJv3gIQmfKT4aiS-8qhLk82_MyL1LsIAh4zhQ; COMPASS=spreadsheet_forms=CjIACWuJV3eORFHnsCcmGTTJJid4wa0vud71G-mZLy-eTQLk1thDeuZfm5HgV-6aM9mObxD-3d20Bho0AAlriVcKKyZ1RVBl15KQyJEQSkmFtEzTDjlvJITFpFXFUVU-lEcDaJ9q7J4BhP83Xj7eHg==; _gid=GA1.2-2.1457162311.1721195818; _ga=GA1.2-2.1925724488.1721195818; _ga_3WTQFP9ECQ=GS1.1-2.1721195817.1.0.1721195819.0.0.0; SEARCH_SAMESITE=CgQIyZsB; OSID=g.a000lgj1rOOGYzwrCxWMFDAlz1uivgu-QABAg_J6keXRpNc_aXTGq0I9j4JQTMta8V6UVv-ntAACgYKAWASARMSFQHGX2Mi20sCnFJGG4VDvJGXCalhDRoVAUF8yKodcf962PURgVsFUpooa2Lg0076; __Secure-OSID=g.a000lgj1rOOGYzwrCxWMFDAlz1uivgu-QABAg_J6keXRpNc_aXTGkHIzgNCKXkJoZEZ_d8_DtAACgYKAVYSARMSFQHGX2MiP21gDEJwDu7QtzsqjMk-FxoVAUF8yKoWK6SaxlLWGUEebwyVLZVQ0076; SID=g.a000lgj1rG6t3w-rmejuEdxwm7edq5C60rSBrNH17bvPVkurJ7g11IZt0sOe_gK12Ai-Sf4jWwACgYKAYgSARMSFQHGX2Mi3BW20tEeh7b_ek3lQ2vWSBoVAUF8yKrokFBtud4ACh5kv-Ztmdzf0076; __Secure-1PSID=g.a000lgj1rG6t3w-rmejuEdxwm7edq5C60rSBrNH17bvPVkurJ7g15e3O45GMwg6-mTN3wdZ_uwACgYKAdsSARMSFQHGX2MilUets2PbWH5d82-oGXHR4BoVAUF8yKpZhkQVWl0RCd10_N4qHpea0076; __Secure-3PSID=g.a000lgj1rG6t3w-rmejuEdxwm7edq5C60rSBrNH17bvPVkurJ7g14NaL_ZcmO5iVQsmQiGoa9AACgYKATkSARMSFQHGX2Mi7pI9mIr0mnS9oRTwO_rQtxoVAUF8yKoZ0EgpQuhgqGX_kw7ckD9j0076; HSID=A_q2tB0IflM4YSgQe; SSID=Ap5zPYQqKz40oV8BE; APISID=Qe29Jps-NE7qFopN/AX0qdLcHofrfgIUW3; SAPISID=MRf627AekTGIYv5A/AzYfDZhSApLAIY-F7; __Secure-1PAPISID=MRf627AekTGIYv5A/AzYfDZhSApLAIY-F7; __Secure-3PAPISID=MRf627AekTGIYv5A/AzYfDZhSApLAIY-F7; AEC=AVYB7coys66c2ayk8bzkGM_Z4Isptc6Se5eqqSGkinReHfEBNi44jMwEN-I; COMPASS=appsfrontendserver=CgAQwtbdtAYaegAJa4lX9J3du2qc0sidUerIUCz49V2qOIWeBSBbTMe-vT-1j-a6gCxSvR5IkAzHnQ7-_RX7AiZEKGgKESfA1-_8yc9taEYe2dNeNBl0tiB9YlP6qDqjkK2DEVrTSgKTRDRscy6WPRhuBUefmc2VbN2qfnXjEoP5A_hKIAEwAQ; __Secure-1PSIDTS=sidts-CjEB4E2dkZjXvucHenoybS3qSU5lqjDuFAgabLKfVN2SzG8ohuNBYsRQ5DofuDGZBIRXEAA; __Secure-3PSIDTS=sidts-CjEB4E2dkZjXvucHenoybS3qSU5lqjDuFAgabLKfVN2SzG8ohuNBYsRQ5DofuDGZBIRXEAA; OTZ=7648197_34_34__34_; NID=515=kHM5htqF_2F-tMcKQkHGWHqzgfe0dLxAQkjKZmfNKciO3Ccg4Uhj3FL9RCVeeJ7kvotyuthyDDZc7h3p0UkEmPimO4GeRaZO5nyN7PCO8nVwRWrh7UtdG3xyUYaZrh1AJPYah7kF5WtP97bJ5AQEVwJsKEDC282YDasUcUR9BiD76r848p3vRzCXKD-xR4b-ZZfiqHYIMr1nqdo7C89XygDjUGxkQQGfHV9wt4lGgQhPYBrQYZUs5rYgjH5CbE3MuYD35Q6wTXlgkBtVoMohY5QP4h66fBNwQEflbGopLv3v4P30FlfsUog5pxzQq9yisSpnmiBBciz-EBge-CSJCz0hwqz111BMYze6Ml2sqzY-TmJ1ZGQY_hYGfHyuG2wlPeKJ0RTWhei50EqXB6h4E5yUHXC-aHAmiZx586HoXaUXjDvea0D_mojBYZNSeMKD0rQ4lUOPp-_uaxoY9KVdPMOQ4n36yHNV_gXUVm6uHUvzqn4dx7VMlRf8_DQxtTk9P1G9qDoZje_phAHUVRRshHlo9q6Kyjtsmi8bajYCXcDEncg4i6DWR8w8gIx8WfKdEHRu1hgkR33UFiHW6VpQ2o4pzDdmCmlneZaC5mlI99LS0DcKgIUgG02m_Vy35mvEhSfNacE1rqkCQGmJLwOhrQrM_MDTVhfjl5-EqD957kp9UlbJtlo5Afg2sQ5xdHg1cu6zjISbkVSgnuAQKeC_EXZZSnkgDs10NAMNxJkbkLiEbd0RqH5ObelAsM0KHQ; SIDCC=AKEyXzWvKQrruXKAdmwehhbNM4pXxMNLO_jrblTYaoc6cYIRBVwWmp1Yt7GrPaw2l2-cVbbvPKg; __Secure-1PSIDCC=AKEyXzU5WA6hUZ5vkrmegK13ZzwdcwUxVokeHnUV3FqrtT0oHu43CQI3GUUxvCP7lzs1k10zRg; __Secure-3PSIDCC=AKEyXzXiE8jvhxeBjwebPGRkcOn-eiBmJiQQu9crJTnDhalPP4QbZ0rQSWl69tDcJ00xzDEEA4I',
    'origin': 'https://docs.google.com',
    'priority': 'u=0, i',
    'referer': 'https://docs.google.com/forms/d/e/1FAIpQLSeN7mNzNn7zmzuUF3vrDECfNBdV6DjZJOLE2aJ8cH0jUGf5mQ/viewform?fbzx=1907626324655614838',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-form-factors': '"Desktop"',
    'sec-ch-ua-full-version': '"126.0.6478.127"',
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
    'x-chrome-connected': 'source=Chrome,id=117215602054226029849,mode=0,enable_account_consistency=false,supervised=false,consistency_enabled_by_default=false',
    'x-client-data': 'CI22yQEIorbJAQipncoBCL7oygEIlaHLAQiTossBCIWgzQEIrJ7OAQinos4BCOGnzgEImqjOAQierM4BCP2szgEIpK7OARj1yc0BGKGdzgEYyZ/OAQ==',
}

data = {
    'entry.534338411': 'kokgmai@f.com',
    'entry.77806846': 'jaiajia',
    'entry.348404257': 'mxfof',
    'entry.1780318721': 'odjn',
    'entry.1176870615_year': '2002',
    'entry.1176870615_month': '12',
    'entry.1176870615_day': '12',
    'entry.1931930803': 'Team A',
    # 'dlut': '1721197502998',
    # 'hud': 'true',
    # 'entry.1931930803_sentinel': '',
    # 'fvv': '1',
    # 'partialResponse': '[null,null,"1907626324655614838"]',
    # 'pageHistory': '0',
    # 'fbzx': '1907626324655614838',
    # 'submissionTimestamp': '1721197507792',
}
par = 'entry.534338411=kamal%40poka.com&entry.77806846=kamal+poka&entry.348404257=kooka&entry.1780318721=jaija&entry.1176870615_year=1212&entry.1176870615_month=12&entry.1176870615_day=12&entry.1931930803=Team+A&dlut=1721196821485&entry.1931930803_sentinel=&fvv=1&partialResponse=%5Bnull%2Cnull%2C%22-1434449377473467695%22%5D&pageHistory=0&fbzx=-1434449377473467695&submissionTimestamp=1721196819424'
post_url = 'https://docs.google.com/forms/d/e/1FAIpQLSeN7mNzNn7zmzuUF3vrDECfNBdV6DjZJOLE2aJ8cH0jUGf5mQ/formResponse'


print(requests.post(url=post_url, data=data,headers=headers, cookies=cookies))
# for i in range(25):
#     print(i, 'th request...')

#!/usr/local/bin/python3
import requests
import json
import sys

URL = "https://www.apple.com/shop/retail/pickup-message?parts.0=Z0YQ&searchNearby=true&option.0=M02F3LL%2FA%2CMY832AM%2FA&store=R072"

PAYLOAD = {':authority': 'www.apple.com',
           ':method': 'GET',
           ':path': '/shop/retail/pickup-message?parts.0=Z0YQ&searchNearby=true&option.0=M02F3LL%2FA%2CMY832AM%2FA&store=R072',
           ':scheme': 'https',
           'accept': 'application/json, text/javascript, */*; q=0.01',
           'accept-encoding': 'gzip, deflate, br',
           'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,zh-TW;q=0.6',
           'cache-control': 'no-cache',
           'cookie': 's_fid=44AC6EAACA5B2D72-3C43D4A98FEA43C6; dssid2=f643b9a8-0930-4f93-9b1f-ebd18685a0aa; dssf=1; xp_ci=3z2v8niAz16tz4RHz9aNzqKhGQmRX;    rtsid=%7BUS%3D%7Bt%3Da%3Bi%3DR072%3B%7D%3B%7D; as_xs=idmsl=1; as_xsm=1&B8QCexeQjrLI6Z8QeORX6w; as_cn=~CejlIc5bS4lDS1mv_cTKP6Wk8_jt4of4nj70V_U9NqY=;    as_loc=714c30af37d47f870f0b0558f5233674138bf9d5e5386c3a37aa814fcfe818e37344df1abb6fdfdda38589edae7e7aa64d5ce53d98814e4b3d4939e198ada309215d612f5fa26782feac62a38d6640427554d   6ddb5840b2fd9edd18b154e2a92; s_vnum_n2_us=4%7C6; pxro=2; acn01=1Bu7+H12ffywFJtKTSxpxpfotuGfhaI/EFZI7wAFgCniiP4c;    as_disa=AAAjAAABi-tBKyEd_Kv8jDY9SE3LpU-vVlr1i5jIRBGNRm8saJYp20jOmmYuERxlVkKtvPytAAIBXlyxfGcCsHr5BKLw5N6TmP0PrsesRfESy2aw54WLz3M=;    as_rec=9a6cf4c96d2b0411392f4dd6ccab9466a053e148a919df0c1e80dcc9d48e1636b83d641b9b645272d7f382f32affcfb2a2fa69f4676829bd368ed3209b4cfd714469842ea68c3d12d8e3e9b30a5b0862;    geo=US; ccl=UB/akMYvpj7v2ef/AAnDLNxY+4k6CdeKtOXEGpfN+0ouIYt8MYKqNKnYLA8Qguwq284J4gXR9YWOlpT2c4Ev6bTCvmVUAnmLdhHr6/XU4k5hgImpOGNQVS4DcsW3Cha6ktFv6jFE2v0YWQtMDx   +soQiJP7P6ksi0cCk+K5XLiPyb4A0KZCmK+rVquQ+72L1aCo7gwNSIWbAbkiNBZ4BDuKn4ya9YKrEzFC8nOsSu/9xPVaWLHgwK2G70EiIrS7/Gx/KAEbeHvOhbZha+SRUtHHaf2i01TqHz8   +jmfyjR8xRyA699GG3dmuK0ug5MAdrY; check=true; mbox=PC#7ac65ee833d04472ad8da360c0954717.35_0#1658017162|session#8779c07e62354880992a301aae63ce99#1601662940;    as_pcts=4rfrGBzddzMjlGncDp28sGKw-N3hcWqpoSjckW+lk-cliAz6aiTgELkJ_pR:SgrDdoV03_; as_dc=nc; s_cc=true; s_vi=[CS]v1|2FBBB44B8515964A-60000979E38CBE1C[CE];    as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; s_sq=%5B%5BB%5D%5D; as_atb=1.0|MjAyMC0xMC0wMiAxMDo1ODoyNA|14879726a4f30a8bd056c701a9043999eb7820a0',
           'pragma': 'no-cache',
           'referer': 'https://www.apple.com/shop/buy-watch/apple-watch?option.watch_cases=M02F3LL%2FA&option.watch_bands=MY832AM%2FA&configured=true&product=Z0YQ&step=detail',
           'sec-fetch-dest': 'empty',
           'sec-fetch-mode': 'cors',
           'sec-fetch-site': 'same-origin',
           'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Mobile Safari/537.36',
           'x-requested-with': 'XMLHttpRequest'}

r = requests.get(url=URL, params=PAYLOAD)
r = r.json()
# print(json.dumps(r, indent=2, separators=(',', ': ')))

available_stores = []

for store in r['body']['stores']:
    name = store['storeName']
    if store['partsAvailability']['Z0YQ']['pickupSearchQuote'] != \
            "Unavailable for Pickup":
        available_stores.append(name)

if not available_stores:
    print('None available')
    sys.exit(0)

print('Available in {}'.format(', '.join(available_stores)))

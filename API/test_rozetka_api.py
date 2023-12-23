import json

import requests


def test_api():
    url = "https://uss.rozetka.com.ua/session/cart-se/add"
    ids = [375225780]
    headers = {
        'csrf-Token': 'pJiXzvFDkwLSKfvy58gWcUNmEx6miL2oyZgXc+dgTdDUTHz9',
        'cookie': 'cart-modal=old; ab-auto-portal=old; promo-horizontal-filters=verticalFilters; social-auth=old; ab_tile_filter=old; xab_segment=70; slang=ru; uid=Cgo9D2WG2acUqnWIye3iAg==; _gcl_au=1.1.836057032.1703336361; _uss-csrf=pJiXzvFDkwLSKfvy58gWcUNmEx6miL2oyZgXc+dgTdDUTHz9; ussapp=mSvffR3rWw3E3Q9NtakuyWHvOkxclY-h9hQuYYKl; cf_clearance=EvyqXpq9QM3tRy.ZdrbxrFrMfSv5kQh8XsProU8kJfc-1703336360-0-2-4ce27693.2bd322b1.1be32973-0.2.1703336360; ussat_exp=1703379560; ussajwt=eyJhbGciOiJSUzI1NiIsImtpZCI6InVzc2F0LnYwIiwidHlwIjoiSldUIn0.eyJkZXRhaWxzIjoiMjMyNWFmNzgzZGViZGExM2FhNzA3YjFmYzA0MzljOGZlMjJkMjU1OTcxZTY2Y2IxNjAxODBjNTE0YjcwMzY3NDQ1YTE1ZTVjMDJlNzE5NmZlMzNmOTAyZTY3NDc0Nzk5ZDEwMTA4YTNkNGVjZjU2NWJmMzhkYjM2OTE1NmZkZGRhZTIzNGIzZTVjNmU1YmQzNDE1ZDdlMDNhM2NjMmZhYjI3YTc3ZGRlYmI4NTdiOWRhZTJkMDE3YTlkNzQ0ZTdmYTEyYTRhOGE4ZTdiMDJjMmRiMzQzNDhhMGNmYmZmYTQzZDUzMWI3NWNjZTdlYmZlMTA5OGNjYzE2M2VmMjQ4ZSIsImV4cCI6IjE3MDMzNzk1NjAiLCJ1c3NhdCI6IjI1N2NmYjNhN2NmZjU1ZDM4ZDMyNWViMzAyZGJmMDdjLnVhLWM3NmZkMWVlYTVkMTRmMDczYjA1MGMzYzk5ZjM5MDVlLjE3MDMzNzk1NjAifQ.TBgl_8m2Kt17w1CaM6dM1m6lT5aCuiZpUZz_7YAdFfvXs-urwH82JgnftDL2RwI9IJoDy9iQjHPIvYYj8Td-0qdo6xaHGQ1B1TIjeK-FzvA1Gi-PmbvM084LBl9y-MjLBOuq1ITsqf0hx58Tx_jSDJKKXx9t3EyAsU4fx_SUXgWbdp8TFEANWzDfdZkn0XDSYVCimDNkqA_TE3HNBSb3QxPJDiL6peMh5RE7FHf3-lofZYvQzXwuCuTOZaBitDWGRoOdk0TCDmdqjGWRE-2DBkdMtOzH9gD3xdsKBo0TpoxuWl017WdEFval2M4I822AumC3NqJvx_GGdb7AvJBk0g; ussat=257cfb3a7cff55d38d325eb302dbf07c.ua-c76fd1eea5d14f073b050c3c99f3905e.1703379560; ussrt=af447741b01a55d31564affcff9df42a.ua-c76fd1eea5d14f073b050c3c99f3905e.1705928360; __utmz_gtm=utmcsr=google|utmccn=(none)|utmcmd=organic; _ga=GA1.3.1282135181.1703336361; _gid=GA1.3.1865686384.1703336361; afclid=15395859111703336361; city_id=548de26c-2ba4-4b32-82a2-1216f6886ebd; rz_ch_mo=on; __cf_bm=ULs6HT0LA1nuyHvJS6CnhrZAVwTlzfkiBqiHah9BsRg-1703338873-1-ARUXQCQ+iR48mvBjnFPv47z2rouGyRR71kQNMVH6w8Zz9/9v49gzZUuc9+3eHkvnCtyLMSrMAR3bB19NE8DGnvg=',
        'content-type': 'application/json'
    }
    for id in ids:
        payload = json.dumps([
            {
              "goods_id": id,
              "quantity": 1
            }
        ])
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)

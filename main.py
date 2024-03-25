# import library
import requests
import os
import bs4
import json
import pandas as pd


# jumlah halaman
jumlah_halaman = 3

# url website
URL = "https://www.mobil123.com/dealer/carsomeindonesia?page_number={halaman}&page_size=50"

# menggunakan user-agent
headers = {
  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'
}

# menginisialisasi Session request
session = requests.Session()

# menampung semua data
tampung_semua_data = []

# looping semua halaman dan memparsing
for halaman in range(1, jumlah_halaman + 1):
  respon = session.get(url=URL.format(halaman=halaman), headers=headers)
  soup = bs4.BeautifulSoup(respon.content, "lxml")
  datas = soup.find_all("script")[2].text
  datas = json.loads(datas)
  for data1 in datas:
    for data2 in data1['itemListElement']:
      tampung = {}
      tampung["vehicleModelDate"] = data2['item']['vehicleModelDate']
      tampung["brandName"] = data2['item']['brand']['name']
      tampung["name"] = data2['item']['name']
      tampung_semua_data.append(tampung)

# menyimpan file
tampung_semua_data = pd.DataFrame(tampung_semua_data)
tampung_semua_data.to_csv("DATA-MOBIL.csv")

print("---SELESAI---")




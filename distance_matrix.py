
from sklearn.neighbors import DistanceMetric
from math import radians
import pandas as pd
import numpy as np

#df = pd.read_excel('data.xlsx')
cities_df = pd.DataFrame({'city':["Adana Şakirpaşa Airport","İncirlik Air Base","Adıyaman Airport","Afyon Airport","Ağrı Ahmed-i Hani Airport","Gazipaşa Airport","Merzifon Air Base","Güvercinlik Army Air Base","Ankara Esenboğa Airport","Etimesgut Air Base","Mürted Air Base","Antalya Airport","Aydın Çıldır Airport","Balıkesir Air Base","Bandırma Air Base","Balıkesir Koca Seyit Airport","Batman Airport","Bingöl Airport","Bursa Yunuseli Airport","Bursa Yenişehir Airport","Çanakkale Airport","Gökçeada Airport","Denizli Çardak Airport","Diyarbakır Air Base","Elazığ Airport","Erzincan Airport","Erzurum Airport","Sivrihisar Air Base","Eskişehir Air Base","Eskişehir Hasan Polatkan Airport","Gaziantep Airport","Hakkari–Yüksekova Selahaddin Eyyubi Airport","Hatay Airport","Iğdır Airport","Isparta Airport","Isparta Süleyman Demirel Airport","Istanbul Atatürk Airport","Istanbul Samandıra Army Air Base","Istanbul Sabiha Gökçen Airport","Istanbul Hanali Airport","İzmir Adnan Menderes Airport","Gaziemir Army Air Base","Çiğli Air Base","Kaklıç Air Base","Kahramanmaraş Airport","Kars Harakani Airport","Kastamonu Airport","Erkilet Air Base","Cengiz Topel Naval Air Station","Konya Air Base/Airport","Kütahya Air Base","Zafer Airport","Malatya Tulga Army Air Base","Erhaç Air Base","Akhisar Air Base","Mardin Airport","Dalaman Airport","Bodrum-Imsik Airport","Milas–Bodrum Airport","Muş Airport","Nevşehir Kapadokya Airport","Ordu Giresun Airport","Samsun Samair Airport","Samsun-Çarşamba Airport","Siirt Airport","Sinop Airport","Sivas Nuri Demirağ Airport","Şanlıurfa Airport","Şanlıurfa GAP Airport","Şırnak Şerafettin Elçi Airport","Tekirdağ Çorlu Airport","Tokat Airport","Trabzon Airport","Uşak Airport","Van Ferit Melen Airport","Yalova Air Base", "Zonguldak Çaycuma Airport"],
    'lat':[36.98, 37, 37.73, 38.75, 39.65, 36.3, 40.83, 39.93, 40.12, 39.95, 40.07, 36.9, 37.82, 39.62, 40.32, 39.55, 37.93, 38.87, 40.17, 40.25, 40.13, 40.2, 37.78, 37.88, 38.6, 39.72, 39.95, 39.45, 39.77, 39.82, 36.95, 37.55, 36.37, 39.98, 37.75, 37.87, 40.97, 41, 40.9, 41.27, 38.28, 38.32, 38.5, 38.52, 37.53, 40.57, 41.32, 38.77, 40.73, 37.97, 39.42, 39.1, 38.35, 38.43, 38.97, 37.22, 36.7, 37.13, 37.25, 38.75, 38.77, 40.97, 41.27, 41.27, 37.98, 42.02, 39.8, 37.12, 37.45, 37.37 ,41.13, 40.3, 41, 38.67, 38.47, 40.68, 41.52],
                          'lon':[35.28,35.42,38.47,30.52,43.03,32.3,35.52,32.75,32.98,32.68,32.57,30.8,27.88,27.92,27.97,27.02,41.12,40.58,29.07,29.57,26.42,25.88,29.7,40.2,39.28,39.52,41.17,31.35,30.57,30.52,37.48,44.23,36.28,43.87,30.55,30.38,28.82,29.22,29.3,28.75,27.15,27.15,27.02,26.98,36.95,43.12,33.8,35.48,30.07,32.55,30.02,30.12,38.25,38.08,27.85,40.63,28.78,27.67,27.67,41.67,34.52,38.07,36.28,36.57,41.83,35.07,36.9,38.77,38.9,42.07,27.92,36.37,39.77,29.47,43.33,29.38,32.08]
                          })
cities_df['lat'] = np.radians(cities_df['lat'])
cities_df['lon'] = np.radians(cities_df['lon'])

dist = DistanceMetric.get_metric('haversine')

cities_df[['lat','lon']].to_numpy()
dist.pairwise(cities_df[['lat','lon']].to_numpy())*6373

test = pd.DataFrame(dist.pairwise(cities_df[['lat','lon']].to_numpy())*6373,  columns=cities_df.city.unique(), index=cities_df.city.unique())
print(test.to_string())

file_name = 'DistanceMatrix_sheet.xlsx'
  
# saving the excelsheet
test.to_excel(file_name)
print('Successfully exported into Excel File')

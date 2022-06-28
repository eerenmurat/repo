
from sklearn.neighbors import DistanceMetric
from math import radians
import pandas as pd
import numpy as np

#df = pd.read_excel('data.xlsx')
cities_df = pd.DataFrame({'city':['Adana Şakirpaşa Airport','İncirlik Air Base','Adıyaman Airport','Afyon Airport','Ağrı Ahmed-i Hani Airport','Gazipaşa Airport'],
    'lat':[36.98,37,37.73,38.75,39.65,36.3],
                          'lon':[35.28,35.42,38.47,30.52,43.03,32.3],
                          })
cities_df['lat'] = np.radians(cities_df['lat'])
cities_df['lon'] = np.radians(cities_df['lon'])

dist = DistanceMetric.get_metric('haversine')

cities_df[['lat','lon']].to_numpy()
dist.pairwise(cities_df[['lat','lon']].to_numpy())*6373

print(pd.DataFrame(dist.pairwise(cities_df[['lat','lon']].to_numpy())*6373,  columns=cities_df.city.unique(), index=cities_df.city.unique()))

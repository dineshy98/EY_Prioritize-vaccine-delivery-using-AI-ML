# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 23:13:57 2020

@author: dineshy86
"""

import geopandas as gpd
import pandas as pd

df1 = gpd.read_file('S:/Hackathons/EY/vis/c44c9b96-f570-4ee3-97f1-ebad64efa4c2202044-1-1rb4x6s.8xx6.shp')
df1.head()

df1.plot()
for i in range(df1.shape[0]): df1['statename'][i] = df1['statename'][i].title()

df1['statename'].replace({'Andaman & Nicobar': 'Andaman and Nicobar Islands', 
                          'Dadra & Nagar Have': 'Dadra and Nagar Haveli and Daman and Diu',
                          'Daman & Diu' : 'Dadra and Nagar Haveli and Daman and Diu',
                          'Jammu & Kashmir' : 'Jammu and Kashmir'}, inplace=True)


df1['distname'].replace({'Baramula' : 'Baramulla',
                         'Bandipore' : 'Bandipora',
                         'Badgam' : 'Budgam',
                         'Shupiyan' : 'Shopiyan',
                         'Sahibzada Ajit Singh Nag*' : 'S.A.S. Nagar',
                         'Firozpur': 'Ferozepur',
                         'Lahul & Spiti' : 'Lahaul and Spiti',
                         'Charki Dadri': 'Charkhi Dadri',
                         'Central' : 'Central Delhi',
                         'East' : 'East Delhi',
                         'North' : 'North Delhi', 
                         'South West' : 'South West Delhi', 
                         'South' : 'South Delhi', 
                         'North East' : 'North East Delhi', 
                         'West' : 'West Delhi', 
                         'South East': 'South East Delhi', 
                         'North West' : 'North West Delhi',
                         'Jhunjhunun': 'Jhunjhunu', 
                         'Jalor' : 'Jalore', 
                         'Chittaurgarh' : 'Chittorgarh', 
                         'Dhaulpur': 'Dholpur',
                         'Chota Udaipur': 'Chhota Udaipur', 
                         'Kachchh' : 'Kutch', 
                         'The Dangs' : 'Dang', 
                         'Banas Kantha' : 'Banaskantha', 
                         'Ahmadabad' : 'Ahmedabad', 
                         'Sabar Kantha' : 'Sabarkantha', 
                         'Dohad' : 'Dahod', 
                         'Mahesana' : 'Mehsana', 
                         'Panch Mahals' : 'Panchmahal', 
                         'Faizabad' : 'Ayodhya', 
                         'Kheri' : 'Lakhimpur Kheri', 
                         'Bara Banki': 'Barabanki', 
                         'Mahrajganj' : 'Maharajganj',
                         'Pashchim Champaran': 'West Champaran', 
                           'Mahrajganj' : 'Maharajganj',
                         'Pashchim Champaran': 'West Champaran', 
                         'Kaimur (bhabua)': 'Kaimur', 
                         'Purba Champaran': 'East Champaran',
                         'Purbi Singhbhum': 'East Singhbhum', 
                         'Pashchimi Singhbhum': 'West Singhbhum', 
                         'Saraikela-kharsawan': 'Saraikela-Kharsawan', 
                         'Kodarma': 'Koderma',
                         'Narsimhapur': 'Narsinghpur', 
                         'West Nimar': 'Khargone', 
                         'East Nimar': 'Khandwa',
                         'Janjgir - Champa' : 'Janjgir Champa',
                         'Almora\n': 'Almora',
                         'Garhwal': 'Pauri Garhwal', 
                         'Hardwar': 'Haridwar', 
                         'Darjiling': 'Darjeeling', 
                         'Maldah' : 'Malda', 
                         'North Twenty Four Pargan*' : 'North 24 Parganas', 
                         'Medinipur West' : 'Paschim Medinipur', 
                         'Puruliya': 'Purulia', 
                         'South Twenty Four Pargan*' : 'South 24 Parganas',
                         'North  District': 'North District',
                         'South Salmara Mancachar': 'South Salmara Mankachar',
                         'Anugul': 'Angul', 
                         'Jajapur': 'Jajpur', 
                         'Jagatsinghapur' : 'Jagatsinghpur', 
                         'Baleshwar': 'Balasore', 
                         'Baudh': 'Boudh', 
                         'Debagarh' : 'Deogarh',
                         'Ahmadnagar' : 'Ahmednagar', 
                         'Gondiya' : 'Gondia', 
                         'Bid' : 'Beed', 
                         'Buldana': 'Buldhana',
                         'Jagitial' : 'Jagtial', 
                         'Jayashankar' : 'Jayashankar Bhupalapally', 
                         'Jangoan': 'Jangaon', 
                         'Kumuram Bheem Asifabad' : 'Komaram Bheem',
                         'Y.S.R.': 'Y.S.R. Kadapa', 
                         'Sri Potti Sriramulu Nell*' : 'S.P.S. Nellore',
                         'Bangalore' : 'Bengaluru Urban',
                         'The Nilgiris': 'Nilgiris', 
                         'Kanniyakumari' : 'Kanyakumari',
                         'North  & Middle Andaman': 'North and Middle Andaman',
                      'Dadra & Nagar Haveli': 'Dadra and Nagar Haveli'},inplace = True)



df1_key = pd.DataFrame(df1[['statename','distname']])
df1_key.columns = ['state','district']

district_wise.columns
dist_key = pd.DataFrame(main[['State','District','State_Code']])
dist_key.columns = ['state','district','state_code']

compare(df1_key['district'],main['district'])



 
dict2 = {
'Ashok Nagar': 'Ashoknagar',
 'Ayodhya':'Faizabad',
 
 
 'Bagalkote':'Bagalkot',

 'Bametara':'Bemetara',
 
 'Bargarh':'Bargarh (Baragarh)',
 'Belagavi':'Belgaum',
 
 'Bengaluru Rural':'Bangalore Rural',
 'Bengaluru Urban':'Bangalore Urban',
 'Biswanath' : 'Bishwanath',
 
 'Boudh':'Boudh (Bauda)',
 'Budgam':'Badgam',

 'Chhota Udaipur':'Chhota Udepur',
 'Chikkamagaluru': 'Chikmagalur',

 'Debagarh (Deogarh)' : 'Deogarh',
 'Devbhumi Dwarka':'Devbhoomi Dwarka',

 'East District':'East Sikkim',
 'Ferozepur':'Firozpur',

 'Gautam Buddha Nagar': 'Gautam Buddh Nagar',
'Gurugram':'Gurgaon',

 'Hisar': 'Hissar',

 'Janjgir Champa':'Janjgir-Champa',
 'Jayashankar Bhupalapally':'Jayashankar Bhupalpally',
 'Kabeerdham':'Kabirdham',
 'Kancheepuram':'Kanchipuram',
 'Kendujhar':'Kendujhar (Keonjhar)',

'Mahabubnagar':'Mahbubnagar',
 'Mahe':'Mahé',
 'Malda':'Maldah',
 'Medchal Malkajgiri':'Medchal-Malkajgiri',

 
 'Mumbai':'Mumbai City',
 'Mumbai Suburban':'Mumbai suburban',

 'Mysore':'Mysuru',
 'Nabarangapur':'Nabarangpur',
 'Nicobar':'Nicobars',
 
 'North District':'North Sikkim',
 
 'Ri Bhoi':'Ribhoi',
 
 'S.P.S. Nellore':'Sri Potti Sriramulu Nellore',
'Saraikela-Kharsawan':'Seraikela Kharsawan',
 
  'Rae Bareli':'Raebareli',
  'South District':'South Sikkim',
  'Thoothukkudi':'Thoothukudi',
  'Tiruppur':'Tirupur',
  'West District':'West Sikkim',
 
  'Shimoga':'Shivamogga',
 'Shopian':'Shopiyan',
 'Shravasti':'Shrawasti',

 'South Salmara':'South Salmara Mankachar',
  'Subarnapur':'Subarnapur (Sonepur)',

 'Thiruvallur': 'Tiruvallur',
 'Thiruvarur': 'Tiruvarur',
 'Allahabad' :  'Prayagraj',
  'Dakshin Bastar Dantewada':'Dantewada',
  'Y.S.R. Kadapa':'Kadapa',
 'Kalaburagi': 'Gulbarga',
 'Punch' :  'Poonch',
 
 'Hazaribagh':'Ramgarh',
'Kakching':'Thoubalbokeh',
 'Tengnoupal':'Chandel',
 'Tenkasi':'Tirunelveli',

 'Uttar Bastar Kanker':'Bastar',
 'Vijayapura':'Bijapur',
 
 'Kangpokpi':'Senapati',



  'Khandwa':'Harda',
 
 'Kra Daadi': 'Kurung Kumey',
}


df2_key = df1_key.replace(dict2)

dict3 = dict(zip(dist_key['state'].unique(),dist_key['state_code'].unique()))
df2_key['state_code'] =df2_key['state']
df2_key['state_code'].replace(dict3,inplace = True)

df2_key['district_key'] = df2_key['state_code']+'_'+df2_key['district']
compare(df2_key['district_key'],main['District_Key'])

 
 
 impute same values :

     
 'Hojai':'Nagaon',
 'Khargone':'Indore',
     
 'Leh':'Kishtwar',
 'Kargil':'Kishtwar'
 
 
 'Lepa Rada' : 'Siang',
 'Lower Siang':'Siang',
 
 
 
 'Mirpur':'Poonch',
 
 
  'Noney',
 
 'Pakke Kessang',
 'Muzaffarabad',
 'Raigad',
 'Ranipet',
 'S.A.S. Nagar',
 'Sahibzada Ajit Singh Nagar',
 'Shahdara',

 'Gaurella-Pendra-Marwahi',
 'South East Delhi',
 'Tirupattur',



 'Kallakurichi',
 'Yamunanagar'
 'Baghpat',

  'Agar Malwa' : part of Shajapur

 'Chengalpattu': part of kanchipuram






















vellore ranipet tirupathur ---->  sum
for i in range(df1.shape[0]):
        if df1['statename'][i] == 'Maharashtra' and df1['distname'][i] == 'Raigarh':
            df1['distname'][i] = 'Raigad'            

# Changing column name
df1 = df1.rename(columns={'distname': 'District', 'statename': 'State'})














































compare(df1['State'],main['state'])
compare(df1['District'],main['District_Key'])

df2 = pd.merge(df1,district_wise[['State_Code','District','State']],on = ['State','District'],how = 'left')
district_wise[['State_Code','State']]

df2['State_Code'].unique()
df2['District'] =  df2['State_Code'] + '_' + df2['District'] 




df1.loc[0]

newdf = df1.merge(districtdata[['State', 'District', 'Confirmed', 'Active', 'Recovered', 'Deceased']], on = ['District', 'State'])
newdf = newdf.merge(zones[['State', 'District', 'Zone']], on = ['District', 'State'])
newdf = newdf.drop(columns = ['statecode', 'state_ut', 'distcode', 'countrynam'])
newdf.head()



import json
from bokeh.io import show
from bokeh.io import output_file, save
from bokeh.models import (CDSView, ColorBar, ColumnDataSource,
                          CustomJS, CustomJSFilter, 
                          GeoJSONDataSource, HoverTool,
                          CategoricalColorMapper, LinearColorMapper, Slider)
from bokeh.layouts import column, row, widgetbox
from bokeh.io import output_notebook
from bokeh.plotting import figure




geosource = GeoJSONDataSource(geojson = newdf.to_json())

palette = ['red', 'orange', 'green']

color_mapper = CategoricalColorMapper(palette = palette, factors = ['Red', 'Orange', 'Green'])









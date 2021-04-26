import pandas as pd
import datetime

#import the data

dataset2014_Rivel =  pd.read_csv('Reading the 2014 river level database')
dataset2015_Rivel = pd.read_csv('Reading the 2015 river level database')
dataset2016_Rivel = pd.read_csv('Reading the 2016 river level database')

dataset2014_Meter = pd.read_csv('Reading weather database from 2014')
dataset2015_Meter = pd.read_csv('Reading weather database from 2015')
dataset2016_Meter = pd.read_csv('Reading weather database from 2016') 


#Standardizing base datetime

dataset2014_Rivel['tempo']= pd.to_datetime(dataset1['tempo'], dayfirst=True )
dataset2015_Rivel['tempo']= pd.to_datetime(dataset2['tempo'], dayfirst=True )
dataset2016_Rivel['tempo']= pd.to_datetime(dataset2['tempo'], dayfirst=True )
dataset2014_Meter['tempo']= pd.to_datetime(dataset2['tempo'], dayfirst=True )
dataset2015_Meter['tempo']= pd.to_datetime(dataset2['tempo'], dayfirst=True )
dataset2016_Meter['tempo']= pd.to_datetime(dataset2['tempo'], dayfirst=True )


#Merge the data by year even years

Dados_2014 = pd.merge_asof(dataset2014_Rivel, dataset2014_Rivel, on='tempo',by='tempo')
Dados_2015 = pd.merge_asof(dataset2015_Rivel, dataset2015_Meter, on='tempo',by='tempo')
Dados_2016 = pd.merge_asof(dataset2016_Rivel, dataset2016_Meter, on='tempo',by='tempo')


# Handling missing data and drop columns Date

Dados_2014.fillna(0,inplace=True)
Dados_2015.fillna(0,inplace=True)
Dados_2016.fillna(0,inplace=True)


Dados_2014 = Dados_2014.drop(['tempo'], axis=1)
Dados_2015 = Dados_2015.drop(['tempo'], axis=1)
Dados_2016 = Dados_2015.drop(['tempo'], axis=1)

# Gather all the data
dataset_all = pd.concat([Dados_2014,Dados_2015,Dados_2016])


#Transform the level value into a label (0 or 1), with 1 if it is above 200 cm or 0 below 200.

def categoriza(s):
   if s >= 200:
    return 1;
   else:
    return 0;


dataset_all = dataset_all['label'] = dataset_all['valor'].apply(categoriza)


#Add variable concentration time

dataset_all['TempoConcentracao'] = dataset_all['precipitacao'].rolling(min_periods=5, window=24).sum()


#Fiim
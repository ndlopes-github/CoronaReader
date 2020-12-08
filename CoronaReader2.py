#!/usr/bin/env python
# coding: utf-8

# In[190]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style as style
print(style.available)

style.use('seaborn-paper')
#style.use('Solarize_Light2') #ggplot')
style.use('seaborn-pastel') #ggplot')
style.use('seaborn-whitegrid') #ggplot')
#style.use('seaborn-darkgrid') #ggplot')
#style.use('fivethirtyeight') #ggplot')
# import seaborn as sns
# sns.set()
# sns.set_style("whitegrid")
#sns.set_style("whitegrid")
from datetime import date
plt.rcParams['figure.dpi'] = 170
plt.rcParams.update({'figure.autolayout': True})
plt.rcParams.update({'legend.labelspacing':0.15})
# # DADOS ECDPC
#  Com um dia de atraso para PT - DGS
#
#   https://www.ecdc.europa.eu/en/geographical-distribution-2019-ncov-cases
#
#  Tem a informação sobre a população.

#
# ## European Centre for Disease Prevention and Control
#
# Incubation period of 5.2 days on average
#
# A Chinese study published in the New England Journal of Medicine on Jan. 30[7], has found the incubation period to be 5.2 days on average, but it varies greatly among patients. The Chinese team conducting the study said their findings support a 14-day medical observation period for people exposed to the pathogen.
#
# For Wuhan travellers:
#
# The mean incubation period was estimated to be 6.4 days. The incubation period ranges from 2.1 to 11.1 days. The upper limit of 11.1 days could be considered conservative.[10]
#

# In[191]:


MA=14 # FOR MOVING AVERAGES
def moving_average(data_set, periods=6):
    weights = np.ones(periods) / periods
    return np.convolve(data_set, weights, mode='valid')

# In[192]:


# Create URL to CSV (since 27-03) file (alternatively this can be a filepath)
#
#urlxls = 'https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide-2020-07-03.xlsx'
#xlsFile = requests.get(url, allow_redirects=True)

urlcsv='https://opendata.ecdc.europa.eu/covid19/casedistribution/csv'

# Load the first sheet of the Excel file into a data frame
#df = pd.read_excel(urlxls, sheet_name=0, header=0)
df = pd.read_csv(urlcsv, encoding = "ISO-8859-1")
#df['dateRep'] = pd.to_datetime(df['dateRep'], format='%d/%m/%Y')
print(df[:3])
#df.loc[:,'Countries and territories']


# ## adaptação do formato da data

# In[193]:


df['dateRep'] = pd.to_datetime(df['dateRep'], format='%d/%m/%Y')
#print(df[1000:1500])


# In[194]:


countries=df['countriesAndTerritories'].unique()
geoIDS=df['geoId'].unique()
#print(len(countries),countries)


# # Find first day with a positive case for each country

# In[195]:


df[df['countriesAndTerritories']=='United_States_of_America'].iloc[:4]
#df[df['countriesAndTerritories']=='Brazil'].iloc[:40,5].sum()


# In[196]:


df[df['countriesAndTerritories']=='Italy'].iloc[:3]


#
#
# indexpositives=[]
# for countryindex in range(len(countries)):
#     indexpositives.append(np.where(conf[countryindex]>=1))
#
#



### Base de Dados Johns Hopkins Recovered
#recov='COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv'
## recov=' https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_recovered_global.csv&filename=time_series_covid19_recovered_global.csv'
recov='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv'
dfr=pd.read_csv(recov)
#dfr['dateRep'] = pd.to_datetime(df['dateRep'], format='%d/%m/%Y')
print(dfr[dfr['Country/Region']=='US'])





ptdf = df[df['geoId'] == 'PT']
ptdate='2020-03-03'
ptdf = ptdf[ptdf['dateRep'] >= ptdate]
Npt=ptdf.iloc[0,9]/100000 # População por 100 000
ptrec=dfr[dfr['Country/Region']=='Portugal'].iloc[0,4:].loc['3/2/20':]
print(len(ptrec.values), len(ptdf['deaths'].values),len(ptdf['cases'].values))
print(ptrec)
print(ptdf[:5])

#print(ptdf)


# # DADOS ESPANHA

# In[198]:


spdf = df[df['geoId'] == 'ES']
spdate='2020-02-25'
spdf = spdf[spdf['dateRep'] >= spdate]
Nsp = spdf.iloc[0,9]/100000 # População por 100 000
sprec=dfr[dfr['Country/Region']=='Spain'].iloc[0,4:].loc['2/24/20':]
print(len(sprec.values), len(spdf['cases'].values))
#print(sprec.values)


# # DADOS ITÁLIA

# In[199]:


itdf = df[df['geoId'] == 'IT']
itdate='2020-02-22'
itdf = itdf[itdf['dateRep'] >= itdate]
Nit =  itdf.iloc[0,9]/100000 # População por 100 000
itrec=dfr[dfr['Country/Region']=='Italy'].iloc[0,4:].loc['2/21/20':]
print(len(itrec.values) == len(itdf['cases'].values), "deveria ser igual")
#print(itrec.values)
#print(itdf)


# # DADOS FRANçA

# In[200]:


frdf = df[df['geoId'] == 'FR']
frdate='2020-02-26'
#frschool='2020-03-2'
#frschoolgap=frdf[frdf['DateRep'] == frdate].index-frdf[frdf['DateRep'] == frschool].index
#print(frschoolgap[0])
frdf = frdf[frdf['dateRep'] >= frdate]
Nfr = frdf.iloc[0,9]/100000 # População por 100 000
frrec=dfr[dfr['Country/Region']=='France'].iloc[0,4:].loc['2/25/20':]
print(len(frrec.values) == len(frdf['cases'].values), "deveria ser igual")

# # Dados Suécia

# In[201]:


sedf = df[df['geoId'] == 'SE']
sedate='2020-02-27'
sedf = sedf[sedf['dateRep'] >= sedate]
Nse = sedf.iloc[0,9]/100000 # População por 100 000
serec=dfr[dfr['Country/Region']=='Sweden'].iloc[0,4:].loc['2/26/20':]
print(len(serec.values) == len(sedf['cases'].values), "deveria ser igual")
#print(serec.values)


# # DADOS SUíçA

# In[202]:


chdf = df[df['geoId'] == 'CH']
chdate='2020-02-26'
chdf = chdf[chdf['dateRep'] >= chdate]
Nch = chdf.iloc[0,9]/100000 # População por 100 000
chrec=dfr[dfr['Country/Region']=='Switzerland'].iloc[0,4:].loc['2/25/20':]
print(len(chrec.values) == len(chdf['cases'].values), "deveria ser igual")
#print(chrec.values)


# # DADOS ALEMANHA, BRASIL, UK

# In[203]:


dedf = df[df['geoId'] == 'DE']
dedate='2020-02-26'
dedf = dedf[dedf['dateRep'] >= dedate]
Nde = dedf.iloc[0,9]/100000 # População por 100 000
derec=dfr[dfr['Country/Region']=='Germany'].iloc[0,4:].loc['2/25/20':]
print(len(derec.values) == len(dedf['cases'].values), "deveria ser igual")
#print(derec.values)


ukdf = df[df['geoId'] == 'UK']
ukdate='2020-02-24'
ukdf = ukdf[ukdf['dateRep'] >= ukdate]
Nuk = ukdf.iloc[0,9]/100000 # População por 100 000
ukrec=dfr[dfr['Country/Region']=='United Kingdom'].iloc[6,4:].loc['2/23/20':]
print(len(ukrec.values) == len(ukdf['cases'].values), "deveria ser igual")
#print(ukrec.values)


brdf = df[df['geoId'] == 'BR']
brdate='2020-02-26'
brdf = brdf[brdf['dateRep'] >= brdate]
Nbr = brdf.iloc[0,9]/100000 # População por 100 000
brrec=dfr[dfr['Country/Region']=='Brazil'].iloc[0,4:].loc['2/25/20':]
#print(brrec.values)


# # DADOS United States of America

# In[204]:


usdf = df[df['geoId'] == 'US']
usdate='2020-02-21'
usdf = usdf[usdf['dateRep'] >= usdate]
Nus = usdf.iloc[0,9]/100000 # População por 100 000
usrec=dfr[dfr['Country/Region']=='US'].iloc[0,4:].loc['2/20/20':]
#print(usrec.values)

print(Nus)


# # Dados JAPAN
jpdf = df[df['geoId'] == 'JP']
jpdate='2020-02-13'
jpdf = jpdf[jpdf['dateRep'] >= jpdate]
print(jpdf['cases'])
Njp = jpdf.iloc[0,9]/100000 # População por 100 000
jprec=dfr[dfr['Country/Region']=='Japan'].iloc[0,4:].loc['2/12/20':]
print(jprec)



nldf = df[df['geoId'] == 'NL']
nldate='2020-03-07'
nldf = nldf[nldf['dateRep'] >= nldate]
Nnl = nldf.iloc[0,9]/100000 # População por 100 000
nlrec= dfr[dfr['Country/Region']=='Netherlands'].iloc[0,4:].loc['3/6/20':]# A tratar
print(nldf[30:40])
print(nlrec.values)

bedf = df[df['geoId'] == 'BE']
bedate='2020-03-02'
bedf = bedf[bedf['dateRep'] >= bedate]
Nbe =  bedf.iloc[0,9]/100000 # População por 100 000
berec= dfr[dfr['Country/Region']=='Belgium'].iloc[0,4:].loc['3/1/20':]# A tratar
print(bedf['cases'])
print(berec.values)


rudf = df[df['geoId'] == 'RU']
rudate='2020-03-03'
rudf = rudf[rudf['dateRep'] >= rudate]
Nru =  rudf.iloc[0,9]/100000 # População por 100 000
rurec= dfr[dfr['Country/Region']=='Russia'].iloc[0,4:].loc['3/2/20':]# A tratar
print(rudf['cases'])
print(rurec.values)


# # Dados San Marino
smdf = df[df['geoId'] == 'SM']
smdate='2020-02-27'
smdf = smdf[smdf['dateRep'] >= smdate]
Nsm =  smdf.iloc[0,9]/100000 # População por 100 000
smrec= dfr[dfr['Country/Region']=='San Marino'].iloc[0,4:].loc['2/26/20':]# A tratar
print(smdf['cases'])
print(smrec.values)

# # Dados Greece
eldf = df[df['geoId'] == 'EL']
eldate='2020-02-27'
eldf = eldf[eldf['dateRep'] >= eldate]
Nel =  eldf.iloc[0,9]/100000 # População por 100 000
elrec= dfr[dfr['Country/Region']=='Greece'].iloc[0,4:].loc['2/26/20':]# A tratar
print(eldf['cases'])
print(elrec.values)

trdf = df[df['geoId'] == 'TR']
trdate='2020-03-12'
trdf = trdf[trdf['dateRep'] >= trdate]
Ntr =  trdf.iloc[0,9]/100000 # População por 100 000
trrec= dfr[dfr['Country/Region']=='Turkey'].iloc[0,4:].loc['3/11/20':]# A tratar
print(trdf['cases'])
print(trrec.values)


czdf = df[df['geoId'] == 'CZ']
czdate='2020-03-02'
czdf = czdf[czdf['dateRep'] >= czdate]
Ncz =  czdf.iloc[0,9]/100000 # População por 100 000
czrec= dfr[dfr['Country/Region']=='Czechia'].iloc[0,4:].loc['3/1/20':]# A tratar
print(czdf['cases'])
print(czrec.values)


hudf = df[df['geoId'] == 'HU']
hudate='2020-03-05'
hudf = hudf[hudf['dateRep'] >= hudate]
Nhu =  hudf.iloc[0,9]/100000 # População por 100 000
hurec= dfr[dfr['Country/Region']=='Hungary'].iloc[0,4:].loc['3/4/20':]# A tratar
print(hudf['cases'])
print(hurec.values)

atdf = df[df['geoId'] == 'AT']
atdate='2020-02-26'
atdf = atdf[atdf['dateRep'] >= atdate]
Nat =  atdf.iloc[0,9]/100000 # População por 100 000
atrec= dfr[dfr['Country/Region']=='Austria'].iloc[0,4:].loc['2/25/20':]# A tratar
print(atdf['cases'])
print(atrec.values)

ecdf = df[df['geoId'] == 'EC']
ecdate='2020-02-29'
ecdf = ecdf[ecdf['dateRep'] >= ecdate]
Nec =  ecdf.iloc[0,9]/100000 # População por 100 000
ecrec= dfr[dfr['Country/Region']=='Ecuador'].iloc[0,4:].loc['2/28/20':]# A tratar
print(ecdf['cases'])
print(ecrec.values)


phdf = df[df['geoId'] == 'PH']
phdate='2020-03-03'
phdf = phdf[phdf['dateRep'] >= phdate]
Nph =  phdf.iloc[0,9]/100000 # População por 100 000
phrec= dfr[dfr['Country/Region']=='Philippines'].iloc[0,4:].loc['3/2/20':]# A tratar
print(phdf['cases'])
print(phrec.values)

# # DADOS CHINA

# In[205]:


cndf = df[df['geoId'] == 'CN']
cndate='2020-01-03'
cndf = cndf[cndf['dateRep'] >= cndate]
#Ncn =  cndf.iloc[0,9]/1000000 # aqui isto não presta....
cnrec= dfr[dfr['Country/Region']=='China'].iloc[0,4:].loc['2/1/20':]# A tratar
#print(cnrec.values)
Ncn=1390
NcnW=11
NcnHub=59


# # Tratamento numérico e plots

# In[206]:



portugal={'country': 'Portugal', 'color':'b', 'label':'Portugal','ls': '-.','markers': '.',
          'cases':ptdf['cases'].values,'deaths':ptdf['deaths'].values,'pop':Npt,
          'recovered':ptrec.values}

spain={'country': 'Spain', 'color':'y', 'label':'Espanha', 'ls': '-','markers': '',
       'cases':spdf['cases'].values,'deaths':spdf['deaths'].values,'pop':Nsp,
       'recovered':sprec.values}

italy={'country': 'Italy', 'color':'g', 'label':'Itália','ls': '-','markers': '',
       'cases':itdf['cases'].values,'deaths':itdf['deaths'].values,'pop':Nit,
       'recovered':itrec.values}

france={'country': 'France', 'color':'r', 'label':'França','ls': '-','markers': '',
        'cases':frdf['cases'].values,'deaths':frdf['deaths'].values,'pop':Nfr,
        'recovered':frrec.values}

sweden={'country': 'Sweden', 'color':'c', 'label':'Suécia','ls': '-','markers': '',
        'cases':sedf['cases'].values,'deaths':sedf['deaths'].values,'pop':Nse,
        'recovered':serec.values}

switzerland={'country': 'Switzerland', 'color':'brown', 'label':'Suiça','ls': '-','markers': '+',
             'cases':chdf['cases'].values,'deaths':chdf['deaths'].values,'pop':Nch,
             'recovered':chrec.values}

germany={'country': 'Germany', 'color':'purple', 'label':'Alemanha','ls': '-','markers': '',
         'cases':dedf['cases'].values,'deaths':dedf['deaths'].values,'pop':Nde,
         'recovered':derec.values}

united_kingdom={'country': 'United_Kingdom', 'color':'coral', 'label':'Inglaterra','ls': '-','markers': '',
                'cases':ukdf['cases'].values,'deaths':ukdf['deaths'].values,'pop':Nuk,
                'recovered':ukrec.values}

brazil={'country': 'Brazil', 'color':'silver', 'label':'Brasil','ls': '-','markers': '',
        'cases':brdf['cases'].values,'deaths':brdf['deaths'].values,'pop':Nbr,
        'recovered':brrec.values}

usa={'country': 'United_States_of_America', 'color':'cyan', 'label':'USA','ls': (0, (1, 1)),'markers': '',
       'cases':usdf['cases'].values,'deaths':usdf['deaths'].values,'pop':Nus,
     'recovered':usrec.values}

japan={'country': 'Japan', 'color':'gold', 'label':'Japão','ls': '-.','markers': '',
       'cases':jpdf['cases'].values,'deaths':jpdf['deaths'].values,'pop':Njp,
     'recovered':jprec.values}

netherlands={'country': 'Netherlands', 'color':'rosybrown', 'label':'Holanda','ls':(0, (2, 1, 1, 1)),'markers': '',
       'cases':nldf['cases'].values,'deaths':nldf['deaths'].values,'pop':Nnl,
     'recovered':nlrec.values}

belgium={'country': 'Belgium', 'color':'fuchsia', 'label':'Bélgica','ls': (0, (3, 1, 1, 1)),'markers': '.',
         'cases':bedf['cases'].values,'deaths':bedf['deaths'].values,'pop':Nbe,
         'recovered':berec.values}

russia={'country': 'Russia', 'color':'slategray', 'label':'Rússia','ls': (0, (4, 1, 3, 7)),'markers': '',
         'cases':rudf['cases'].values,'deaths':rudf['deaths'].values,'pop':Nru,
         'recovered':rurec.values}

sanmarino={'country': 'San Marino', 'color':'slateblue', 'label':'San Marino','ls': (1, (3, 2, 1, 2)),'markers': '*',
         'cases':smdf['cases'].values,'deaths':smdf['deaths'].values,'pop':Nsm,
         'recovered':smrec.values}

greece={'country': 'Greece', 'color':'peru', 'label':'Grécia','ls': (1, (1, 10, 1, 5)),'markers': '*',
         'cases':eldf['cases'].values,'deaths':eldf['deaths'].values,'pop':Nel,
         'recovered':elrec.values}

turkey={'country': 'Turkey', 'color':'rebeccapurple', 'label':'Turquia','ls': (1, (1, 3, 1, 10)),'markers': '.',
         'cases':trdf['cases'].values,'deaths':trdf['deaths'].values,'pop':Ntr,
         'recovered':trrec.values}

hungary={'country': 'Hungary', 'color':'forestgreen', 'label':'Hungria','ls': (1, (3, 3, 3, 3)),'markers': '',
         'cases':hudf['cases'].values,'deaths':hudf['deaths'].values,'pop':Nhu,
         'recovered':hurec.values}


austria={'country': 'Austria', 'color':'gainsboro', 'label':'Austria','ls': (1, (4, 1, 3, 4)),'markers': '*',
         'cases':atdf['cases'].values,'deaths':atdf['deaths'].values,'pop':Nat,
         'recovered':atrec.values}

czechia={'country': 'Czechia', 'color':'burlywood', 'label':'Req. Checa','ls': (1, (5, 1, 1, 5)),'markers': '+',
         'cases':czdf['cases'].values,'deaths':czdf['deaths'].values,'pop':Ncz,
         'recovered':czrec.values}

ecuador={'country': 'Ecuador', 'color':'brown', 'label':'Equador','ls': ':' ,'markers': '2',
         'cases':ecdf['cases'].values,'deaths':ecdf['deaths'].values,'pop':Nec,
         'recovered':ecrec.values}

philippines={'country': 'Filipinas', 'color':'k', 'label':'Filipinas','ls': '--' ,'markers': ' ',
         'cases':phdf['cases'].values,'deaths':phdf['deaths'].values,'pop':Nph,
         'recovered':phrec.values}

china={'country': 'China', 'color':'k', 'label':'China','ls': '-','markers': '',
       'cases':cndf['cases'].values,'deaths':cndf['deaths'].values,'pop':Ncn,
       'recovered':cnrec.values}

countrieslist=[portugal,
               spain,
               france,
               italy,
               switzerland,
               germany,
               united_kingdom,
               usa,
               sweden,
               japan,
               netherlands,
               belgium,
               #greece,
               #czechia,
               #turkey,
               #hungary,
               #philippines,
               austria,
               russia,
               brazil,
               china]

countrieslist0=countrieslist[:-1]
#for country in countrieslist:
#    print(country)





# Os dados estão ordenados do último para o primeiro dia.
# flip -> passa do primeiro para o último dia.

# In[207]:


for country in countrieslist0:
    country['cases']=np.flip(country['cases'])
    country['deaths']=np.flip(country['deaths'])


# # CASOS POSITIVOS

# In[208]:


for country in countrieslist0:
    plt.plot(moving_average(country['cases'],MA),
             label=country['label']+' '+str(round(country['pop']/10.0,2))+'M',
             ls=country['ls'],marker=country['markers'],
             color=country['color'])
plt.legend()
plt.ylim(0,50000)
plt.text(-2,10000,'WARNING: Valores Absolutos\n (Não compara bem)')
plt.xlabel("dias após primeiro caso")
plt.title('casos positivos por dia (média móvel  a '+str(MA)+' dias) '+str(date.today()))
plt.savefig('casospospordia'+str(date.today())+'.png')
plt.show()

# In[209]:


for country in countrieslist0:
    plt.plot(moving_average(country['cases']/country['pop'],MA),
        label=country['label'], ls=country['ls'],marker=country['markers'],color=country['color'])
plt.xlabel("dias após primeiro caso")
plt.title('(Velocidade de crescimento)\n casos positivos por dia por 100k (média móvel a '+str(MA)+' dias) '+str(date.today()))
#plt.text(5,100,'O período de incubação médio\n $\\approx$ 6 dias\n mas há casos entre 2 e 27 dias')
plt.legend()
#plt.ylim(0,1200)
plt.savefig('casospospordiapor100milmedia'+str(date.today())+'.png')
plt.show()



# In[211]:


for country in countrieslist0:
    plt.plot(country['cases'].cumsum()/country['pop'],
             label=country['label'], ls=country['ls'],marker=country['markers'],
             color=country['color'])
plt.legend()
plt.xlabel("dias após primeiro caso")
plt.title('casos positivos acumulados (por 100k) '+str(date.today()))
plt.savefig('casospospordiaacumuladopor100k'+str(date.today())+'.png')
plt.show()

# for country in countrieslist0:
#     plt.plot(country['cases'].cumsum()-country['recovered']/country['pop'],
#              label=country['label'], ls=country['ls'],marker=country['markers'],
#              color=country['color'])
# plt.legend()
# plt.xlabel("dias após primeiro caso")
# plt.title('casos ativos acumulados (por 100k) '+str(date.today()))
# plt.savefig('casospospordiamenosrecupacumuladopor100k'+str(date.today())+'.png')
# plt.show()


# # MORTOS

# In[212]:


for country in countrieslist0:
    plt.plot(moving_average(country['deaths'],MA),
             label=country['label']+' '+str(round(country['pop']/10.0,2))+'M',
             ls=country['ls'],marker=country['markers'],
             color=country['color'])
plt.legend(loc='upper right')
plt.ylim(0,1100)
plt.text(100,400,'WARNING: Valores Absolutos\n (Não compara bem)')
plt.xlabel("dias após primeiro caso")
plt.title('Mortos por dia (valores absolutos média a '+str(MA)+'dias)'+str(date.today()))
plt.savefig('mortospospordiamedia'+str(date.today())+'.png')
plt.show()

# In[213]:


for country in countrieslist0:
    plt.plot(country['deaths'].cumsum()/country['pop'],
             label=country['label']+' '+
             str(round(country['deaths'].cumsum().max()/country['pop'],1))+'(por 100k)',
             ls=country['ls'],marker=country['markers'],
             color=country['color'])

#plt.text(0,35,'?China: '+str(round(china['deaths'].cumsum().max()/china['pop'],1))+'($\\times$ M. Hab.)?')
#plt.text(0,25,'?China-Wuhan: '+str(round(china['deaths'].cumsum().max()/NcnW,1))+'/($\\times$ M. Hab.)?')
plt.xlabel("dias após primeiro caso")
#plt.xlim(0,40)
#plt.ylim(0,175)
plt.gca().set_yticklabels(['{:.0f}'.format(x) for x in plt.gca().get_yticks()])
plt.legend(loc='upper left')
plt.title('Evolução do nº de mortos por 100k '+str(date.today()))
plt.savefig('mortoscaumpor100k'+str(date.today())+'.png')
plt.show()

############################################## RECUPERADOS #################
for country in countrieslist0:
    plt.plot(moving_average(country['recovered']/country['pop'],MA),
             label=country['label']+' '+
             str(round(country['recovered'].max()/country['pop'],1))+'(por 100k)',
             ls=country['ls'],marker=country['markers'],
             color=country['color'])

plt.xlabel("dias após primeiro caso")
#plt.xlim(0,40)
#plt.ylim(0,16500)
plt.legend(loc='upper left')
#plt.yscale('log')
plt.gca().set_yticklabels(['{:.0f}'.format(x) for x in plt.gca().get_yticks()])
plt.title('Evolução do nº de recuperados por 100k '+str(date.today()))
plt.savefig('recuppor100k'+str(date.today())+'.png')
plt.show()


# for country in countrieslist0:
#     plt.plot(moving_average(country['recovered']/country['deaths'].cumsum(),MA),
#              label=country['label']+' '+
#              str(round(country['recovered'].max()/country['deaths'].sum(),1)),
#              ls=country['ls'],marker=country['markers'],
#              color=country['color'])

# plt.xlabel("dias após primeiro caso")
# #plt.xlim(0,40)
# #plt.ylim(0,100)
# plt.legend(loc='upper left')
# #plt.yscale('log')
# plt.title('Evolução do nº de recuperados (acumulado) por mortos (acumulado) '+str(date.today()))
# #plt.savefig('recuppormortos'+str(date.today())+'.png')
# plt.show()



# for country in countrieslist0:
#     plt.plot(moving_average(country['recovered']/country['cases'].cumsum(),MA),
#              label=country['label']+' '+
#              str(round(country['recovered'].max()/country['cases'].sum(),1)*100),
#              ls=country['ls'],marker=country['markers'],
#              color=country['color'])

# plt.xlabel("dias após primeiro caso")
# #plt.xlim(0,40)
# #plt.ylim(0,100)
# plt.gca().set_yticklabels(['{:.0f} %'.format(x*100) for x in plt.gca().get_yticks()])
# plt.legend(loc='upper left')
# #plt.yscale('log')
# plt.title('Evolução do nº de recuperados (acumulados) por nº casos (acumulados) '+str(date.today()))
# #plt.savefig('recupporcasos'+str(date.today())+'.png')
# plt.show()
# # In[214]:
####################################################################################


#  # CURVAS DE FASE DE CRESCIMENTO DE CASOS POSITIVOS

# In[210]:


# china['pop']=NcnW
# MA=6
for country in countrieslist0:
    plt.plot(moving_average(country['cases'].cumsum()/country['pop'],MA),moving_average(country['cases']/country['pop'],MA),
             label=country['label'], ls=country['ls'],marker=country['markers'],color=country['color'])
    # x=moving_average(country['cases'].cumsum()/country['pop'],MA)
    # y=moving_average(country['cases']/country['pop'],MA)
    # z = np.polyfit(x, y, 2)
    # pz =np.poly1d(z)
    # x=np.linspace(0,3000,150)
    # ptest=pz(x)
    # plt.ylim(0,170)
    # plt.plot(x,ptest, ls='--',lw=0.5,marker=country['markers'],color=country['color'])
plt.xlabel("Números de casos por 100k")
plt.title('velocidade de crescimento de casos positivos\n em função do número de casos (por 100k) (média móvel a '+str(MA)+' dias) '+str(date.today()))
#plt.text(800,40,'O período de incubação médio\n $\\approx$ 6 dias\n mas há casos entre 2 e 27 dias')
plt.legend()
#plt.xlim(0,25000)
#plt.ylim(0,1000)
plt.savefig('curvasdefase'+str(date.today())+'.png')
plt.show()




################################ Ajustes ##########################################
# adjustpredfile=open('numcaseprediction.txt','a+')
# for country in countrieslist[:-1]:
#     plt.plot(moving_average(country['cases'].cumsum()/country['pop'],MA),moving_average(country['cases']/country['pop'],MA),
#         label=country['label'], ls=country['ls'],marker=country['markers'],color=country['color'])
#     x=moving_average(country['cases'].cumsum()/country['pop'],MA)
#     y=moving_average(country['cases']/country['pop'],MA)
#     z = np.polyfit(x, y, 2)
#     pz =np.poly1d(z)
#     x=np.linspace(0,5500,5500)
#     ptest=pz(x)
#     stringtoprint=country['country']+' '+str(date.today())+' '+str(np.fabs(ptest).min())+' '\
#         +'{:.0f}'.format(round(x[np.fabs(ptest).argmin()],0)*country['pop'])+'\n'
#     print(stringtoprint)
#     adjustpredfile.write(stringtoprint)
#     plt.plot(x,ptest, ls='--',lw=0.5,color=country['color'])

# plt.xlabel("Números de casos por 100k")
# plt.title('velocidade de crescimento de casos positivos\n em função do número de casos (por 100k) (média móvel a '+str(MA)+'dias) '+str(date.today()))
# #plt.text(800,40,'O período de incubação médio\n $\\approx$ 6 dias\n mas há casos entre 2 e 27 dias')
# plt.ylim(0,300)
# plt.legend()
# plt.savefig('curvasdefaseAdjusted'+str(date.today())+'.png')
# plt.show()
# adjustpredfile.close()


# from scipy.optimize import curve_fit
# def sigm(x, a, b, c):
#     return a /( np.exp(-b * (x-c)) + 1)


# for country in countrieslist:
#     plt.plot(country['deaths'].cumsum()/country['cases'].sum(),
#              label=country['label'],ls=country['ls'],marker=country['markers'],
#              color=country['color'])
#     xdata=np.linspace(0,len(country['cases']),len(country['cases']))
#     popt, pcov = curve_fit(sigm,xdata,
#                        country['deaths'].cumsum()/country['cases'].sum(),bounds=([0,0,10], [.4, 1., 70])) # fitting sem constrangimentos
#     xdata=np.linspace(0,len(china['cases']),len(china['cases']))
#     plt.plot(xdata, sigm(xdata, *popt), lw=0.5, color=country['color']) #plot do fiiting

# #xdata=np.linspace(0,len(portugal['cases']),len(portugal['cases']))
# #popt, pcov = curve_fit(sigm,xdata,
#             #           portugal['deaths'].cumsum()/portugal['cases'].sum(),bounds=([0,0,20], [.1, 1., 60])) # fitting sem constrangimentos

# #xdata=np.linspace(0,len(china['cases']),len(china['cases']))
# #plt.plot(xdata, sigm(xdata, *popt), '.', color=portugal['color'],label='fit: pt') #plot do fiiting

# plt.xlabel("dias após primeiro caso")
# plt.xlim(0,180)
# plt.ylim(0,0.2)
# plt.legend()
# plt.gca().set_yticklabels(['{:.0f} %'.format(x*100) for x in plt.gca().get_yticks()])
# plt.title('Evolução do nº mortos por nº casos '+str(date.today()))
# plt.savefig('evolmortosporcasosAdjust'+str(date.today())+'.png')
# plt.show()

# In[215]:
#############################################################################################

for country in countrieslist0:
    plt.plot(moving_average(
        country['deaths'].cumsum()/
        country['cases'].sum(),MA),
        label=country['label']+' '+str(round(country['deaths'].sum()/country['cases'].sum()*100,2))+'%',
             ls=country['ls'],marker=country['markers'],
        color=country['color'])

plt.xlabel("Dias após o primeiro caso")
plt.legend(loc='upper left')
plt.title('Evolução do nº mortos por nº casos (média a '+str(MA)+' dias) '+str(date.today()))
plt.savefig('evolmortosporcasos'+str(date.today())+'.png')
plt.show()

# In[216]:


for country in countrieslist0:
    plt.plot(country['cases'].cumsum()/country['pop'],country['deaths'].cumsum()/country['pop'],
        label=country['label']+' '+str(round(country['deaths'].sum()/country['cases'].sum()*100,2))+'%',
             ls=country['ls'],marker=country['markers'],
        color=country['color'])

plt.xlabel("nº casos por 100k")
plt.legend(loc='lower right')
plt.title('(fase) nº mortos/100k em função do nº casos/100k '+str(date.today()))
plt.savefig('fasemortosporcasos'+str(date.today())+'.png')
plt.show()

# # %  TOTAL DEATHS PER TOTAL NUMBER OF CASES * 100

# In[ ]:


print('Percentagem de mortos \npor número de casos\n')
for country in countrieslist:
    print(country['country'],'=',round(country['deaths'].sum()/country['cases'].sum()*100,1),'%')


# In[ ]:


print('Número mortos por \n100k  pessoas\n')
for country in countrieslist:
    print(country['country'],'=',round(country['deaths'].sum()/country['pop'],1))


# # # O CASO CHINÊS

# # In[ ]:


# macncases=moving_average(cncases,MA)
# macndeaths=moving_average(cndeaths,MA)
# macndays=np.linspace(1,len(macncases),len(macncases))
# plt.plot(macndays,macncases,'-',label='cn')
# plt.legend()
# plt.xlabel("dias após primeiro caso")
# plt.title('casos positivos por dia china média móvel a '+ str(MA) +' dias')


# # In[ ]:


# macncases=moving_average(cncases,MA)
# macndeaths=moving_average(cndeaths,MA)
# plt.plot(macndeaths,'-',label='cn')
# plt.legend()
# plt.title('mortos por dia china média móvel a '+ str(MA)+ 'dias')


# # In[ ]:


# macndeaths=moving_average(cndeaths.cumsum()/cncases.sum(),MA)
# plt.plot(macndeaths,'-',label='cn')
# plt.legend()
# plt.title('mortos acumulados por dia  por total de casos china (média móvel a '+ str(MA)+ 'dias)')


# # # Dados do John Hopkins Github
# #
# # Estes dados estão em concordância com os europeus.
# #
# # https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv

# # In[ ]:



# #dailyurl='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/03-24-2020.csv'
# #dfdaily = pd.read_csv(dailyurl)
# #dfdaily.dtypes

# confseriesurl='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
# deathseriesurl='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'

# dfJHcases = pd.read_csv(confseriesurl,na_values='-')
# #dfconfseries.dtypes
# dfJHdeaths = pd.read_csv(deathseriesurl,na_values='-')
# #print(dfJHcases.dtypes)
# dfJHcases[dfJHcases['Country/Region']=='Brazil'].iloc[0,4:]
# #df['dateRep'] = pd.to_datetime(df['dateRep'], format='%d/%m/%Y')
# brdfconf=dfJHcases[dfJHcases['Country/Region']=='Brazil'].iloc[0,39:]
# brdfdeathds=dfJHdeaths[dfJHdeaths['Country/Region']=='Brazil'].iloc[0,39:]
# #brdfconf, brdfdeathds


# # In[ ]:


# ptdfconfseries = dfconfseries[dfconfseries['Country/Region'] == 'Portugal']
# ptdfdeathseries = dfdeathseries[dfdeathseries['Country/Region'] == 'Portugal']


# # In[ ]:


# conf=ptdfconfseries.iloc[0,4:].values
# deaths=ptdfdeathseries.iloc[0,4:].values
# len(deaths)==len(conf)
# #deaths


# # In[ ]:


# indexpositives=np.where(conf>=1)
# conf=conf[indexpositives]
# deaths=deaths[indexpositives]
# #deaths


# # In[ ]:


# plt.plot(conf,'-.',label='pt',color='steelblue')
# plt.plot(ptcases.cumsum(),'--',label='pt',color='b')


# # In[ ]:


# plt.plot(deaths,'-.',label='pt',color='steelblue')
# plt.plot(ptdeaths.cumsum(),'--',label='pt',color='b')


# # In[ ]:


# ptdfconfseries = dfconfseries[dfconfseries['Country/Region'] == 'Portugal']
# ptdfconfseries.iloc[0,4:].values


# # In[ ]:


# spdfconfseries = dfconfseries[dfconfseries['Country/Region'] == 'Spain']
# spdfconfseries.iloc[0,4:].values


# # In[ ]:


# itdfconfseries = dfconfseries[dfconfseries['Country/Region'] == 'Italy']
# itdfconfseries.iloc[0,4:].values


# # # Plots de TODOS OS PAíSES NA BASE DE DADOS da J.H

# # # Criação de listas com as dataframes indexada por pais

# # In[ ]:


# countries=dfconfseries['Country/Region'].unique()
# worldconfdf=[]
# worlddeathdf=[]
# for country in countries:
#     worldconfdf.append(dfconfseries[dfconfseries['Country/Region'] == country])
#     worlddeathdf.append(dfdeathseries[dfdeathseries['Country/Region'] == country])



# # ## Aglomeração no mesmo país (não faz sentido quando os países são compostos por estados separados...ilhas.."colónias"...etc)

# # In[ ]:


# conf=[]
# death=[]
# for countryindex in range(len(countries)):
#     conf.append(worldconfdf[countryindex].iloc[0,4:].values)
#     death.append(worlddeathdf[countryindex].iloc[0,4:].values)
#     for i in range(1,len(worldconfdf[countryindex])):
#         conf[countryindex]+=worldconfdf[countryindex].iloc[i,4:].values
#         death[countryindex]+=worlddeathdf[countryindex].iloc[i,4:].values


# # # Find first day of positives for each country and plot >1 casos

# # In[ ]:


# indexpositives=[]
# for countryindex in range(len(countries)):
#     indexpositives.append(np.where(conf[countryindex]>=1))


# # ## Lista de países a fazer plot

# # In[ ]:


# listtoplot=np.where(countries=='Portugal')
# listtoplot+=np.where(countries=='Spain')
# listtoplot+=np.where(countries=='Italy')
# listtoplot+=np.where(countries=='France')
# countriestoplot=np.array(listtoplot).flatten().tolist()
# countriestoplot

# #conf[138]
# countriestoplot= range(len(countries)) # para plottar todos


# # In[ ]:


# import matplotlib.pylab as plt
# plt.rcParams['figure.dpi'] = 100
# for countryindex in countriestoplot:
#     #conf[countryindex]=conf[countryindex][indexpositives[countryindex]]
#     plt.plot(conf[countryindex],'-',label=countries[countryindex])
# plt.legend(loc=2, prop={'size': 6})


# # In[ ]:


# for countryindex in countriestoplot:
#     #death[countryindex]=death[countryindex][indexpositives[countryindex]]
#     plt.plot(death[countryindex],'-',label=countries[countryindex])
# plt.legend(loc=2, prop={'size': 6})


# # In[ ]:


# for countryindex in countriestoplot:
#     #death[countryindex]=death[countryindex][indexpositives[countryindex]]
#     plt.plot(conf[countryindex],death[countryindex],'-',label=countries[countryindex])
# plt.legend(loc=2, prop={'size': 6})


# # # Mais fontes de dados estruturados e opensource:
# #
# # ## Itália
# # - https://github.com/pcm-dpc/COVID-19/tree/master/dati-province
# #
# #

# # In[ ]:


import pandas as pd

data = pd.read_csv('framingham.csv')

# Create separate copies of the data for men and women
women = data[data["male"] == 0].copy()
men = data[data["male"] == 1].copy()

# Reset the index of the new dataframes
women.reset_index(drop=True, inplace=True)
men.reset_index(drop=True, inplace=True)


womenCHD = women[women["TenYearCHD"] == 1].copy()
womenNoCHD = women[women["TenYearCHD"] == 0].copy()

menCHD = men[men["TenYearCHD"] == 1].copy()
menNoCHD = men[men["TenYearCHD"] == 0].copy()

womenCHD.reset_index(drop=True, inplace=True)
womenNoCHD.reset_index(drop=True, inplace=True)
menCHD.reset_index(drop=True, inplace=True)
menNoCHD.reset_index(drop=True, inplace=True)

women.to_csv('fhs_women.csv', index=True) #export for easier use in modeling in R
men.to_csv('fhs_men.csv', index=True)



max_age = int(men['age'].max()) + 1 # since the max age of all the men is unknown, use this to set an upper limit to our lists

elist = [0] * max_age
slist = [0] * max_age
flist = [0] * max_age

for i in range(len(men)): # see how many of each age got CHD
    elist[int(men.loc[i]['age'])] += men.loc[i]['TenYearCHD']

for i in range(len(men)): # count how many of each age there is
    slist[int(men.loc[i]['age'])] += 1

for i in range(len(men)): # finds percentage of those that got CHD per age
    flist[int(men.loc[i]['age'])] = elist[int(men.loc[i]['age'])]/slist[int(men.loc[i]['age'])]

data = [flist, slist]

df = pd.DataFrame(data)
df.index = ['with chd', 'people']

df.to_csv("menfinal.csv")



wmax_age = int(women['age'].max()) + 1 # since the max age of all the men is unknown, use this to set an upper limit to our lists

welist = [0] * wmax_age
wslist = [0] * wmax_age
wflist = [0] * wmax_age

for i in range(len(women)): # see how many of each age got CHD
    welist[int(women.loc[i]['age'])] += women.loc[i]['TenYearCHD']

for i in range(len(women)): # count how many of each age there is
    wslist[int(women.loc[i]['age'])] += 1

for i in range(len(women)): # finds percentage of those that got CHD per age
    wflist[int(women.loc[i]['age'])] = welist[int(women.loc[i]['age'])]/wslist[int(women.loc[i]['age'])]

data1 = [wflist, wslist]
dp = pd.DataFrame(data1)

dp.index = ['with chd', 'people']
dp.to_csv("womenfinal.csv")






max_cig = int(women['cigsPerDay'].max()) + 1

e = [0] * max_cig
s = [0] * max_cig
f = [0] * max_cig

d = pd.DataFrame(women)
d['cigsPerDay'] = d['cigsPerDay'].fillna(0).astype(int)

for i in range(len(women)): # see how many of each age got CHD
    e[int(d.loc[i]['cigsPerDay'])] += d.loc[i]['TenYearCHD']

for i in range(len(women)): # count how many of each age there is
    s[int(d.loc[i]['cigsPerDay'])] += 1

for i in range(len(women)): # finds percentage of those that got CHD per age
    f[int(d.loc[i]['cigsPerDay'])] = e[int(d.loc[i]['cigsPerDay'])]/s[int(d.loc[i]['cigsPerDay'])]

data = [f, s]
pdf = pd.DataFrame(data)
pdf.index = ['with chd', 'people']

for i in range(len(pdf)):
    if (pdf.iloc[1][i] < 2):
        pdf.drop(pdf.columns[[i]], axis=1, inplace=True)

pdf.to_csv("womencigs.csv")
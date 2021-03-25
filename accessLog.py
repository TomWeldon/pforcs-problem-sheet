import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns



logFilename = 'accessLogShort.log'



colNames = ('ip','dash','userId','time','url','status code','data response','referer','user agent','unknown')
df = pd.read_csv(logFilename,sep=' ', header=None, names=colNames)
df.drop(columns=['dash','userId','unknown'], inplace=True)
#get rid of [] in 'time'
'''
def getNewValue(x):
    newvalue = re.search('[\w:/]+',x).group()
    return newvalue
'''
# New col contents
def sessionId(x):
    newSessionCol= re.search('(?<=D=)(.*)(?= HTTP)',x).group()
    return newSessionCol
	
# Making new column and populating it
df['session ID'] = df['url'].apply(sessionId)	

excelFilename = 'access.xlsx'
df.to_excel(excelFilename, index=True, sheet_name='data')

sessionIdDownload = df.groupby('session ID', as_index=False).agg({'data response': 'sum'})
sessionIdDownload = sessionIdDownload.sort_values('data response', ascending = False).head(10)
print(sessionIdDownload)



res=sessionIdDownload.reset_index()
#fig = plt.figure()
#ax = fig.add_subplot()
#fig, ax = plt.subplots()
#ax.set_ylabel('Data Response')

ax=sns.barplot(x='session ID', y='data response',data=res)
ax.set(xlabel='Data Response', ylabel='Data Download')
plt.xticks(rotation=70, fontsize=8, weight='bold', color='#800000')
plt.yticks(fontsize=8, weight='bold', color='#800000')
#plt.tight_layout()
plt.show()

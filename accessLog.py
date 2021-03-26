# accessLog.py. Write a program that takes in an access.log file and plots the output of 'session ID' against amount of data downloaded
# by each 'session ID'
# Log file to be inputted from the command line.

# Author: Tom Weldon G00398828

# Import the required python module libraries
import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns
import sys

# access.log file to be inputted from command line. Assigned to the name 'logFilename'
logFilename = sys.argv[1]

# Each column in the log file given a name
colNames = ('ip','dash','userId','time','url','status code','data response','referer','user agent','unknown')
# Access file read in as a csv file to a dataframe (df) with space(' ') used as a delimiter
df = pd.read_csv(logFilename,sep=' ', header=None, names=colNames)
# Not required or useless data columns dropped 
df.drop(columns=['dash','userId','unknown'], inplace=True)

# Function defined to search for the session ID in the rows and given to a group. Regular expression used to extract the session ID.
# Session ID contained in the url of each row. Extracted by searching all characters(.*) between 'D=' using the lookbehind assertion(?<=) and
# ' H' using the lookahead assertion (?=)
# The last 6 characters from the session ID used. This is to ensure easy labelling of each parameter of the x axis in the resulting plot
def sessionId(x):
    newSessionCol= re.search('(?<=D=)(.*)(?= HTTP)',x).group()
    return newSessionCol[-6:]

# New column called 'session ID' added to the 'df' dataframe. Function 'sessionID()' applied to each url in the 'url' column 
df['session ID'] = df['url'].apply(sessionId)	

# df now written to an excel file 'access.xlsx'. This gives user friendly visibility of the entire dataframe
excelFilename = 'access.xlsx'
df.to_excel(excelFilename, index=True, sheet_name='data')

# New dataframe called 'sessionIdDownload' created using groupby 'session ID' and the aggregate function used to sum
# all 'data response' for each session ID.
sessionIdDownload = df.groupby('session ID', as_index=False).agg({'data response': 'sum'})

# The top ten 'session ID' data downloads assigned to 'sessionIdDownload' dataframe and sorted in descending value
sessionIdDownload = sessionIdDownload.sort_values('data response', ascending = False).head(10)

# 'sessionIdDownload' printed to view the top ten values
print(sessionIdDownload)


# 'sessionIdDownload' dataframe assigned to name 'resPlot'
resultPlot=sessionIdDownload

#two font dictionaries 'font1' and 'font2' created
font1 = {'family':'arial','color':'#0033cc','size':10, 'weight': 'bold'}
font2 = {'family':'arial','color':'#008080','size':20, 'weight': 'bold'}

# Seaborn used to assign a bar plot to 'ax' using the data frame 'resultPlot'
ax=sns.barplot(x='session ID', y='data response',data=resultPlot)

# x label and y label created using fontdict 'font1'
plt.xlabel('Session ID', fontdict= font1 )
plt.ylabel('Data Download', fontdict= font1 )

# x axis ticks angled at 45 degress to allow eaase of reading on the resulting plot.
plt.xticks(rotation=45, fontsize=8, weight='bold', color='#800000')
plt.yticks(fontsize=8, weight='bold', color='#800000')

# Plot title assigned using fontdict 'font2'
plt.title('Session ID Data Download', fontdict = font2)

# plt.tight_layout() used to ensure x and y axix label visible in the resulting plot
plt.tight_layout()

# Graphic of the plot saved as a .png image
plt.savefig('Data_Download.png')

# plt.show() function called to display the resulting plot.
plt.show()

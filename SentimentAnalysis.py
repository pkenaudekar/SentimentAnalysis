import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.downloader.download('vader_lexicon')   #Vader(Valence Aware Dictionary and Entiment Reasoner.)
                                            #acts as a dictionary that helps in sentiment analysis
file='F:/data_files.xlsx'
xl = pd.ExcelFile(file)                     #Read from Excel file
dfs = xl.parse(xl.sheet_names[0])           #Parsing Excel sheet to Dataframes
dfs = list(dfs['Sentances'])                #Removes the blank rows from Dataframes
print(dfs)
sid = SentimentIntensityAnalyzer()          #Performing sentimental analysis on dataframes 
for data in dfs:
     ss = sid.polarity_scores(data)         #Performs sentimental analysis on encoutered data
     print(data)
     for k in ss:
        print(k,ss[k])                      #Prints if given data is positive, negitive or nuetral and also intensity of the sentiment

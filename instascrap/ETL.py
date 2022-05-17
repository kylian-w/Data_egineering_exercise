import pandas as pd
from sqlalchemy import create_engine
import re

def needed_df(df_name):
  df=pd.read_csv(df_name)
  new=df.drop(columns=['Unnamed: 0', 'Photos','Comments'])
  new['Text']=new['Text'].astype('str')
  
  #remove html tags
  def cleanhtml(new):
    y=new['Text']
    cleaned=[]
    CLEANR = re.compile('<.*?>')
    for line in y:
      cleantext = re.sub(CLEANR, '', line)
      cleaned.append(cleantext)
    #print(cleaned)
    return cleaned
  l=cleanhtml(new)  # apply the cleanhtml function
  new['text']=pd.Series(l) # add the clean text to the new data frame

  final = list(dict.fromkeys(l)) #filter out the data frame to remove double entries

  def filter(array_):
    l1 = ['décès', 'Jacques', 'CHIRAC']
    l=[]
    for el in l1:
      el=el.lower()
      l.append(el)
    filter_data = [x for x in array_ if
                all(y not in x for y in l)]
    return filter_data
  final1=filter(final) #apply filter fucntion
  new['result']=pd.Series(final1)  #add result to df
  new.to_csv('filtered_dataset.csv', index=False)  #convert resulting df to csv file

  return new
print(needed_df("Data_engineer_test.csv"))

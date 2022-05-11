from cgi import print_arguments
import pandas as pd

### cons_email=                         email,create_dt,modified_dt
### cons_email_chapter_subscritions=    isunsub
### cons=                               source

#Read and obtain columns fron differnt csv files
df_1 = pd.read_csv('cons_email.csv' , usecols = ['email','create_dt','modified_dt'])
df_2 = pd.read_csv('cons_email_chapter_subscription.csv' , usecols = ['isunsub'])
df_3 = pd.read_csv('cons.csv' , usecols = ['source'])

#Create 'people.csv' file
df_1.to_csv('people.csv' , index = False)
 
#Merge all 3 files with respective columns into one dataframe
df_1 = pd.concat([df_1, df_2, df_3], axis = 1 ) 
print(df_1)

#Write dataframe into the csv files
df_1.to_csv('people.csv' , index = False)

#-------------------------------------------------------------------------------------------





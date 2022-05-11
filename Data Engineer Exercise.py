from cgi import print_arguments
import pandas as pd

### cons_email=                         email,create_dt,modified_dt
### cons_email_chapter_subscritions=    isunsub     1 = is unsubscribed         and         0 = is subscribed
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

#Read and obtain columns csv file 'people'
df_agg = pd.read_csv('people.csv', usecols = ['create_dt','isunsub'])

# Rename columns
#   create_dt  ->  acquisition_date
#   isunsub    ->  acquisitions

df_agg.rename(
    columns=({'create_dt' : 'acquisition_date', 'isunsub' : 'acquisitions'  }),
    inplace=True,
)
df_agg.head()

#Aggregates stats about when people in the dataset were acquired

# check 'create_dt' or 'modified_dt' repeats
# record dates that are used 
# count days that are repeated 

#Create 'acquisition_facts.csv' file
df_agg.to_csv('acquisition_facts.csv' , index = False)








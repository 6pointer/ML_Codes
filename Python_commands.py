### 1) MERGE COMMAND( Same as join in SQL)
df_new = pd.merge(df1,df12,how = 'left',left_on = ['super_category','sub_category'],right_on = ['Cat','Sub_cat'])
## Above command is a left join . Df1 and DF2 are the left and right tables and left on and right on are respective keys


### 2) Apply Command(How to apply a function on all the rows)
df_text['mfr_len'] =  df_text['merchant_first_reply'].apply(lambda x : len(x)) - df_text['merchant_first_reply'].apply(lambda x : x.count(' '))
 ## Above command shows how to usee apply in 2 different types of fucntions

import pandas as pd


df_ful = pd.read_excel('All_files/df_ful.xlsx')
df_hal = pd.read_excel('All_files/df_half.xlsx')

df_fil = pd.DataFrame({'prod_url':[],'cate':[],'subcat':[]})


for index,rw in df_ful.iterrows():
    if not rw['prod_url'] in df_hal['prod_url'].to_list():

        df_cur = pd.DataFrame({'prod_url':[rw['prod_url']],'cate':[rw['category']],'subcat':[rw['sub_category']]})

        df_fil = pd.concat([df_fil,df_cur])

# print(df_fil)
# quit()
df_fil.to_excel('filtered.xlsx')

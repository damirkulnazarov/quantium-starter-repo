import pandas as pd

dfs = []

file_names = ['/Users/a3141592653/Desktop/quantum at forage/quantium-starter-repo/data/daily_sales_data_0.csv',
              '/Users/a3141592653/Desktop/quantum at forage/quantium-starter-repo/data/daily_sales_data_1.csv',
              '/Users/a3141592653/Desktop/quantum at forage/quantium-starter-repo/data/daily_sales_data_2.csv']


for file in file_names:
    df = pd.read_csv(file)
    df = df[df['product'] == 'pink morsel']
    df['price'] = df['price'].str.replace('$', '').astype(float)
    df['sales'] = (df['price'] * df['quantity']).astype(int)
    df = df.drop(['price', 'quantity', 'product'], axis=1)
    dfs.append(df)

if dfs:
    df_final = pd.concat(dfs, ignore_index=True)
    df_final = df_final.rename(columns={'date': 'Date', 'region': 'Region', 'sales': 'Sales'})
    df_final = df_final[['Sales', 'Date', 'Region']]
    df_final.to_csv('output.csv', index=False)
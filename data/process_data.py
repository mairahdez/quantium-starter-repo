import pandas as pd
import glob

# 1. Get the list of all CSV files in the 'data' folder that match the pattern
all_files = glob.glob('data/daily_sales_data_*.csv')

# 2. read  and combine all CSV files into a single DataFrame
li = []
for filename in all_files:
    df = pd.read_csv(filename)
    li.append(df)

df_combined = pd.concat(li, axis=0, ignore_index=True)

# 3. Flexible filter: remove spaces, convert to lowercase, and then check
# This cleans the 'product' column before comparing
df_combined['product'] = df_combined['product'].str.strip().str.lower()

# Now filter for 'pink morsel' (in lowercase)
df_pink = df_combined[df_combined['product'] == 'pink morsel'].copy()

# 4. process: create a new column 'sales' by multiplying 'quantity' and 'price'
# remove the dollar sign and commas from the 'price' column and convert it to float
df_pink['price'] = df_pink['price'].replace(r'[\$,]', '', regex=True).astype(float)
df_pink['sales'] = df_pink['quantity'] * df_pink['price']

# 5. Select only the relevant columns for the final output: date and region
df_final = df_pink[['sales', 'date', 'region']]

# 6. save the resulting DataFrame to a new CSV file
df_final.to_csv('data/daily_sales_data_final.csv', index=False)

print("¡Processing complete! Check the 'data' folder for 'daily_sales_data_final.csv'.")
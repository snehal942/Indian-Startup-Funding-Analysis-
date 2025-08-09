import pandas as pd
df=pd.read_csv('/content/startup_funding.csv')
display(df.head())
display(df.info())



#df = df.drop('Remarks',axis=1) # Removed this line as 'Remarks' is not found
for col in['Industry Vertical','SubVertical','City  Location','Investors Name','InvestmentnType']:
  df[col].fillna('Unknown',inplace=True)

df['Amount in USD']=df['Amount in USD'].astype(str).str.replace(',','',regex=False).str.replace('+','',regex=False)
df['Amount in USD']=pd.to_numeric(df['Amount in USD'],errors='coerce')
df['Amount in USD'].fillna(0,inplace=True)

df['Date dd/mm/yyyy']=pd.to_datetime(df['Date dd/mm/yyyy'],format='%d/%m/%Y',errors='coerce')

for col in['Startup Name','Industry Vertical','SubVertical','City  Location','Investors Name','InvestmentnType']:
  df[col] = df[col].astype(str).str.strip().str.replace('\\\\xc2\\\\xa0','',regex=True)
  df[col] = df[col].apply(lambda x: ' '.join(x.split()))
  df[col] = df[col].str.lower()
  # display(df.info()) # Removed these display calls from the loop
  # display(df.head()) # Removed these display calls from the loop

# Added display calls outside the loop for cleaner output
display(df.info())
display(df.head())



# Extract year and month from the date column
df['FundingYear'] = df['Date dd/mm/yyyy'].dt.year
df['FundingMonth'] = df['Date dd/mm/yyyy'].dt.month

# Group by FundingYear and calculate total funding and number of deals
yearly_funding_trends = df.groupby('FundingYear').agg(
    total_funding_usd=('Amount in USD', 'sum'),
    number_of_deals=('Sr No', 'count')
).reset_index()

# Display the result
display(yearly_funding_trends)



monthly_funding_trends = df.groupby('FundingMonth').agg(
    total_funding_usd=('Amount in USD','sum'),
    number_of_deals=('Sr No','count')

).reset_index()

display(monthly_funding_trends)



sector_funding = df.groupby('Industry Vertical')['Amount in USD'].sum().reset_index()
sector_funding = sector_funding.sort_values(by='Amount in USD', ascending=False)
print("Top 10 Sectors by Funding:")
display(sector_funding.head(10))

city_funding =df.groupby('City Location')['Amount in USD'].sum().reset_index()
city_funding =city_funding.sort_values(by='Amount in USD',ascending=False)
print("\nTop 10 Cities by Funding:")
display(City.head(10))

startup_funding = df.groupby('Startup Name')['Amount in USD'].sum().reset_index()
startup_funding = startup_funding.sort_values(by='Amount in USD',ascending=False)
print("\nTop 10 Startups by Funding:")
display(startup_funding.head(10))


investor_activity=df.groupby('Investors Name').agg(
    total_funding_usd=('Amount in USD','sum'),
    number_of_deals=('Sr No','count')

).reset_index()


top_investors_by_funding=investor_activity.sort_values(by='total funding_usd',ascending=False)
print("top 10 Investors by Total Funding:")
display(top_investors_by_funding.head(10))



top_investors_by_deals=investor_activity.sort_values(by='number_of_deals',ascending=False)
print("\ntop 10 Investors by Number of deals:")
display(top_investors_by_deals.head(10))



investment_type_summary = df.groupby('InvestmentnType').agg(
    total_funding_usd=('Amount in USD','sum'),
    number_of_deals=('Sr No','count')
).reset_index()

investment_type_summary_by_funding = investment_type_summary.sort_values(by='total_funding_usd',ascending=False)
print("Investment Type Summary by Total Funding:")
display(investment_type_summary_by_funding)


investment_type_summary_by_deals = investment_type_summary.sort_values(by='number_of_deals',ascending=False)
print("Investment Type Summary by Number of Deals:")
display(investment_type_summary_by_deals)


import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(12, 6))
sns.lineplot(data=yearly_funding_trends,x='FundingYear', y='total_funding_usd',marker='o',label='Total Funding(USD)')
sns.lineplot(data=yearly_funding_trends,x='FundingYear', y='number_of_deals',marker='o',label='Number of Deals')

plt.title('Yearly Funding Trends')
plt.xlabel('Year')
plt.ylabel('Amount / Count')
plt.xticks(yearly_funding_trends['FundingYear'])
plt.grid(True)
plt.legend()
plt.show()

plt.figure(figsize=(14, 7))
sns.barplot(data=sector_funding.head(10), x='Industry Vertical', y='Amount in USD',palette='viridis')
plt.title('Top 10 Sectors by TOtal Funding')
plt.xlabel('Industry Vertical')
plt.ylabel('Total Funding (USD)')
plt.xticks(rotation=45,ha='right')
plt.tight_layout()
plt.show()


plt.figure(figsize=(14, 7))
sns.barplot(data=city_funding.head(10), x='City  Location', y='Amount in USD',palette='viridis')
plt.title('Top 10 Cities by Total Funding')
plt.xlabel('City Location')
plt.ylabel('Total Funding (USD)')
plt.xticks(rotation=45,ha='right')
plt.tight_layout()
plt.show()


plt.figure(figsize=(14, 7))
sns.barplot(data=startup_funding.head(10), x='Startup Name', y='Amount in USD',palette='viridis')
plt.title('Top 10 Startups by Total Funding')
plt.xlabel('Startup Name')
plt.ylabel('Total Funding (USD)')
plt.xticks(rotation=45,ha='right')
plt.tight_layout()
plt.show()


plt.figure(figsize=(14, 7))
sns.barplot(data= top_investors_by_funding.head(10), x='Investors Name', y='total_funding_usd',palette='viridis')
plt.title('Top 10 Investors by Total Funding')
plt.xlabel('Investors Name')
plt.ylabel('Total Funding (USD)')
plt.xticks(rotation=45,ha='right')
plt.tight_layout()
plt.show()


plt.figure(figsize=(14, 7))
sns.barplot(data=top_investors_by_deals.head(10), x='Investors Name', y='number_of_deals',palette='viridis')
plt.title('Top 10 Investors by Number of Deals')
plt.xlabel('Investors NAme')
plt.ylabel('Number of Deals')
plt.xticks(rotation=45,ha='right')
plt.tight_layout()
plt.show()


plt.figure(figsize=(14, 7))
sns.barplot(data=investment_type_summary_by_funding.head(10), x='InvestmentnType', y='total_funding_usd',palette='viridis')
plt.title('Top 10 Investment Types by Total Funding')
plt.xlabel('Investment Type')
plt.ylabel('Total Funding (USD)')
plt.xticks(rotation=45,ha='right')
plt.tight_layout()
plt.show()


plt.figure(figsize=(14, 7))
sns.barplot(data=investment_type_summary_by_funding.head(10), x='InvestmentnType', y='number_of_deals',palette='viridis')
plt.title('Top 10 Investment Types by Number of Deals')
plt.xlabel('Investment Type')
plt.ylabel('Number of Deals')
plt.xticks(rotation=45,ha='right')
plt.tight_layout()
plt.show()


























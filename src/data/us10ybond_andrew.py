from datetime import date
import investpy

search_result = investpy.search_quotes(text='us10', products=['bonds'],
                                       countries=['united states'], n_results=1)
print(search_result)


data = search_result.retrieve_historical_data(from_date='1/1/', to_date=date.today().strftime('%d/%m/%Y'))
print(data.head())


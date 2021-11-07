from datetime import date
import investpy

search_result = investpy.bonds.get_bond_historical_data('United States 10-Year', '1/1/1000', date.today().strftime('%d/%m/%Y'), order='descending')

print(search_result)


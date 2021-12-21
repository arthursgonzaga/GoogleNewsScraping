import pandas as pd
from GoogleNews import GoogleNews

SEARCHING = 'Dados'

googlenews = GoogleNews()
googlenews.set_lang('pt')
googlenews.search(SEARCHING)
print("Searching for... " + SEARCHING)
results = googlenews.result()
df = pd.DataFrame(results)
df.to_csv('exported_results.csv', index=False)
print("Done!")

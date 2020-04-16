
import COVID19Py

import matplotlib.pyplot as mpl
import pandas as pd
from covid.api import CovId19Data
import ast
from covid_india import states
import json

api = CovId19Data(force=False)
# res = api.get_stats()
# res = api.get_all_records_by_country("India")
res = api.get_all_records_by_provinces()
# res = api.filter_by_country("india")
# res = api.filter_by_province("Delhi")
# res = api.show_available_regions()
# res = api.get_history_by_country("india")
# dump = json.dumps(res)
# my_dict = json.loads(str(res))

# value = ast.literal_eval(res)
df = pd.DataFrame.from_dict(res, orient='columns')
# print(df.head(20))
res = states.getdata()
dump = json.dumps(res)
print(dump)
# virusdetail = dict(res["latest"])
# names = list(virusdetail.keys())
# values = list(virusdetail.values())
# covid19 = COVID19Py.COVID19()
# data = covid19.getAll(timelines=True)
# # data = covid19.getLocationById(91)
virusdetail = dict(res["Andhra Pradesh"])
# names = list(virusdetail.keys())
# values = list(virusdetail.values())

# changes = covid19.getLatestChanges()
mpl.plot(range(len(virusdetail)), res.values(), tick_label=res.keys())
# print(virusdetail)
mpl.show()

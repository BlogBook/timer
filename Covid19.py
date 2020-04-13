
import COVID19Py

import matplotlib.pyplot as mpl


covid19 = COVID19Py.COVID19()
# data = covid19.getAll(timelines=True)
data = covid19.getLocationById(12)
virusdetail = dict(data["latest"])
names = list(virusdetail.keys())
values = list(virusdetail.values())

changes = covid19.getLatestChanges()
mpl.bar(range(len(virusdetail)), values, tick_label=names)
print(virusdetail)
mpl.show()

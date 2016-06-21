import json
import pickle
from visir.models import Data

df = pickle.load(open("non_zero_codes.p","rb"))
names = df.name.values
names = names.tolist()

data1 = Data()
data1.dataname = 'Station list'
data1.datatype = 'string'
data1.datalength = 4113
data1.datadata = json.dumps(names)
data1.save()


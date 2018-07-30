from Orange.data import ContinuousVariable, Domain, Table
import scipy.sparse as sp

attrs = {}
dt = None
line = -1
items, i, j = [], [], []

for f in in_data:
    dt_ = str(f['Datetime'])
    if dt_ != dt:
        line += 1
        dt = dt_
    attr = str(f['Activity'])
    items.append(1)
    i.append(line)
    j.append(attrs.setdefault(attr, len(attrs)))

mat = sp.coo_matrix((items, (i, j))).tocsr()
mat.sort_indices()
attrs_ = [ContinuousVariable(x) for _, x in sorted((ind, name) for name, ind in attrs.items())]
domain = Domain(attrs_)
table = Table.from_numpy(domain, attrs_ and mat)
table.name = 'The Basket'
print(table)
out_data = table
data = None
date = None
acc = []
time_, act_ = 1, 2
# 0 - time, 4 - activity
for row in in_object:
    if data is None:
        data = []
        continue
    if row[time_] != date:
        if len(acc):
            data.append(acc)
        acc = []
        date = row[time_]
    acc.append(row[act_])

if len(acc):
    data.append(acc)
    acc = []
    date = row[time_]

out_object = data
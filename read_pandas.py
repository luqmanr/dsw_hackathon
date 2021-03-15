import csv
import pandas as pd

prime_norm = pd.read_csv("./data/from_ato/prime_norm_v2.csv")
type_label = pd.read_csv("./data/from_ato/type_label.csv")

type_list = type_label["type"].values.tolist()
# print(type_list)

df_size = prime_norm.index.size
data = prime_norm["subtype_label"].isna()
print(data.sum())
prime_norm["subtype_null"] = data

for type_index,types in enumerate(type_list):
    for i in range(df_size):
        if (prime_norm["subtype_null"][i] == True) and (prime_norm["type"][i] == types):
            print(prime_norm["subtype_null"][i], prime_norm["type"][i], print(type_index))
            prime_norm["subtype_label"][i] = type_index + 1
            prime_norm["subtype_null"][i] = False

# print(prime_norm["subtype_label"])
prime_norm.to_csv(r'./data/from_ato/prime_norm_v3.csv', index=False)

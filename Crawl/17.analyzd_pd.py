import pandas as pd

df = pd.read_json("./gangnam.json")
print(df.count())

#dfSum = df.groupby("bloggername").count()
#print(dfSum)

bloggernames = df['bloggername']
print(bloggernames)
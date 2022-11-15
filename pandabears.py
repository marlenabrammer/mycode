import pandas as pd 

pet1 = {"name":"Misty", "age":12, "species":"cat"}
pet2 = {"name":"Peach", "age":1, "species":"cat"}
pet3 = {"name":"Pepper", "age":5, "species":"cat"}
pet4 = {"name":"Bones", "age":8, "species" :"dog"}

pets_df = pd.DataFrame([pet1, pet2, pet3, pet4])
print(pets_df.head())
print(pets_df.info())



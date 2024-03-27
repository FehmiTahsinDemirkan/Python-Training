import pandas as pd

list = [["Ahmet",50],["Ali",60],["Yağmur",70],["Çınar",80]]
dict = {"Name": ["Ahmet","Ali","Yağmur","Çınar"],"Grade":[50,60,70,80]}

df = pd.DataFrame()

df = pd.DataFrame([1,2,3,4])
df = pd.DataFrame(list,index=[1,2,3,4],columns=['Name','Grade'],dtype=float)

print(df)
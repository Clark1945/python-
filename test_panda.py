import pandas as pd
status=[[70,40,10,35],[45,80,30,45],[10,15,90,25]] #資料串列作成表格
career=["Warrior","Archer","Wiseman"]
ability=["Str","Dex","Int","Luc"]
df=pd.DataFrame(status,columns=ability,index=career)
print(df)
career[2]="Wizard"
df.index=career
print(df)
print("-----------------------------------")
print("敏捷排序:\n",df["Dex"])
print("擅長敏捷者:\n",df[df.Dex>30])
print("能力值總覽:\n",df.values)
print("戰士:\n",df.loc["Warrior"])
print("戰士敏捷值:\n",df.loc["Warrior"]["Dex"])
print("鬥士智慧:\n",df.loc[("Warrior","Archer"),:]["Int"])
print("法師能力值：\n",df.loc["Wizard"].head(2),"\n",df.loc["Wizard"].tail(1))
print("-----------------------------------")
print("力量排序:\n",df.sort_values(by="Str",ascending=False))#遞增排序
df2=df.drop("Archer")
print(df2)
print("-----------------------------------")
df.plot()

import pandas as pd
# x=pd.read_csv("info.csv")

#may help you , some tips
# -> ctrl + forward slash will comment the lines you selected
# -> ctrl + s to save the file

#converting a list into series
# a=[8,5,9]
# y=pd.Series(a)
# print(y)



#list to series with index 
# a=[8,5,9]
# y=pd.Series(a,index=["a","h","p"])
# # print(y)
# print(y["h"])



# #dictionary into series
# calories={"day1":420,"day2":380,"day3":370}
# x=pd.Series(calories)
# print(x)



#dictionary into series with specified values
# calories={"day1":420,"day2":380,"day3":370}
# x=pd.Series(calories,index=["day1","day2"])
# print(x)


#dictionary into DataFrame
# hlo={"cars":['a','b','c'],"cost":[8,9,3]}
# x=pd.DataFrame(hlo)
# print(x)


#locate row
hlo={"cars":['a','b','c'],"cost":[8,9,3]}
x=pd.DataFrame(hlo)
# print(x)
# print(x.loc[[0,1,2]])
# print(x.loc[0:2])


#dictionary to DataFrame with index
# hlo={"cars":['a','b','c'],"cost":[8,9,3]}
# x=pd.DataFrame(hlo,index=["India","USA","Japan"])
# # print(x)
# print(x.loc["India"])


import warnings
import pandas as pd # importing the pandas module / before importing I installed pandas "pip install pandas"
import numpy as np
import datetime
from datetime import date

warnings.simplefilter(action="ignore")

pd.set_option("display.max_columns", None)
pd.set_option("display.float_format", lambda x : "%5f" %x)

pd.set_option('display.max_rows', 500)


###First I created the date list outside, and here with the module my code read my list.
df = pd.read_excel("C:/Users/s2200083/PycharmProjects/pythonProject/venv/date_leanvay.xlsx")  # In this list Generoidaan elementtejä 1.1.2022 - 13.1.2023 aikavälille

df.head()  # Returns the first 5 rows of the dataframe . The head function in Python displays the first five rows of the dataframe by default

df.loc[df["id"]==183]  ## Access a group of rows and columns by label(s) or a boolean array. .loc[] is primarily label based,
                        # but may also be used with a boolean array.
                        # Here I access the 183.element and defined 183.element for the next step.
                        # Haetaan listan 183 elementti. Tulostetaan edellinen ja seuraava päivämäärä viitteen kautta

# I defined the before and after element here.

##Tulostetaan edellinen ja seuraava päivämäärä
def two_way_linked(df,rank): # The rank() function is used to compute numerical data ranks (1 through n) along axis. By default, equal values are assigned a rank that is the average of the ranks of those values.
    before_element = df.loc[df["id"] == rank-1]  # Here I call the 182.element
    first_element = df.loc[df["id"]==rank]
    after_element = df.loc[df["id"] == rank+1] # here I call the 184.element
    return before_element,first_element,after_element

a,b,c = two_way_linked(df,183)
print(a,b,c)

df["days"]= pd.to_datetime(df['dates']).dt.day

#df.loc[(df["days"]%3 == 0) & (df["days"]%6 != 0)]["dates"].count()


### Tulostetaan  päivämäärät, jotka ovat jaollisia kolmella, mutta ei kuudella.
def day_divide_three_not_six(df,column):
    return df.loc[(df[column]%3 == 0) & (df[column]%6 != 0)]["dates"].to_frame()

day_divide_three_not_six(df,"days")

### Käännetään listan elementit toisinpäin eli 13.1.2023 on esimmäinen elementti ja 1.1.2022 on viimeinen.
def reverse_dataframe(df):
    return df.iloc[::-1]  ### .iloc[] is primarily integer position based (from 0 to length-1 of the axis)



reversed_df = df.loc[::-1]
reversed_df.head()

reversed_df.index
reversed_df = reversed_df.reset_index()

reversed_df = reversed_df.drop(columns = "index")
reversed_df.head()
###  Tulostetaan ensimmäisen listan kolmella, mutta ei kuudella jaollisen alkion päivien erotus käännetyn listan ensimmäiseen samoilla ehdoilla haettuun alkioon.

firs_df = day_divide_three_not_six(df,"days")
second_df = day_divide_three_not_six(reversed_df,"days")

def reset_drop_index(df):
    df = df.reset_index()
    df = df.drop(columns = "index")
    return df

firs_df = reset_drop_index(firs_df)
second_df = reset_drop_index(second_df)

type(firs_df)
#df['C'] = (df['B'] - df['A']).dt.days
third_df = pd.DataFrame()

third_df["dates"] = (second_df["dates"] - firs_df["dates"]) / np.timedelta64(1,"D")

third_df.head(1) # first index (ensimmäinen indeksi)

from textblob import TextBlob
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from pandas import DataFrame
import matplotlib.pyplot as plt
import string

class Sentiment:
    def __init__(self):
        self.tokens=[]

    def read_csv(self):
        service={}
        prod_perc={}
        df1 = pd.read_excel('Book1.xlsx', sheet_name='Sheet1')
        df=pd.DataFrame(data=df1)
        df.columns = df.columns.str.lstrip()
        df.columns=df.columns.str.rstrip()
        prod_rating={}
        posneg={}
       con=df[‘Product name’].tolist()
        print(con)
        product=input("Enter the Product name")
        counts = df['Product name'].value_counts().to_dict()
        pos=0
        neg=0
        neut=0
        polarity=0.0
        for i in df.index:
            temp=(str)(df['Product name'][i])
            
            if temp == product:
                stmt=(str)(df['Review'][i])
                testominal=TextBlob(stmt)
                prod=df['Product name'][i]
                polarity=polarity+testominal.sentiment.polarity
                if testominal.sentiment.polarity<0:
                    neg=neg+1
                elif testominal.sentiment.polarity>0:
                    pos=pos+1
                else:
                  neut=neut+1
        posneg=[pos,neg,neut]
        service[product]=polarity
        labels=['Positive','Negative',’Neutral’]
        colors=['red','green',’blue’]
        plt.pie(posneg,labels=labels,colors=colors,startangle=90,autopct='%.1f%%')
        plt.title(product)
        plt.show()
        for key in counts.keys():
            temp1=key.lstrip()
            temp2=temp1.rstrip()
            if temp2 == product:
                count=counts[key]
                prod_perc[product]=(service[product]/count)
        print(prod_perc)
        for key in prod_perc:
            if prod_perc[key]<=-3:
                prod_rating="Worst"
            elif prod_perc[key]>-3 and prod_perc[key]<0:
                prod_rating[key]="Bad"
            elif prod_perc[key]>=0 and prod_perc[key]<2:
                prod_rating[key]="Average"

            elif prod_perc[key]>=2 and prod_perc[key]<3:
                prod_rating[key]="Good"
            elif prod_perc[key]>=3:
                prod_rating[key]="Best"
        print(prod_rating)
        
s=Sentiment()
s.read_csv()



 


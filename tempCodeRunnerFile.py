import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file = pd.read_csv("shopping_behavior_modified.csv")
# print(file.head(10))
# print(file.info())
# print(file.describe())
# print(file.isnull().sum())


file.drop_duplicates(inplace=True)
file.columns = file.columns.str.strip().str.replace(" ", "_")


def sentiment(rating):
    if rating >= 4:
        return "Positive"
    elif rating == 3:
        return "Neutral"
    else:
        return "Negative"
file["Sentiment"] = file["Review_Rating"].apply(sentiment)

# SENTIMENT DISTRIBUTION
sns.countplot(x="Sentiment", data=file)
plt.savefig("Sentiment_distribution.png", dpi = 300, bbox_inches = "tight")
plt.show()



customer_analysis = file.groupby("Customer_ID").agg({
    "Purchase_Amount_(USD)": "sum",
    "Review_Rating": "mean",
    "Previous_Purchases": "sum"
}).reset_index()
print(customer_analysis)


customer_analysis["Normalized_Spend"] = (
    customer_analysis["Purchase_Amount_(USD)"] -
    customer_analysis["Purchase_Amount_(USD)"].min()) /(
    customer_analysis["Purchase_Amount_(USD)"].max() -
    customer_analysis["Purchase_Amount_(USD)"].min())

print(customer_analysis)
    
    

def segment(row):
    if row["Purchase_Amount_(USD)"] > 300 and row["Review_Rating"] >= 4:
        return "Loyalist"
    elif row["Review_Rating"] < 3:
        return "At-Risk"
    else:
        return "New"
    
customer_analysis["Customer_Type"] = customer_analysis.apply(segment, axis=1)
print(customer_analysis["Customer_Type"].value_counts())


# CUSTOMER SEGMENT CHART
sns.countplot(x="Customer_Type", data=customer_analysis)
plt.savefig("Customer_segemnt_chart.png", dpi = 300, bbox_inches = "tight")
plt.show()

    

    
#  SHOPPING PATTERN
pivot = file.pivot_table(values="Purchase_Amount_(USD)", index="Category", columns="Gender",
                       aggfunc="sum")

sns.heatmap(pivot, annot=True)
plt.title("Purchase Heatmap")
plt.savefig("Shopping_pattern.png", dpi = 300, bbox_inches = "tight")
plt.show()
print(pivot)



# SPENDING DISTRIBUTION
sns.boxplot(x="Category", y="Purchase_Amount_(USD)", data=file)
plt.xticks(rotation=45)
plt.savefig("Spending_distribution.png", dpi = 300, bbox_inches = "tight")
plt.show()





print(file.info())
file.to_excel("shopping_behavior_modified.xlsx", index=False)

customer_analysis.to_excel("customer_analysis.xlsx", index=False)

pivot.to_excel("shopping_pattern.xlsx")
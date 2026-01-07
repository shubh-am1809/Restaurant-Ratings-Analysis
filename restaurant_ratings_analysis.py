import pandas as pd

df = pd.read_csv("dataset .csv")
df = df[['Aggregate rating', 'Votes']].dropna()
rating_distribution = df['Aggregate rating'].value_counts().sort_index()

print("\nRating Distribution:\n")
print(rating_distribution)

bins = [0, 1, 2, 3, 4, 5]
labels = ['0–1', '1–2', '2–3', '3–4', '4–5']

df['Rating Range'] = pd.cut(df['Aggregate rating'], bins=bins, labels=labels)

rating_range_counts = df['Rating Range'].value_counts().sort_index()
most_common_range = rating_range_counts.idxmax()

print("\nRating Range Distribution:\n")
print(rating_range_counts)
print(f"\nMost Common Rating Range: {most_common_range}")
average_votes = df['Votes'].mean()
print(f"\nAverage Number of Votes per Restaurant: {average_votes:.2f}")

rating_range_counts_df = rating_range_counts.reset_index()
rating_range_counts_df.columns = ['Rating Range', 'Restaurant Count']
rating_range_counts_df.to_csv(
    "output/rating_range_distribution.csv", index=False
)

summary_df = pd.DataFrame({
    'Metric': ['Most Common Rating Range', 'Average Votes'],
    'Value': [most_common_range, round(average_votes, 2)]
})

summary_df.to_csv(
    "output/ratings_summary.csv", index=False
)

print("\nResults saved in output/ folder")

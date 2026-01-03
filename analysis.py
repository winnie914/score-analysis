import pandas as pd

df = pd.read_csv("score.csv")

print("평균 점수:", df["Score"].mean())
print("최댓값:", df["Score"].max())
print("최솟값:", df["Score"].min())
import pandas as pd

docs = pd.read_csv("data/processed/duplicate_costs.csv")

actions = []

for _, row in docs.iterrows():

    if row["views"] == 0:
        action = "Archive report"

    elif row["creation_cost"] > 600:
        action = "Review duplication risk"

    else:
        action = "Merge with similar report"

    actions.append(action)

docs["recommended_action"] = actions

docs.to_csv("data/processed/action_recommendations.csv", index=False)
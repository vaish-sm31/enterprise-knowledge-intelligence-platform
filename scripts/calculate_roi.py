import pandas as pd

docs = pd.read_csv("data/processed/documents_clean.csv")

duplicates = pd.read_csv("data/processed/duplicate_reports.csv")

analyst_hourly_rate = 60

docs["creation_cost"] = docs["creation_hours"] * analyst_hourly_rate

duplicate_ids = set(duplicates["doc_b_id"])

docs["duplicate_flag"] = docs["doc_id"].apply(lambda x: x in duplicate_ids)

duplicate_reports = docs[docs["duplicate_flag"] == True]

total_duplicate_reports = len(duplicate_reports)

total_duplicate_cost = duplicate_reports["creation_cost"].sum()

summary = {
    "total_reports": len(docs),
    "duplicate_reports": total_duplicate_reports,
    "duplicate_percentage": total_duplicate_reports / len(docs),
    "estimated_duplicate_cost": total_duplicate_cost
}

summary_df = pd.DataFrame([summary])

summary_df.to_csv("data/processed/roi_summary.csv", index=False)

duplicate_reports.to_csv("data/processed/duplicate_costs.csv", index=False)
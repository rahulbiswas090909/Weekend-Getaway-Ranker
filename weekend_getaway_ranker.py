import pandas as pd # type: ignore

def rank_weekend_getaways(csv_path, source_city):
    # Load dataset
    df = pd.read_csv(csv_path)

    # Aggregate place-level data to city-level
    city_df = df.groupby("City").agg({
        "Google review rating": "mean",
        "Number of google review in lakhs": "sum",
        "time needed to visit in hrs": "mean"
    }).reset_index()

    # Remove source city
    destinations = city_df[
        city_df["City"].str.lower() != source_city.lower()
    ].copy()

    # Normalize scores
    destinations["Rating_Score"] = (
        (destinations["Google review rating"] -
         destinations["Google review rating"].min()) /
        (destinations["Google review rating"].max() -
         destinations["Google review rating"].min())
    )

    destinations["Popularity_Score"] = (
        (destinations["Number of google review in lakhs"] -
         destinations["Number of google review in lakhs"].min()) /
        (destinations["Number of google review in lakhs"].max() -
         destinations["Number of google review in lakhs"].min())
    )

    destinations["Time_Score"] = 1 - (
        (destinations["time needed to visit in hrs"] -
         destinations["time needed to visit in hrs"].min()) /
        (destinations["time needed to visit in hrs"].max() -
         destinations["time needed to visit in hrs"].min())
    )

    # Final weighted score
    destinations["Final_Score"] = (
        0.4 * destinations["Rating_Score"] +
        0.4 * destinations["Popularity_Score"] +
        0.2 * destinations["Time_Score"]
    )

    # Sort results
    ranked = destinations.sort_values(
        by="Final_Score", ascending=False
    )

    return ranked


if __name__ == "__main__":
    source_city = input("Enter Source City: ")
    result = rank_weekend_getaways("travel_data.csv", source_city)

    print(f"\nTop 5 Weekend Getaways from {source_city}:\n")
    print(result[[
        "City",
        "Google review rating",
        "Number of google review in lakhs",
        "Final_Score"
    ]].head(5))
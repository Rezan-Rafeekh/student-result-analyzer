import pandas as pd


def analyze_results(file_path):
    df = pd.read_csv(file_path)

    df["Average"] = (
        df["Math"] +
        df["Science"] +
        df["English"]
    ) / 3

    df["Rank"] = (
        df["Average"]
        .rank(ascending=False, method="dense")
        .astype(int)
    )

    topper = df.loc[df["Average"].idxmax()]
    lowest = df.loc[df["Average"].idxmin()]

    print("\n========== STUDENT RESULT ANALYSIS ==========\n")

    print("Overall Statistics")
    print("-" * 40)

    print(f"Class Average: {df['Average'].mean():.2f}")
    print(f"Highest Average: {df['Average'].max():.2f}")
    print(f"Lowest Average: {df['Average'].min():.2f}")

    print("\nTop Performer")
    print("-" * 40)
    print(f"{topper['Name']} ({topper['Average']:.2f})")

    print("\nLowest Performer")
    print("-" * 40)
    print(f"{lowest['Name']} ({lowest['Average']:.2f})")

    print("\nStudent Rankings")
    print("-" * 40)

    rankings = df.sort_values("Rank")

    print(
        rankings[
            ["Rank", "Name", "Average"]
        ].to_string(index=False)
    )

    df.to_csv(
        "analysis_report.csv",
        index=False
    )

    print(
        "\nAnalysis report saved as analysis_report.csv"
    )


if __name__ == "__main__":
    analyze_results("students.csv")

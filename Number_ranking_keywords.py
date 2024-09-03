import pandas as pd
import glob

# Bestandspaden
input_files = glob.glob(r"C:\Users\maiko\OneDrive\Documents\Python Semrush total ranking keywords\Semrush_data_positions\*.csv")
output_file = r"C:\Users\maiko\OneDrive\Documents\Python Semrush total ranking keywords\Ranking_keywords_summary.xlsx"


# Nieuwe DataFrame aanmaken voor de samenvatting
summary = pd.DataFrame(columns=["Maand", "Posities 1-3", "Posities 4-10", "Posities 11-20", "Posities 21-50", "Posities 51-100", "SERP Features"])

# CSV-bestand inlezen
for input_file in input_files:
    try:
        df = pd.read_csv(input_file)
    except Exception as e:
        print(f"Fout bij het inlezen van bestand {input_file}: {e}")
        continue        

# Maand bepalen op basis van de eerste timestamp in het bestand
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    eerste_maand = df['Timestamp'].iloc[0].strftime('%Y %B')

    organic_df = df[df["Position Type"] == "Organic"]

# Tellen van de posities in de aangegeven categorieën op basis van alleen Organic rijen
    posities_1_3 = len(organic_df[(organic_df["Position"] >= 1) & (organic_df["Position"] <= 3)])
    posities_4_10 = len(organic_df[(organic_df["Position"] >= 4) & (organic_df["Position"] <= 10)])
    posities_11_20 = len(organic_df[(organic_df["Position"] >= 11) & (organic_df["Position"] <= 20)])
    posities_21_50 = len(organic_df[(organic_df["Position"] >= 21) & (organic_df["Position"] <= 50)])
    posities_51_100 = len(organic_df[(organic_df["Position"] >= 51) & (organic_df["Position"] <= 100)])
    serp_features = len(df[df["Position Type"] != "Organic"])

# Gegevens toevoegen aan de DataFrame
    summary = summary._append({
        "Maand": eerste_maand,
        "Posities 1-3": posities_1_3,
        "Posities 4-10": posities_4_10,
        "Posities 11-20": posities_11_20,
        "Posities 21-50": posities_21_50,
        "Posities 51-100": posities_51_100,
        "SERP Features": serp_features
    }, ignore_index=True)

# Opslaan naar een nieuw CSV-bestand
summary.to_excel(output_file, index=False)

print(f"De samenvatting is opgeslagen in {output_file}")

import pandas as pd
import os

# --- Helper function to clean and save ---
def clean_and_save(input_file, output_file):
    try:
        df = pd.read_csv(input_file)

        # BASIC CLEANING — can expand later
        df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
        df.dropna(how="all", inplace=True)

        df.to_csv(output_file, index=False)
        print(f"✅ Cleaned: {input_file} → {output_file}")
    except Exception as e:
        print(f"❌ Error processing {input_file}: {e}")


# --- Batch clean all 8 files ---
file_map = {
    "wellness_habits_distribution.csv":       "cleaned_wellness_habits.csv",
    "screen_vs_sleep_by_age.csv":             "cleaned_screen_vs_sleep.csv",
    "modern_teen_mental_health_main.csv":     "cleaned_mental_health_main.csv",
    "daily_mood_stress_trends.csv":           "cleaned_daily_mood_stress.csv",
    "average_support_feeling_by_country.csv": "cleaned_support_by_country.csv",
    "average_mood_stress_by_gender.csv":      "cleaned_mood_by_gender.csv",
    "ai_usage_by_country.csv":                "cleaned_ai_usage_country.csv",
    "ai_tool_popularity.csv":                 "cleaned_ai_tool_popularity.csv"
}

# --- Loop through and process each ---
for raw_name, clean_name in file_map.items():
    raw_path = os.path.join("data", "raw", raw_name)
    clean_path = os.path.join("data", "cleaned", clean_name)
    clean_and_save(raw_path, clean_path)


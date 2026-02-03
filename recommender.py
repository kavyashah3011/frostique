import pandas as pd
import ast

# loading dataset
df = pd.read_csv('dessert_ing2inst.csv')

# drop unwanted columns
df = df.drop([
    'id', 'description', 'prep_minutes', 'cook_minutes',
    'review_count', 'saturated_fat_g', 'sodium_mg',
    'carbs_g', 'fiber_g', 'sugar_g', 'split',
    'target', 'input'
], axis=1)

# fill missing values
df[['total_minutes', 'rating']] = df[['total_minutes', 'rating']].fillna(
    df[['total_minutes', 'rating']].mean()
)

# convert ingredients column from string → list
df["ingredients"] = df["ingredients"].apply(ast.literal_eval)

# clean ingredients
def clean_ingredients(ingredients_list):
    units = [
        "cup", "cups", "tbsp", "tsp", "gram", "grams", "kg",
        "ml", "liter", "litre", "oz", "lb"
    ]
    
    cleaned = []
    
    for item in ingredients_list:
        for word in item.lower().split():
            # remove numbers and fractions
            if word.replace("/", "").replace(".", "").isdigit():
                continue
            
            # remove measurement units
            if word in units:
                continue
            
            cleaned.append(word)
    
    return " ".join(cleaned)

# apply cleaning
df["ingredients"] = df["ingredients"].apply(clean_ingredients)

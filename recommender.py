<<<<<<< HEAD
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

print(df["ingredients"].head())
=======
# importing libries
import pandas as pd

# loading dataset
df = pd.read_csv('dessert_ing2inst.csv')

### data inspection and data manipulation

# removing unwanted columns from dataset
df = df.drop(['id', 'description', 'prep_minutes', 'cook_minutes', 'review_count', 'saturated_fat_g', 'sodium_mg', 'carbs_g', 'fiber_g', 'sugar_g', 'split', 'target', 'input'], axis=1)

# handling missing values
null = df.isnull().sum()
df[['total_minutes', 'rating']] = df[['total_minutes', 'rating']].fillna(df[['total_minutes', 'rating']].mean())
null = df.isnull().sum()

["250 cream cheese", "2 salt", "1 icing sugar", "1 sweet sherry", "1/2"]
# removing measurements from ingredients in dataset for recommendation
def clean_ingredients(ingredients_str):
    """
    Takes a string of ingredients and:
    - Removes numbers
    - Removes units
    - Converts to lowercase
    - Returns a single clean string
    """
    cleaned = []
    # Parse the string representation of list if needed
    if isinstance(ingredients_str, str):
        items = ingredients_str.split(',')
    else:
        items = ingredients_str
    
    for item in items:
        item = item.lower().strip()
        words = item.split()
        for word in words:
            clean_word = word.replace("/", "").replace(".", "")
            if not clean_word.isdigit() and word not in cleaned:
                cleaned.append(word)
    return " ".join(cleaned)

df["ingredients"] = df["ingredients"].apply(clean_ingredients)

print(df['ingredients'])
>>>>>>> acdf7acfe58b5be76df8a9dd06ac4b1f36a028d3

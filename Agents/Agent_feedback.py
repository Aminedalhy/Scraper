import pandas as pd
from LLM.openai import ask_openai

def recommend_best_deal_with_ai(filename: str) -> tuple:
    try:
        df = pd.read_csv(filename)

        # Use the correct column names from your data
        df = df[df['rating'] >= 4.0]
        df = df.sort_values(by=['current_price'])

        products_text = "\n".join(
            f"{row['product_title']} : {row['current_price']}$, {row['rating']}"
            for _, row in df.iterrows()
        )

        prompt = f"""Here is a list of Amazon products:
{products_text}

Give me the best value-for-money product, with a short explanation (max 2 sentences).
"""

        result = ask_openai(prompt)
        product = df.iloc[0]['product_title'] if not df.empty else "No product found"
        return product, result

    except Exception as e:
        return "Error", f"An error occurred: {e}"
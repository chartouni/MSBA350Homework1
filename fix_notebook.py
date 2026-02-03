import json

# Read the notebook
with open('/home/user/MSBA350Homework1/G3_Homework2.ipynb', 'r') as f:
    notebook = json.load(f)

# Find and fix the incorrect volatility analysis
for cell in notebook['cells']:
    if cell['cell_type'] == 'markdown':
        if 'source' in cell:
            source = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']

            if 'Highest Volatility Stocks' in source and 'META and LLY' in source:
                # Fix the error
                old_text = """**Key Findings:**
1. **Highest Volatility Stocks**: META and LLY typically show higher volatility, reflecting tech sector and biotech uncertainty
2. **Lowest Volatility Stocks**: KO (Coca-Cola) and MCD (McDonald's) show lower volatility as stable consumer staples
3. **Risk-Return Tradeoff**: Higher volatility stocks may offer higher returns but with greater risk"""

                new_text = """**Key Findings:**
1. **Highest Volatility Stocks**: KO (Coca-Cola) at 40.55% and MSFT at 38.62% show the highest volatility - KO surprisingly tops the list despite being a "defensive" consumer staple
2. **Lowest Volatility Stocks**: KEY (KeyCorp) at 18.15% and MCD (McDonald's) at 20.51% show the lowest volatility as stable stocks
3. **Risk-Return Tradeoff**: Higher volatility stocks may offer higher returns but with greater risk - note that KO has high volatility but lower returns compared to MSFT"""

                if isinstance(cell['source'], list):
                    cell['source'] = [new_text]
                else:
                    cell['source'] = new_text

                print("Fixed the volatility analysis error!")
                break

# Save the corrected notebook
with open('/home/user/MSBA350Homework1/G3_Homework2.ipynb', 'w') as f:
    json.dump(notebook, f, indent=1)

print("Notebook corrected successfully!")

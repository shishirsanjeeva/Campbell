import pandas as pd
import re

def clean_text(text):
    if isinstance(text, str):
        return re.sub(r'\b(Hz|rpm)\b', '', text, flags=re.IGNORECASE).strip()
    return text

def process_excel(file_path, output_path):
    df = pd.read_excel(file_path, header=None, engine='openpyxl')

    header1 = ['S.no', 'Whirls', 'Stability', 'Critical Speed']
    rotational_velocity = [1, 10000, 20000, 30000, 40000]
    generated_headers = header1 + rotational_velocity

    if df.shape[1] != len(generated_headers):
        raise ValueError(f"Column count mismatch: Data has {df.shape[1]} columns, but {len(generated_headers)} headers were provided.")

    df.columns = generated_headers
    df = df.map(clean_text)
    df.to_excel(output_path, index=False)
    print(f"Processed file saved to {output_path}")

if __name__ == "__main__":
    input_file = 'Inputs.xlsx'
    output_file = 'output_cleaned.xlsx'
    process_excel(input_file, output_file)

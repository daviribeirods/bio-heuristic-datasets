import pandas as pd
import numpy as np

# Criar um dataset aleatório com as colunas mais simples possíveis e valores aleatórios
def generate_dataset_randomly(number_of_samples) -> pd.DataFrame:

    # Generate random dates
    start_date = pd.to_datetime('2026-01-01')
    end_date = pd.to_datetime('2026-07-01')

    random_dates_int = np.random.randint(start_date.value, end_date.value, size=number_of_samples)

    # convert into datetime
    random_dates = pd.to_datetime(random_dates_int)

    # Generate random user id within a range
    random_user_ids = np.random.randint(1, 100, size=number_of_samples)

    # is_fraud or not
    random_label = np.random.randint(0, 2, size=number_of_samples)

    # Generate random prices

    random_low_values = np.random.rand(10)

    data = {
        'Date': random_dates,
        'UserID': random_user_ids,
        'IsFraud': random_label,
        'Price': [],
        'ProductCategory': [],
        'GeoLocation': []
    }

    df = pd.DataFrame(data=data)

    return df

df = generate_dataset_randomly(number_of_samples=10000)
df.to_csv('./data/raw/random.csv',index=False)
def transform_data(data):
    rates = data["rates"]
    
    result = []
    for currency, rate in rates.items():
        result.append({
            "currency": currency,
            "rate": rate
        })
    
    return result
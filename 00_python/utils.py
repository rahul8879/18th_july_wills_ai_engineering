
def test(x,y):
    z = x + y
    return z

def sales_comparison(data):
    if len(data) < 2:
        return "Not enough data to compare."
    avg_odd_day_sales = sum(data[1::2]) / len(data[1::2])
    avg_even_day_sales = sum(data[0::2]) / len(data[0::2])
    if avg_odd_day_sales > avg_even_day_sales:
        return "Odd days are performing better."
    elif avg_even_day_sales > avg_odd_day_sales:
        return "Even days are performing better."
    else:
        return "Both are performing equally well."
    

def cleaning_output(data):
    
    category = []
    score = []
    for i in data:
        result = i.split("|")
        category.append(result[0].strip())
        score.append(float(result[1].strip()))

    return category, score



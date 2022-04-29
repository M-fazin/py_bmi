def bmi(weight, height):
    wweight = int(weight)
    hheight = float(height)
    calculator = (wweight/hheight**2)
    if calculator  < 18.5:
        return "OH No! You are Underweight, Go to gym and become healthy"
    elif calculator >= 18.5 and calculator  < 25:
        return "You Are Healthy, Normal"
    elif calculator >= 25 and calculator  < 30:
        return "OH.. You are Overweight"
    elif calculator >= 30:
        return "OH.. Noo.. You are Obesity"
    else:
        return "The Weight Must Be An Integer And Height In Decimal"

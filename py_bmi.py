def bmi(weight, height):
    wweight = int(weight)
    hheight = float(height)
    calculator = (wweight/hheight**2)
    if calculator  < 18.5:
        return "Underweight"
    elif calculator >= 18.5 and calculator  < 25:
        return "Normal"
    elif calculator >= 25 and calculator  < 30:
        return "Overweight"
    elif calculator >= 30:
        return "Obesity"
    else:
        return "The Weight Must Be An Integer And Height In Decimal"

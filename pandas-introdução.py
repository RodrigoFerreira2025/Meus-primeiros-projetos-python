import pandas as pd

mydataset = {
    'carros':['BMW','Volvo','Ford'],
    'passings':[8,6,4],
}

myvar = pd.DataFrame(mydataset)

print(myvar)
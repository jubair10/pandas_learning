import pandas as pd

var = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})

print(var.ndim)
print(var)


# can use any pyhton arithmetic operator
var["C"] = var["A"] ** var["B"]
print(var)

var["D"] = var["A"] ** var["B"] + var["C"]
print(var)


# ========= Logical Operator ==========

# returns Series
var1 = (var["D"] * var["C"]) < 5000

# can't decide true or false in the basis of Series 
# That's why "ValueError: The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all()."
# var2 = 1 if (var["D"] * var["C"]) < 5000 else 0
var2 = (var["D"] * var["C"]).apply(lambda x: 1 if x < 5000 else 0)
var2 = (var["D"] * var["C"] < 5000)


print(var2)

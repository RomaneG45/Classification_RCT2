X_dom = [1,2,3,4,5,6,7,8,9]
X_non_dom = [1,2,3,4,5]

min_longueur = min(len(X_dom), len(X_non_dom))
X_dom = X_dom[:min_longueur]
X_non_dom = X_non_dom[:min_longueur]

print("X_dom :", X_dom)
print("X_non_dom :", X_non_dom)
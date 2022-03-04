d1={'x':20, 'y':30}
d2={'z':60, 'b':80}
print("dict1:",d1)
print("dict1:",d2)
d=d1.copy()
d.update(d2)
print("merge dictionary:",d)
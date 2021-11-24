# Combining escape sequences and format strings to create a more complex format



formatter = "{} {} {} {} {}"

a = "This is good but\f never mind"

b = "I know that I can choose between a\\b\\c\\d\n but can'\t choose d"

c = " Below is what i need to buy\nmylist is :\n\t*car\n\t*house\n\t*cloth\nThat will bee\b all for now"

d = "formatting\f is\f now\f sweet\f me"

print(f"{a}, {b},{c}, {d}")

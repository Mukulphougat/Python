# Some knowledge from youtube
# Lambda expressions
def f(x):
    return 3*x+1
print(f(2))
print(lambda x: 3*x+1)
g = lambda x: 3*x+1
print(g(2))
full_name = lambda fn, ln: fn.strip().title() + " " +ln.strip().title()
print(full_name("Mukul"," Phougat"))
scifi_authors = ["Issac newton","stephan hawking"]
help(scifi_authors)
scifi_authors.sort(key = lambda name: name.split(" ")[-1].lower())
print(scifi_authors)
print(sys.argv)

# positional arg example : pos_only_arg(1)
# keyword arg example: kwd_only_arg(3)

# positional and keyword arguments
# *param receives a tuple beyond the formal param list
# **param receives a dict beyond the formal param list
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any kind", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
import sys

args = sys.argv
flags = []
coolText = ""
for arg in args:
        if "-" in arg:
                flags.append(arg)
        elif arg != args[0]:
                coolText += arg
                if arg != args[len(args)-1]:
                        coolText += " "

str_len = len(coolText)
eyes = "oo"
mouth = "__"
ears = "^__^"
tail = "\\/\\"
tonque = " "

if "-p" in flags: eyes = "@@"
if "-a" in flags: mouth = "/\\"
if "-e" in flags: ears = "/\\/\\"
if "-d" in flags: eyes = "$$"
if "-t" in flags: tail = "-------------->"
if "-to" in flags: tonque = "U"

print(f'''
  {"_" * len(coolText)}
< {coolText} >
  {"-" * len(coolText)}''')
print(" " * (str_len//2), f"\\  {ears}")
print(" " * (str_len//2), f" \\ ({eyes})\\________")
print(" " * (str_len//2), f"   ({mouth})\\        ){tail}")
print(" " * (str_len//2), f"     {tonque} ||------w|")
print(" " * (str_len//2), "       ||      ||")


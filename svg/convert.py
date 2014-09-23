import os

a = os.listdir(".")
for f in a:
    name = os.path.splitext(f);
    if (name[1] == ".svg"):
        print(name[0])
        os.system("inkscape -z -D -e ../png/{0}.png -w 370 {0}.svg".format(name[0]))

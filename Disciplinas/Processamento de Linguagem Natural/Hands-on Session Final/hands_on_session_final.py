import pgf as gf

gr = gf.readPGF("Processamento de Linguagem Natural/Hands-on Session 4/FoodsRGL.pgf")
eng = gr.languages["FoodsEngRGL"]
name = input("Write a sentence in English: ")

try:
    i = eng.parse(name)
    p,e = i.__next__()
    print(e)
    print("You have written: " + eng.linearize(e))
except gf.ParseError:
    print("This is not a valid sentence of FoodsEngRGL.")
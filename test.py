from op_text.models import DistilBert

fp = r"C:\Users\The Baboon\Downloads\distilbert5labels"
m = DistilBert(fp)

t = ["Test"] * 100
l = [1] * 100

m.fit(t, l, nb_epoch=10, verbose=True)

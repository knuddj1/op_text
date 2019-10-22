import os
from op_text.models import Bert, Roberta, DistilBert

base_dir = r"F:\fine_tuned_models"

bert_models_dir = os.path.join(base_dir, "bert models")
bert_models = ['bert-base-uncased'] + [os.path.join(bert_models_dir, m, "chkpt epochs=1") for m in os.listdir(bert_models_dir)]

roberta_models_dir = os.path.join(base_dir, "roberta models")
roberta_models = ['roberta-base'] + [os.path.join(roberta_models_dir, m, "chkpt epochs=1") for m in os.listdir(roberta_models_dir)]

distil_models_dir = os.path.join(base_dir, "distilbert models")
distil_models = ['distilbert-base-uncased']+ [os.path.join(distil_models_dir, m, "chkpt epochs=1") for m in os.listdir(distil_models_dir)]

X_train = [
    "This is a test sentence",
    "This is also a test sentence",
    "Whoop another test sentence",
    "Dogs are better than cats",
    "You thought the last one was gonna be about cats huh?"
]

y_train = [0, 0, 1, 1, 0]

for m in bert_models:
    model = Bert(m)
    model_save = os.path.join(r"F:\\", m.split("\\")[-2])
    if not os.path.exists(model_save):
        os.mkdir(model_save)
    model.fit(X_train, y_train, validation_split=0.4, chkpt_model_every=1, model_save_dir=model_save, nb_epoch=2) 
    print(m, model.evaluate(X_train, y_train))
    print(m, model.predict(X_train[:1]))

for m in roberta_models:
    model = Roberta(m)
    model_save = os.path.join(r"F:\\", m.split("\\")[-2])
    if not os.path.exists(model_save):
        os.mkdir(model_save)
    model.fit(X_train, y_train, validation_split=0.4, chkpt_model_every=1, model_save_dir=model_save, nb_epoch=2)
    print(m, model.evaluate(X_train, y_train))
    print(m, model.predict(X_train[:1]))

for m in distil_models:
    model = DistilBert(m)
    model_save = os.path.join(r"F:\\", m.split("\\")[-2])
    if not os.path.exists(model_save):
        os.mkdir(model_save)
    model.fit(X_train, y_train, validation_split=0.4, chkpt_model_every=1, model_save_dir=model_save, nb_epoch=2)
    print(m, model.evaluate(X_train, y_train))
    print(m, model.predict(X_train[:1]))
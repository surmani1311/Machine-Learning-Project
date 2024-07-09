import tkinter as tk
import joblib
from PIL import Image, ImageTk
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
import re
from sklearn.metrics import r2_score
from tkinter import messagebox


def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
             y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

# Load the trained model and vectorizer
tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))



def showme():
    message = ent.get()
    if message:
        preprocessed_message = transform_text(message)
        message_vector = tfidf.transform([preprocessed_message])
        prediction = model.predict(message_vector)[0]
        result = "Spam" if prediction == 1 else "Not Spam"
        messagebox.showinfo("Prediction", f"The message is: {result}")
    else:
        messagebox.showwarning("Input Error", "Please enter a message to classify")        
        
app=tk.Tk()
app.geometry("500x500")
app.title("Spam Detection")


lbl=tk.Label(app, text=" SMS SPAM DETECTOR",font=("robort",24,"bold"))
lbl.pack(fill="x",padx=5,pady=10,ipady=10,side="top")

lbl1=tk.Label(app, text="Enter the message",font=("robort",20,"bold"))
lbl1.pack(fill="x",padx=5,pady=5,ipady=10,side="top")

ent=tk.Entry(app,justify="center",font=("robort",20,"bold"))
ent.pack(padx=15,pady=10,ipady=10,side="top")


btn=tk.Button(app,text="Check",font=("robort",20),command=showme)
btn.pack(pady=20)

lblx=tk.Label(app, text=" ",font=("robort",15))
lblx.pack()










app.mainloop()
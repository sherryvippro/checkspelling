# pip install langdetect
# pip install TextBlob
# pip install pyspellchecker

import tkinter as tk

from langdetect import detect 
from textblob import TextBlob 
from spellchecker import SpellChecker 
from dictionary import vietnameseDictionary


def detectLanguage(inputText):
    language = detect(inputText)
    return language

def initVocab():
    listVocab = []
    for word in vietnameseDictionary.keys():
        listVocab.append(word)
    return listVocab

def detectAndFixEnglishError(inputText):
    blob = TextBlob(inputText)
    correctedText = blob.correct()
    return str(correctedText)

def detectVietNameseError(inputText):
    check = SpellChecker(language=None)
    check.word_frequency.load_words(initVocab())

    words = inputText.split(' ')
    errorWord = []
    for word in words:
        if word not in check:
            errorWord.append(word)
        
    return ', '.join(errorWord)

# def correctSpelling(inputText):
#     language = detectLanguage(inputText)
#     if language == 'en':
#         print('Detected Language: English')
#         return detectAndFixEnglishError(inputText)
#     elif language == 'vi':
#         print('Detected Language: Vietnamese')
#         print('Spelling Word Error:', end=' ')
#         return detectVietNameseError(inputText)
#     else:
#         return "Language not supported"

def correctSpelling():
    inputText = text_input.get("1.0", tk.END)

    language = detectLanguage(inputText)
    text_output.delete("1.0", tk.END)
    if language == 'vi':
        text_output.insert(tk.END, 'Detected Language: Vietnamese\n')
        text_output.insert(tk.END, 'Spelling Word Error:')
        text_output.insert(tk.END, detectVietNameseError(inputText))
    else:
        text_output.insert(tk.END, 'Detected Language: English\n')
        text_output.insert(tk.END, detectAndFixEnglishError(inputText))

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Spell Checker")

# Khung nhập văn bản
text_input = tk.Text(root, height=10, width=50)
text_input.pack()

# Nút kiểm tra chính tả
btn = tk.Button(root, text="Check Spelling", command=correctSpelling)
btn.pack()

# Khung kết quả
text_output = tk.Text(root, height=10, width=50)
text_output.pack()

# Chạy giao diện
root.mainloop()


# if __name__ == '__main__':
#     sentence = "I want to saay that I realy realy lovo you"
#     sentence1 = "Hơm qua tooi bị phạt."
#     sentence2 = "Tôi thích lập trinhg và i lovv programming"
#     # fixed = correctSpelling(sentence)
#     fixed1 = correctSpelling(sentence2)
#     # print(fixed)
#     print(fixed1)
#     # print('Từ sai chính tả: ', fixed1)


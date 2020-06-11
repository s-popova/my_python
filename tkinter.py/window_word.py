{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import tkinter\n",
    "import random\n",
    "dictionary = {'anaconda': 'анаконда', 'python': 'питон', 'snake': 'змея', 'boa': 'удав'}\n",
    "word = random.choice(list(dictionary.keys()))\n",
    "\n",
    "window = tkinter.Tk()\n",
    "\n",
    "def click():\n",
    "    word1 = dictionary.get(word)\n",
    "    if entry.get() == word1:\n",
    "        result = 'Слово угадано!'\n",
    "        label.config(text = result)\n",
    "    elif entry.get() != word1:\n",
    "        result = 'Слово не угадано!'\n",
    "        label.config(text = result)\n",
    "        \n",
    "def exit():\n",
    "    window.destroy()\n",
    "        \n",
    "a = tkinter.Label(window, text = 'Случайное слово: ')\n",
    "a.pack()\n",
    "word2 = tkinter.Label(window, text = word)\n",
    "word2.pack()\n",
    "b = tkinter.Label(window, text = 'Укажите перевод слова: ')       \n",
    "b.pack()\n",
    "frame = tkinter.Frame(window)\n",
    "frame.pack()\n",
    "entry = tkinter.Entry(frame)\n",
    "entry.pack()\n",
    "label = tkinter.Label(window)\n",
    "label.pack()\n",
    "button = tkinter.Button(window, text = 'Готово!',command = click)\n",
    "button.pack()\n",
    "button1 = tkinter.Button(window, text = 'Выход',command = exit)\n",
    "button1.pack()\n",
    "\n",
    "window.mainloop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

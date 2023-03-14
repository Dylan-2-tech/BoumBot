

# BoumBot

**BoumBot** is a bot created by myself in the purpose of playing the game **[Bomb Party](https://jklm.fun/)**

## Explanation of the Bomb Party game

The goal is to give a word who contains the letter combo that the game choosed the most quickly you can to survive. If you take too long to give a correct answer the bomb will explode and you loose a heart.
At 0 heart you loose the game. 

**Exemple**: 
The game wants a word with 'ph' in it and the bot may give the answer 'philosophie' if you're playing with French words.
## Explanation of the BoumBot

To search the correct word, the bot use 2 files. A json file that stores a list of words arranged by their letters contained inside and a text file that store a lot of words.

When the game is asking for a letter combo. The programm is first searching if the combo is in the keys of the json file named **'vocabulary.json'** and if so it gives a word who contains it.

If the letter combo is not in the json keys, it search the first word who contains the combo and sends it.

At the end of the game,
for all letters combo that were not in the json keys. The bot creates his own data by searching a list of 20 words in the list of words txt file and add it to the json file with the letter combo as key and the list as the value.

The bot is ***'learning'***.
## Requirements

Works on **UBUNTU** and **WINDOWS**

This project has been tested on ubuntu 22.04 and window 10.
*Make sure to have the **Python 3.11.1** version and **Chrome installed**.

#
Download the latest chrome version on **UBUNTU** thanks to this:
```bash
  wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
```
Then install it with:
```bash
  sudo apt install ./google-chrome-stable_current_amd64.deb
```

#
Download the latest chrome version on **WINDOWS** thanks to this link: https://www.google.com/chrome/
#

On **UBUNTU** and **WINDOWS**

This is used to control your **Chrome Application**.
```bash
  pip install webdriver_manager
```

This is used to control the **Chrome Web Pages**
```bash
  pip install selenium
```

and *Tkinter is the library to create a user interface*
```bash
  pip install tk
```


## Run the BoumBot

On **UBUNTU** and **WINDOWS**

Clone the project

```bash
  git clone https://github.com/Dylan-2-tech/BoumBot.git
```

###
On **WINDOWS**

Open the Windows CMD window on the directory **'BoumBot'** and run the boumbot.py
```bash
  python.exe boumbot.py
```
###
On **UBUNTU**

Open a terminal and write:
```bash
  python3 boumbot.py
```

## How to join a Party

First, you or your friend need to create a party and get 4 letters game Code on the jklm.fun/XXXX.

Once you've got the code type it in the entry 'Enter the code party'.
You can also choose a username, by default its 'BoumBot'.

If it's done you can start the bot and enjoy :)

## Author

- [@dylan-2-tech](https://www.github.com/Dylan-2-tech)

#

![Python](https://img.shields.io/badge/-Python-05122A?style=flat&logo=python)&nbsp;

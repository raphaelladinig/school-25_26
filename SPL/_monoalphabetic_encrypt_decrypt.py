# tkinter provides GUI objects and commands
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import font

# An object (root) is created which represents the window.
# Its title and full screen property are set.
root = tk.Tk()
root.title("Monoalphabetic Encryption")
root.wm_state("iconic")

# Modern dark theme colors
BG_DARK = "#1e1e2e"
BG_MEDIUM = "#2a2a3e"
BG_LIGHT = "#363650"
ACCENT_BLUE = "#89b4fa"
ACCENT_GREEN = "#a6e3a1"
ACCENT_RED = "#f38ba8"
ACCENT_PURPLE = "#cba6f7"
TEXT_PRIMARY = "#cdd6f4"
TEXT_SECONDARY = "#a6adc8"
BORDER_COLOR = "#45475a"

# Configure root window
root.configure(bg=BG_DARK)

# Custom fonts
title_font = font.Font(family="Segoe UI", size=14, weight="bold")
button_font = font.Font(family="Segoe UI", size=10)
label_font = font.Font(family="Segoe UI", size=9)
text_font = font.Font(family="Consolas", size=10)

# Configure ttk styles
style = ttk.Style()
style.theme_use('clam')

# Frame styles
style.configure("Dark.TFrame", background=BG_DARK, borderwidth=0)
style.configure("Medium.TFrame", background=BG_MEDIUM, borderwidth=2, relief="flat")

# Label styles
style.configure("Title.TLabel", background=BG_MEDIUM, foreground=ACCENT_PURPLE, 
                font=title_font, padding=10)
style.configure("Normal.TLabel", background=BG_MEDIUM, foreground=TEXT_PRIMARY, 
                font=label_font)
style.configure("Feedback.TLabel", background=BG_MEDIUM, foreground=ACCENT_GREEN, 
                font=label_font, padding=5)

# Button styles
style.configure("Accent.TButton", background=ACCENT_BLUE, foreground=BG_DARK,
                font=button_font, borderwidth=0, focuscolor='none', padding=10)
style.map("Accent.TButton",
          background=[('active', ACCENT_PURPLE), ('pressed', ACCENT_PURPLE)],
          foreground=[('active', BG_DARK)])

# Entry styles
style.configure("Dark.TEntry", fieldbackground=BG_LIGHT, foreground=TEXT_PRIMARY,
                borderwidth=1, relief="flat", insertcolor=TEXT_PRIMARY)

# Checkbutton styles
style.configure("Dark.TCheckbutton", background=BG_MEDIUM, foreground=TEXT_PRIMARY,
                font=label_font, borderwidth=0, focuscolor='')
style.map("Dark.TCheckbutton",
          background=[('active', BG_MEDIUM)],
          foreground=[('active', ACCENT_BLUE)])

# Radiobutton styles
style.configure("Dark.TRadiobutton", background=BG_MEDIUM, foreground=TEXT_PRIMARY,
                font=label_font, borderwidth=0, focuscolor='')
style.map("Dark.TRadiobutton",
          background=[('active', BG_MEDIUM)],
          foreground=[('active', ACCENT_PURPLE)])

# Combobox styles
style.configure("Dark.TCombobox", fieldbackground=BG_LIGHT, background=BG_LIGHT,
                foreground=TEXT_PRIMARY, borderwidth=1, arrowcolor=ACCENT_BLUE)
style.map("Dark.TCombobox",
          fieldbackground=[('readonly', BG_LIGHT)],
          selectbackground=[('readonly', BG_LIGHT)])

# This function normalizes the parameter text according to the
# settings "Keep blanks" and "Keep non-alphabetic chars".
def NormalizeText(text, strict = False):
    s = ""
    for c in text:
        if ((ord(c) <= ord("Z")) and (ord(c) >= ord("A"))):
            s += c
        elif ((ord(c) <= ord("z")) and (ord(c) >= ord("a"))):
            s += chr(ord(c) + ord("A") - ord("a"))
        elif ((c == "ä") or (c == "Ä")):
            s += "AE"
        elif ((c == "ö") or (c == "Ö")):
            s += "OE"
        elif ((c == "ü") or (c == "Ü")):
            s += "UE"
        elif (c == "ß"):
            s += "SS"
        elif ((c == " ") or (ord(c) == 10)):
            if ((KeepBlanks.get() == "1") and not strict):
                s += " "
        elif ((KeepNonalpha.get() == "1") and not strict):
            s += c
    return s

# The labels used to interact with the user are cleared.
def ClearFeedbackLabels():
    LabelPlainFeedback["text"] = ""
    LabelPlainFeedback["foreground"] = ACCENT_GREEN
    LabelCiphFeedback["text"] = ""
    LabelCiphFeedback["foreground"] = ACCENT_GREEN

# This function is invoked when the user clicks the button
# "Load plaintext from file".
def ButtonPlainLoadClick():
    ClearFeedbackLabels()
    try:
        with open(PathPlain.get(), mode = "rt", encoding = "utf-8") as PlainFile:
            plain = PlainFile.read()
    except:
        LabelPlainFeedback["text"] = "✗ An error occurred while reading the file."
        LabelPlainFeedback["foreground"] = ACCENT_RED
    else:
        if plain == "":
            LabelPlainFeedback["text"] = "⚠ File empty"
            LabelPlainFeedback["foreground"] = TEXT_SECONDARY
        else:
            plain = NormalizeText(plain)
            TextPlain.delete("1.0", "end")
            TextPlain.insert("1.0", plain)
            LabelPlainFeedback["text"] = "✓ File loaded successfully."
            LabelPlainFeedback["foreground"] = ACCENT_GREEN

# This function is invoked when the user clicks the button
# "Save ciphertext to file".
def ButtonCiphSaveClick():
    ClearFeedbackLabels()
    ciph = TextCiph.get("1.0", "end")[:-1]
    if len(ciph) < 1:
        LabelCiphFeedback["text"] = "⚠ Nothing to save"
        LabelCiphFeedback["foreground"] = TEXT_SECONDARY
        return
    try:
        with open(PathCiph.get(), mode = "wt", encoding = "utf-8") as CiphFile:
            if (CiphFile.write(ciph) != len(ciph)):
                raise Exception
    except:
        LabelCiphFeedback["text"] = "✗ An error occurred while saving to file."
        LabelCiphFeedback["foreground"] = ACCENT_RED
    else:
        LabelCiphFeedback["text"] = "✓ Ciphertext saved successfully."
        LabelCiphFeedback["foreground"] = ACCENT_GREEN

# This function is invoked when the user selects a radio
# button corresponding to one of the various cipher modes.
def ChangeMode():
    ClearFeedbackLabels()
    if GeneralMode.get() == 0:
        ComboText[0].set("a")
        UpdateCombosCaesarMode()
        ComboSubst[0]["state"] = "normal"
        for i in range(1, 26):
            ComboSubst[i]["state"] = "disabled"
    elif GeneralMode.get() == 1:
        for i in range(26):
            ComboSubst[i]["state"] = "normal"
            ComboText[i].set(chr(ord("A")+i))
    else:
        for i in range(26):
            ComboText[i].set(chr(ord("Z")-i))
            ComboSubst[i]["state"] = "disabled"
    UpdatePlaintext()

# This function fills all the combo boxes with ascending
# letters starting from the letter of the first one.
def UpdateCombosCaesarMode():
    c = ComboText[0].get()
    for i in range(1, 26):
        if c == "z":
            c = "a"
        else:
            c = chr(ord(c) + 1)
        ComboText[i].set(c)

# This function creates the list of selectable letters
# for the combo box with the given index.
def FillComboList(index):
    if GeneralMode.get() == 0:
        l = []
        skip_list = []
    else:
        l = [chr(ord("A")+index)]
        skip_list = [ComboText[i].get() for i in range(26) if i != index]
    for i in range(26):
        c = chr(ord("a")+i)
        if not c in skip_list:
            l.append(c)
    ComboSubst[index]["values"] = l

# This function is invoked when a combo box loses the focus.
def FocusOutCombo(contents, index):
    c = contents.get()
    if len(c) == 0:
        if GeneralMode.get() == 1:
            c = chr(ord("A")+index)
        else:
            c = "a"
    else:
        c = c[-1]
        if (ord(c) < ord("a")) or (ord(c) > ord("z")):
            if GeneralMode.get() == 1:
                c = chr(ord("A")+index)
            else:
                c = "a"
    contents.set(c)
    if GeneralMode.get() == 0:
        UpdateCombosCaesarMode()
    else:
        for i in range(26):
            if i == index:
                continue
            if c == ComboText[i].get():
                ComboText[i].set(chr(ord("A")+i))
                break
    UpdatePlaintext()

# This function applies the encryption to the plaintext.
def UpdatePlaintext():
    plain = NormalizeText(TextPlain.get("1.0", "end")[:-1])
    TextPlain.delete("1.0", "end")
    TextPlain.insert("1.0", plain)
    cipher = ""
    for c in plain:
        if ((ord(c) < ord("A")) or (ord(c) > ord("Z"))):
            cipher += c
        else:
            cipher += ComboText[ord(c)-ord("A")].get()
    TextCiph.delete("1.0", "end")
    TextCiph.insert("1.0", cipher)

# The window is divided into three frames.
FramePlain = ttk.Frame(master = root, style="Medium.TFrame", padding=15)
FrameKey = ttk.Frame(master = root, style="Medium.TFrame", padding=15)
FrameCiph = ttk.Frame(master = root, style="Medium.TFrame", padding=15)
FramePlain.pack(side = "left", fill = "both", expand = True, padx=(10,5), pady=10)
FrameKey.pack(side = "left", fill = "y", padx=5, pady=10)
FrameCiph.pack(side = "left", fill = "both", expand = True, padx=(5,10), pady=10)

# PLAINTEXT SECTION
LabelPlainCaption = ttk.Label(master = FramePlain, text = "📄 PLAINTEXT", style="Title.TLabel")
LabelPlainCaption.pack(side = "top", pady=(0,10), fill="x")

FramePlainBtnEntry = ttk.Frame(master = FramePlain, style="Medium.TFrame")
FramePlainBtnEntry.pack(side = "top", pady = 10, fill = "x")

ButtonPlainLoad = ttk.Button(master = FramePlainBtnEntry,
                             text = "Load from file",
                             style="Accent.TButton",
                             command = ButtonPlainLoadClick)
PathPlain = tk.StringVar(value = "./text.txt")
EntryPlain = ttk.Entry(master = FramePlainBtnEntry, textvariable=PathPlain, 
                       style="Dark.TEntry", font=label_font)
ButtonPlainLoad.pack(side = "left", padx = (0,10))
EntryPlain.pack(side = "left", fill = "x", expand = True)

LabelPlainFeedback = ttk.Label(master = FramePlain, text = "", style="Normal.TLabel")
LabelPlainFeedback.pack(side = "top", pady = 5, fill = "x")

TextPlain = tk.Text(master = FramePlain, width = 10, 
                   bg=BG_LIGHT, fg=TEXT_PRIMARY, 
                   insertbackground=ACCENT_BLUE,
                   selectbackground=ACCENT_PURPLE,
                   selectforeground=BG_DARK,
                   font=text_font,
                   borderwidth=0,
                   relief="flat",
                   padx=10, pady=10)
TextPlain.pack(side = "bottom", fill = "both", expand = True, pady = (10,0))

# KEY SECTION
LabelKeyCaption = ttk.Label(master = FrameKey, text = "🔑 KEY", style="Title.TLabel")
LabelKeyCaption.pack(side = "top", pady= 0, fill="x")

KeepBlanks = tk.StringVar(value = 1)
KeepNonalpha = tk.StringVar(value = 1)
CheckKeyKeepBlanks = ttk.Checkbutton(master = FrameKey, text = "Keep blanks",
                                     variable = KeepBlanks, style="Dark.TCheckbutton")
CheckKeyKeepSpecials = ttk.Checkbutton(master = FrameKey, text = "Keep non-alphabetic chars",
                                       variable = KeepNonalpha, style="Dark.TCheckbutton")
CheckKeyKeepBlanks.pack(side = "top", pady = 5, fill = "x", anchor="w")
CheckKeyKeepSpecials.pack(side = "top", pady = 5, fill = "x", anchor="w")

# Separator
ttk.Separator(master=FrameKey, orient='horizontal').pack(side="top", fill="x", pady=5)

GeneralMode = tk.IntVar(value = 0)
RadioButtonAtbash = ttk.Radiobutton(master = FrameKey, text = "Atbash Cipher",
                                    value = -1, variable = GeneralMode,
                                    command = ChangeMode, style="Dark.TRadiobutton")
RadioButtonCaesar = ttk.Radiobutton(master = FrameKey, text = "Caesar Cipher",
                                    value = 0, variable = GeneralMode,
                                    command = ChangeMode, style="Dark.TRadiobutton")
RadioButtonGeneral = ttk.Radiobutton(master = FrameKey, text = "General Substitution",
                                    value = 1, variable = GeneralMode,
                                    command = ChangeMode, style="Dark.TRadiobutton")
RadioButtonAtbash.pack(side = "top", fill = "x", pady = 5, anchor="w")
RadioButtonCaesar.pack(side = "top", fill = "x", pady = 5, anchor="w")
RadioButtonGeneral.pack(side = "top", fill = "x", pady = 5, anchor="w")

# Separator
ttk.Separator(master=FrameKey, orient='horizontal').pack(side="top", fill="x", pady=(5,10))

FrameKeyPad1 = ttk.Frame(master = FrameKey, style="Medium.TFrame")
FrameKeyPad2 = ttk.Frame(master = FrameKey, style="Medium.TFrame")
FrameKeyPad3 = ttk.Frame(master = FrameKey, style="Medium.TFrame")
FrameKeyPad1.pack(side = "left", fill = "both", padx = (0,5))
FrameKeyPad3.pack(side = "right", fill = "both", padx = (5,0))
FrameKeyPad2.pack(side = "right", fill = "both", expand = True)

FramesSubst = []
LabelSubst = []
ComboSubst = []
ComboText = []

for i in range(26):
    if i < 13:
        FramesSubst.append(ttk.Frame(master = FrameKeyPad1, style="Medium.TFrame"))
    else:
        FramesSubst.append(ttk.Frame(master = FrameKeyPad3, style="Medium.TFrame"))
    FramesSubst[i].pack(side = "top", fill = "both", expand = True, pady=1)
    
    LabelSubst.append(ttk.Label(master = FramesSubst[i], 
                               text = chr(ord("A")+i) + " →", 
                               style="Normal.TLabel",
                               foreground=ACCENT_BLUE))
    ComboText.append(tk.StringVar(value = chr(ord("A")+i)))
    ComboSubst.append(ttk.Combobox(master = FramesSubst[i],
                                   width = 3,
                                   textvariable = ComboText[i],
                                   style="Dark.TCombobox",
                                   font=label_font,
                                   postcommand = lambda i=i: FillComboList(i)))
    ComboSubst[i].bind("<FocusOut>", lambda event, i=i: FocusOutCombo(ComboText[i], i))

for i in range(13):
    LabelSubst[i].pack(side = "left", padx=(5,5))
    ComboSubst[i].pack(side = "right", padx=(0,5))
    LabelSubst[i+13].pack(side = "left", padx=(5,5))
    ComboSubst[i+13].pack(side = "right", padx=(0,5))

# CIPHERTEXT SECTION
LabelCiphCaption = ttk.Label(master = FrameCiph, text = "🔐 CIPHERTEXT", style="Title.TLabel")
LabelCiphCaption.pack(side = "top", pady=(0,10), fill="x")

FrameCiphBtnEntry = ttk.Frame(master = FrameCiph, style="Medium.TFrame")
FrameCiphBtnEntry.pack(side = "top", pady = 10, fill = "x")

ButtonCiphSave = ttk.Button(master = FrameCiphBtnEntry,
                            text = "Save to file",
                            style="Accent.TButton",
                            command = ButtonCiphSaveClick)
PathCiph = tk.StringVar(value = "./text.txt")
EntryCiph = ttk.Entry(master = FrameCiphBtnEntry, textvariable=PathCiph,
                      style="Dark.TEntry", font=label_font)
ButtonCiphSave.pack(side = "left", padx = (0,10))
EntryCiph.pack(side = "left", fill = "x", expand = True)

LabelCiphFeedback = ttk.Label(master = FrameCiph, text = "", style="Normal.TLabel")
LabelCiphFeedback.pack(side = "top", pady = 5, fill = "x")

TextCiph = tk.Text(master = FrameCiph, width = 10,
                  bg=BG_LIGHT, fg=TEXT_PRIMARY,
                  insertbackground=ACCENT_BLUE,
                  selectbackground=ACCENT_PURPLE,
                  selectforeground=BG_DARK,
                  font=text_font,
                  borderwidth=0,
                  relief="flat",
                  padx=10, pady=10)
TextCiph.pack(side = "bottom", fill = "both", expand = True, pady = (10,0))

ChangeMode()
root.mainloop()

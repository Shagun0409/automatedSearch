import tkinter as tk
from tkinter import Entry,Label,Button
import webbrowser

#define the main window

root=tk.Tk()
root.title("MY AI ASSISTANT")

#adding colour

root.configure(bg='purple')

#function for utube

def search_youtube():
    query=entry.get()
    url=f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)
    
def search_google():
    query=entry.get()
    url=f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    
def search_instagram():
    Username=entry.get().replace('@' ," ")
    url=f"https://www.instagram.com/accounts/onetap/?next=%2F&hl=en/{Username}/"
    webbrowser.open(url)
    
def search_gfg():
    query=entry.get()
    url=f"https://auth.geeksforgeeks.org/user/shagunsg2003/?utm_source=geeksforgeeks={query}"
    webbrowser.open(url)
    
def search_leetcode():
    query=entry.get()
    url=f"https://leetcode.com/shagun_0409/={query}"
    webbrowser.open(url)
    
def search_chatgpt():
    query=entry.get()
    url=f"https://chat.openai.com/={query}"
    webbrowser.open(url)
    
def search_github():
    query=entry.get()
    url=f"https://github.com/Shagun0409={query}"
    webbrowser.open(url)
    
    
Label(root,text="enter your command: ").pack(pady=10)
entry=Entry(root,width=80)
entry.pack(pady=10)
Button(root,text="search on youtube",fg='green', command=search_youtube).pack(pady=5)
Button(root,text="search on google", fg='green',command=search_google).pack(pady=5)
Button(root,text="search on intagram",fg='green', command=search_instagram).pack(pady=5)
Button(root,text="search on geeksforgeeks shagun",fg='green', command=search_gfg).pack(pady=5)
Button(root,text="search on leetcode",fg='green', command=search_leetcode).pack(pady=5)
Button(root,text="search on chatgpt",fg='green', command=search_chatgpt).pack(pady=5)
Button(root,text="search on github",fg='green', command=search_github).pack(pady=5)




root.mainloop()
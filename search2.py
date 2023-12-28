import tkinter as tk
from tkinter import Entry, Label, Button, messagebox
import webbrowser

class MyAIAssistant:
    def __init__(self, master):
        self.master = master
        master.title("MY AI ASSISTANT")
        master.configure(bg='purple')

        Label(master, text="Enter your command: ").pack(pady=10)
        self.entry = Entry(master, width=80)
        self.entry.pack(pady=10)

        Button(master, text="Search on YouTube", fg='green', command=self.search_youtube).pack(pady=5)
        Button(master, text="Search on Google", fg='green', command=self.search_google).pack(pady=5)
        Button(master, text="Search on Instagram", fg='green', command=self.search_instagram).pack(pady=5)
        Button(master, text="Search on GeeksforGeeks Shagun", fg='green', command=self.search_gfg).pack(pady=5)
        Button(master, text="Search on LeetCode", fg='green', command=self.search_leetcode).pack(pady=5)
        Button(master, text="Search on ChatGPT", fg='green', command=self.search_chatgpt).pack(pady=5)
        Button(master, text="Search on GitHub", fg='green', command=self.search_github).pack(pady=5)
        Button(master, text="Clear", fg='red', command=self.clear_entry).pack(pady=5)

    def search_youtube(self):
        self.perform_search("https://www.youtube.com/results?search_query=")

    def search_google(self):
        self.perform_search("https://www.google.com/search?q=")

    def search_instagram(self):
        username = self.entry.get().replace('@', '')
        self.perform_search(f"https://www.instagram.com/accounts/onetap/?next=%2F&hl=en/{username}/")

    def search_gfg(self):
        self.perform_search("https://auth.geeksforgeeks.org/user/shagunsg2003/?utm_source=geeksforgeeks=")

    def search_leetcode(self):
        self.perform_search("https://leetcode.com/shagun_0409/=")

    def search_chatgpt(self):
        self.perform_search("https://chat.openai.com/=")

    def search_github(self):
        self.perform_search("https://github.com/Shagun0409=")

    def clear_entry(self):
        self.entry.delete(0, 'end')

    def perform_search(self, base_url):
        query = self.entry.get()
        if query:
            url = f"{base_url}{query}"
            webbrowser.open(url)
        else:
            messagebox.showwarning("Empty Input", "Please enter a command.")

if __name__ == "__main__":
    root = tk.Tk()
    my_assistant = MyAIAssistant(root)
    root.mainloop()

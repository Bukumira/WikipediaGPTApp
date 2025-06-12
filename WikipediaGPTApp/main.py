import tkinter as tk
import requests
from datetime import datetime
import re
import openai
from tkinter import messagebox

from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_gpt_response(user_input):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": user_input}
            ]
        )
        return response.choices[0].message['content']
    except Exception as e:
        messagebox.showerror("Error", f"Error fetching GPT response: {e}")
        return "Error in generating GPT response."


def get_last_revision_text_2021(page_title, language_code):
    S = requests.Session()
    URL = "https://en.wikipedia.org/w/api.php"

    PARAMS = {
        "action": "query",
        "format": "json",
        "prop": "revisions",
        "titles": page_title,
        "rvlimit": "1",
        "rvprop": "ids|timestamp",
        "redirects": "1",
        "rvstart": "2021-01-01T00:00:00Z",
        "rvdir": "older"
    }

    if language_code == "sr-latin":
        URL = "https://sh.wikipedia.org/w/api.php"
    else:
        URL = f"https://{language_code}.wikipedia.org/w/api.php"

    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()

    pages = DATA.get('query', {}).get('pages', {})
    page_id = next(iter(pages))
    if page_id == '-1':
        return "Page does not exist."

    revisions = pages[page_id].get('revisions', [])
    if not revisions:
        return "No revisions found."

    last_revision_2020 = None
    for revision in revisions:
        revision_date = datetime.strptime(revision['timestamp'], "%Y-%m-%dT%H:%M:%SZ")
        if revision_date.year == 2020: 
            if not last_revision_2020 or revision_date > last_revision_2020['timestamp']:
                last_revision_2020 = revision
                last_revision_2020['timestamp'] = revision_date

    if not last_revision_2020:
        return "No revision found in 2020."

    closest_revision_id = last_revision_2020['revid']
    
    PARAMS = {
        "action": "query",
        "format": "json",
        "prop": "revisions",
        "revids": closest_revision_id,
        "rvprop": "content",
        "rvslots": "main"
    }

    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()

    pages = DATA.get('query', {}).get('pages', {})
    page_content = next(iter(pages.values())).get('revisions', [{}])[0].get('slots', {}).get('main', {}).get('*', "")

    clean_content = clean_wiki_text(page_content)
    return clean_content[:2400]

def clean_wiki_text(text):
    text = re.sub(r'(^\s*==.*?==\s*\n)+', '', text, flags=re.MULTILINE)  
    text = re.sub(r'\{\|.*?\|\}', '', text, flags=re.DOTALL)  
    text = re.sub(r'\{\{[^{}]*\}\}', '', text)  
    text = re.sub(r'<[^>]+>', '', text)  
    text = re.sub(r'\[\[File:[^\]]*\]\]', '', text)  
    text = re.sub(r'\[\[Image:[^\]]*\]\]', '', text)  
    text = re.sub(r'\[\[([^\]|]+)\|([^\]]+)\]\]', r'\2', text)  
    text = re.sub(r'\[\[([^\]]+)\]\]', r'\1', text)  
    text = re.sub(r'\{\{[^\}]+\}\}', '', text)  
    text = re.sub(r'{{[^\}]*}}', '', text) 
    text = re.sub(r'\*\s*', '', text)  
    text = re.sub(r'\n\s*\n', '\n', text)  
    text = re.sub(r'\s+', ' ', text)  
    text = re.sub(r'\|-\s*', '', text)  
    text = re.sub(r'<ref.*?>.*?</ref>', '', text, flags=re.DOTALL)  
    text = re.sub(r'\[http[^ ]+ [^]]+\]', '', text)  
    text = re.sub(r'\[[^ ]+ [^]]+\]', '', text)  
    text = re.sub(r'\|\s*', '', text) 
    text = re.sub(r'\s*align=".*?"\s*', '', text)  
    text = re.sub(r'\s*bgcolor=".*?"\s*', '', text)  
    text = re.sub(r'\s*bgcolor#\w+\s*', '', text) 
    text = re.sub(r'\[\[.*?\]\]', '', text)
    text = re.sub(r'^\s+|\s+$', '', text)  
    text = re.sub(r"\[\[.*?\]\]", "", text)  
    text = re.sub(r"<ref>.*?</ref>", "", text) 
    text = re.sub(r"\s+", " ", text).strip()  
    text = re.sub(r"[\'=]", "", text) 
    text = text.replace("]", "")  
    return text.strip() 



def update_output():
    page_title = input_field.get()
    selected_language = language_var.get()

    language_code = {
        "English": "en",
        "German": "de",
        "Serbian (Latin)": "sr-latin"
    }.get(selected_language, "en")

    if page_title:
        text = get_last_revision_text_2021(page_title, language_code)
        if text == "Page does not exist.":
            output_field.config(state=tk.NORMAL)
            output_field.delete(1.0, tk.END)
            output_field.insert(tk.END, text)
            output_field.config(state=tk.DISABLED)
            generate_button.config(state=tk.DISABLED)
        elif text == "No revisions found.":
            output_field.config(state=tk.NORMAL)
            output_field.delete(1.0, tk.END)
            output_field.insert(tk.END, text)
            output_field.config(state=tk.DISABLED)
            generate_button.config(state=tk.DISABLED)
        else:
            output_field.config(state=tk.NORMAL)
            output_field.delete(1.0, tk.END)
            output_field.insert(tk.END, text)
            output_field.config(state=tk.DISABLED)
            generate_button.config(state=tk.NORMAL)


def generate_ai_text():
    page_title = input_field.get()
    selected_language = language_var.get()
    language_code = {
        "English": "en",
        "German": "de",
        "Serbian (Cyrillic)": "sr",
        "Serbian (Latin)": "sr-latin"
    }.get(selected_language, "en")

    if page_title:
        user_input = f"Write a short academic essay about {page_title} in {selected_language}."
        ai_text = get_gpt_response(user_input)
        ai_output_field.config(state=tk.NORMAL)
        ai_output_field.delete(1.0, tk.END)
        ai_output_field.insert(tk.END, ai_text[:2400])  
        ai_output_field.config(state=tk.DISABLED)

def clear_output_fields(event=None):
    output_field.config(state=tk.NORMAL)
    output_field.delete(1.0, tk.END)
    output_field.config(state=tk.DISABLED)
    
    ai_output_field.config(state=tk.NORMAL)
    ai_output_field.delete(1.0, tk.END)
    ai_output_field.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Wikipedia Revision Search")

tk.Label(root, text="Enter Wikipedia Page Title:").grid(row=0, column=0, padx=10, pady=5, sticky='w')
input_field = tk.Entry(root)
input_field.grid(row=1, column=0, padx=10, pady=5)
input_field.bind("<KeyRelease>", clear_output_fields) 

tk.Label(root, text="Select Language:").grid(row=2, column=0, padx=10, pady=5, sticky='w')
language_var = tk.StringVar(value="English")
language_dropdown = tk.OptionMenu(root, language_var, "English", "German", "Serbian (Latin)")
language_dropdown.grid(row=3, column=0, padx=10, pady=5)

tk.Label(root, text="Wikipedia Output:").grid(row=4, column=0, padx=10, pady=5, sticky='w')
output_field = tk.Text(root, height=15, width=60, wrap=tk.WORD, state=tk.DISABLED)
output_field.grid(row=5, column=0, padx=10, pady=5)

tk.Label(root, text="AI Generated Text:").grid(row=6, column=0, padx=10, pady=5, sticky='w')
ai_output_field = tk.Text(root, height=15, width=60, wrap=tk.WORD, state=tk.DISABLED)
ai_output_field.grid(row=7, column=0, padx=10, pady=5)

submit_button = tk.Button(root, text="Fetch Revision Text", command=update_output)
submit_button.grid(row=8, column=0, padx=10, pady=10)

generate_button = tk.Button(root, text="Generate AI Text", command=generate_ai_text)
generate_button.grid(row=9, column=0, padx=10, pady=10)
generate_button.config(state=tk.DISABLED)  

root.mainloop()

import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
import random
import datetime
import os
import webbrowser
from bs4 import NavigableString
import sys
import tkinter as tk
from tkinter import Listbox, Entry, Button, END

# Function to run the main scraping script
def run_scraping(keywords, countries):
    base_site_url = "https://unjobs.org/duty_stations/"
    all_job_data = []

    for country in countries:
        base_url = f"{base_site_url}{country}"
        job_data = []
        page = 1

        print(f' 🔍  Collecting data from {country.upper()}...')
        while True:
            URL = f"{base_url}/{page}" if page > 1 else base_url
            response = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
            soup = BeautifulSoup(response.content, 'html.parser')

            jobs = soup.find_all('div', class_='job')
            if not jobs:
                break

            for job in jobs:
                a_tag = job.find('a', class_='jtitle')
                if a_tag:
                    title = a_tag.text.strip()
                    url = a_tag['href']
                    try:
                        duty_station, country = title.split(',')[-2:]
                        duty_station = duty_station.strip()
                        country = country.strip()
                    except ValueError:
                        duty_station = "N/A"
                        country = "N/A"

                    if a_tag.find_next('br') and a_tag.find_next('br').next_sibling:
                        next_sibling = a_tag.find_next('br').next_sibling
                        organization = next_sibling.strip() if isinstance(next_sibling, NavigableString) else "N/A"
                    else:
                        organization = "N/A"
                    job_data.append({'country': country, 'duty_station': duty_station, 'title': title, 'organization': organization, 'url': url})

            page += 1
            time.sleep(random.randint(2, 5))

        all_job_data.extend(job_data)

    priority_data = [job for job in all_job_data if any(keyword.lower() in job['title'].lower() for keyword in keywords)]
    if not priority_data:
        priority_data = [{"title": "No positions matched with the priority criteria", "url": "", "organization": "", "closing_date": "", "duty_station": "", "country": ""}]

    current_date = datetime.datetime.now().strftime("%Y%m%d")
    file_name = f"{current_date}_job_listings_multicountry_im.xlsx"
    file_path = os.path.join(os.getcwd(), file_name)

    with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
        pd.DataFrame(all_job_data).to_excel(writer, index=False, sheet_name='full_list')
        pd.DataFrame(priority_data).to_excel(writer, index=False, sheet_name='selected_list')

    print(f" ✅  Job listings for multiple countries have been successfully saved to {file_name}!")
    try:
        os.startfile(file_path)
    except AttributeError:
        webbrowser.open(file_path)

# Initialize the main application window
root = tk.Tk()
root.title("Job Scraper Settings")

# Variables for the editable lists
keywords = ['Data', 'data', 'Information', 'information', 'analysis', 'Analysis', 'Engineer', 'Developer', 'GIS', 'Geographic']
countries = ['serbia', 'hungary', 'poland']

# Function to update the list boxes
def update_listboxes(keyword_listbox, country_listbox):
    keyword_listbox.delete(0, END)
    country_listbox.delete(0, END)
    for keyword in keywords:
        keyword_listbox.insert(END, keyword)
    for country in countries:
        country_listbox.insert(END, country)

# Function to add items to lists and clear entry
def add_item(listbox, entry, list_data):
    item = entry.get()
    if item and item not in list_data:
        list_data.append(item)
        update_listboxes(keyword_listbox, country_listbox)
        entry.delete(0, END)  # Clear the entry box after adding item

# Function to remove items from lists
def remove_item(listbox, list_data):
    index = listbox.curselection()
    if index:
        list_data.pop(index[0])
        update_listboxes(keyword_listbox, country_listbox)

# UI layout
keyword_frame = tk.Frame(root)
keyword_frame.pack(side=tk.LEFT, padx=20, pady=20)
country_frame = tk.Frame(root)
country_frame.pack(side=tk.LEFT, padx=20, pady=20)

tk.Label(keyword_frame, text="Keywords").pack()
keyword_listbox = Listbox(keyword_frame)
keyword_listbox.pack()
keyword_entry = Entry(keyword_frame)
keyword_entry.pack()
tk.Button(keyword_frame, text="Add Keyword", command=lambda: add_item(keyword_listbox, keyword_entry, keywords)).pack()
tk.Button(keyword_frame, text="Remove Keyword", command=lambda: remove_item(keyword_listbox, keywords)).pack()

tk.Label(country_frame, text="Countries").pack()
country_listbox = Listbox(country_frame)
country_listbox.pack()
country_entry = Entry(country_frame)
country_entry.pack()
tk.Button(country_frame, text="Add Country", command=lambda: add_item(country_listbox, country_entry, countries)).pack()
tk.Button(country_frame, text="Remove Country", command=lambda: remove_item(country_listbox, countries)).pack()

tk.Button(root, text="Start Scraping", command=lambda: run_scraping(keywords, countries)).pack(pady=20)

update_listboxes(keyword_listbox, country_listbox)

root.mainloop()
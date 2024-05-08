# HumanitarianJobs-Extractor-Plus
HumanitarianJobs-Extractor-Plus is an advanced Python script tailored for job-seekers in the humanitarian sector. This project is the enhanced version of the earlier scraping tool, [UNJobs-Selective-Extractor](https://github.com/Op27/UNJobs-Selective-Extractor), and offers more refined capabilities for automated job scraping from international humanitarian job boards.

## Key Features
- **Automated Job Scraping**: Automatically extracts job listings from multiple humanitarian job boards using a dynamic URL parsing method based on selected countries.
- **Keyword Filtering**: Filters job listings by user-defined keywords to ensure the results are highly relevant to the searcher’s interests.
- **Multi-Country Searches**: Supports scraping from multiple countries simultaneously, enhancing the script's utility for users looking for global opportunities.
- **Excel Output**: Organizes scraped data into an Excel spreadsheet with two sheets: one for all listings and another for listings that match priority keywords.
- **Customizable Parameters**: Users can easily add or remove keywords and countries through a simple graphical user interface, making the script flexible and user-friendly.

These features are designed to make the job search process more efficient and tailored, especially for professionals in the humanitarian sector.


## Installation

### Prerequisites
- Git (for cloning the repository)
- Python 3.x
- pip (Python package installer)

### Cloning the Repository
To clone the repository and access the script, run the following command in your terminal:
   ```bash
   git clone https://github.com/Op27/HumanitarianJobs-Extractor-Plus.git
  cd HumanitarianJobs-Extractor-Plus
   ```

### Dependencies
Install the necessary Python packages using pip:
   ```bash
   pip install requests beautifulsoup4 pandas openpyxl
   ```

## Usage
### Setting Up Your Keywords and Countries
To customize the job scraper to better match your job search criteria, you can modify the default `keywords` and `countries` lists in the script. 

Here is how you can edit these default lists in the `job_scraper.py` script:
   ```python
   # Variables for the editable lists
    keywords = ['Data', 'data', 'Information', 'information', 'analysis', 'Analysis', 'Engineer', 'Developer', 'GIS', 'Geographic']
    countries = ['serbia', 'hungary', 'poland']
   ```

### Running the Script
To run the script, use the following command in your terminal:
   ```bash
   python job_scraper.py
   ```

### User Interface
The script includes a simple GUI built with Tkinter, allowing users to add or remove keywords and countries interactively before starting the scraping process.

<img width="344" alt="UI" src="https://github.com/Op27/HumanitarianJobs-Extractor-Plus/assets/39921621/5b61f3cc-02b4-4606-a81d-9798fc3b6808">

## Features
- Scrapes job listings from specified URLs based on country and keyword filters.
- Outputs the results in an Excel file, categorizing them into full and selected listings based on priority keywords.
- Provides a GUI for dynamic interaction with the user to customize the scraping process.

## Contributing
Contributions to the HumanitarianJobs-Extractor-Plus are welcome! Please fork the repository and submit a pull request with your proposed changes.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.

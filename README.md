
# CulinaryPress: Mealie Recipe PDF Generator

## Introduction
CulinaryPress: Mealie Recipe PDF Generator is a sophisticated, Python-based tool designed for culinary professionals, food bloggers, and cooking enthusiasts. It simplifies the process of managing recipes by seamlessly fetching them from the Mealie recipe management system and converting them into elegantly formatted PDF documents. This tool is ideal for those looking to efficiently organize, share, and print their treasured recipes.

## Features
- **Seamless API Integration**: Fetches recipes directly from the Mealie API, ensuring real-time access to your recipe collection.
- **Elegant PDF Conversion**: Transforms recipes into professionally formatted PDF files, perfect for printing or digital distribution.
- **Customizable Styling**: Employs a CSS file to provide attractive and reader-friendly formatting, adaptable to personal preferences.

## Requirements
- Python 3.x
- Requests library
- pdfkit library
- Access to Mealie API with a valid token.

## Installation
1. Clone the repository.
2. Install the required Python packages: `requests` and `pdfkit`.
3. Ensure wkhtmltopdf is installed on your system (required by pdfkit).


## Configuration
Create a `config.ini` file in the project root with the following structure:
------------------------------------------
[Mealie]
api_url = http://YOUR_MEALIE_HOST_ADDRESS:9925/api
api_token = YOUR_MEALIE_API_TOKEN

[Paths]
OutputDirectory = C:\WHERE_EVER_YOU_ARE_RUNNING_THIS_FROM\WHAT_EVER_OUTPUT_FOLDER_NAME_YOU_LIKE
-------------------------------------------
- **Mealie Section**: Contains the URL and token for Mealie API access.
- **Paths Section**: Define the output directory for the generated PDF recipes.

Note: Update the `OutputDirectory` path to match your desired location for saving the PDF files.
Update the `config.ini` file in the project root, to add your Mealie API URL and access token.

## Usage
1. **Fetching Recipes**:
   - Execute `Mealie-API-Recipe-Pull.py` to retrieve recipes from Mealie.
   - Recipes are stored in `recipes.json`.

2. **Converting to PDF**:
   - Run `recipe_to_pdf.py` to convert the JSON recipe data into PDF.
   - This script formats each recipe using `template.html` and `style.css`.

## Project Structure
- `Mealie-API-Recipe-Pull.py`: Script for pulling recipes from Mealie's API.
- `recipe_to_pdf.py`: Script for converting recipes into PDF format.
- `recipes.json`: A sample JSON file containing recipe data.
- `style.css`: CSS file for styling the PDF outputs.
- `template.html`: HTML template used in PDF generation.
- `recipe_to_pdf_log.log`: Logging file for tracking the conversion process (if enabled).

## Contributions
We highly encourage contributions! Feel free to submit pull requests or open issues for any enhancements, feature requests, or bug fixes.

## License
Whatever, if ya like it buy me a coffee. Enjoy, use how you would like.

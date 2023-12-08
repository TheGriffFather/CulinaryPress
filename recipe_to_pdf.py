import json
import pdfkit
import os
import logging
import configparser
import traceback

# Configure logging
logging.basicConfig(filename='recipe_to_pdf_log.log', level=logging.ERROR, format='%(asctime)s:%(levelname)s:%(message)s')

# Function to generate HTML content from a recipe dictionary
def generate_html(recipe):
    with open('template.html', 'r') as file:
        template = file.read()

    # Ingredient handling
    ingredients_list = []
    for ingredient in recipe["recipeIngredient"]:
        if isinstance(ingredient, str):
            ingredients_list.append('<li>' + ingredient + '</li>')
        elif isinstance(ingredient, dict) and 'note' in ingredient:
            ingredients_list.append('<li>' + ingredient['note'] + '</li>')
        else:
            ingredients_list.append('<li>Unknown ingredient format</li>')

    ingredients = '<ul>' + ''.join(ingredients_list) + '</ul>'

    # Instruction handling
    instructions_list = []
    if isinstance(recipe["recipeInstructions"], list):
        for step in recipe["recipeInstructions"]:
            if isinstance(step, dict) and 'text' in step:
                instructions_list.append('<p>' + step['text'] + '</p>')
            else:
                instructions_list.append('<p>Unknown instruction format</p>')
    else:
        instructions_list.append('<p>Invalid instructions format</p>')

    instructions = ''.join(instructions_list)

    # Replace placeholders in the template
    html_content = template.replace("{{ title }}", recipe["name"])
    html_content = html_content.replace("{{ ingredients }}", ingredients)
    html_content = html_content.replace("{{ instructions }}", instructions)

    return html_content

# Main function to load recipes and generate PDFs
def main():
    config = configparser.ConfigParser()
    config.read('config.ini')

    output_directory = config['Paths']['OutputDirectory']

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    options = {
        'no-images': '',
        'custom-header': [
            ('Accept-Encoding', 'gzip')
        ]
    }

    with open('recipes.json', 'r') as file:
        recipes = json.load(file)

    for recipe in recipes:
        try:
            html_content = generate_html(recipe)
            pdf_filename = f'{recipe["name"]}.pdf'
            pdf_filename = ''.join(x for x in pdf_filename if x.isalnum() or x in "._- ")
            pdf_path = os.path.join(output_directory, pdf_filename)
            pdfkit.from_string(html_content, pdf_path, options=options)
            logging.info(f'Successfully created PDF for: {recipe["name"]}')
        except Exception as e:
            logging.error(f'Error generating PDF for {recipe["name"]}: {e}')

if __name__ == "__main__":
    main()
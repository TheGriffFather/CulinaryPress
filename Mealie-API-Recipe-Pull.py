import json
import requests
import configparser

def fetch_recipes_from_mealie(api_url, api_token):
    headers = {
        'Authorization': f'Bearer {api_token}',
        'Content-Type': 'application/json'
    }
    response = requests.get(f'{api_url}/recipes/summary', headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Error fetching recipe summaries: {response.status_code}')
        return []

def fetch_recipe_details(api_url, api_token, recipe_slug):
    headers = {
        'Authorization': f'Bearer {api_token}',
        'Content-Type': 'application/json'
    }
    response = requests.get(f'{api_url}/recipes/{recipe_slug}', headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Error fetching recipe details for {recipe_slug}: {response.status_code}')
        return None

def clean_recipe_data(recipe_data):
    if isinstance(recipe_data, dict):
        return {k: clean_recipe_data(v) for k, v in recipe_data.items() if v is not None and (k != 'title' or v)}
    elif isinstance(recipe_data, list):
        return [clean_recipe_data(item) for item in recipe_data if item is not None]
    else:
        return recipe_data

def main():
    config = configparser.ConfigParser()
    config.read('config.ini')

    api_url = config['Mealie']['api_url']
    token = config['Mealie']['api_token']

    recipe_summaries = fetch_recipes_from_mealie(api_url, token)
    if recipe_summaries:
        print(f'Fetched {len(recipe_summaries)} recipe summaries')

        detailed_recipes = []
        for summary in recipe_summaries:
            recipe_details = fetch_recipe_details(api_url, token, summary['slug'])
            if recipe_details:
                cleaned_data = clean_recipe_data(recipe_details)
                detailed_recipes.append(cleaned_data)

        print(f'Fetched details for {len(detailed_recipes)} recipes')

        with open('recipes.json', 'w') as file:
            json.dump(detailed_recipes, file, indent=4)

        print('Recipes saved to recipes.json')
    else:
        print('No recipes found or error in fetching recipes')

if __name__ == '__main__':
    main()

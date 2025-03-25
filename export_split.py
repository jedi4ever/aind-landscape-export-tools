from utils.landscape_helper import domains_from_csv, categories_from_csv, tools_from_csv, all_tools
from utils.string_helpers import clean_name
import yaml
import os

REPO_PATH = "data/repo/data/landscape"

def main():
    # create the repo path
    os.makedirs(REPO_PATH, exist_ok=True)

    input_file = "data/csv/AI Native Dev Tool Catalog - Internal - Domains.csv"
    domains = domains_from_csv(input_file)

    input_file = "data/csv/AI Native Dev Tool Catalog - Internal - Categories.csv"
    categories = categories_from_csv(input_file)

    input_file = "data/csv/AI Native Dev Tool Catalog - Internal - Tools.csv"
    tools = tools_from_csv(input_file)

    landscape = all_tools(domains, categories, tools)

    domains = landscape["domains"]
    # split the tools into 3 files
    for domain in domains:
        # clean the domain name
        domain_name = clean_name(domain["name"])
        # remove categories key from the domain
        categories = domain["categories"]
        del domain["categories"]

        # create the domain folder
        domain_folder = f"{REPO_PATH}/{domain_name}"
        os.makedirs(domain_folder, exist_ok=True)

        # create the domain file
        domain_file = f"{REPO_PATH}/{domain_name}.yaml"
        with open(domain_file, 'w', encoding='utf-8') as file:
            file.write(yaml.dump(domain))

        for category in categories:
            category_name = clean_name(category["name"])
            # remove tools key from the category
            tools = category["tools"]
            del category["tools"]

            # create the category folder
            category_folder = f"{REPO_PATH}/{domain_name}/{category_name}"
            os.makedirs(category_folder, exist_ok=True)

            # create the category file
            category_file = f"{REPO_PATH}/{domain_name}/{category_name}.yaml"
            with open(category_file, 'w', encoding='utf-8') as file:
                file.write(yaml.dump(category))
            
            for tool in tools:
                tool_name = clean_name(tool["name"])

                # create the tool file
                tool_file = f"{REPO_PATH}/{domain_name}/{category_name}/{tool_name}.yaml"
                with open(tool_file, 'w', encoding='utf-8') as file:
                    file.write(yaml.dump(tool))

if __name__ == "__main__":
    main()

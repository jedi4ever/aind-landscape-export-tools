from utils.landscape_helper import all_tools, domains_from_csv, categories_from_csv, tools_from_csv
import json
    
def main():
    input_file = "data/csv/AI Native Dev Tool Catalog - Internal - Domains.csv"
    domains = domains_from_csv(input_file)

    input_file = "data/csv/AI Native Dev Tool Catalog - Internal - Categories.csv"
    categories = categories_from_csv(input_file)

    input_file = "data/csv/AI Native Dev Tool Catalog - Internal - Tools.csv"
    tools = tools_from_csv(input_file)

    yaml_file = all_tools(domains, categories, tools)

    json_file = json.dumps(yaml_file)

    print(json_file)

if __name__ == "__main__":
    main()

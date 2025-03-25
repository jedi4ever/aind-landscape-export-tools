import csv

DOMAIN_ORDER_FIELD = "Domain Order"
DOMAIN_NAME_FIELD = "Domain Name"
DOMAIN_DESCRIPTION_FIELD = "Domain Description"
CATEGORY_ORDER_FIELD = "Category Order"
CATEGORY_NAME_FIELD = "Category Name"
CATEGORY_DESCRIPTION_FIELD = "Category Description"

TOOL_DOMAIN_FIELD = "Domain"
TOOL_CATEGORY_FIELD = "Category"
TOOL_NAME_FIELD = "Tool Name"
TOOL_DESCRIPTION_FIELD = "Tool Description"
TOOL_ORDER_FIELD = "Tool Order"
TOOL_WEBSITE_URL_FIELD = "Tool Website URL"
TOOL_ICON_URL_FIELD = "Tool Icon URL"
TOOL_VERIFIED_FIELD = "Verified"
TOOL_OSS_FIELD = "OSS"
TOOL_OSS_REPO_URL = "OSS Repo URL"
TOOL_BETA_FIELD = "Beta"
TOOL_SOCIAL_MEDIA_FIELD = "Tool Socials"
TOOL_DATE_ADDED_FIELD = "Date Added"
TOOL_COMPANY_NAME_FIELD = "Company Name"
TOOL_COMPANY_DESCRIPTION_FIELD = "Company Description"
TOOL_KEYWORDS_FIELD = "Tool Keywords"


def domains_from_csv(csv_file):
    with open(csv_file, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        domains = list(csv_reader)  
        return domains
    
def categories_from_csv(csv_file):
    with open(csv_file, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        categories = list(csv_reader)  
        return categories

def tools_from_csv(csv_file):

    # Read CSV file
    with open(csv_file, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        tools = list(csv_reader)  
        return tools



def all_tools(domains, categories, tools):
    # sort domains by order
    sorted_domains = sorted(domains, key=lambda x: x[DOMAIN_ORDER_FIELD])
    #print(sorted_domains)

    # sort categories by order
    sorted_categories = sorted(categories, key=lambda x: x[CATEGORY_ORDER_FIELD])
    #print(sorted_categories)

    # for each domain
    yaml_file = {}
    yaml_file["domains"] = []

    for domain in sorted_domains:
        #print("*",domain)
        yaml_domain = {}
        yaml_domain["name"] = domain[DOMAIN_NAME_FIELD]
        yaml_domain["description"] = domain[DOMAIN_DESCRIPTION_FIELD]
        yaml_domain["level"] = int(domain[DOMAIN_ORDER_FIELD])
        yaml_domain["categories"] = []

        # find all categories for the domain
        categories = categories_for_domain(domain, sorted_categories)

        for category in categories:
            yaml_category = {}
            yaml_category["name"] = category[CATEGORY_NAME_FIELD]
            yaml_category["description"] = category[CATEGORY_DESCRIPTION_FIELD]
            yaml_category["level"] = int(category[CATEGORY_ORDER_FIELD])
            yaml_category["tools"] = []

            #print("**",category)
            category_tools = tools_for_domain_and_category(domain, category, tools)

            # sort by name
            sorted_category_tools = sorted(category_tools, key=lambda x: x[TOOL_NAME_FIELD])

            for tool in sorted_category_tools:
                #print("***",tool[TOOL_NAME_FIELD])
                yaml_tool = {}
                yaml_tool["name"] = tool[TOOL_NAME_FIELD]
                yaml_tool["description"] = tool[TOOL_DESCRIPTION_FIELD]
                yaml_tool["website_url"] = tool[TOOL_WEBSITE_URL_FIELD]
                yaml_tool["icon_url"] = tool[TOOL_ICON_URL_FIELD]

                yaml_tool["tags"] = []

                # if the tool is verified, set the verified field to true
                if (tool[TOOL_VERIFIED_FIELD] is not None and tool[TOOL_VERIFIED_FIELD] != ""):
                    yaml_tool["tags"].append("verified")
                    yaml_tool["verified"] = True
                else:
                    yaml_tool["verified"] = False

                # check oss field
                if (tool[TOOL_OSS_FIELD] is not None and tool[TOOL_OSS_FIELD] != ""):
                    yaml_tool["tags"].append("oss")
                    yaml_tool["oss"] = True
                else:
                    yaml_tool["oss"] = False


                if (tool[TOOL_BETA_FIELD] is not None and tool[TOOL_BETA_FIELD] != ""):
                    yaml_tool["tags"].append("beta")
                else:
                    yaml_tool["tags"].append("GA")

                yaml_tool["tags"].append(category[CATEGORY_NAME_FIELD])
                yaml_tool["tags"].append(domain[DOMAIN_NAME_FIELD])

                # check social media fields
                if (tool[TOOL_SOCIAL_MEDIA_FIELD] is not None and tool[TOOL_SOCIAL_MEDIA_FIELD] != ""):
                    # split by new line
                    social_urls = tool[TOOL_SOCIAL_MEDIA_FIELD].split("\n")
                    yaml_tool["social_urls"] = []
                    for social_url in social_urls:
                        social_url = social_url.strip()
                        if social_url.startswith("https://"):
                            yaml_tool["social_urls"].append(social_url)

                if (tool[TOOL_DATE_ADDED_FIELD] is not None and tool[TOOL_DATE_ADDED_FIELD] != ""):
                    yaml_tool["date_added"] = tool[TOOL_DATE_ADDED_FIELD]



                if (tool[TOOL_KEYWORDS_FIELD] is not None and tool[TOOL_KEYWORDS_FIELD] != ""):
                    yaml_tool["keywords"] = []
                    keywords = tool[TOOL_KEYWORDS_FIELD].split(",")
                    for keyword in keywords:
                        keyword = keyword.strip()
                        yaml_tool["keywords"].append(keyword)

                # company name
                # company website url
                # company logo url
                #yaml_tool["company"] = {}
                #yaml_tool["company"]["name"] = tool[TOOL_COMPANY_NAME_FIELD]
                #yaml_tool["company"]["description"] = tool[TOOL_COMPANY_DESCRIPTION_FIELD]

                yaml_category["tools"].append(yaml_tool)

            yaml_domain["categories"].append(yaml_category)

        yaml_file["domains"].append(yaml_domain)

    return yaml_file

def categories_for_domain(domain, categories):
    domain_categories = []
    for category in categories:
        domain_prefix = domain[DOMAIN_NAME_FIELD]+"-"
        if category[CATEGORY_NAME_FIELD].startswith(domain_prefix):
            category_name = category[CATEGORY_NAME_FIELD][len(domain_prefix):]
            category[CATEGORY_NAME_FIELD] = category_name

            domain_categories.append(category)
    return domain_categories

def tools_for_domain_and_category(domain, category, tools):
    domain_tools = []
    for tool in tools:
        if tool[TOOL_DOMAIN_FIELD] == domain[DOMAIN_NAME_FIELD] and tool[TOOL_CATEGORY_FIELD] == category[CATEGORY_NAME_FIELD]:
            domain_tools.append(tool)
    return domain_tools


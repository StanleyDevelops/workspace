# my way

raw_input = "status=active&role=admin&verified=true"

def parse_query_string(raw_string: str):
    parsed_data = raw_string.split("&")

    filtered_data = []
    for item in parsed_data:
        filtered_data.append(item.split("="))

    filtered_dict = {}
    for item in filtered_data:
        for key in item:       # irrelevant introduction of key
            filtered_dict[item[0]] = item[1]

    return filtered_dict

print(parse_query_string(raw_input))   # the logic works fine

#pythonic way

def parse_query_string(raw_string: str):
    filtered_dict = {}
        
    # Step 1: Break into ['status=active', 'role=admin', 'verified=true']
    pairs = raw_string.split("&")

    # Step 2: Loop through each pair
    for pair in pairs:
        # Python Magic: Split by '=' and instantly assign to key and value!
        key, value = pair.split("=") 
        filtered_dict[key] = value
        
    return filtered_dict

print(parse_query_string(raw_input))

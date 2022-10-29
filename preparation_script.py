with open("C:/Users/muria/Downloads/data_prep_clean.csv", "rb") as f: #f steht für file
    lines = f.readlines()

results = []
current_object = {"message_type":"","message":""}

for line in lines:
    line = line.strip().decode("UTF-8")

    message_type = line[:line.index(",")].strip()
    message_text = line[line.index(",")+1:].strip('"').strip()

    if current_object["message_type"] != message_type:

        results.append(current_object)
        current_object = {"message_type":"","message":""}

    current_object["message_type"] = message_type
    
    if current_object["message"] == "":
        current_object["message"] = message_text
    else:
        current_object["message"] += " " + message_text

results.append(current_object)

result_string = ""
for result in results:
    
    if result["message_type"] in ["completion","prompt"]:

        result_string += '"' + result["message_type"] + '"' + "," + '"' + result["message"].replace('"','\"') + '"' + "\n"
    
print(result_string)



with open("C:/Users/muria/Downloads/data_prep_clean_af.csv", "wb") as f:
    f.write(result_string.encode("UTF-8"))
    

    
    
    
    






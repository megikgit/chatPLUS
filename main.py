# Importing tools
import pywebio
import json

# Database link
name = "database.json"

# Host params (local by wifi)
host = "0.0.0.0"
port = 7777



def site():
    # Setup
    database = json.load(open(name, "rt", encoding = "utf-8"))
    msgs = database["msg"]
    main_text = ""
    for mssg in msgs:
        main_text += f"{mssg[0]}: {mssg[1]}\n"


    # Messages    
    username = pywebio.input.input(label= "Enter username: ", placeholder= "Sigma_boi1488")
    input_area = pywebio.input.input(placeholder="Enter message Example: \"Hello\"", label="Message area")
    text_msg = pywebio.output.put_text(main_text, position = pywebio.output.OutputPosition.TOP)
    
    # Instructions
    instruction = pywebio.output.put_text("Enter username and message and refresh the page.", position = pywebio.output.OutputPosition.BOTTOM)
    instruction_2 = pywebio.output.put_text("If you want to not send nothing just skip all, it will save nothing.", position = pywebio.output.OutputPosition.BOTTOM)
    
    # Skip algorhytm
    if username == "" and input_area == "":
        pass
    else:
        msgs.append([f"{username}", f"{input_area}"])
    
    # Saving messages
    database["msg"] = msgs
    
    json.dump(database, open(name, "wt", encoding="utf-8"), indent=8)

# Starting   
pywebio.start_server(site, port, host)
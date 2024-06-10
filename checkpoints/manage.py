FILE = "./machine/checkpoints/DIRECTORY"

def check(entry):
    with open(FILE, "r") as f:
        record = f.readlines()
    if entry in record:
        return True
    return False

def build(parameters):
    string = "(_)"
    series = " | ".join(parameters)
    string = string.replace("_", series).replace("( ", "(").replace(" )", ")")
    return string 

def register(unique_identifier, current_location, primary_location, public_address, private_address, description, seeds):
    entry = build([unique_identifier, current_location, primary_location, public_address, private_address, description, seeds])
    if check(entry) is not True:
        with open(FILE, "a") as g:
            g.write(entry)
            g.write("\n")
    return check(entry)

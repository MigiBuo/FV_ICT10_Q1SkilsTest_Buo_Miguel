from pyscript import display, document

def Restate(e):
    name = document.getElementById("name").value
    address = document.getElementById("address").value
    contactinfo = document.getElementById("contactinfo").value
    food1 = float(document.getElementById("patatas").value) if document.getElementById("patatas").checked else 0 
    food2 = float(document.getElementById("potatos").value) if document.getElementById("potatos").checked else 0 
    food3 = float(document.getElementById("patotas").value) if document.getElementById("patotas").checked else 0 

    total = (food1 + food2 + food3)

    msg1 = f"Order for: {name}"
    msg2 = f"Address: {address}" 
    msg3 = f"Contact number: {contactinfo}" 
    msg4 = f"Total: ₱ {total}" # Google AI

    display(msg1, target="appear1", append=False)
    display(msg2, target="appear2", append=False)
    display(msg3, target="appear3", append=False)
    display(msg4, target="appear4", append=False)
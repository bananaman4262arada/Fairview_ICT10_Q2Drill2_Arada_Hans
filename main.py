from pyscript import document

def checkNum(e):
    document.getElementById("output1").innerHTML = ""
    num_bers= ["maia fabro", "erin mandapat", "erin mundo", "erin sakda", "erin murda"]

    num1= document.getElementById("num1").value
    num2= document.getElementById("num2").value
    name= num1 + " " + num2
    num3= num1.lower()
    num4= num2.lower()
    Labid = num3 + " " + num4

    confirm_num = Labid in num_bers

    message = (f'Sorry {name}, youre not part of the club', f'Congrats {name}, youre part of the club.')

    document.getElementById("output1").innerHTML = message[confirm_num]
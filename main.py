from pyscript import document

def checkNum(e):
    document.getElementById("output1").innerHTML = ""
    Grade_7= {"John Sahur", "Mon Seiur", "Entrepreneur Duer", "Air Shakur"}
    Grade_8= {"Silver Stein", "Murder Klein", "Epstein Silvine", "Boy Moder"}
    Grade_9= {"Hont Ton", "Won Ton", "Noodle Moodle", "Rooble Shooble"}
    Grade_10= {"Swinging Thinging", "Minging Ringing", "Slipping Silking", "Flicking Midding"}

    num1= document.getElementById("num1").value
    num2= document.getElementById("num2").value
    name= num1 + " " + num2
    num3= num1.lower()
    num4= num2.lower()
    Labid = num3 + " " + num4

    confirm_num = Labid in num_bers

    message = (f'Sorry {name}, youre not part of the club', f'Congrats {name}, youre part of the club.')

    document.getElementById("output1").innerHTML = message[confirm_num]
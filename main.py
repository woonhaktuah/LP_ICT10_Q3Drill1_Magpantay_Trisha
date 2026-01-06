from pyscript import document

def compute_average(event) :
    #Get the input values and convert to float
    score1 = float(document.getElementById("score1").value)  
    score2 = float(document.getElementById("score2").value) 

    #Compute Average
    average = (score1 + score2) / 2

    #Determine if Pass/Fail
    if average >= 75 :
        result = "Yes"
    else:
        result = "No"

    #Display results
    document.getElementById("average").innerText = str(round(average,2))
    document.getElementById("result").innerText = result
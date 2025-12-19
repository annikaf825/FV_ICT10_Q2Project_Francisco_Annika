from pyscript import document, display

def general_weighted_average(e):

    # get students Name
    First_name = document.getElementById("First_name").value
    Last_name = document.getElementById("Last_name").value

    # Get Grades
    Math = float(document.getElementById("Math").value)
    ICT = float(document.getElementById("ICT").value)
    PE = float(document.getElementById("PE").value)
    Science = float(document.getElementById("Science").value)
    English = float(document.getElementById("English").value)
    Filipino = float(document.getElementById("Filipino").value)

    # Subject labels
    subjects = ["Science", "Math", "English", "Filipino", "ICT", "PE"]
          #        0         1         2           3       4      5
    # Calculation
    weighted_sum = (Math * 5 + Science * 5 + English * 5 +
                    Filipino * 3 + ICT * 2 + PE * 1)

    total_units = 21  
    gwa = weighted_sum / total_units

    # Summary 
    summary_text = f"""
    {subjects[0]}: {Science:.0f}
    {subjects[1]}: {Math:.0f}
    {subjects[2]}: {English:.0f}
    {subjects[3]}: {Filipino:.0f}
    {subjects[4]}: {ICT:.0f}
    {subjects[5]}: {PE:.0f}
    """

    display(f"Name: {First_name} {Last_name}", target="output1")
    display(summary_text, target="output1")
    display(f"GWA: {gwa:.2f}", target="output1")

    # Pass or Fail Message
    if gwa >= 75:
        message = f"Average: {gwa:.2f} — You Passed!! 🥳"
    else:
        message = f"Average: {gwa:.2f} — You Failed!! 💔"

    display(message, target="output1")


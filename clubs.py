from pyscript import document

# Dictionary
clubs = {
    "Science Club": {
        "Description": "Conducts experiments and science activities",
        "Meeting Time": "Tuesday 03:00 - 04:00 PM",
        "Location": "Room 404",
        "Advisor": "Ms. Jameelyn Maramag",
        "Members": 15,
        "Category": "Academic"
    },

    "Math Club": {
        "Description": "Improves math and problem-solving skills",
        "Meeting Time": "Monday 02:30 - 03:00 PM",
        "Location": "Room 404",
        "Advisor": "Mr. Nicole Gabuya",
        "Members": 20,
        "Category": "Academic"
    },

    "Dance Club": {
        "Description": "Focuses on dance performances",
        "Meeting Time": "Tuesday 03:00 - 05:00 PM",
        "Location": "Teatro Preciosa",
        "Advisor": "Mr. Alfred Cases",
        "Members": 24,
        "Category": "Non-Academic"
    },

    "Marching Band": {
        "Description": "Performs music during school events",
        "Meeting Time": "Tuesday & Wednesday 03:00 - 04:30 PM",
        "Location": "Band Room",
        "Advisor": "Mr. Emilio Alumno",
        "Members": 30,
        "Category": "Non-Academic"
    },

    "Glee Club": {
        "Description": "Focuses on singing and vocal performances",
        "Meeting Time": "Monday 03:00 - 05:00 PM",
        "Location": "High School Music Room",
        "Advisor": "Mr. Denver Martin",
        "Members": 22,
        "Category": "Non-Academic"
    },

    "Communications Arts Club": {
        "Description": "Develops communication and media skills",
        "Meeting Time": "Wednesday & Friday 03:00 - 04:00 PM",
        "Location": "Room 406",
        "Advisor": "Ms. Yannis Fernandez",
        "Members": 18,
        "Category": "Academic"
    },

    "COCC": {
        "Description": "Leadership and military training program",
        "Meeting Time": "Wednesday 02:30 - 04:30 PM",
        "Location": "Quadrangle / Teatro Preciosa",
        "Advisor": "SSgt. Jemima David PA (Res)",
        "Members": 35,
        "Category": "Non-Academic"
    },

    "Social Science Club": {
        "Description": "Talk about society, culture, and history",
        "Meeting Time": "Tuesday 03:00 - 04:00 PM",
        "Location": "Room 409",
        "Advisor": "Mr. Roberto Lim",
        "Members": 19,
        "Category": "Academic"
    },

    "Volleyball Varsity": {
        "Description": "Competitive volleyball team",
        "Meeting Time": "Wednesday 03:00 - 04:00 PM",
        "Location": "Quadrangle",
        "Advisor": "Mr. Adrian Ruiz",
        "Members": 12,
        "Category": "Sports"
    },

    "Basketball Varsity": {
        "Description": "Competitive basketball team",
        "Meeting Time": "Monday 03:00 - 04:00 PM",
        "Location": "Quadrangle",
        "Advisor": "Mr. Adrian Ruiz",
        "Members": 12,
        "Category": "Sports"
}}

# Function display club info
def show_club_info(event):
    selected_club = document.getElementById("club_select").value

    if selected_club == "":
        document.getElementById("club_output").innerHTML = "Please select a club."
        return

    club = clubs[selected_club]

    output = (
        f"Club Name: {selected_club}\n"
        f"Description: {club['Description']}\n"
        f"Meeting Time: {club['Meeting Time']}\n"
        f"Location: {club['Location']}\n"
        f"Advisor: {club['Advisor']}\n"
        f"Number of Members: {club['Members']}\n"
        f"Category: {club['Category']}"
    )

    document.getElementById("club_output").innerHTML = f"<pre>{output}</pre>"
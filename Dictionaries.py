# Dictionaries :

monthConversion = {
    "Jan": "January",   # insted of "Jan" we can use numbers as well
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "Julay",
    "Aug": "August",
    "Sep": "September",
    "Oct": "Octomber",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversion["Apr"])
print(monthConversion.get("Dec"))
print(monthConversion.get("Luv","not valid key"))    # we can get default value like this
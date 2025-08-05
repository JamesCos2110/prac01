def say_hello(name):
    salutation = "Hello, " + name
    print(salutation)

say_hello("VS Code") # This is a simple Python function to greet the user
# It takes a name as an argument and prints a greeting message to the console 

def say_day_of_week(date):
    """
    Prints the day of the week for the given date.

    Parameters:
    date (datetime.date or datetime.datetime): The date for which to print the day of the week.
    """
    import datetime
    day_of_week = date.strftime("%A")
    print(f"Today is {day_of_week}")    
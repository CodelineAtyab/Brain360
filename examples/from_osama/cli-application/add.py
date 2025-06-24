import feedbackdatabase
def add(inputted_value):
    feedbackdatabase.database.append(inputted_value)
    return add(inputted_value)
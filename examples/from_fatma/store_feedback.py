import file_creation

_feedback = file_creation.load_feedback()

def get_all_feedback():
    return _feedback

def add_feedback(entry):
    _feedback.append(entry)
    file_creation.save_feedback(_feedback)

def update_feedback(index, new_entry):
    if 0 <= index < len(_feedback):
        _feedback[index] = new_entry
        file_creation.save_feedback(_feedback)
        return True
    return False

def delete_feedback(index):
    if 0 <= index < len(_feedback):
        del _feedback[index]
        file_creation.save_feedback(_feedback)
        return True
    return False
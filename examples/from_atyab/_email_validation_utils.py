import re

print(__name__)

def is_email_valid(email_string):
  """
  Validate the given email to make sure the format is correct
  Examples:
      syed.atyab.hussain@gmail.com
      saraalabaddi@gmai.com
  Args:
      email_string (str): Given email as a string
  Returns:
      bool: True if the format is correct and False otherwise
  """
  match_success = re.match("^[a-z|A-Z|0-9|.]+@[a-z|A-Z]{2,}+[.][a-z|A-Z]+$", email_string)
  return (True if match_success else False)


if __name__ == "__main__":
  # Unit Tests
  print(is_email_valid("syed.atyab.hussain@gmail.com"))
  print(is_email_valid("saraalabaddi@gmai.com"))
  print(is_email_valid("@gmai.com"))
  print(is_email_valid("saraalabaddi"))
  print(is_email_valid(""))
  print(is_email_valid("syed.atyab.hussain@g.com"))
  print(is_email_valid("syed.atyab.hussain@g."))
  print(is_email_valid("syed.atyab.hussain@gcom"))
  print(is_email_valid("syedatyabhussain@gmail.com"))
  print(is_email_valid("syedatyab@hussain@gmail.com"))
  print(is_email_valid("sy@edatyab@hussain@gmail.com"))
  print(is_email_valid("syed atyab hussain@gmail.com"))
  print(is_email_valid("syed-atyab-hussain@gmail.com"))
  print(is_email_valid("syed!atyab!hussain@gmail.com"))
  print(is_email_valid("syed#atyab#hussain@gmail.com"))
  print(is_email_valid("syed(atyab)hussain@gmail.com"))
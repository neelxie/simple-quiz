class Credit_card:
  def __init__(self, card_number, expiration_date, security_code):
    self.card_number = card_number
    self.expiration_date = expiration_date
    self.security_code = security_code

  def __repr__(self):
    return f"Card number: {self.card_number}"

  def print_details(self, account):
    print(f"Card number: {self.card_number} \nExpiration Date: {self.expiration_date} \nSecurity Code: {self.security_code}")

my_credit_card = Credit_card(1234566, "27/3", 234)
my_credit_card.print_details()

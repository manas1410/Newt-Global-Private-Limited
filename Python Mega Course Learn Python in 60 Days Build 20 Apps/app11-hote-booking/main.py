import pandas as pd

df = pd.read_csv(r"C:\Users\mm\Arsac_Python_Mega_learn\Python\App 11-Hotel Booking App\data\hotels.csv",
                 dtype={"id": str})

df_cards = pd.read_csv(r"C:\Users\mm\Arsac_Python_Mega_learn\Python\App 11-Hotel Booking App\data\cards.csv",
                       dtype=str).to_dict(
    orient="records")
df_card_security = pd.read_csv(
    r"C:\Users\mm\Arsac_Python_Mega_learn\Python\App 11-Hotel Booking App\data\card_security.csv", dtype=str)


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv(r"C:\Users\mm\Arsac_Python_Mega_learn\Python\App 11-Hotel Booking App\data\hotels.csv", index=False)

    def available(self):
        """Check the availability of the hotel with hotel_id"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation !!
        Name  : {self.customer_name},
        Hotel : {self.hotel.name}
 """
        return content


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, cvc, holder):
        card_data = {"number": self.number, "expiration": expiration,
                     "cvc": cvc, "holder": holder}
        if card_data in df_cards:
            return True
        else:
            return False


class SecureCreditCard(CreditCard):
    def authenticate(self, given_password):
        password = df_card_security.loc[df_card_security["number"] == self.number, "password"].squeeze()
        if given_password == password:
            return True
        else:
            return False


print(df.head(5))
hotel_id = input("Enter the id of the Hotel : ")
hotel = Hotel(hotel_id)

if hotel.available():
    credit_card = SecureCreditCard(number="1234")
    if credit_card.validate(expiration="12/26", cvc="123", holder="JOHN SMITH"):
        if credit_card.authenticate(given_password="mypass"):
            hotel.book()
            customer_name = input("Enter your name")
            reserve_ticket = ReservationTicket(customer_name, hotel)
            print(reserve_ticket.generate())
        else:
            print("Authentication failed !")
    else:
        print("There is something wrong with your card....Try again")
else:
    print("Hotel is not free!!")


#  completed
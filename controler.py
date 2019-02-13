import view
from model import Client, SavingAccount, DebitAccount, session

def home():
    choice = None
    while choice != 0:
        choice = view.home()
        if choice == 2:
            client = add_client()
            display_client_file(client)
        elif choice == 1:
            #clients = session.query(Client).all()
            #clients = session.query(Client).filter(Client.firstname.startswith("K"))
            #clients = session.query(Client).first()
            clients = session.query(Client).order_by(Client.lastname)
            index = view.display_client_list(clients)
            if index != 0:
                display_client_file(clients[index - 1])


def add_client():
    firstname, lastname, email = view.add_client()
    client = Client(firstname, lastname, email)
    session.add(client)
    session.commit()
    return client

def display_client_file(client):
    choice = None
    while choice != 0:
        choice = view.display_client_file(client)
        if choice == 0:
            # user wants to return to home
            return
        elif choice == -1:
            # user wants to add an account
            account_type = view.display_add_account()
            if account_type == 1:
                # debit account
                account = DebitAccount(client.client_id)
            else:
                # saving account
                account = SavingAccount(client.client_id, 0.03)
            session.add(account)
            session.commit()
        else:
            # user want to see choice - 1 account of client
            index = choice - 1
            account = client.accounts[index]
            display_account(account)

def display_account(account):
    raise NotImplementedError()

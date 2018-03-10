from datetime import date

from .model import Person
from .model import Wallet
from common.base import session_factory
from sqlalchemy import create_engine

def create_people():
    session = session_factory()
    bruno = Person("Bruno Krebs", date(1984, 10, 20), 182, 84.5)
    john = Person("John Doe", date(1990, 5, 17), 173, 90)
    session.add(bruno)
    session.add(john)
    session.commit()
    session.close()


def get_people():
    session = session_factory()
    people_query = session.query(Person)
    session.close()
    return people_query.all()

def create_wallet():
    session = session_factory()
    walletA = Wallet("0x12345", 1000, "")
    walletB = Wallet("0x12345", 2000, "")
    session.add(walletA)
    session.add(walletB)
    session.commit()
    session.close()


if __name__ == "__main__":
    wallet = get_wallet()
    if len(wallet) == 0:
        create_wallet()
    people = get_wallet()

    for person in people:
        print(f'{wallet.name} was born in {wallet.balance}')

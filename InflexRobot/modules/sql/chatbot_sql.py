import threading

from sqlalchemy import Column, String

from InflexRobot.modules.sql import BASE, SESSION


class InflexChats(BASE):
    __tablename__ = "Inflex_chats"
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id


InflexChats.__table__.create(checkfirst=True)
INSERTION_LOCK = threading.RLock()


def is_Inflex(chat_id):
    try:
        chat = SESSION.query(InflexChats).get(str(chat_id))
        return bool(chat)
    finally:
        SESSION.close()


def set_Inflex(chat_id):
    with INSERTION_LOCK:
        Inflexchat = SESSION.query(InflexChats).get(str(chat_id))
        if not Inflexchat:
            Inflexchat = InflexChats(str(chat_id))
        SESSION.add(Inflexchat)
        SESSION.commit()


def rem_Inflex(chat_id):
    with INSERTION_LOCK:
        Inflexchat = SESSION.query(InflexChats).get(str(chat_id))
        if Inflexchat:
            SESSION.delete(Inflexchat)
        SESSION.commit()

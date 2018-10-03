from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from typing import Tuple
import sys

app = Flask(__name__)


def generate_session() -> Tuple[app, int, scoped_session]:
    try:
        app = Flask(__name__)
        lines = [line.rstrip('\n') for line in open('.config')]
        user = lines[0]
        password = lines[1]
        port_num = int(lines[2])  # port being served on
        engine = create_engine(
            "postgresql://%s:%s@localhost/tsunami" % (user, password)
        )
        Session = sessionmaker(bind=engine)
        session = Session()
        return app, port_num, session

    except Exception:
        sys.exit("Couldn't get connection credentials. Does .config exist?")

from app.models import Message, KPI
from app import db

def create_log(data):
    if 'type' not in data:
        return 1
    type = data['type']
    value = None
    if 'value' in data:
        value = data['value']
    kpi = KPI(type, value)
    db.session.add(kpi)
    db.session.commit()
    return "created %s kpi with value %s"%(type, value)


def get_response(msg):
    """
    you can place your mastermind AI here
    """
    message = Message(msg)
    db.session.add(message)
    db.session.commit()
    parts = msg.split(".")
    out = "logged %s"%message
    if parts[0].lower() == "log":
        type = parts[1]
        value = None
        if len(parts) > 2:
            value = parts[2]
        kpi = KPI(type, value)
        db.session.add(kpi)
        db.session.commit()
        out = "created %s kpi with value %s"%(type, value)
    return out

from app.models import Message, KPI
from app import app, db
from fuzzywuzzy import process

def get_pomodoro_project(value):
    project = value
    if value == 'last':
        #get the last logged get_pomodo
        last = KPI.query.filter_by(type='pomo').order_by(KPI.received.desc()).first()
        project = last.value
    else:
        highest = process.extractOne(value, app.config['LIST_OF_PROJECTS'])
        if highest[1] > app.config['CUTOFF_VALUE']:
            project = highest[0]
        else:
            project = "Non-project pomo: %s"%value
    return project


def create_log(data):
    if 'type' not in data:
        return 1
    type = data['type']
    value = None
    if 'value' in data:
        value = data['value']
    if type.lower().startswith('pomo'):
        value = get_pomodoro_project(value)
    kpi = KPI(type, value)
    db.session.add(kpi)
    db.session.commit()
    return "created %s log with value %s"%(type, value)


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
            value = ".".join(parts[2:])
        data = {'type':type, 'value':value}
        out = create_log(data)
    return out

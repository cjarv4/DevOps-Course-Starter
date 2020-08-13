from flask import Flask, render_template, request, redirect, url_for
from operator import itemgetter
import session_items as session

app = Flask(__name__)
app.config.from_object('flask_config.Config')
sortSwitch = True


@app.route('/', methods=['POST', 'GET'])
def index():
    todo, doing, done = session.get_items()
    # global sortSwitch
    # if sortSwitch:
    #     todo = sorted(todo, key=itemgetter('closed'))
    # else:
    #     todo = sorted(todo, key=itemgetter('closed'), reverse=True)
    return render_template('index.html', todos=todo, doings=doing, dones=done)


@app.route('/item/createNew', methods=['POST'])
def create_new_item():
    session.add_item(request.form['item_title'])
    return index()


@app.route('/item/<id>/complete')
def complete_item(id):
    session.complete_item(id)
    return redirect("/")


@app.route('/item/<id>/checklistItem/<checklistId>/complete')
def complete_checklist_item(id, checklistId):
    session.complete_checklist_item(id, checklistId)
    return get_item(id)


@app.route('/item/<id>/delete')
def delete_item(id):
    session.delete_item(id)
    return redirect("/")


@app.route('/item/<id>/checklistItem/<checklistId>/delete')
def delete_checklist_item(id, checklistId):
    session.delete_checklist_item(id, checklistId)
    return get_item(id)


@app.route('/item/<id>')
def get_item(id):
    return render_template('todoSingle.html', items=session.get_item(id), checklist=session.get_card_checklist(id))


# @app.route('/sorted_items')
# def sort_item():
#     global sortSwitch
#     if sortSwitch:
#         sortSwitch = False
#     else:
#         sortSwitch = True
#     return redirect("/")


if __name__ == '__main__':
    app.run()

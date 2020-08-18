from flask import Flask, render_template, request, redirect, url_for
import Item as Item

app = Flask(__name__)
app.config.from_object('flask_config.Config')


@app.route('/', methods=['POST', 'GET'])
def index():
    todo, doing, done = Item.get_cards()
    return render_template('index.html', todos=todo, doings=doing, dones=done)


@app.route('/card/createNew', methods=['POST'])
def create_new_card():
    Item.add_card(request.form['item_title'], request.form['desc'], request.form['date'])
    return index()


@app.route('/card/<id>/checklistItem/createNew', methods=['POST'])
def create_new_checklist_item(id):
    Item.add_checklist_item(id, request.form['item_title'])
    return get_card(id)


@app.route('/card/<id>/complete')
def complete_card(id):
    Item.set_card_to_complete(id)
    return redirect("/")


@app.route('/card/<id>/checklistItem/<checklistId>/complete')
def complete_checklist_item(id, checklistId):
    Item.complete_checklist_item(id, checklistId)
    return get_card(id)


@app.route('/card/<id>/delete')
def delete_card(id):
    Item.delete_card(id)
    return redirect("/")


@app.route('/card/<id>/checklistItem/<checklistId>/delete')
def delete_checklist_item(id, checklistId):
    Item.delete_checklist_item(id, checklistId)
    return get_card(id)


@app.route('/card/<id>/moveToDoing')
def set_card_in_progress(id):
    Item.set_card_in_progress(id)
    return redirect("/")


@app.route('/card/<id>')
def get_card(id):
    return render_template('todoSingle.html', items=Item.get_card(id), checklist=Item.get_card_checklist(id))


if __name__ == '__main__':
    app.run()

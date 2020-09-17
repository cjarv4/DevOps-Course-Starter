from flask import Flask, render_template, request, redirect, url_for
import Card as card
import View_Model as view_model
show_all_done = False


def create_app():
    app = Flask(__name__)
    app.config.from_object('flask_config.Config')

    @app.route('/', methods=['POST', 'GET'])
    def index():
        todo, doing, done = card.get_cards()
        item_view_model = view_model.ViewModel(todo, doing, done, show_all_done)
        return render_template('index.html', view_model=item_view_model)

    @app.route('/showAll', methods=['GET'])
    def flip_show_all_done():
        global show_all_done
        show_all_done = not show_all_done
        print(show_all_done)
        return redirect("/")

    @app.route('/card/createNew', methods=['POST'])
    def create_new_card():
        card.add_card(request.form['item_title'], request.form['desc'], request.form['date'])
        return redirect("/")

    @app.route('/card/<id>/checklistItem/createNew', methods=['POST'])
    def create_new_checklist_item(id):
        card.add_checklist_item(id, request.form['item_title'])
        return get_card(id)

    @app.route('/card/<id>/complete')
    def complete_card(id):
        card.set_card_to_complete(id)
        return redirect("/")

    @app.route('/card/<id>/checklistItem/<checklistId>/complete')
    def complete_checklist_item(id, checklistId):
        card.complete_checklist_item(id, checklistId)
        return get_card(id)

    @app.route('/card/<id>/delete')
    def delete_card(id):
        card.delete_card(id)
        return redirect("/")

    @app.route('/card/<id>/checklistItem/<checklistId>/delete')
    def delete_checklist_item(id, checklistId):
        card.delete_checklist_item(id, checklistId)
        return get_card(id)

    @app.route('/card/<id>/moveToDoing')
    def set_card_in_progress(id):
        card.set_card_in_progress(id)
        return redirect("/")

    @app.route('/card/<id>')
    def get_card(id):
        return render_template('todoSingle.html', items=card.get_card_by_id(id), checklist=card.get_card_checklist(id))

    return app


if __name__ == '__main__':
    # app.run()
    create_app().run()
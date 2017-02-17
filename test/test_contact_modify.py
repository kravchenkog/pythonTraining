from model.contact import Contact


def test_contact_modify_firstname(app):
   app.session.login(user_name="admin", password="secret")
   app.contact.modify(0, Contact(firstname="Karamba"))
   app.session.logout()
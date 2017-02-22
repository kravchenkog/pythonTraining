from model.contact import Contact


def test_contact_modify_firstname(app):

   app.contact.modify(0, Contact(firstname="Karamba"))


def test_contact_modify_lastname(app):
   app.contact.modify(0, Contact(lastname="ArivaHuriva"))
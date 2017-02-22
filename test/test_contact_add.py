from model.contact import Contact


def test_create_contact(app):
    app.contact.create_contact(Contact(firstname='Gregory', lastname='Kravchenko',
                                       nickname="grif0n", email='g300884@gmail.com',
                                       home='380637267402'))
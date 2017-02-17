from model.contact import Contact


def test_create_contact(app):

    app.session.login(user_name='admin', password='secret')
    app.contact.create_contact(Contact(firstname='Grigoriy', lastname='Kravchenko',
                                       nickname='grif0n', email='g300884@gmail.com',
                                       home='380637267402'))
    app.session.logout()
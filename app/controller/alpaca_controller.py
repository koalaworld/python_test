from flask import render_template, json

# as the models file contains all the models, import what you need
from app.models import Alpaca

class AlpacaController(object):

    # TODO: Implement Index
    # WHAT: Grabs data from model and uses it to display the relevant
    # alpacas from the database
    # CONDITIONS: If user specifies age, then must filter the list
    # RETURN: Return formatted Alpaca's to use for the view
    def index(self, sel):
        if sel == "ALL":
            alpacas = Alpaca.get_all(None)
        elif sel == "below":
            alpacas = Alpaca.get_below(25)
        else:
            alpacas = Alpaca.get_above(25)
            
        data = []
        for alpaca in alpacas:
            data.append({'name': alpaca.name,'displayName': alpaca.display_name,'age': alpaca.age, 'sex': alpaca.sex, 'filename': alpaca.get_filename()})

        return render_template("index.html", alpacas=data, sel=sel)
    
    # TODO: Implement Profile
    # WHAT: Grabs the relevant Alpaca from the model and uses it to
    # display the profile for that alpaca from the database
    # RETURN: Return formatted Alpaca to use for the view
    def profile(self, name):
        alpaca = Alpaca.get(name)
        return render_template("profile.html", displayName=alpaca.display_name, filename=alpaca.get_filename(), age=alpaca.age, bio=alpaca.bio, hobbies=alpaca.hobbies,
    contact=json.dumps(alpaca.contact))
    
    # TODO: Implement Search
    # WHAT: Uses the data recieved to find the Alpaca from the data
    # CONDITIONS: If user specifies nothing you can return everything or nothing!
    # that part if determined by you however if something is specified, it must
    # be a filtered list of alpacas
    # RETURN: Return formatted alpacas as a list using the
    # search criteria
    def search(self):
        alpaca = Alpaca.get(name)
        return render_template("profile.html/<name>", displayName=alpaca.display_name, filename=alpaca.get_filename(), age=alpaca.age, bio=alpaca.bio, hobbies=alpaca.hobbies,
    contact=json.dumps(alpaca.contact))
    # TODO: Implement Create
    # WHAT: Uses the data recieved to create an Alpaca model
    # REQUIREMENTS: Make a 'fake' save function in Alpaca that
    # Prints saving alpaca and then list the information recieved
    # and then give back a message stating what was saved
    # i.e Fred was created!
    # CONDITIONS:
    # RETURN: Return formatted message using the relevant information
    def create(self, id, name, display_name, bio, age, hobbies, contact, sex):
        alpaca = Alpaca(id, name, display_name, bio, age, hobbies, contact, sex)
        return {'message': '%s was created' % (name),'success': True}
    # TODO: Implement Delete
    # WHAT: Uses the data recieved to find the Alpaca from the data
    # and then deletes it
    # REQUIREMENTS: Make a 'fake' delete function in Alpaca that
    # Prints the alpaca that will be delted followed by deleting alpaca
    # and then list the information recieved and then give back a
    # message stating what was saved i.e Fred was deleted!
    # CONDITIONS:
    # RETURN: Return formatted message using the relevant information
    # def above():

    def delete(name):
        alpaca = Alpaca.get(name)
        return render_template("profile.html", displayName=alpaca.display_name, filename=alpaca.get_filename(), age=alpaca.age, bio=alpaca.bio, hobbies=alpaca.hobbies,
    contact=json.dumps(alpaca.contact))

alpaca_controller = AlpacaController()
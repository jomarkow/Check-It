import json

class data:

    def __init__(self):

        pass

    def read_data(self):

        with open("data/notes.json", "r") as file:

            self.data = json.load(file)

        self.username = self.data["username"]
        self.note = self.note["note"]

        return({"Username": self.username, "Note": self.note})

    def write_data(self, username, note):

        

        with open("data/notes.json", "w") as file:

            self.data = json.dump(data, file)


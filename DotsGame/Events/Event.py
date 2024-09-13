class Event:
    list = []

    def add_listener(self, listener):
        self.list += [listener]

    def remove_listener(self, listener):
        self.list -= [listener]

    def invoke(self, *params):
        for x in self.list:
            x(*params)

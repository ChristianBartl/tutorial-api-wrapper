

class TV(object):
    def __init__(self, id) -> None:
        self.id = id

    def info(self):
        return {'id': self.id}
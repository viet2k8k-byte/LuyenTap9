class User:
    def __init__(self, id):
        self._id = id
    @property
    def id(self):
        return self._id
u = User(101)
print(f"User id: {u.id}")
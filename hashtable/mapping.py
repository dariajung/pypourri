
class Dict(object):

    def __init__(self):
        self.dict = {}

    # returns nothing
    def add_kv_pair(self, key, value):
        self.dict[key] = value

    def get_value(self, key):
        if key in self.dict:
            return self.dict[key]
        else:
            print "%s is not a valid key" % key
            return None

    def remove_key(self, key):
        if key in self.dict:
            del self.dict[key]

if __name__ == "__main__":
    m = Dict()

class Options:
    def __init__(self, source):
        self.config = {
            "graphs_path": source["GRAPHS_PATH"],
            "xml_file": source["XML_FILE"],
        }

    def get(self, key):
        return self.config[key]

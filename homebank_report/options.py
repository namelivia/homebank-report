import yaml

class Options:
    def __init__(self, source):
        self.config = {
            "graphs_path": source["GRAPHS_PATH"],
            "xml_file": source["XML_FILE"],
            "notifications_config_file": source["NOTIFICATIONS_CONFIG_FILE"],
            "notifications": {},
        }

        with open(self.config["notifications_config_file"]) as file:
            try:
                data = yaml.safe_load(file)
                accounts = data.get('accounts', [])
                for account_info in accounts:
                    account = account_info.get('account')
                    endpoint = account_info.get('endpoint')
                    self.config["notifications"][account] = endpoint
            except yaml.YAMLError as exc:
                print(f"Error in configuration file: {exc}")


    def get(self, key):
        return self.config[key]

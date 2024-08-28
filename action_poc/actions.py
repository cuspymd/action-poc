
class ActionsFW:
    def __init__(self) -> None:
        self.action_definitions = []
        self.action_app_map = {}

    def get_actions(self, messages):
        # search actions by messages
        return self.action_definitions
    
    def scan_actions(self, app):
        action_definitions = app.get_action_definitions()
        self.action_definitions += action_definitions
        
        action_app_map = {
            action_definition["name"]: app
            for action_definition in action_definitions
        }
        self.action_app_map.update(action_app_map)

    def execute_action(self, name, arguments):
        app = self.action_app_map[name]
        return app.__getattribute__(name)(arguments)


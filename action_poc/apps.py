class VolumeApp:
    def __init__(self):
        self.volume = 10

    def get_action_definitions(self):
        return [{
            "name": "get_tv_volume",
            "description": "Get audio volume value of TV. TV 볼륨 값을 알고 싶을 때 호출하라. 예를 들어 사용자가 '현재 TV 볼륨이 얼마지?' 라고 물었을 때 호출 가능하다."
        }, {
            "name": "set_tv_volume",
            "description": "Set audio volume value of TV. TV 볼륨 값을 설정할 때 호출하라. 예를 들어 사용자가 'TV 볼륨을 10으로 설정해줘.' 라고 요청했을 때 호출 가능하다.",
            "parameters": {
                "type": "object",
                "properties": {
                    "volume": {
                        "type": "integer",
                        "description": "TV에 설정하고자 하는 volume 값"
                    }
                },
                "required": ["volume"],
                "additionalProperties": False
            }
        }]
    
    def get_tv_volume(self, params):
        return {
            "current_volume": self.volume
        }
    
    def set_tv_volume(self, params):
        self.volume = params['volume']
        return {
            "result": f"볼륨 값이 {self.volume} 으로 설정되었음."
        }
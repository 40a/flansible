from flask_restful_swagger import swagger

@swagger.model
class AnsibleCommandModel:
    def __init__(self, module):
        pass

@swagger.model
class AnsibleRequestResultModel:
    def __init__(self, task_id):
        pass
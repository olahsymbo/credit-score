class api_response:

    def __init__(self, output):
        self.output = output

    def true_output(self):
        return {"status": "success",
                "message": "Successfully Rated Credit",
                "data": self.output}

    def error_output(self):
        return {"code": 400,
                "status": "error",
                "message": "invalid data",
                "data": []}

    def error_req(self):
        return {"code": 404,
                "status": "error",
                "message": "bad request"}

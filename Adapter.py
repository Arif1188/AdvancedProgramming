class ResponseDTO:
    def __init__(self, model: str, version: str) -> None:
        self.model = model
        self.version = version


class ResponseHandler:
    def __init__(self, adapter: "Adapter") -> None:
        self.adapter = adapter

    def handle(self):
        return self.adapter.adapt()


class NewResponseDTO:
    def __init__(self, model: str, version: str, size: int, weight: float) -> None:
        self.model = model
        self.version = version
        self.size = size
        self.weight = weight


class Adapter:
    def __init__(self, response_dto: NewResponseDTO) -> None:
        self.response_dto = response_dto

    def adapt(self) -> dict:
        return {"model": self.response_dto.model, "version": self.response_dto.version}



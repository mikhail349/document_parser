import base64
from abc import ABC, abstractmethod

import requests
from django.conf import settings


class AbstractParser(ABC):
    """Абстрактный класс парсера файла."""
    
    @abstractmethod
    def parse(self, file: bytearray) -> str:
        """Распарсить файл.

        Args:
            file: массив байт

        Returns:
            str: распарсенный файл

        """


class CloudVisionParser(AbstractParser):
    """Абстрактный класс парсера файла."""

    def __init__(self, api_url: str) -> None:
        super().__init__()
        self.api_url = api_url

    def extract_text(self, body: dict) -> str:
        """Достать текст из тела ответа.

        Args:
            body: тело ответа

        Returns:
            str: текст

        """
        text_annotations = body['responses'][0]['textAnnotations']
        descriptions = [
            annotation['description']
            for annotation in text_annotations
        ]
        return ' '.join(descriptions)

    def parse(self, file: bytearray) -> str:
        body = {
            'requests': [
                {
                    'image': {
                        'content': base64.b64encode(file).decode('utf-8'),
                    },
                    'features': [
                        {
                            'type': 'TEXT_DETECTION',
                        }
                    ],
                    'imageContext': {
                        'languageHints': ['pt', 'en'],
                    }
                }
            ]
        }

        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }

        response = requests.post(self.api_url, headers=headers, json=body)
        return self.extract_text(response.json())


def get_parser() -> AbstractParser:
    """Получить инстанс парсера.

    Returns:
        AbstractParser: парсер

    """
    return CloudVisionParser(settings.CLOUD_VISION_API)

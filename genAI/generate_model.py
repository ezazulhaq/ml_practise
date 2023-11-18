import os
import google.generativeai as palm

from google.api_core import retry


class GenerateModel:

    def __init__(self):
        self.api_key = os.environ.get('GOOGLE_API_KEY')

    def get_bison_model(self):
        palm.configure(
            api_key=self.api_key
        )

        return [m for m in palm.list_models()
                if 'generateText'
                in m.supported_generation_methods][0]

    @retry.Retry()
    def generate_text(self,
                      prompt,
                      model=None,
                      temperature=0.0):
        if model is None:
            model = self.get_bison_model()
        return palm.generate_text(prompt=prompt,
                                  model=model,
                                  temperature=temperature)

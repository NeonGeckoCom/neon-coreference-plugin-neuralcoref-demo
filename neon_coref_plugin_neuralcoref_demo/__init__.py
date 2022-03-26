import requests
from ovos_plugin_manager.coreference import CoreferenceSolverEngine


class NeuralCoreferenceDemoSolver(CoreferenceSolverEngine):

    @classmethod
    def solve_corefs(cls, text, lang="en"):
        try:
            params = {"text": text}
            r = requests.get("https://coref.huggingface.co/coref",
                             params=params).json()
            return r["corefResText"] or text
        except Exception as e:
            return text

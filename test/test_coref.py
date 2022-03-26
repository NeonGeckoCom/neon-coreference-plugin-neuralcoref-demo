import unittest

from neon_coref_plugin_neuralcoref_demo import NeuralCoreferenceDemoSolver


class TestNeuralCoreferenceDemo(unittest.TestCase):

    def test_coref(self):
        solver = NeuralCoreferenceDemoSolver()
        self.assertEqual(solver.solve_corefs(
            "My neighbors have a cat. It has a bushy tail"),
            "My neighbors have a cat. a cat has a bushy tail")
        self.assertEqual(solver.solve_corefs(
            "Here is the book now take it"),
            "Here is the book now take the book")
        self.assertEqual(solver.solve_corefs(
            "The sign was too far away for the boy to read it"),
            "The sign was too far away for the boy to read the sign")
        #self.assertEqual(solver.solve_corefs(
        #    "Dog is man's best friend. It is always loyal"),
        #    "Dog is man's best friend. Dog is always loyal")
        self.assertEqual(solver.solve_corefs(
            "The girl said she would take the trash out"),
            "The girl said the girl would take the trash out")
        self.assertEqual(solver.solve_corefs(
            "I voted for Nader because he is clear about his values. His ideas represent a majority of the nation. He is better than Rajeev"),
            "I voted for Nader because nader is clear about nader values. nader ideas represent a majority of the nation. nader is better than Rajeev")
        self.assertEqual(solver.solve_corefs(
            "Jack von Doom is one of the top candidates in the elections. His ideas are unique compared to Neha's"),
            "Jack von Doom is one of the top candidates in the elections. jack von doom ideas are unique compared to Neha's")
        self.assertEqual(solver.solve_corefs(
            "Members voted for John because they see him as a good leader"),
            "Members voted for John because members see john as a good leader")
        self.assertEqual(solver.solve_corefs(
            "Leaders around the world say they stand for peace"),
            "Leaders around the world say leaders around the world stand for peace")
        self.assertEqual(solver.solve_corefs(
            "My neighbours just adopted a puppy. They care for it like a baby"),
            "My neighbours just adopted a puppy. my neighbours care for a puppy like a baby")
        self.assertEqual(solver.solve_corefs(
            "I have many friends. They are an important part of my life"),
            "I have many friends. many friends are an important part of my life")


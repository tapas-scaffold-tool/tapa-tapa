from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase

from tapas.tools.tapas_integration_tests import (
    communicate,
    pass_to_process,
)


class GenerateTapasTest(TestCase):
    def test_examle(self):
        with TemporaryDirectory() as target:
            code, out, err = communicate(
                ["tapas", "dir:.", target],
                input=pass_to_process(
                    "mit",
                    "yes",
                ),
            )

            self.assertEqual(0, code, "Exit code is not zero")
            self.assertEqual(0, len(err), "Errors occurred")

            target = Path(target)
            file = target / "place-your-template-files-here"

            self.assertTrue(file.exists(), "File was not created")
            self.assertTrue(file.is_file(), "File is not file")

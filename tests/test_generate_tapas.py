from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase

from tapas.tools.tapas_integration_tests import (
    communicate,
    pass_to_process,
)


class GenerateTapasTest(TestCase):
    def test_tapa_template_generated(self):
        with TemporaryDirectory() as target:
            code, out, err = communicate(
                ["tapas", "dir:.", target],
                input=pass_to_process(
                    "test-tapa-tapa",
                    "mit",
                    "yes",
                ),
            )

            self.assertEqual(0, code, "Exit code is not zero")
            self.assertEqual(0, len(err), "Errors occurred")

            target = Path(target)

            template_dir = target / "template"
            self.assertTrue(template_dir.exists() and template_dir.is_dir(), "Template directory was not created")

            template_file = template_dir / "place-your-template-files-here"
            self.assertTrue(template_file.exists() and template_file.is_file(), "Template file was not created")

            license = target / "LICENSE"
            self.assertTrue(license.exists(), "LICENSE file does not exists")

            git_dir = target / ".git"
            self.assertTrue(git_dir.exists() and git_dir.is_dir(), "Git directory was not created")

            generated_nox_file = target / "noxfile.py"
            code, out, err = communicate(
                ["nox", "--noxfile", str(generated_nox_file)],
            )

            self.assertEqual(0, code, "Exit code is not zero")

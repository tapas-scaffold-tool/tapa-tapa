import os

from tapas.tools import prompt_bool, init_git_repo, prompt_str, prompt_license, generate_license_file


# Require from user to enter parameters in this function
def ask():
    prompt_str("name", prompt_string="Enter tapa name: ")

    # Remove if no need to control README.md
    prompt_bool('readme', default_value="y", prompt_string="Create README.md file? [Y/n]: ")

    # Remove if no need in LICENSE file
    prompt_license()

    # Remove if no need in git repo init control
    prompt_bool('git', default_value="y", prompt_string="Init git repository? [Y/n]: ")

    prompt_bool('nox', default_value="y", prompt_string="Create noxfile.py for test? [Y/n]: ")

    prompt_bool('travis', default_value="y", prompt_string="Create .travis.yml for CI? [Y/n]: ")

# Perform additional actions after generation in this function
def post_init(readme: bool, license: str, git: bool, nox: bool, travis: bool):
    # Remove if no need to control README.md
    if not readme:
        os.remove('README.md')

    # Remove if no need in LICENSE file
    generate_license_file(license)

    if not nox:
        os.remove("noxfile.py")

    if not travis:
        os.remove(".travis.yml")

    # Remove if no need in git repo init control
    if git:
        init_git_repo(dot_files=[
            ".travis.yml",
        ])

import os


def test_main_file_exists():
    assert os.path.exists("main.py")


def test_required_files_exist():
    assert os.path.exists("README.md")
    assert os.path.exists("requirements.txt")
    assert os.path.exists(".env.example")
    assert os.path.exists(".gitignore")


def test_requirements():
    with open("requirements.txt", "r") as file:
        content = file.read()

    assert "groq" in content
    assert "python-dotenv" in content


def test_env_example():
    with open(".env.example", "r") as file:
        content = file.read()

    assert "GROQ_API_KEY" in content
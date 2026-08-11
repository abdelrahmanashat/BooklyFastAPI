from pathlib import Path
import fastapi_mail

# Locate the config.py file inside the installed fastapi-mail package
config_path = Path(fastapi_mail.__file__).parent / "config.py"
content = config_path.read_text()

# Inject the missing import if it isn't there
if "SecretStr" not in content:
    config_path.write_text("from pydantic import SecretStr\n" + content)
    print("Successfully patched fastapi-mail config.py!")
else:
    print("Patch already applied or no longer needed.")
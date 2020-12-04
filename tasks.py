from invoke import task
from pathlib import Path

REPO_ROOT = Path(__file__).parent.absolute()
REGISTRY_DATA = REPO_ROOT / '.registry'


@task
def run_registry(c):
    c.run(f"docker run --rm -dp 5000:5000 -v {REGISTRY_DATA}:/var/lib/registry --name registry registry")

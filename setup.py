import os

from setuptools import setup, find_packages


def parse_requirements(filename):
    """Parse requirements from a file, ignoring comments and empty lines."""
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        return [
            line.strip()
            for line in f
            if line.strip() and not line.startswith("#")
        ]


setup(
    name="human-eval",
    package_dir={"human_eval": ""},
    version="1.0",
    description="",
    author="OpenAI",
    packages=["human_eval.human_eval", "human_eval.data"],
    install_requires=parse_requirements("requirements.txt"),
    entry_points={
        "console_scripts": [
            "evaluate_functional_correctness = human_eval.human_eval.evaluate_functional_correctness:main",
        ]
    },
    package_data={"": ["*.jsonl", "*.jsonl.gz"]},
    include_package_data=True,
)

import os

import pkg_resources
from setuptools import setup, find_packages


setup(
    name="human-eval",
    package_dir={"human_eval": ""},
    version="1.0",
    description="",
    author="OpenAI",
    packages=["human_eval.human_eval", "human_eval.data"],
    install_requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
        )
    ],
    entry_points={
        "console_scripts": [
            "evaluate_functional_correctness = human_eval.human_eval.evaluate_functional_correctness:main",
        ]
    },
    package_data={"": ["*.jsonl", "*.jsonl.gz"]},
    include_package_data=True,
)

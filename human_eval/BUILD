# Copyright Exafunction, Inc.

load("@local_pip//:requirements.bzl", "requirement")

py_library(
    name = "human_eval",
    srcs = [
        "__init__.py",
        "data.py",
        "evaluate_functional_correctness.py",
        "evaluation.py",
        "execution.py",
    ],
    data = [
        "//third_party/human_eval/data:human_eval_data",
    ],
    deps = [
        requirement("numpy"),
        requirement("tqdm"),
    ],
    visibility = ["//visibility:public"],
)
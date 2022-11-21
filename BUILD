# Copyright Exafunction, Inc.

load("@local_pip//:requirements.bzl", "requirement")

py_library(
    name = "human_eval_problems",
    srcs = [
        "//third_party/human_eval/human_eval:human_eval"
    ],
    data = [
        "//third_party/human_eval/data:human_eval_data"
    ],
    deps = [
        requirement("numpy"),
        requirement("tqdm"),
    ],
    visibility = ["//visibility:public"],
)
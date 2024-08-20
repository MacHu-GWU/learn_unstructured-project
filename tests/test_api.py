# -*- coding: utf-8 -*-

from learn_unstructured import api


def test():
    _ = api


if __name__ == "__main__":
    from learn_unstructured.tests import run_cov_test

    run_cov_test(__file__, "learn_unstructured.api", preview=False)

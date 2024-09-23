# -*- coding: utf-8 -*-

from unstructured.partition.pdf import partition_pdf

elements = partition_pdf(filename="f1040.pdf")
print(len(elements))
for ith, element in enumerate(elements, start=1):
    print(f"========== Element {ith} ==========")
    print(element.to_dict())
    print(element.metadata.coordinates)
#!/usr/bin/env python3
#
# Based on OMOP 5.4 schema, see
# https://github.com/OHDSI/CommonDataModel/blob/main/inst/ddl/5.4/postgresql/OMOPCDM_postgresql_5.4_ddl.sql

import argparse
import csv
import os
import random
import string

chars = string.ascii_letters + string.digits

species = [
    "Mus musculus",
    "Rattus norvegicus",
]


def write_tsv(path, rows):
    """
    Given a path and a list of rows (dicts),
    write a TSV file using the keys of the first row as headers.
    """
    with open(path, "w") as f:
        fieldnames = rows[0].keys()
        writer = csv.DictWriter(f, fieldnames, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

def generate_strains():
    random.seed(0)
    rows = []
    for r in range(1, 100):
        sp = random.choice(species)
        length = random.randint(2, 6)
        strain = "".join(random.choice(chars) for i in range(length))
        rows.append({
            "ID": f"ex:strain_{r}",
            "label": f"{sp} strain {strain}",
            "species": sp,
        })

    # generate errors
    row = random.choice(rows)
    row["ID"] += "-"
    row = random.choice(rows)
    row["label"] = ""
    row = random.choice(rows)
    row["ID"] = ""
    row["species"] = "Rattus"

    return rows


if __name__ == "__main__":
    strains = generate_strains()
    write_tsv("src/tables/strain.tsv", strains)


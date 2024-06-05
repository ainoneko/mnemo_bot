#!/bin/bash
set -x

ZIP_DIR="./zip"
DATA_DIR="./data"

mkdir -p ${DATA_DIR}
for f in ${ZIP_DIR}/*.zip;	do
  # Keep existing data files
  unzip -n "${f}" -d "${DATA_DIR}"
done

ls -l ${DATA_DIR}
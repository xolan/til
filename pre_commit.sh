#!/bin/bash
version=$(python -V 2>&1 | grep -Po '(?<=Python )(.+)')
if [[ -z "$version" ]]
then
    exit 1
fi

parsedVersion=$(echo "${version//./}")
if [[ "$parsedVersion" -lt "300" ]]
then
    python create_readme.py
    exit 0
else
    exit 1
fi
#!/usr/bin/env bash

thing="pyrcc5"
ext_in=".qrc"
ext_out=".py"
location="../ressources/"

files=(
    images
)

for file in "${files[@]}"
do
    ${thing} "${location}${file}${ext_in}" "-o" "${location}${file}${ext_out}"
done

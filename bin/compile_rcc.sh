#!/usr/bin/env bash

#!/usr/bin/env bash

thing="pyrcc5"
ext_in=""
ext_out=""
location=""

files=(
)

for file in "${files[@]}"
do
    ${thing} "-x" "${location}${file}${ext_in}" "-o" "${location}${file}${ext_out}"
done

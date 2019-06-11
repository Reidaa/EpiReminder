#!/usr/bin/env bash

thing="pyuic5"
ext_in=".ui"
ext_out=".py"
location="../ui/"

files=(
    EventWidget
    LoggingWidget
    PlanningWidget
    ObjectivesWidget
    HelpObjectivesWidget
)

for file in "${files[@]}"
do
    ${thing} "-x" "${location}${file}${ext_in}" "-o" "${location}Ui_${file}${ext_out}"
done

#!/usr/bin/env bash

parents=(
"./Period_4"
    "./Period_5"
    "./Period_6"
    "./Period_7"
    "./Period_8"
    "./Early"
    "./Makeups"
)

for parent in "${parents[@]}"; do
    counter=1

    # Verify parent directory exists
    if [[ ! -d "$parent" ]]; then
        echo "Directory not found: $parent"
        continue
    fi

    echo "Processing: $parent"

    for dir in "$parent"/*/; do
        [[ -d "$dir" ]] || continue

        new_path="$parent/Student_$counter"

        # Skip if already correctly named
        if [[ "${dir%/}" == "$new_path" ]]; then
            ((counter++))
            continue
        fi

        # Prevent overwriting existing directories
        if [[ -e "$new_path" ]]; then
            echo "Skipping: $new_path already exists"
            ((counter++))
            continue
        fi

        # Confirm the output
        echo "Renaming: $dir -> $new_path"

        # Comment out this line when output is confirmed
        mv -- "$dir" "$new_path"
        ((counter++))
    done
done
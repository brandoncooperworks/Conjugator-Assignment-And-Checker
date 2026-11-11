
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

    # Verify parent directory exists
    if [[ ! -d "$parent" ]]; then
        echo "Directory not found: $parent"
        continue
    fi

    echo "Processing: $parent"

    for dir in "$parent"/*/; do
        [[ -d "$dir" ]] || continue

        # Get student folder name (e.g., Student_1)
        student=$(basename "$dir")

        # Construct new filename
        new_path="${dir}Verb_Conjugator_${student}.py"

        # Find Python files in student's folder
        for file in "$dir"*.py; do
            [[ -f "$file" ]] || continue

            # Skip if already correctly named
            [[ "$file" == "$new_path" ]] && continue

            # Prevent overwriting existing files
            if [[ -e "$new_path" ]]; then
                echo "Skipping: $new_path already exists"
                continue
            fi

            echo "Renaming: $file -> $new_path"

            # Uncomment to execute
            mv -- "$file" "$new_path"

        done
    done
done

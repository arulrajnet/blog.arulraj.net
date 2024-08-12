#!/bin/bash

BASH_DIR=$(dirname $(realpath "${BASH_SOURCE}"))

# Loop through all markdown files in the current directory and its subdirectories
find $BASH_DIR/content/ -maxdepth 2 -type f -name "*.md" | while read -r file; do
    # Check if the file contains YAML-style tags
    if grep -q '^tags:$' "$file"; then
        # Extract the tags list, convert to comma-separated, and store it in a temporary variable
        tags=$(awk '/^tags:/{flag=1;next}/^[^ -]/{flag=0}flag' "$file" | sed 's/ *- //g' | paste -sd "," -)

        # Replace the tags section in the file
        if [ -n "$tags" ]; then
            line_number=$(sed -n '/^tags:/=' "$file")
            # Remove the original tags section
            sed -i '/^tags:/,/^[^ -]/ {/^[^ -]/!d; /^slug:/!d;}' "$file"

            # Insert the new tags format
            sed -i "${line_number}s/^/tags: $tags\n/" "$file"
            # sed -i "/^---/a tags: $tags" "$file"
            # sed -i "s/^tags:/tags: $tags/" "$file"

            echo "Converted tags in $file"
        fi
    fi
done

echo "Tags conversion completed!"

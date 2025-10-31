import json
import re

def parse_output_to_dict(text):
    result = {}
    current_key = None
    current_values = []

    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue

        # Detect new section headers
        if line.endswith(":") or "detected" in line.lower():
            # Save the previous section before moving to the next
            if current_key:
                if "labels" in current_key.lower() or "logos" in current_key.lower():
                    cleaned_values = [re.sub(r"\s*\(confidence:.*?\)", "", v).strip() for v in current_values if v]
                    result[current_key] = cleaned_values
                elif "detected text" in current_key.lower():
                    result[current_key] = " ".join(current_values).strip()
                else:
                    result[current_key] = "\n".join(current_values).strip()

            current_key = line.rstrip(":")
            current_values = []

        elif line.startswith("Logo:"):
            logo_name = line.replace("Logo:", "").strip()
            if logo_name:
                current_values.append(logo_name)

        elif line.startswith("Label:"):
            label_name = line.replace("Label:", "").strip()
            if label_name:
                current_values.append(label_name)

        else:
            current_values.append(line)

    # Save the last section
    if current_key:
        if "labels" in current_key.lower() or "logos" in current_key.lower():
            cleaned_values = [re.sub(r"\s*\(confidence:.*?\)", "", v).strip() for v in current_values if v]
            result[current_key] = cleaned_values
        elif "detected text" in current_key.lower():
            result[current_key] = " ".join(current_values).strip()
        else:
            result[current_key] = "\n".join(current_values).strip()

    return result


# Example usage
if __name__ == "__main__":
    input_file = 'SampleOutput.txt'
    output_file = 'issue_data.json'

    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    parsed_dict = parse_output_to_dict(content)

    # Save the output as a JSON file
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(parsed_dict, json_file, indent=4, ensure_ascii=False)

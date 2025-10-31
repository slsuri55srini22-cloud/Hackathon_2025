import json
import os
from recommendations import IssueRecommendations

# ==============================
# Read issue text from JSON
# ==============================
def read_issue_from_json(json_path):
    """Read the issue text from a JSON file."""
    if not os.path.exists(json_path) or os.stat(json_path).st_size == 0:
        raise FileNotFoundError(f"JSON file '{json_path}' missing or empty.")
    
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    possible_keys = ["issue", "error", "description", "text", "detected_issue"]
    for key in possible_keys:
        if key in data:
            return data[key]
    
    def extract_text(obj):
        texts = []
        if isinstance(obj, dict):
            for v in obj.values():
                texts.extend(extract_text(v))
        elif isinstance(obj, list):
            for item in obj:
                texts.extend(extract_text(item))
        elif isinstance(obj, str):
            texts.append(obj)
        return texts
    
    all_texts = extract_text(data)
    if all_texts:
        return " ".join(all_texts)
    else:
        raise ValueError("No readable issue text found in JSON file.")


# ==============================
# Find recommendation from class
# ==============================
def find_recommendation(issue_text, recommendations_class):
    """Find matching recommendation for an issue using the class data."""
    issue_text_lower = issue_text.lower()
    for item in recommendations_class.get_all():
        known_issue = item["Issue"].lower()
        recommendation = item["Recommendation"]

        # Exact match
        if known_issue == issue_text_lower:
            return recommendation
        
        # Partial match
        if known_issue in issue_text_lower or issue_text_lower in known_issue:
            return recommendation
    
    return None


# ==============================
# Main Execution
# ==============================
def main():
    json_input = "issue_data.json"
    json_output = "Output.json"

    # Load issue text
    issue_text = read_issue_from_json(json_input)
    print(f"\n🔍 Detected Issue: {issue_text}\n")

    # Load class-based recommendations
    issue_recommender = IssueRecommendations()

    # Find match
    recommendation = find_recommendation(issue_text, issue_recommender)
    
    if recommendation:
        output = {
            "Issue": issue_text,
            "Recommendation": recommendation
        }
        print("✅ Match found! Recommendation retrieved.\n")
    else:
        output = {
            "Issue": issue_text,
            "Recommendation": "No predefined recommendation found for this issue."
        }
        print("⚠️ No exact match found in the known recommendations.\n")

    # Save output as JSON file
    with open(json_output, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    # Clean human-readable terminal print (no {}, no "")
    print("📋 Final Output:")
    print("------------------------------------------------------------")
    print(f"Issue Detected: {output['Issue']}\n")
    print(f"Recommendation:\n{output['Recommendation']}")
    print("------------------------------------------------------------")
    
    print(f"\n💾 Output saved to '{json_output}'")


if __name__ == "__main__":
    main()

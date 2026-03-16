import json
import os

repo_dir = os.path.dirname(os.path.abspath(__file__))
template_file = os.path.join(repo_dir, "AI_Financial_Extraction.blueprint.json")
variables_file = os.path.join(repo_dir, "variables.json")
output_file = os.path.join(repo_dir, "AI_Financial_Extraction_Ready.json")

def main():
    if not os.path.exists(template_file):
        print(f"Error: Template file not found -> {template_file}")
        return

    if not os.path.exists(variables_file):
        print(f"Error: Variables file not found -> {variables_file}")
        return

    with open(variables_file, 'r', encoding='utf-8') as vf:
        variables = json.load(vf)

    with open(template_file, 'r', encoding='utf-8') as tf:
        content = tf.read()

    # Replace string variables
    content = content.replace("{{YOUR_EMAIL}}", str(variables.get("YOUR_EMAIL", "")))
    content = content.replace("{{YOUR_SPREADSHEET_ID}}", str(variables.get("YOUR_SPREADSHEET_ID", "")))

    # For connection IDs, we originally replaced numbers with '"{{...}}"'.
    # We must replace '"{{OPENAI_CONNECTION_ID}}"' with the actual integer number string
    # so the resulting Make.com blueprint imports correctly!
    content = content.replace('"{{OPENAI_CONNECTION_ID}}"', str(variables.get("OPENAI_CONNECTION_ID", "")))
    content = content.replace('"{{GOOGLE_CONNECTION_ID}}"', str(variables.get("GOOGLE_CONNECTION_ID", "")))

    with open(output_file, 'w', encoding='utf-8') as of:
        of.write(content)

    print(f"Successfully generated {output_file}!")
    print("WARNING: Do NOT commit this generated file or variables.json to GitHub!")

if __name__ == "__main__":
    main()

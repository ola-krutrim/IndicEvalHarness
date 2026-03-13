import argparse

import yaml


# --- Custom Dumper that can handle !function without quotes ---
class NoQuotesDumper(yaml.SafeDumper):
    pass


def tuple_presenter(dumper, data):
    tag, value = data
    # Represent scalar with a custom YAML tag, no quotes
    return dumper.represent_scalar(tag, value, style=None)


NoQuotesDumper.add_representer(tuple, tuple_presenter)
# -------------------------------------------------------------


LANGS = {
    "as": "Assamese",
    "bn": "Bengali",
    "gu": "Gujarati",
    "hi": "Hindi",
    "kn": "Kannada",
    "ml": "Malayalam",
    "mr": "Marathi",
    "or": "Odia",
    "pa": "Punjabi",
    "ta": "Tamil",
    "te": "Telugu",
    "ur": "Urdu",
}


def generate_gen_lang_yamls(output_dir: str, overwrite: bool) -> None:
    """
    Generate generation-based YAML files for each language.

    :param output_dir: The directory to output the files to.
    :param overwrite: Whether to overwrite files if they already exist.
    """
    err = []

    for lang in LANGS.keys():
        task_name = f"gen_crosssum_in_{lang}"
        file_name = f"{task_name}.yaml"
        description = f"I will first show a news article in English. Provide a summary of it in the {LANGS[lang]} language. Only output the summary and nothing else. You're given few-shot examples to help you answer."

        try:
            with open(
                f"{output_dir}/{file_name}",
                "w" if overwrite else "x",
                encoding="utf8",
            ) as f:
                yaml.dump(
                    {
                        "include": "gen_crosssum_in_common_yaml",
                        "task": task_name,
                        "description": description,
                        "process_docs": ("!function", f"utils.process_docs_{lang}"),
                    },
                    f,
                    sort_keys=False,
                    allow_unicode=True,
                    Dumper=NoQuotesDumper,
                )
        except FileExistsError:
            err.append(file_name)

    if err:
        raise FileExistsError(
            "Files were not created because they already exist "
            "(use --overwrite flag): "
            f"{', '.join(err)}"
        )


def main() -> None:
    """Parse CLI args and generate language-specific YAML files."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--overwrite",
        action="store_true",
        default=False,
        help="Overwrite files if they already exist.",
    )
    parser.add_argument(
        "--output-dir",
        default=".",
        help="Directory to write yaml files to.",
    )
    args = parser.parse_args()

    generate_gen_lang_yamls(
        output_dir=args.output_dir,
        overwrite=args.overwrite,
    )
    print(
        f"Updated gen yaml files for each language in the directory {args.output_dir}."
    )


if __name__ == "__main__":
    main()

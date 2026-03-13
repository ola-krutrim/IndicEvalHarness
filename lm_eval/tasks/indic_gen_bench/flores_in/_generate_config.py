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


LANGS = ["as", "bn", "gu", "hi", "kn", "ml", "mr", "or", "pa", "ta", "te", "ur"]


def generate_gen_lang_yamls(output_dir: str, overwrite: bool, target_lang: str) -> None:
    """
    Generate generation-based YAML files for each language.

    :param output_dir: The directory to output the files to.
    :param overwrite: Whether to overwrite files if they already exist.
    """
    err = []

    for lang in LANGS:
        if target_lang == "en":
            direction = f"{lang}_en"
        elif target_lang == "xx":
            direction = f"en_{lang}"
        task_name = "gen_flores_in"
        file_name = f"{task_name}_{direction}.yaml"

        try:
            with open(
                f"{output_dir}/{file_name}",
                "w" if overwrite else "x",
                encoding="utf8",
            ) as f:
                yaml.dump(
                    {
                        "include": "gen_flores_in_common_yaml",
                        "task": f"{task_name}_{direction}",
                        "process_docs": (
                            "!function",
                            f"utils.process_docs_{direction}",
                        ),
                        "doc_to_text": ("!function", f"utils.doc_to_text_{direction}"),
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
        output_dir=args.output_dir, overwrite=args.overwrite, target_lang="en"
    )
    print(
        f"Updated gen yaml files for each language in the directory {args.output_dir} with target language english."
    )

    generate_gen_lang_yamls(
        output_dir=args.output_dir, overwrite=args.overwrite, target_lang="xx"
    )
    print(
        f"Updated gen yaml files for each language in the directory {args.output_dir} with target language indic."
    )


if __name__ == "__main__":
    main()

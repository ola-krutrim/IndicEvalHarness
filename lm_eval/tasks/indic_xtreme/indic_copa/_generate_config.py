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


LANGS = ["as", "bn", "gu", "hi", "kn", "ml", "mr", "or", "pa", "ta", "te"]


def generate_gen_lang_yamls(output_dir: str, overwrite: bool) -> None:
    """
    Generate generation-based YAML files for each language.

    :param output_dir: The directory to output the files to.
    :param overwrite: Whether to overwrite files if they already exist.
    """
    err = []

    for lang in LANGS:
        task_name = f"gen_indic_copa_{lang}"
        file_name = f"{task_name}.yaml"

        try:
            with open(
                f"{output_dir}/{file_name}",
                "w" if overwrite else "x",
                encoding="utf8",
            ) as f:
                yaml.dump(
                    {
                        "include": "gen_indic_copa_common_yaml",
                        "task": task_name,
                        "dataset_name": f"translation-{lang}",
                        "doc_to_text": ("!function", f"utils.doc_to_text_{lang}"),
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


def generate_logprob_lang_yamls(output_dir: str, overwrite: bool) -> None:
    """
    Generate logprob-based YAML files for each language.

    :param output_dir: The directory to output the files to.
    :param overwrite: Whether to overwrite files if they already exist.
    """
    err = []

    for lang in LANGS:
        task_name = f"logprob_indic_copa_{lang}"
        file_name = f"{task_name}.yaml"

        try:
            with open(
                f"{output_dir}/{file_name}",
                "w" if overwrite else "x",
                encoding="utf8",
            ) as f:
                yaml.dump(
                    {
                        "include": "logprob_indic_copa_common_yaml",
                        "task": task_name,
                        "dataset_name": f"translation-{lang}",
                        "doc_to_text": ("!function", f"utils.doc_to_text_{lang}"),
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
    parser.add_argument(
        "--logprob",
        action="store_true",
        default=False,
        help="Generate logprob-based YAMLs instead of generation YAMLs.",
    )
    args = parser.parse_args()

    if args.logprob:
        generate_logprob_lang_yamls(
            output_dir=args.output_dir,
            overwrite=args.overwrite,
        )
        print(
            "Updated logprob yaml files for each language "
            f"in the directory {args.output_dir}."
        )
    else:
        generate_gen_lang_yamls(
            output_dir=args.output_dir,
            overwrite=args.overwrite,
        )
        print(
            "Updated gen yaml files for each language "
            f"in the directory {args.output_dir}."
        )


if __name__ == "__main__":
    main()

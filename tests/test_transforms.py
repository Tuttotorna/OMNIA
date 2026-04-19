from omnia.transforms import build_variants


def test_build_variants_returns_non_empty_list_for_valid_text() -> None:
    variants = build_variants("The answer is 4.")
    assert isinstance(variants, list)
    assert len(variants) > 0
    assert all(isinstance(v, str) for v in variants)
    assert all(v.strip() != "" for v in variants)


def test_build_variants_includes_baseline() -> None:
    text = "The answer is 4."
    variants = build_variants(text)
    assert text in variants


def test_build_variants_is_deterministic() -> None:
    text = "The answer is 4."
    v1 = build_variants(text)
    v2 = build_variants(text)
    assert v1 == v2


def test_build_variants_has_no_duplicates() -> None:
    variants = build_variants("The answer is 4.")
    assert len(variants) == len(set(variants))


def test_build_variants_strips_empty_results() -> None:
    variants = build_variants("   The answer is 4.   ")
    assert all(v.strip() != "" for v in variants)


def test_build_variants_handles_prefix_collapse() -> None:
    variants = build_variants("Answer: 4")
    assert "4" in variants


def test_build_variants_handles_lowercase_variant() -> None:
    variants = build_variants("The Answer Is 4.")
    assert "the answer is 4." in variants


def test_build_variants_returns_empty_list_for_blank_text() -> None:
    variants = build_variants("   ")
    assert variants == []


def test_build_variants_raises_on_non_string_input() -> None:
    try:
        build_variants(4)  # type: ignore[arg-type]
        assert False, "Expected TypeError"
    except TypeError:
        assert True
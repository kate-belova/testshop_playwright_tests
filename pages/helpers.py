from playwright.sync_api import expect


def assert_products_count(actual, expected):
    actual_int = int(actual) if isinstance(actual, str) else actual
    expected_int = int(expected) if isinstance(expected, str) else expected

    assert (
        actual_int == expected_int
    ), f'Products count should be {expected_int}, but got {actual_int}'


def assert_text(actual, expected):
    expect(actual).to_have_text(expected)


def get_expected_text_in_product_url_from_product_title(product_title):
    url_text = product_title.lower().strip()
    url_text = url_text.replace(' ', '-')

    return url_text

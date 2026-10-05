from extract import transform


def test_transform_cleans_text():
    rows = [{
        "customer_id": " 1 ",
        "customer_name": " nandini ",
        "city": " kochi ",
    }]

    assert transform(rows) == [{
        "customer_id": "1",
        "customer_name": "NANDINI",
        "city": "Kochi",
    }]


def test_transform_skips_blank_name():
    rows = [{
        "customer_id": "2",
        "customer_name": "   ",
        "city": "Delhi",
    }]

    assert transform(rows) == []


def test_transform_skips_none_name():
    rows = [{
        "customer_id": "3",
        "customer_name": None,
        "city": "Chennai",
    }]

    assert transform(rows) == []
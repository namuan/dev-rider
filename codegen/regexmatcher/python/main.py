import re


def rgx_extract_from_text(document, extract_query):
    compiled_rgx = re.compile(extract_query)  # Pass flags like re.IGNORECASE to amend matching process
    match = compiled_rgx.search(document)
    if match:
        # group(0) will return full match i.e. download/0.2.0/
        return match.group(1)


def rgx_find_all_with_iterator(document, search_query):
    compiled_rgx = re.compile(search_query)  # Pass flags like re.IGNORECASE to amend matching process
    return [match for match in compiled_rgx.finditer(document)]


def rgx_find_all(document, search_query):
    compiled_rgx = re.compile(search_query)  # Pass flags like re.IGNORECASE to amend matching process
    return compiled_rgx.findall(document)


def test_regex_find():
    document = """
There is a serious problem with the state of simple development tools on the internet. 
Most of the websites providing simple encoders/decoders/formatters/prettifiers are filled with ads and popups which makes it difficult and risky to use.
And then there is also a huge problem with privacy and leaking any private data that is used on any of these websites.

[DevRider](https://github.com/namuan/dev-rider) is an attempt to provide a desktop tool which includes a shell and addins for various utilities.    
    """

    found_matches = rgx_find_all(document, "tool")
    assert len(found_matches) == 2


def test_regex_find_with_positions():
    document = """
There is a serious problem with the state of simple development tools on the internet. 
[DevRider](https://github.com/namuan/dev-rider) is an attempt to provide a desktop tool which includes a shell and addins for various utilities.    
    """

    found_matches = rgx_find_all_with_iterator(document, "tool")
    assert len(found_matches) == 2
    assert found_matches[0].span() == (65, 69)
    assert found_matches[1].span() == (172, 176)


def test_regex_extract():
    document = """
[Mac OS App](https://github.com/namuan/dev-rider-osx/releases/download/0.2.0/devrider-0.2.0.zip)    
    """

    release_number = rgx_extract_from_text(document, "download/([\\d\\.]+)/")
    assert release_number == "0.2.0"

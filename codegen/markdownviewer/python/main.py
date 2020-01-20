# https://pypi.org/project/mistune/
# pip install mistune
import mistune


def md_to_html(src):
    return mistune.markdown(src)


def test_md_to_html():
    plain = "### Heading"
    md_html = "<h3>Heading</h3>"
    assert md_to_html(plain).strip() == md_html

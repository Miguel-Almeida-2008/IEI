import main
import pyshorteners

link = "google.com"


def test_copy():
    assert main.copiar_para_clipboard(link) == link


def test_shorten_and_lenghten():
    assert main.encurtar_link(link) == pyshorteners.Shortener().tinyurl.short(link)
    assert main.alongar_link(link) == pyshorteners.Shortener().tinyurl.expand(link)

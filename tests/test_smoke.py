"""Teste de fumaça: confirma que o pacote está instalado e pode ser importado."""

import observatorio


def test_pacote_importavel():
    assert observatorio.__name__ == "observatorio"

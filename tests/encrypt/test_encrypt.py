from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("mensagem", "secreta")

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(77, 8)

    result_message = encrypt_message("secreta", 3)
    mock_message = "ces_ater"

    result_message_big = encrypt_message("secreta", 7)
    mock_message_big = "aterces"

    assert mock_message == result_message
    assert mock_message_big == result_message_big

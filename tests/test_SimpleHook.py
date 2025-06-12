import pytest
import httpx
from simplehook import SimpleHook
from unittest.mock import patch, mock_open

hook = SimpleHook("")


@pytest.mark.parametrize("num", [0, 1, 36012, 65280])
def test_is_valid(num):
    assert hook.validate(color=num) == num


@pytest.mark.parametrize("num", [-1, -65280, 65281, 99999])
def test_is_invalid(num):
    with pytest.raises(ValueError, match="Value of color must be between 0 and 65280!"):
        hook.validate(num)


def test_send_message(mocker):
    mocker_post = mocker.patch.object(hook, "post")
    message = "test"
    hook.send_message(message=message)

    mocker_post.assert_called_once_with(
        json={"content": message})


def test_post(mocker):
    mocker_post = mocker.patch("httpx.Client.post")
    mocker_response = mocker_post.return_value

    mocker_response.raise_for_status = mocker.Mock()

    hook.post(json={"content": "test"})

    mocker_post.assert_called_once_with(
        url=hook.webhook_url, json={"content": "test"})
    mocker_response.raise_for_status.assert_called_once_with()


def test_post_error(mocker):
    mocker_post = mocker.patch("httpx.Client.post")
    mock_response = mocker_post.return_value
    mock_response.raise_for_status = mocker.Mock(
        side_effect=httpx.HTTPError("Error!"))

    with pytest.raises(httpx.HTTPError):
        hook.post(json={"content": "test"})


def test_send_customized_message_full(mocker):
    mocker_post = mocker.patch.object(hook, "post")
    message = "test"
    username = "test"
    avatar_url = "test"
    mention = "everyone"
    tts = True

    hook.send_customized_message(
        message=message, username=username, avatar_url=avatar_url, mention=mention, tts=tts)
    if mention is "everyone" or mention is "here":
        mocker_post.assert_called_once_with(
            json={"content": f"@{mention} {message}", "username": username, "avatar_url": avatar_url, "tts": tts})
    else:
        mocker_post.assert_called_once_with(
            json={"content": f"<@{mention}> {message}", "username": username, "avatar_url": avatar_url, "tts": tts})


def test_send_customized_message_empty_message(mocker):
    mocker_post = mocker.patch.object(
        hook, "post", side_effect=httpx.HTTPError("Error!"))

    with pytest.raises(expected_exception=httpx.HTTPError):
        hook.send_customized_message(message="")

    mocker_post.assert_called_once()


def test_send_file_error(mocker):
    mocker_post = mocker.patch.object(hook, "post")

    with pytest.raises(expected_exception=FileNotFoundError):
        hook.send_file(file_path="")

    mocker_post.assert_not_called()


def test_send_file(mocker):
    file = mock_open(read_data="Data")
    with patch("builtins.open", file):
        mocker_post = mocker.patch.object(hook, "post")
        hook.send_file("path.png")

        mocker_post.assert_called_once()


def test_send_embedded_files(mocker):
    files = mock_open()
    files.side_effect = [mock_open(read_data="Data").return_value, mock_open(
        read_data="DATA").return_value]
    with patch("builtins.open", files):
        mocker_post = mocker.patch.object(hook, "post")
        hook.send_embedded_files(paths=["path1,jpg", "path2.png"], color=241)

        mocker_post.assert_called_once()


def test_send_embedded_files_over_10(mocker):
    mocker_post = mocker.patch.object(hook, "post")

    with pytest.raises(expected_exception=ValueError, match="Cannot send more than 10 images"):
        hook.send_embedded_files(paths=["path1.png", "path1.png", "path1.png", "path1.png", "path1.png", "path1.png",
                                 "path1.png", "path1.png", "path1.png", "path1.png" "path1.png", "path1.png", "path1.png"])

    mocker_post.assert_not_called()


def test_send_embedded_files_empty(mocker):
    mocker_post = mocker.patch.object(hook, "post")

    with pytest.raises(expected_exception=FileNotFoundError):
        hook.send_embedded_files(paths=[""])

    mocker_post.assert_not_called()
    
def test_send_embedded_files_color_error(mocker):
    file = mock_open(read_data="Data")
    with patch("builtins.open", file):
        mocker_post = mocker.patch.object(hook, "post")
        
        with pytest.raises(expected_exception=ValueError, match="Value of color must be between 0 and 65280!"):
            hook.send_embedded_files(paths=["path.png"], color=-1)
        
        mocker_post.assert_not_called()

def test_create_poll(mocker):
    pass

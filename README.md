# SimpleHook 🎣

![SimpleHook](https://img.shields.io/badge/SimpleHook-Python%20Webhook%20Wrapper-brightgreen)

Welcome to **SimpleHook**, a minimalistic Python wrapper for Discord webhooks. This library simplifies the process of sending messages to Discord channels through webhooks, making it easier for developers to integrate Discord into their applications.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)
- [Releases](#releases)
- [Support](#support)

## Features

- **Asynchronous and Synchronous Support**: Choose between async and sync methods based on your needs.
- **Easy Integration**: Quickly send messages and embeds to Discord channels.
- **Lightweight**: Minimal dependencies make it easy to install and use.
- **Flexible**: Customize your messages with embeds, colors, and more.

## Installation

To install SimpleHook, use pip. Open your terminal and run:

```bash
pip install simplehook
```

## Usage

Using SimpleHook is straightforward. First, import the library and create a webhook instance with your Discord webhook URL. 

```python
from simplehook import SimpleHook

webhook = SimpleHook('YOUR_WEBHOOK_URL')
```

You can then send messages or embeds easily:

```python
# Send a simple message
webhook.send('Hello, Discord!')

# Send an embed
embed = {
    "title": "Sample Embed",
    "description": "This is an example of an embed.",
    "color": 5814783
}
webhook.send(embed=embed)
```

## Examples

### Sending a Message

Here’s how to send a simple message to your Discord channel:

```python
from simplehook import SimpleHook

webhook = SimpleHook('YOUR_WEBHOOK_URL')
webhook.send('This is a test message!')
```

### Sending an Embed

You can also send rich embeds:

```python
from simplehook import SimpleHook

webhook = SimpleHook('YOUR_WEBHOOK_URL')

embed = {
    "title": "Embed Title",
    "description": "This is an embed description.",
    "color": 16711680
}

webhook.send(embed=embed)
```

### Asynchronous Usage

If you prefer asynchronous programming, SimpleHook supports that too. Here’s an example:

```python
import asyncio
from simplehook import SimpleHook

async def send_message():
    webhook = SimpleHook('YOUR_WEBHOOK_URL')
    await webhook.send('Hello from async!')

asyncio.run(send_message())
```

## Contributing

We welcome contributions! If you want to help improve SimpleHook, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature/YourFeature`).
6. Open a pull request.

Your contributions help make SimpleHook better for everyone!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Releases

For the latest releases and updates, visit the [Releases](https://github.com/marcelo43214/simplehook/releases) section. Download the latest version and follow the installation instructions.

## Support

If you have questions or need help, feel free to open an issue in the repository. We aim to respond promptly.

---

Thank you for checking out SimpleHook! We hope it makes your Discord integration easy and efficient. For further updates, remember to visit the [Releases](https://github.com/marcelo43214/simplehook/releases) section. Happy coding!
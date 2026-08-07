\# WhatsApp Chat Viewer 2.0



> Preserve your WhatsApp conversations. Offline. Forever.



\## Overview



WhatsApp Chat Viewer (WCV) is an offline application that converts WhatsApp Android chat exports into a modern, portable and self-contained HTML archive.



The project is designed with one primary objective:



\*\*Preserve conversations with the highest possible fidelity while keeping the generated archive readable for many years.\*\*



Unlike cloud-based viewers, WCV never uploads conversations or media to external services. Everything happens locally on your computer.



\---



\## Core Principles



\* 📁 \*\*Offline First\*\* — No Internet connection is required.

\* 🔒 \*\*Privacy by Design\*\* — Your conversations never leave your device.

\* 📖 \*\*Faithful Rendering\*\* — Preserve the original conversation as accurately as possible.

\* ⚡ \*\*Performance\*\* — Handle conversations ranging from a few messages to hundreds of thousands.

\* 🛠 \*\*Maintainability\*\* — Clean architecture and long-term sustainability.

\* 📦 \*\*Portable Output\*\* — Generate a self-contained HTML archive that can be opened years later.



\---



\## Current Status



Current version:



```text

2.0.0-dev001

```



Project stage:



```text

Pre-Alpha

```



Development has officially started.



\---



\## Planned Features



\* Parse WhatsApp Android exported chats

\* Preserve multiline messages

\* Detect media attachments automatically

\* Generate modern HTML conversations

\* Image gallery

\* Audio and video playback

\* Document previews

\* Search inside conversations

\* Conversation statistics

\* Offline operation

\* Long-term archive preservation



\---



\## Project Structure



```text

src/

&#x20;   wcv/

&#x20;       core/

&#x20;       domain/

&#x20;       engine/

&#x20;       parser/

&#x20;       classifier/

&#x20;       renderer/

&#x20;       services/

&#x20;       utils/

&#x20;       workspace/



tests/



docs/



examples/



quality/

```



\---



\## Requirements



\* Python 3.12 or newer



\---



\## Installation



```bash

git clone https://github.com/<username>/whatsapp-chat-viewer.git



cd whatsapp-chat-viewer



python -m venv .venv



\# Windows

.venv\\Scripts\\activate



\# Linux / macOS

source .venv/bin/activate



pip install -e .\[dev]

```



\---



\## Running



Display the application version:



```bash

python -m wcv --version

```



Run the application:



```bash

python -m wcv

```



\---



\## Development



Development follows these principles:



\* Architecture-first design

\* Incremental implementation

\* Automated testing

\* Strict type checking

\* Continuous code review



Every completed task must satisfy the project's Definition of Done before being merged.



\---



\## License



This project is released under the MIT License.



\---



\## Project Philosophy



WhatsApp Chat Viewer is \*\*not\*\* intended to be another WhatsApp client.



Its purpose is to become a reliable digital preservation tool that allows conversations to remain accessible for many years without depending on WhatsApp or any online service.



The guiding principle of the project is simple:



> Preserve the conversation.

> Preserve the context.

> Preserve the memories.



\---



\## Project Status



🚧 Active Development




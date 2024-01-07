# Todoist-Google-Keep-Shopping-List

Automatically move your Google Assistant shopping list tasks to Todoist

## Configuration

Open `shopping-list.py` and set your API token and Google credentials at the top of the file

## Usage

Check your Python version and make sure version 3.9 or newer is installed on your system:

```sh
python3 --version
```

Install required python3 modules:

```sh
pip3 install todoist-api-python keyring keyrings.cryptfile gkeepapi
```

Run the script to automatically move your Google Assistant shopping list items to Todoist

```sh
python3 shopping-list.py
```

## License

Copyright (C) 2022 Sam Steele. Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

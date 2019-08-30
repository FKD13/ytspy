# YTSPY

## Requirements

You will need:

- `python3` version 3.6 or higher. Because I am using f strings.
- `pip3`.
- a Unix Machine running bash.
- `mpv` installed and in your PATH
- `youtube-dl` installed and in your PATH

## Installation

### Automatic Install 

clone the repo in the desired folder and run

```bash
./install.sh
```

this will create a virtualenviroment if none there isn't one and download the `colorama` package if not installed already.

### Manual Install

Create a new virtualenviroment under `./venv`. This has to be called venv because that's the venv it will try to use when launching `./player.sh`.

activate the new venv:

```bash
source venv/bin/activate
```

then install the package `colorama`:

```bash
pip install colorama
```

then leave the venv using:

```bash
deactivate
```

Now you are good to go

## Usage

Launch the player using:

```bash
./player.sh [options]
```

with `options`:

- `--video`: enable video playback

When in the player you can use following commands:

- `search [search-term]` search for a term, returns a list with id's.
- `play [id]` add a video to playlist using the id generated in the search cmd.
- `list` list a search results.
- `skip` skip a song.
- `q` or `quit` quit.

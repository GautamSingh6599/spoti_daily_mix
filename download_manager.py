import os

import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth
from textual.app import App, ComposeResult
from textual.widgets import DataTable, Footer, Header

load_dotenv()


scope = "playlist-read-private"
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        os.getenv("SPOTIFY_CLIENT_ID"),
        os.getenv("SPOTIFY_CLIENT_SECRET"),
        os.getenv("SPOTIFY_REDIRECT_URI"),
        scope=scope,
    )
)

ROWS = [("Playlist", "Owner")]
for items in sp.current_user_playlists(limit=50)["items"]:
    display_name = sp.user(items["owner"]["external_urls"]["spotify"][30:])[
        "display_name"
    ]
    ROWS.append((items["name"], display_name))


class Download_Manager(App):
    """A Textual app to manage spotify playlist downloads."""

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield DataTable()
        yield Footer()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns(*ROWS[0])
        table.add_rows(ROWS[1:])
        table.cursor_type = "row"

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark


if __name__ == "__main__":
    app = Download_Manager()
    app.run()

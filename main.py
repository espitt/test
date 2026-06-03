"""
MyApp - Main entry point
Checks for updates on startup, then launches the main window.
"""

import tkinter as tk
from updater import UpdateWizard

APP_VERSION = "2.0.0"
GITHUB_REPO = "your-username/your-repo"   # <-- change this


def launch_main_app(root: tk.Tk):
    """Replace the update wizard with the real application UI."""
    root.title(f"MyApp v{APP_VERSION}")
    root.geometry("700x450")
    root.configure(bg="#0f0f0f")

    # ── Demo main UI ──────────────────────────────────────────
    header = tk.Frame(root, bg="#0f0f0f")
    header.pack(fill="x", padx=30, pady=(30, 0))

    tk.Label(
        header,
        text="MyApp",
        font=("Segoe UI", 28, "bold"),
        fg="#ffffff",
        bg="#0f0f0f",
    ).pack(side="left")

    tk.Label(
        header,
        text=f"v{APP_VERSION}",
        font=("Segoe UI", 12),
        fg="#555555",
        bg="#0f0f0f",
    ).pack(side="left", padx=(10, 0), pady=(12, 0))

    tk.Label(
        root,
        text="Your application content goes here.",
        font=("Segoe UI", 13),
        fg="#888888",
        bg="#0f0f0f",
    ).pack(expand=True)


def main():
    root = tk.Tk()
    root.withdraw()          # hide until update check is done

    def on_update_done():
        """Called by UpdateWizard when it's finished (skip or done)."""
        launch_main_app(root)
        root.deiconify()

    UpdateWizard(root, APP_VERSION, GITHUB_REPO, on_update_done)
    root.mainloop()


if __name__ == "__main__":
    main()

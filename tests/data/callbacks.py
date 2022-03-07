def on_download_start(api, gid):
    print(f"started {gid}")


def on_download_pause(api, gid):
    print(f"paused {gid}")

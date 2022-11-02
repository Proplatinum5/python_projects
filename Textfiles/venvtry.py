function virtualenv_info {
    # Get Virtual Env
    if [[ -n "$VIRTUAL_ENV" ]]; then
        # Strip out the path and just leave the env name
        echo "(venv:${VIRTUAL_ENV##*/})"
    
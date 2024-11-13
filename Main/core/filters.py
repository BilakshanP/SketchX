from pyrogram.filters import Filter, create # type: ignore

from Main.core.helpers.filter_helper import sudo as _sudo

sudo_filter: Filter = create(_sudo, "Sudo Filter")
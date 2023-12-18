from pyrogram import filters

from Main.core.helpers.filter_helper import sudo as _sudo # type: ignore

sudo_filter: filters.Filter = filters.create(_sudo) # type: ignore
from pyrogram import filters

from Main.core.helpers.filter_helper import sudo as _sudo

sudo_filter: filters.Filter = filters.create(_sudo)
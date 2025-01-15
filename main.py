#!/usr/bin/env python3

'''
Contact - A Console UI for Meshtastic by http://github.com/pdxlocations
Powered by Meshtastic.org
V 1.0.1
'''

import curses
from pubsub import pub
import os

from utilities.arg_parser import setup_parser
from utilities.interfaces import initialize_interface
from message_handlers.rx_handler import on_receive
from ui.curses_ui import main_ui, draw_splash
from utilities.utils import get_channels, get_node_list
from db_handler import init_nodedb, load_messages_from_db
import globals

# Set environment variables for ncurses compatibility
os.environ["NCURSES_NO_UTF8_ACS"] = "1"
os.environ["TERM"] = "screen"
os.environ["LANG"] = "C.UTF-8"

def main(stdscr):
    draw_splash(stdscr)
    parser = setup_parser()
    args = parser.parse_args()
    globals.interface = initialize_interface(args)
    globals.channel_list = get_channels()
    pub.subscribe(on_receive, 'meshtastic.receive')
    globals.node_list = get_node_list()
    init_nodedb()
    load_messages_from_db()
    main_ui(stdscr)


if __name__ == "__main__":
    curses.wrapper(main)

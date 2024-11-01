#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from heimdallr.server.board_layout import get_body, get_footer, get_header, get_menu

__author__ = "Christian Heider Nielsen"
__doc__ = ""

from dash import html


def get_root_layout(development=False) -> html.Div:
    """description"""
    return html.Div(
        [
            get_header(),
            *(get_menu() if development else None,),
            *get_body(),
            get_footer(),
        ],
        className="container-fluid",
    )

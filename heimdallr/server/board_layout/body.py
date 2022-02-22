#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Christian Heider Nielsen"
__doc__ = r"""

           Created on 15/03/2020
           """

from dash import dcc, html

from heimdallr.configuration.heimdallr_config import (
    CALENDAR_ID,
    CALENDAR_INTERVAL_ID,
    CALENDAR_INTERVAL_MS,
    DU_INTERVAL_ID,
    DU_INTERVAL_MS,
    DU_TABLES_ID,
    GPU_GRAPHS_ID,
    GPU_INTERVAL_ID,
    GPU_INTERVAL_MS,
    GPU_TABLES_ID,
)

__all__ = ["get_body"]


def get_body() -> html.Div:
    """ """
    return html.Div(
        [
            html.Div(
                [
                    html.Div([], id=CALENDAR_ID),
                    dcc.Interval(
                        id=CALENDAR_INTERVAL_ID,
                        interval=CALENDAR_INTERVAL_MS,
                        n_intervals=0,
                    ),
                ],
                className="col p-2",
            ),
            html.Div([html.Div([], id=GPU_GRAPHS_ID)], className="col"),
            html.Div(
                [
                    html.Div([], id=GPU_TABLES_ID),
                ],
                className="col p-2",
            ),
            dcc.Interval(id=GPU_INTERVAL_ID, interval=GPU_INTERVAL_MS, n_intervals=0),
            html.Div(  # Disk Usage
                [
                    html.Div([], id=DU_TABLES_ID),
                ],
                className="col p-2",
            ),
            dcc.Interval(id=DU_INTERVAL_ID, interval=DU_INTERVAL_MS, n_intervals=0),
        ],
        className="row p-3",
    )

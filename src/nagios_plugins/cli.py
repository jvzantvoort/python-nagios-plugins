# coding: utf-8
"""Command line handling."""

import logging
import click

class State:
    """Maintain logging level."""

    def __init__(self, log_name='nagios-plugins', level=logging.INFO):
        self.logger = logging.getLogger(log_name)
        self.logger.propagate = False
        stream = logging.StreamHandler()
        formatter = logging.Formatter("%(levelname)s %(funcName)s:  %(message)s")
        stream.setFormatter(formatter)
        self.logger.addHandler(stream)

        self.logger.setLevel(level)

# pylint: disable=C0103
pass_state = click.make_pass_decorator(State, ensure=True)

def verbose_option(f):
    """Set more verbose options"""
    def callback(ctx, param, value):
        state = ctx.ensure_object(State)
        if value:
            state.logger.setLevel(logging.DEBUG)
    return click.option('-v', '--verbose',
                        is_flag=True,
                        expose_value=False,
                        help='enable verbose output',
                        callback=callback)(f)

def quiet_option(f):
    """Set less verbose options"""
    def callback(ctx, param, value):
        state = ctx.ensure_object(State)
        if value:
            state.logger.setLevel(logging.ERROR)
    return click.option('-q', '--quiet',
                        is_flag=True,
                        expose_value=False,
                        help='silence warnings',
                        callback=callback)(f)

def verbosity_options(f):
    """set verbosity options"""
    f = verbose_option(f)
    f = quiet_option(f)
    return f

def add_options(options):
    """ Given a list of click options this creates a decorator that
    will return a function used to add the options to a click command.
    :param options: a list of click.options decorator.
    """
    def _add_options(func):
        """ Given a click command and a list of click options this will
        return the click command decorated with all the options in the list.
        :param func: a click command function.
        """
        for option in reversed(options):
            func = option(func)
        return func
    return _add_options

@click.group(context_settings={'help_option_names': ['-h', '--help']})
@click.version_option("0.0.1", '-V', '--version')
def cli():
    """
    Nagios Plugins
    """

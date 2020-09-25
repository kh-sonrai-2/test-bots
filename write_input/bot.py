import logging


def run(ctx):
    config = ctx.config
    # Get custom fields
    if config:
        ticket = config.get("data")
        logging.info(ticket)

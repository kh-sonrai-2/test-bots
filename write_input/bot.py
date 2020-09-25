import logging


def run(ctx):
    config = ctx.config
    logging.info("What is in the config?")
    logging.info(config)
    # Get custom fields
    if config:
        ticket = config.get("data")
        logging.info("What is in the ticket?")
        logging.info(ticket)

    logging.info("Ticket Evidence:")
    logging.info(ctx.get_policy_evidence())

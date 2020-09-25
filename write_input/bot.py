import logging


def run(ctx):
    data_enum = ctx.get_policy_evidence_data()
    logging.info(data_enum)
    for thing in data_enum:
        logging.info(thing)
        logging.info(str(thing))
        logging.info(type(thing))

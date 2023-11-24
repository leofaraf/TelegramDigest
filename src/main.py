import logging
import time

import schedule
from telethon import utils

import telegram
import settings

import ai
import excel


def main():


    channels = excel.read_channels()
    logging.info("Have loaded channels: {}".format(channels))

    summaries = get_summaries_by_channels(channels)

    logging.info(f"have found {len(summaries)} summaries")

    if summaries:
        post = settings.DIGEST_FORMAT.format("\n\n".join(summaries))
        logging.info(f"this post will have send: \"{post}\"")
        telegram.send_post(post)
    else:
        logging.error("summaries weren't found")
    telegram.log_out()


def get_summaries_by_channels(channels):
    summaries = []
    for channel in channels:
        messages = telegram.get_today_message(channel)
        if not messages:
            continue

        title = None
        summary_len = 0
        summary_buf = []
        for message in messages:
            if title is None and message.chat:
                chat_from = message.chat  # telegram MAY not send the chat enity
                chat_title = utils.get_display_name(chat_from)
                title = chat_title

            text = message.message
            if text:
                if (summary_len + len(text)) < settings.MAX_CHANNEL_BUFFER_LIMIT:
                    summary_buf.append(text)
                    summary_len += len(text)
                    logging.debug(f"channel buffer length: "
                                  f"[{summary_len}/{settings.MAX_CHANNEL_BUFFER_LIMIT}]")
                else:
                    logging.debug("message is skipped because buffer is full")

        if summary_buf:
            text = ai.get_summary_text("\n".join(summary_buf)).strip()
            # uncomment code under if you need disable ai-summarization
            # text = "\n".join(summary_buf)
            summaries.append(
                slice_summary_if_too_long(
                    settings.SUMMARY_FORMAT.format(title, text)
                )
            )
        else:
            logging.info("program haven't found message in channel")
    return summaries


# 1. chatgpt can don't understand your role and write a lot of text thus it can slice trash
# 2. it where is many of content chatgpt can give your real big summary
def slice_summary_if_too_long(summary):
    logging.debug(f"summary length: {len(summary)}")
    # if mx_sm_ln = 0 then we just skip slicing
    if settings.MAX_SUMMARY_LENGTH != 0 and len(summary) > settings.MAX_SUMMARY_LENGTH:
        return summary[0:settings.MAX_SUMMARY_LENGTH] + "..."
    return summary


# gateway
if __name__ == "__main__":
    logging.basicConfig(filename='app.log', filemode='a',
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
    logging.info("Program has started")

    # uncomment code under if you wanna write hardcode value to excel db-file
    # excel.write_channels_hardcode("itbeard", "aiapodcast")

    schedule.every().day.at(settings.SCHEDULE_AT).do(main)
    # main()

    logging.info("Program has moved into scheduling state")

    while True:
        schedule.run_pending()
        time.sleep(1)



import json
import ijson
import re
import spacy
from datetime import datetime


def _get_json_from_file(path: str) -> json:
    try:
        with open(path, "r") as file:
            data = json.load(file)
    except FileNotFoundError as e:
        print(f"Error: {path} no found")
    except json.JSONDecodeError as e:
        print(f"Error: Failed to decode JSON from the file. Detaisl: {e}")
    return data


def _extract_from(_from: str) -> str:
    resp = _from.split("_")[0]
    return resp


def _is_after_date(chosed_date: str, after_date: str) -> bool:
    format_pattern = "%Y-%m-%dT%H:%M:%SZ"

    chosed_date_obj = datetime.strptime(chosed_date, format_pattern)
    after_date_obj = datetime.strptime(after_date, format_pattern)

    return after_date_obj > chosed_date_obj


def _extract_emails(text: str) -> list[str]:
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}+"
    return re.findall(pattern=pattern, string=text)


def _get_from_allowed_domais(emails_list: list[str], allowed_domais: list[str]) -> list:
    return [
        email for email in emails_list for domain in allowed_domais if domain in email
    ]


def iter_messages_from_files(path: str):
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            # each line is a small JSON object
            msg = json.loads(line)
            yield msg


def _iter_messages_from_big_json(path: str):
    with open(path, "r", encoding="utf-8") as f:
        for msg in ijson.items(f, "messages.item"):
            yield msg


def extract_email_from_chat_file_streaming(
    file_path: str,
    allowed_domains: list[str],
    min_timestamp: str,
) -> list[str]:
    emails_list = []
    for message in _iter_messages_from_big_json(path=file_path):
        _from = message.get("from", None)
        date = message.get("timestamp", None)
        text = message.get("text", None)
        if (
            _from
            and date
            and text
            and _extract_from(_from) == "user"
            and _is_after_date(min_timestamp, date)
        ):
            extract_emails = _extract_emails(text)
            extract_emails = list(set(extract_emails))
            emails_list += _get_from_allowed_domais(extract_emails, allowed_domains)
    return emails_list


def extract_email_from_chat_file(
    file_path: str,
    allowed_domains: list[str],
    min_timestamp: str,
) -> list[str]:
    data = _get_json_from_file(file_path)
    emails_list = []
    for message in data["messages"]:
        _from = message.get("from", None)
        date = message.get("timestamp", None)
        text = message.get("text", None)
        if (
            _from
            and date
            and text
            and _extract_from(_from) == "user"
            and _is_after_date(min_timestamp, date)
        ):
            extract_emails = _extract_emails(text)
            extract_emails = list(set(extract_emails))
            emails_list += _get_from_allowed_domais(extract_emails, allowed_domains)

    return emails_list


def extract_email_from_nlp(
    file_path: str,
    allowed_domains: list[str],
    min_timestamp: str,
) -> list[str]:
    # extract emails using nlp spacy
    emails_list = []
    nlp = spacy.load("en_core_web_sm")
    for message in _iter_messages_from_big_json(path=file_path):
        _from = message.get("from", None)
        date = message.get("timestamp", None)
        text = message.get("text", None)
        if (
            _from
            and date
            and text
            and _extract_from(_from) == "user"
            and _is_after_date(min_timestamp, date)
        ):
            doc = nlp(text)
            extracted_emails_set = {token.text for token in doc if token.like_email}
            extracted_emails_list = list(extracted_emails_set)
            emails_list += _get_from_allowed_domais(
                extracted_emails_list, allowed_domains
            )
    return emails_list


emails_list = extract_email_from_chat_file_streaming(
    file_path="logs.json",
    allowed_domains=["example.com", "gmail.com"],
    min_timestamp="2025-12-14T12:34:09Z",
)

emails_list_nlp = extract_email_from_nlp(
    file_path="logs.json",
    allowed_domains=["example.com", "gmail.com"],
    min_timestamp="2025-12-14T12:34:09Z",
)

print(emails_list_nlp)

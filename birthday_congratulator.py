import pandas as pd
from datetime import datetime
import random
import requests
import webbrowser
import numpy as np
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
URL = "GOOGLE SHEETS CSV URL"
BROWSER = "firefox"  # replace with browser, e.g. "chrome","safari",...


def fix_datetime(date: str):
    return datetime.strptime(date, "%d/%m/%Y").strftime("%d-%m")


def get_birthdays(today: str, df: pd.DataFrame, birthday_column: str):
    return df[df[birthday_column] == today]


def create_whatsapp_string(phone: str, text: str):
    return f"https://api.whatsapp.com/send/?phone={phone}&text={text}&type=phone_number&app_absent=0"


def create_congratulation_string(
    name: str, language: str, emojis: list, nemojis: int = 2
):
    try:
        with open(f"texts/{language}.txt") as f:
            options = f.readlines()

        choice = random.choice(options)
        if name:
            choice = choice.replace("*", name)
        else:
            choice = choice.replace(" *", "")

        for _ in range(nemojis):
            choice += random.choice(emojis)
        choice = choice.replace("\n", "")
        return choice
    except Exception as e:
        print(e)


def format_text(text: str):
    text = "+".join(text.split())
    return text


def open_url(url: str):
    webbrowser.get(BROWSER).open_new_tab(url)


def download_last_version(
    url: str = URL,
    df_path: str = "birthdays.csv",
):
    with open(df_path, "wb") as f:
        resp = requests.get(
            url,
            verify=False,
        )
        f.write(resp.content)


def logic(
    df_path: str = "birthdays.csv",
    birthday_column: str = "Birthday",
    emojis_path: str = "texts/emojis.txt",
):
    download_last_version()
    with open(emojis_path) as f:
        emojis = f.readlines()

    df = pd.read_csv(df_path)
    today = datetime.today().strftime("%d-%m")
    df[birthday_column] = df[birthday_column].apply(fix_datetime)
    df = df.fillna("")
    birthdays = list(get_birthdays(today, df, birthday_column).T.to_dict().values())
    if birthdays:
        for birthday in birthdays:
            name = birthday["Name"]
            language = birthday["Language"]
            number = birthday["Number"]
            text = create_congratulation_string(name, language, emojis)
            text = format_text(text)
            url = create_whatsapp_string(number, text)
            open_url(url)
    else:
        print("No birthdays today!")


if __name__ == "__main__":
    logic()

### Whatsapp Birthday congratulator script

I usually forget to congratulate people on their birthday so decided to make a tiny script for it. 

Uses a Google Sheets csv to track birthday and sends an api request that should open your local Whatsapp app. You still need to press send (reduces moral guilt). I run the script on startup.

Default browser is firefox. Can be changed [here](https://github.com/Dauriel/WhatsAppBirthdayBot/blob/8070b1220cdeef34f6a3924b63a8ed9d80473046/birthday_congratulator.py#L11)

#### Default CSV example:

| Name  | Birthday   | Number   | Language |
| ----- | ---------- | -------- | -------- |
| John  | 02/01/2023 | 49xxxxxx | EN       |
| Maria | 09/02/2023 | 34xxxxx  | ES       |

Year gets parsed out.

#### Google Sheets csv setup:

1. Open sheet
2. Click on share
3. Allow anyone with the link
4. Copy link, replace `edit?usp=sharing`with `export?gid=0&format=csv`
5. Paste link where [URL](https://github.com/Dauriel/WhatsAppBirthdayBot/blob/8070b1220cdeef34f6a3924b63a8ed9d80473046/birthday_congratulator.py#L10)

#### Text generation

Text is generated in selected language. Asterisk (*) is replaced by person's name. Emojis are chosen at random from the emoji list (default 2 emojis).

##### Languages supported:

- English (EN)

- Spanish (ES)


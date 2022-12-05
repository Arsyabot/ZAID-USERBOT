from os import getenv

API_ID = int(getenv("API_ID", "12957350")) #optional
API_HASH = getenv("API_HASH", "d2c85cdb7406e1583df0b1a66da4a8fe") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
OWNER_ID = int(getenv("OWNER_ID", "5089916692"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://userby:userby@cluster0.e6t8egn.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "5680740751:AAEyL7-IFs2xpemSNL6Y7-WWHzumibmKOns")
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP", "-1001577649059")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQBqchapZAWs_x0DvA5AGBksxmMzaIK49TJBeHPtUKN9xfjZYV5aGKddQWeKh5wg8VU6Hk5pKXuhj1foDg_NMblrn3wFeWb39DPL8PZtbzvjX0GDqAiauvpG7fqV8kefmDrtRfV4j93vyuXf0Px_seLJeBoGgHkVzCU5TrxCRXhYeXxLHrUY_dj4bVaK5xwdF54Q6hQB8DLI0Nauzv06OLuPo9x1vgaQlUd7Z6oC10nvVc_aGInxqWupNy0hy9v5_wJ5nl_0URTRH7D31Y5NIxsbgXlzAvbJCsqkSpFBApxCejGcMY7608QbYTT-fjEooOIc5kEg489xXGReyfaX6DkNAAAAAS9h9xQA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton



START_MESSAGE = '''**{},
I am Tajlink Converter Bot. I Can Convert Links Directly From Your tajlink.com Account,
    
Go To** 👉 https://tajlink.com/member/tools/api?connect=true
**🤗 Than Hit Start If You're Redirected To Bot.**

Other Ways 👇

1. **Go To** 👉 https://tajlink.com/member/tools/api
2. **Than Copy** API Key
3. **Than Type** `/api` than give a single space and than paste your API Key
**(see example to understand more...)**

/api <space> API Key 
(See Example.👇)
**Example:**
 `/api 152e6e7bd9c664b0b693ceb5f84ddb900dcbe00c `

**🤘 Hit** 👉 /features To Know More Features Of This Bot.
**💁‍♀️ Hit** 👉 /help To Get Help.
**➕ Hit** 👉 /channel To Get Help About Adding your channel to bot.
**➕ Hit** 👉 /footer To Get Help About Adding your Custom Footer to bot.

If You are new to tajlink then click on below button to create your account.'''

HELP_MESSAGE = '''**{},**

ɪ  ᴄᴀɴ  ᴄᴏɴᴠᴇʀᴛ  ᴀɴʏ  ᴅɪʀᴇᴄᴛ  ʟɪɴᴋ  ɪɴᴛᴏ  ʏᴏᴜʀ  ᴜʀʟ  ꜱʜᴏʀᴛᴇʀɴ  ʟɪɴᴋꜱ.
    
𝟏.  ɢᴏ  ᴛᴏ  👉  https://tajlink.com/member/tools/api
  
𝟐.  ᴛʜᴀɴ  ᴄᴏᴘʏ  **ᴀᴘɪ  ᴋᴇʏ**

𝟑.  ᴛʜᴀɴ  ᴛʏᴘᴇ  **/api  ʏᴏᴜʀ  ᴀᴘɪ  ᴋᴇʏ**


🗣️   𝐄𝐱𝐚𝐦𝐩𝐥𝐞:

`/api 152e6e7bd9c664b0b693ceb5f84ddb900dcbe00c `


🗣️  /features  ᴛᴏ  ᴋɴᴏᴡ  ᴍᴏʀᴇ  ꜰᴇᴀᴛᴜʀᴇꜱ  ᴏꜰ  ᴛʜɪꜱ  ʙᴏᴛ.

𝐍𝐎𝐓𝐄 :  ꜰᴏʀ  ᴅᴇᴛᴀɪʟꜱ 👇 👇'''

ABOUT_TEXT = '''**
I am Tajlink Converter Bot. I Can Convert Links Directly From Your tajlink.com Account,**

**⚡Features⚡**

**• I can Convert any links or posts to your Tajlink / post. (Button Links Posts, Hidden links/Hyperlinks All Are Supported)**

**• I can Convert unlimited tajlink.com links at once.** (if you are sending a list of urls.)

**• No need to share password or email to convert links.**

**• I Can auto add custom footer text to your every post. Hit 👉 /footer To know more...**

**• I Can auto add custom Header text to your every post. Hit 👉 /Header To know more...**

**• I Can replace / remove other's channel links with your channel link. Hit 👉 /channel To know More...**

**• I Can Automatically Replace Your Banner Image To images in the post. Hit  👉/Banner_image To Know More...**

 Anyone who want to use any **other shortner** instead of Tajlink than **contact to owner** (all **shortners support** available.)'''

CUSTOM_ALIAS_MESSAGE = """For Custom Alias, `[link] | [custom_alias]`, Send in this format

This feature works only in private mode only

Ex: https://telegram.me/RnpUpdate | Rnp Update"""


ADMINS_MESSAGE = """
List of Admins who has access to this Bot

{admin_list}
"""

ABOUT_REPLY_MARKUP = InlineKeyboardMarkup([

    [
        InlineKeyboardButton('ᴄᴏɴᴛᴀᴄᴛ  ᴛ𝚘  𝙾ᴡɴᴇʀ  ❣️', url='https://telegram.dog/MrRnp')
        
    ],


])

HELP_REPLY_MARKUP = InlineKeyboardMarkup([

    [
        InlineKeyboardButton('ᴄᴏɴᴛᴀᴄᴛ  ᴛ𝚘  𝙾ᴡɴᴇʀ  ❣️', url='https://telegram.dog/MrRnp')
        
    ],


])

START_MESSAGE_REPLY_MARKUP  = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('🪄  Connect  To  Tajlink  ⚙️', url=f'https://tajlink.com/ref/technorohanyt')
    ]
])



BACK_REPLY_MARKUP = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('Back', callback_data=f'help_command')
    ],

])

USER_ABOUT_MESSAGE = """
- Website: [{base_site}](https://tajlink.com/ref/technorohanyt)

- Site Link:
 {base_site}

- Current Linked API:
{shortener_api}

- Channel Username: 
@{username}

- Header Text: 
{header_text}

- Footer Text: 
{footer_text}

- Banner Image: 
{banner_image}
"""


SHORTENER_API_MESSAGE = """To add or update your Shortner Website API, 
`/api [api]`
            
Ex: `/api 152e6e7bd9c664b0b693ceb5f84ddb900dcbe00c `

Get API From [{base_site}](https://tajlink.com/ref/technorohanyt)

Current: {base_site} 
API: `{shortener_api}`"""

HEADER_MESSAGE = """Reply to the Header Text You Want

This Text will be added to the top of every message caption or text

For adding line break use \n
To Remove Header Text: `/header remove`"""

FOOTER_MESSAGE = """**Reply to the Footer Text You Want**

This Text will be added to the **bottom** of every message **caption** or text

For adding **line break** use \n
To Remove Footer Text: `/footer remove`


𝐄𝐱𝐚𝐦𝐩𝐥𝐞:

`/footer
━━━━━━━━━━━━━━━━━
💁‍♀️ How To Download 👇
👉 https://youtube.com/@RnpUpdate
━━━━━━━━━━━━━━━━━
🔥 𝐉𝐨𝐢𝐧 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 🔥
👉 https://telegram.dog/RnpUpdate`
"""

USERNAME_TEXT = """**ᴘʟᴇᴀꜱᴇ  ᴛʏᴘᴇ  ɪɴ  ɢɪᴠᴇɴ  ꜰᴏʀᴍᴀᴛ

/channel (channel link or username)


𝐄𝐱𝐚𝐦𝐩𝐥𝐞:

/channel @RnpUpdate

𝐎𝐫

`/channel https://telegram.dog/RnpUpdate`


👉 /features  ᴛᴏ  ᴋɴᴏᴡ  ᴍᴏʀᴇ  ꜰᴇᴀᴛᴜʀᴇꜱ  ᴏꜰ  ᴛʜɪꜱ  ʙᴏᴛ."""

BANNER_IMAGE = """
Usage: `/banner_image image_url` or reply to any Image with this command

This image will be automatically replaced with other images in the post

To remove custom image, `/banner_image remove`

Eg: `/banner_image https://telegra.ph/file/5e96340a91470256b387a.jpg`"""


BANNED_USER_TXT = """
Usage: `/ban [User ID]`

Usage: `/unban [User ID]`

List of users that are banned:

{users}
"""

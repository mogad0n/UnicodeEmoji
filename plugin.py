###
# Copyright (c) 2020, mogad0n
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###

from supybot import utils, plugins, ircutils, callbacks
from supybot.commands import *
try:
    from supybot.i18n import PluginInternationalization
    _ = PluginInternationalization('UnicodeEmoji')
except ImportError:
    # Placeholder that allows to run the plugin on a bot
    # without the i18n module
    _ = lambda x: x

emoji = {'innocent':'ʘ‿ʘ',
        'disapproval':'ಠ_ಠ',
        'tableflip':'(╯°□°）╯︵ ┻━┻',
        'putbacktable':'┬─┬﻿ ノ( ゜-゜ノ)',
        'tidy-up':'┬─┬⃰͡ (ᵔᵕᵔ͜ )',
        'double-Flip':'┻━┻ ︵ヽ(`Д´)ﾉ︵﻿ ┻━┻',
        'fisticuffs':'ლ(｀ー´ლ)',
        'cute-bear':'ʕ•ᴥ•ʔ',
        'squinting-bear':'ʕᵔᴥᵔʔ',
        'gtfo-bear':'ʕ •`ᴥ•´ʔ',
        'cuteface':'(｡◕‿◕｡)',
        'surprised':'（　ﾟДﾟ）',
        'shrug-face':'¯\\_(ツ)_/¯',
        'meh':'¯\\(°_o)/¯',
        'feel-perky':'(`･ω･´)',
        'angry-face':'(╬ ಠ益ಠ)',
        'at-what-cost':'ლ(ಠ益ಠლ)',
        'excited':'☜(⌒▽⌒)☞',
        'running':'ε=ε=ε=┌(;*´Д`)ﾉ',
        'happy-face':'ヽ(´▽`)/',
        'glory':'ヽ(´ー｀)ノ',
        'kitty-emote':'ᵒᴥᵒ#',
        'fido':'V•ᴥ•V',
        'meow':'ฅ^•ﻌ•^ฅ',
        'cheers':'（ ^_^）o自自o（^_^ ）',
        'devious':'ಠ‿ಠ',
        '4chan':'( ͡° ͜ʖ ͡°)',
        'crying':'ಥ_ಥ',
        'breakdown':'ಥ﹏ಥ',
        'disagree':'٩◔̯◔۶',
        'flexing':'ᕙ(⇀‸↼‶)ᕗ',
        'do-you-even-lift-bro?':' ᕦ(ò_óˇ)ᕤ',
        'kirby':'⊂(◉‿◉)つ',
        'tripping-out':'q(❂‿❂)p',
        'discombobulated':'⊙﹏⊙',
        'sad-and-confused':'¯\\_(⊙︿⊙)_/¯',
        'japanese-lion-face':'°‿‿°',
        'confused':'¿ⓧ_ⓧﮌ',
        'confused-scratch':'(⊙.☉)7',
        'worried':'(´･_･`)',
        'dear-god-why':'щ（ﾟДﾟщ）',
        'staring':'٩(๏_๏)۶',
        'pretty-eyes':'ఠ_ఠ',
        'strut':'ᕕ( ᐛ )ᕗ',
        'zoned':'(⊙_◎)',
        'crazy':'ミ●﹏☉ミ',
        'trolling':'༼∵༽ ༼⍨༽ ༼⍢༽ ༼⍤༽',
        'angry-troll':'ヽ༼ ಠ益ಠ ༽ﾉ',
        'fuck-it':'t(-_-t)',
        'sad-face':'(ಥ⌣ಥ)',
        'hugger':'(づ￣ ³￣)づ',
        'stranger-danger':'(づ｡◕‿‿◕｡)づ',
        'flip-friend':'(ノಠ ∩ಠ)ノ彡( \\o°o)\\',
        'cry-face':'｡ﾟ( ﾟஇ‸இﾟ)ﾟ｡',
        'cry-troll':'༼ ༎ຶ ෴ ༎ຶ༽',
        'tgif':'“ヽ(´▽｀)ノ”',
        'dancing':'┌(ㆆ㉨ㆆ)ʃ',
        'sleepy':'눈_눈',
        'angry-birds':'( ఠൠఠ )ﾉ',
        'no-support':'乁( ◔ ౪◔)「      ┑(￣Д ￣)┍',
        'shy':'(๑•́ ₃ •̀๑)',
        'fly-away':'⁽⁽ଘ( ˊᵕˋ )ଓ⁾⁾',
        'careless':'◔_◔',
        'love':'♥‿♥',
        'ididit':'ԅ(≖‿≖ԅ)',
        'kissing':'( ˘ ³˘)♥',
        'shark-face':'( ˇ෴ˇ )',
        'emo-dance':'ヾ(-_- )ゞ',
        'dance':'♪♪ ヽ(ˇ∀ˇ )ゞ',
        'opera':'ヾ(´〇`)ﾉ♪♪♪',
        'winnie-the-pooh':'ʕ •́؈•̀)',
        'boxing':'ლ(•́•́ლ)',
        'fight':"(ง'̀-'́)ง",
        'headphones':'◖ᵔᴥᵔ◗ ♪ ♫',
        'robot':'{•̃_•̃}',
        'seal':'(ᵔᴥᵔ)',
        'questionable':'(Ծ‸ Ծ)',
        'winning':'(•̀ᴗ•́)و ̑̑',
        'zombie':'[¬º-°]¬',
        'pointing':'(☞ﾟヮﾟ)☞',
        'whistling':'(っ•́｡•́)♪♬',
        'injured':'(҂◡_◡)',
        'creeper':'ƪ(ړײ)‎ƪ​​',
        'eye-roll':'⥀.⥀',
        'flying':'ح˚௰˚づ',
        'cannotunsee':'♨_♨',
        'looking-down':'(._.)',
        'imahugger':'(⊃｡•́‿•̀｡)⊃',
        'wizard':'(∩｀-´)⊃━☆ﾟ.*･｡ﾟ',
        'yum':'(っ˘ڡ˘ς)',
        'judging':'( ఠ ͟ʖ ఠ)',
        'tired':'( ͡ಠ ʖ̯ ͡ಠ)',
        'dislike':'( ಠ ʖ̯ ಠ)',
        'hitchhiking':'(งツ)ว',
        'satisfied':'(◠﹏◠)',
        'sadcry':'(ᵟຶ︵ ᵟຶ)',
        'stunna-shades':'(っ▀¯▀)つ',
        'chicken':'ʚ(•｀',
        'barf':'(´ж｀ς)',
        'fuck-off':'(° ͜ʖ͡°)╭∩╮',
        'smiley-toast':'ʕʘ̅͜ʘ̅ʔ',
        'exorcism':'ح(•̀ж•́)ง †',
        'love':'-`ღ´-',
        'taking-a-dump':'(⩾﹏⩽)',
        'dab':'ヽ( •_)ᕗ',
        'wave-dance':'~(^-^)~',
        'happy-hug':'\\(ᵔᵕᵔ)/',
        'resting-my-eyes':'ᴖ̮ ̮ᴖ',
        'peepers':'ಠಠ',
        'judgemental':'{ಠʖಠ}',
        }


class UnicodeEmoji(callbacks.Plugin):
    """A growing set of Unicode Emojis"""

    def e(self, irc, msg, args, emote):
        """<emote>

        Prints the Unicode emoji as listed here https://gist.github.com/mogad0n/476c3880dc0e0a059ed03efa265e50f7
        """

        re = emoji[emote]
        irc.reply('%s' % re, msg=msg, prefixNick=False )

    e = wrap(e, ['text'])


Class = UnicodeEmoji



# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:

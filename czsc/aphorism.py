# -*- coding: utf-8 -*-
"""
author: zengbin93
email: zeng_bin8888@163.com
create_dt: 2021/9/25 13:38
describe: 摘录一些缠中说禅良言警句，希望能帮助更多人走出来。
"""
import random

texts = {
    "1": """
一定要注意，你不是多头也不是空头，但你一定要知道一旦发生什么情况，多头会干什么，空头会
干什么。例如，多头的愿望肯定是想补上面的缺口，这就构成市场的一个潜在力量，这个力量，在
其他力量的干扰下，可能一时发挥不出来，但这反而构成我们一个更好的买入点。请好好品味这句
话：你不当多头也不当空头，但一定要知道空头多头想干什么，而走势是最终的结果，他们想干的
是否干出来了，这才是关键。干不出来，有什么后果，他们会有什么后续的步骤，这才是该想的东
西。

--摘自《2008-01-29 15:19 年线支持初显现》""",

    "2": """
要战胜市场，首先要了解市场的众生。市场是合力的，而合这力的不是机械，而是活生生的人。市
场中，最多数的，都是糊涂蛋，赚钱了不知道为什么，亏钱了不知道为什么，最后变青蛙了，也会
说，井上面的天空好大，好复杂，怎么处理啊？哪里有拐杖啊？几乎绝大多数的人，进市场来时，
根本不知道市场是什么，然后就不断投入，最后有些输红眼了，砸锅卖铁也就进来了。对于市场，
本ID有一个观点，大概有点过分，但确实是对的。市场，就是要0投入去赚钱。

--摘自《2008-01-22 16:10 教你炒股票95：修炼自己》""",

    "3": """
要认清市场，首先要认清自己，知道自己的弱点在哪里，自己在市场中的每个行为，都要清楚地意
识到。每天收盘后，都找十分钟，把自己当天的操作以及看盘时的心理过程复一次盘，这是十分必
要的。

--摘自《2007-04-04 15:31 教你炒股票42：有些人是不适合参与市场的》""",

    "4": """
今天该股90%多的换手意味着，所有中签的人基本都抛了（对手盘包括其中），而且绝大多数都在
10几元抛的。这就对了，你们10几元不看好，有人要看好，市场向所有人开着，凭什么不能买？
市场就是一个斗心理的过程，大家都想一块去了，大家还用不用活了？

--摘自《2006-06-19 16:45 鄙视所有对N中工15元不敢买50元就吃醋的人！》""",

    "5": """
你的喜好，就是你的死亡陷阱！在市场中要生存，第一条就是在市场中要杜绝一切喜好。市场的诱
惑，永远就是通过你的喜好而陷你于死亡。市场中需要的是露水之缘而不是比翼之情，天长地久之
类的东西和市场无关。市场中唯一值得天长地久的就是赢钱，任何一个来市场的人，其目的就是赢
钱，任何与赢钱无关的都是废话。必须明白，任何让你买入一只股票的理由，并不是因为这股票如
何好或被忽悠得如何好，只是你企图通过买入而赢钱，能赢钱的股票就是好的，否则都是废话。因
此，市场中的任何喜好，都是把你引入迷途的陷阱，必须逐一看破，进而洗心革面，才能在市场上
生存。

--摘自《2006-06-09 17:03 教你炒股票3：你的喜好，你的死亡陷阱！》""",

    "6": """
能看清楚自己周围的市场陷阱，还只是第一步，更进一步，要学会利用市场陷阱来赢钱。当你要买
的时候，空头的陷阱就是你的最佳机会，当你要卖的时候，多头的陷阱当然就是你的天堂。这市场
，永远不缺卖在最低点，买在最高点的人，这世界上没有什么是可以让所有人赢钱的，连大牛市中
都有很多人要亏损累累。而市场中的行为，就如同一个修炼上乘武功的过程，最终能否成功，还是
要落实到每个人的智慧、秉性、天赋、勤奋上来！

--摘自《2006-06-09 17:03 教你炒股票3：你的喜好，你的死亡陷阱！》""",

    "7": """
市场是有规律的，但市场的规律并不是显而易见的，是需要严格的分析才能得到。更重要的是，市
场的规律是一种动态的，在不同级别合力作用下显示出来的规律，企图用些单纯的指标、波段、 
波浪、分型、周期等等预测、把握，只可能错陋百出。但只要把这动态的规律在当下的直观中把握
好、应用纯熟，踏准市场的节奏，并不是不可能的。

--摘自《2006-12-27 15:18 教你炒股票19：学习缠中说禅技术分析理论的关键》""",

    "8": """
战胜市场，其实就是战胜自己的贪婪、恐惧、愚蠢，本ID的理论只是把市场拔光给各位看，而拔光
一个人并不意味着就等于征服一个人，对于市场，其道理是一样的。不干，不可能征服市场。对于
市场来说，干就是一切。技术分析的最终意义不是去预测市场要干什么，而是市场正在干什么，是
一种当下的直观。在市场上所有的错误都是离开了这当下的直观，用想象、用情绪来代替。

--摘自《2006-12-27 15:18 教你炒股票19：学习缠中说禅技术分析理论的关键》""",

    "9": """
熟悉本ID所解《论语》的都知道，风险是“不患”的，是无位次的，任何妄求在投资中的绝对无风险，
都是痴心妄想。唯一的办法，就是设置一个系统，使得无位次、“不患”的风险在该系统中成为有位
次，“患”的系统，这是长期战胜市场的唯一方法。

--摘自《2006-12-01 12:03 教你炒股票12：一吻何能消魂？》""",

    "10": """
贪婪和恐惧，人的死穴，周末到了，请给自己一小时去找找自己！

--摘自《2007-01-26 15:03 罗杰斯，有种的和本ID来个PK》
""",

    "11": """
任何个人、阶级，其力量归根结底来自自己，无须期盼或感恩于所谓的救世主、大救星。所有救世
主、大救星都不过是人造的，连神都是人造的，没有造的人，即使是神，也什么都不是！    

--摘自《2006-04-23 18:32 鼓吹救世主、大救星的是真正的精神鸦片！》
""",

    "12": """
每一个人，都是天地不能覆盖，世界的风云雷电就在每个人脚下，自我憋屈只不过是去成就如大救
星般的无聊玩意。历史由每个人所创造，历史由每个人而命名，如果真有什么大救星，你就是你的
大救星！

--摘自《2006-04-19 21:42 布什，当今世界的大救星！》
""",

    "13": """
市场中没有人会同情你，当你哀求着股市跌时不要跌，楼市涨时不要涨，最终都不过成为了市场中
的炮灰。市场只有在所有能成为炮灰的都成为炮灰后，才会休息或改变方向。市场就是市场，市场
上的炮灰都是那些企图成为“大救星”或企图成为被“大救星”的人，而人类社会这个大市场也一样！

--摘自《2006-04-24 21:08 中国楼市股市的闹剧，都是“大救星”思维流毒所致！》
""",

    "14": """
操作其实很简单，一个基本的原则就是，任何走势，无论怎么折腾，都逃不出这个节奏，就是底、
顶以及连接两者的中间过程，因此，在两头的操作节奏就是中枢震荡，只是底的时候要先买后卖，
顶的时候要先卖后买，这样更安全点。至于中间的连接部分，就是持有，当然，对于空头走势，小
板凳就是一个最好的持有，一直持有到底部构造完成。而有技术的，根本就不需要什么小板凳，按
操作级别，分清楚目前是三阶段中的哪一段，然后日日是好日，时时是花时，不赚钱那真是脑子有
水了。亏钱都是错误操作引起的，不断反省，才会有进步的。

--摘自《2008-08-29 09:15 教你炒股票108：何谓底部？从月线看中期走势演化》
""",

    "15": """
底部都是分级别的，如果站在精确走势类型的角度，那么第一类买点出现后，直到该买点所引发的
中枢第一次走出第三类买卖点前，都可以看成底部构造的过程。只不过如果是第三类卖点先出现，
就意味着这底部构造失败了，反之，第三类买点意味着底部构造的最终完成并展开新的行情。当然
，顶部的情况，反过来定义就是。有了这个定义，就一定要搞明白，不是在底部的区间上买，而是
相反，应该和中枢震荡的操作一样，在区间下探失败时买，这才是最好的买点。

--摘自《2008-08-29 09:15 教你炒股票108：何谓底部？从月线看中期走势演化》
""",

    "16": """
牛人，一般是指站在潮流之巅的。在投资市场里，整体的失败是一次都不能发生的，只要发生一次
，基本就翻不了身了。个别的失败是允许的，但不能影响大局。

最早时几千万就可以当庄家了，现在几千万连大散户都算不上，在投资市场中，一次的跌倒，终生
都追不回来，基本只能在后面跟着玩了。而在后面跟着玩，怎么都算不了牛人。

--摘自《2006-11-20 12:00 教你炒股票8：投资如选面首，G点为中心，拒绝ED男！》评论
""",

    "17": """
意画心描自主奴，不管你相信与否，你的命运都是自己造成的，你的命运的改变也是自己造成的，
没有你自己种下的种子，佛也救不了你。有空，就好好看看你自己这个世界吧，看看自己曾种下什
么，又有什么正萌发，又有什么还在潜伏，又有什么被新种下了。善种子、恶种子，堆满你的世界。

--摘自《2008-01-20 21:01 刚到家，说两句》
""",

    "18": """
市场就如同一头牛，只有目无全牛，才可能随心解之而合其关节。在本ID的理论中，机械化操作
的本质就是目无全牛而合其关节，因为，根据本ID的理论，市场的结构已经被彻底分解，站在本
ID理论的角度，哪里有什么市场，不过是一堆的关节。而机械化操作，就是逐步合于其关节的节
奏，而不被全牛的繁复所影响。

--摘自《2008-04-13 21:51 教你炒股票105：远离聪明、机械操作》
""",

    "19": """
挣钱，本来就是很简单的事情，不过就是一个良好习惯与操作策略的结果，一点劲都不用费。那些
费力才能挣到的钱，也不会袋得住。

--摘自《2008-04-13 21:51 教你炒股票105：远离聪明、机械操作》
""",

    "20": """
股票这种面首，一定要控制成本，不要追高，有技术的，一定要通过震荡把成本往0甚至负处玩弄
下去，这才是玩弄股票之道。

--摘自《2007-07-09 15:35 中国股市前途的大决战》
""",

    "21": """
不要用你的想象代替现实。股市里的牛人每年都有，死去的牛人更多，市场的第一原则就是生存，
只要你30年后还能活下来，自然就是最大的牛人。

--摘自《2006-11-20 12:00 教你炒股票8：投资如选面首，G点为中心，拒绝ED男！》评论
""",

    "22": """
要长期胜利，就一定要坚持用最小风险换取最大利润，风险是第一的，这里没有什么高低之分。亏
损是按百分比的，一百亿和一百万，亏了百分百，都是零。人弃我不一定取，人抢我一定给。

--摘自《2006-11-16 12:00 教你炒股票7：给赚了指数亏了钱的一些忠告》评论
""",

    "23": """
有人说每天看盘很累很疲惫，关键是对市场没有充分理解，看盘何尝不是一种放松，不能放松，是
因为有烦恼，被烦恼所烦恼，智慧才是最大的放松。

资本市场就是战场，每时每刻都在进行战争，没有硝烟但杀人不见血！

一个真正的杀手，就等着那血腥的一刻，如同豺狼嗅到了猎物伤口散发的气味一般。 

大浪淘沙，下跌是检验股票成色的试金石。

--摘自《即缠非缠》微博
""",

    "24": """
在现实中，所谓的天命，都是在人谋之中，只是你的谋划是否完全，另外，一个很重要的是，完全
的谋划是否超越你的能力。

对于股票来说，完全的分类或谋划，基本不存在超越能力的问题，只是买卖多少的问题，有能力就
多点，没能力就少点，不存在某种分类完全不能执行的情况。因此，所有的重点，都在这完全的分
类上了。但完全的分类，不是单层次的，一定也必须是多层次的。本ID的理论最重要的特点之一，
就是自然给出了分类的层次，也就是不同的自然形成的级别。不同的级别，有不同的完全分类，而
综合起来，就有了一个立体的完全分类的系统，这才是我们的操作必须依赖的。

把市场分析好了，把情况分类好了，然后问一下自己，你有这个处理所有可能情况的能力吗？如果
没有，那就算了；如果有，就上。事情就这么简单。

--摘自《2008-02-25 16:32 教你炒股票100：中医、兵法、诗歌、操作3》
""",

    "25": """
小人，虽说是对利益之网而游刃有余，但因为画地为牢，自我小之，为一我所牵，最终不过仍是机
关木人，到头来，被一点聪明所误，一场游戏一场梦而已。而君子，尽知小人所知，行小人之行而
无一我之所牵，不废一法而行千法万法，行千法万法而不立一法，于所知所行而自在。

--摘自《2007-08-20 22:36 《论语》详解：给所有曲解孔子的人（67）》
""",

    "26": """
人，总是自己骗自己；人，只能自己骗自己。没有你自己，谁都骗不到你。

--摘自《2008-01-27 10:15 教你打坐22：佛魔最难除》
""",

    "27": """
你在操作时，你后续的所有可能面对的情况与对策都必须了然，否则你就没资格操作。对于一个真
正的操作者，没有任何情况是意外的，因为，所有的情况都被完全地分类了，所有相应的对策都事
先有了，只是等着市场自己去选择，去触及我们事先给定的开关。

--摘自《2008-02-04 19:51 教你炒股票98：中医、兵法、诗歌、操作2》
""",

    "28": """
市场中，最大的敌人之一，就赌徒心理、赌徒思维。赌，最终的结局就只有一个，如果你以赌徒心
理参与市场，那么你的结局就已经注定，你就算还没再锅里，那也只是养肥了再煮而已，没什么区
别。

赌徒心理一个最大的特点，就是预设一个虚拟的目标，一个想象中的目标，完全无视市场本身。

--摘自《2008-01-23 16:18 教你炒股票96：无处不在的赌徒心理》
""",

    "29": """
市场真正的成功，都是严格的操作下完成的。操作失误了有什么大不了的，市场的机会不断涌现，
一个严格的操作程序，足以保证你长期的成功。

生活，很简单，一天三顿，五谷为养、五果为助、五畜为益、五菜为充，而不是那些古灵精怪的玩
意；市场很简单，就如同生活，在一定的韵律中生长出利润。只有那韵律，那平凡但又能长久的赢
利模式，才能使得你战胜市场。市场，只是生活的一部分，如此而已。

--摘自《2008-01-23 16:18 教你炒股票96：无处不在的赌徒心理》
""",

    "30": """
在本ID这里，只有严格分类后的不同操作类型，没有其他那么多无聊的不切边际的所谓预测。来本
ID这里学习，第一层次，就是要达到：当机立断。

机会，是可以预先分析的，但这分析，不是预测，而是建立在完全分类基础上的边界分划，这分划
完全来自本ID理论的纯数学构造，这构造的唯一性与精确性保证了这分类与边界的当下确认性。任
何一个当下，你都可以根据本ID的理论马上给出后面必然要出现的机会。

--摘自《2008-01-21 17:29 教你炒股票94：当机立断》
""",

    "31": """
学了本ID的理论，脑子里必须时刻有两个字：级别。如果连级别都搞不清楚，你还419？被419还
差不多。有了级别，就是节奏问题了，419，就是见好要收，而不是天长地久，这都不明白，就等
着灾难连连吧。不会卖出，就等于失去了下次买入的机会。这个节奏之所以难，说白了，就是贪嗔
痴疑慢作怪。

--摘自《2008-01-21 17:29 教你炒股票94：当机立断》
""",

    "32": """
投资是一门艺术，而投资的艺术归根结底是资金管理的艺术，这就像歌唱的艺术，归根结底是呼吸
的艺术一样。而市场的波动，归根结底是在前后两个高低点关系构成的一个完全分类中展开的，明
白了这一点，市场就如同自己的掌纹一样举手可见了。

--摘自《2006-05-12 19:02 股市闲谈：G股是G点，大牛不用套！》
""",

    "33": """
艺术高度往往和素材或技术无关，是否能把各种因素结合成一个生命的整体，才是艺术的关键。

--摘自《2006-02-20 10:04 连载1：“睡过”或“消费过”的男人们！》
""",

    "34": """
在市场中，第一就要分清楚预测与操作的严重区别：预测是游戏，是茶余饭后的谈资；而操作是真
刀真枪去干，是血与火的斗争。绝对的预测归根结底都是笑话，而非绝对的操作归根结底是死路一
条。像这次，绝对的操作是怎么样，本ID早已反复说明：3656点站不住走，3300缺口位置不回补
可以回补筹码再短差一把，否则就让大盘越南盾去。这里，整个操作的设计是没有任何不确定的地
方，都是绝对性的，这才能股票股票而不是被股票股票，而任何预测都只能永远在被股票股票的死
路上轮回。

--摘自《2008-06-10 16:40 今年诸多灾难与妖蛾子事的历史性解释》
""",

    "35": """
当前一段领涨个股和大盘走势相背离的时候，往往意味着一个结构性震荡的来临，这是股票中的常
见现象。

--摘自《2006-03-11 22:02 用股票技术分析的方法考察毛泽东现象！》
""",

    "36": """
股票就是废纸，该卖的时候不卖，把股票当宝，这就是投资的最大软肋。如果你看图形操作时，做
不到无我无股票，只有走势图形，那基本可以不看图了，因为有我有股票，被自己的贪婪恐惧所牵
引，你看的图，也不过就是自己的贪婪与恐惧，那何必看图？

请回想一下那些卖点时，你自己究竟在干什么？心里是不是有很多幻想，被幻想蒙蔽了眼睛？看图
操作，唯一的对象只有图，谁说都没用，市场是当下发生着的，没有人能替你去反应。

--摘自《2007-06-04 22:34 教你炒股票58：图解分析示范三》
""",

    "37": """
技术上，关键是看好各种底部形态的颈线位置的具体走势，这对短线发现好股票有帮助。

在震荡中，要注意千万别追高。

--摘自《2007-06-13 08:22 《论语》详解：给所有曲解孔子的人（66）》附录
""",

    "38": """
做股票，说白了就是忽悠着冲锋陷阱，只是你去忽悠别人，别让别人忽悠你。既然08年属于早收
割早有面包的年份，我们当然要在年初就大力忽悠。说实在，“向5600高地攻击前进”这点小目
标，说出来都不好意思，也太低了，不过先忽悠低的，现在的人胆子小，毒药要慢慢喂，不像以
前，说年内冲10000点，都有人和你急，他愣要说10000太低，还是12500比较好，50个250呀。

--摘自《2008-01-03 15:18 向5600高地攻击前进》附录
""",

    "39": """
走势反映的是人的贪嗔痴疑慢，如果你能通过走势当下的呈现，而观照其中参与的心理呈现，就等
于看穿了市场参与者的内心。心理，不是虚无飘渺的，最终必然要留下痕迹，也就是市场走势本身
。而一些具有自相似性的结构，就正好是窥测市场心理的科学仪器。

--摘自《2007-09-24 21:31 教你炒股票82：分型结构的心理因素》
""",

    "40": """
消息面、政策面、资金面，这面那面，最终作用的都是人心，人心因预期而交易，这里关系的就是
人的贪婪与恐惧、人的贪嗔痴疑慢。

--摘自《2007-06-19 08:04 教你炒股票60：图解分析示范五》
""",

    "41": """
不预测、不预期，并不是不可预测、不可预期，而是不为贪婪恐惧而预期、预测，是根据走势的自
身规律来。走势是有规律的，这规律是不患的，这不患的根源在于人贪嗔痴疑慢的不患。为什么本
ID要强调当下分解的多样性？因为走势本身就是当下形成中的，是市场各种预期的合力当下画出来
的，而每种画法都是不患的，都是源自人的贪嗔痴疑慢，因此每种多样性的分解都是符合理论的，
多样性不是模糊性，而是多角度去让市场本身自己去画地为牢，由此使得市场的走势万变不离本ID
理论的控制之中，而这，恰好是市场自身的规律之一。

--摘自《2007-06-19 08:04 教你炒股票60：图解分析示范五》
""",

    "42": """
市场上不是每一笔钱都适合任何人去赚的，面对市场的机会，少点贪嗔痴疑慢，认清自己的能力，
这比什么都重要。

市场是连续的，高位走了不是天堂，高位没走不是地狱。大跌，不过是下一买点后大反弹的前戏。
这一切，都逃不过本ID的理论，而是否参与，则与你的操作级别相关，也和你的操作能力相关。

--摘自《2007-09-11 21:38 教你炒股票80：市场没有同情、不信眼泪》
""",

    "43": """
没有人天生就是胜利者，也没有人天生就与失败为伍。人人是佛，无一人可度，无一人需救，人人
有明珠一颗，照破山河大地，又何必憋屈了自己？

--摘自《2007-09-11 21:38 教你炒股票80：市场没有同情、不信眼泪》
""",

    "44": """
对于散户来说，本质上没有卖错，只有买错。为什么？卖错又不会亏钱，买错就不同了。卖错了，
有钱，这么多股票可以被面首，为什么要一棵树吊死？

--摘自《2007-09-11 21:38 教你炒股票80：市场没有同情、不信眼泪》
""",


    "45": """
股票从来就不是股票，而是你的贪嗔痴疑慢；没有任何的失败相关于股票，而只关于你的贪嗔痴疑
慢，股票不过是一个幌子，一个道具。在西方，真正在资本市场上有成就的，基本都成了哲学家。
没有对市场的洞察，靠整天这消息、那题材地折腾，那永远只能在散户的区间中震荡。有此眼界，
不一定能达此高度，毕竟眼高手低也是通病；但无此眼界，就一定不可能达此高度。

--摘自《2007-09-11 21:38 教你炒股票80：市场没有同情、不信眼泪》
""",

    "46": """
万古长空，一朝风月，没有任何走势值得叨唠的，过去的就过去了，关键是后面的操作。无论前面
的操作是成功还是失败，只要市场在，人在，股票在，资金在，这游戏就继续运转，没有必然的胜
利者和失败者，关键是从此刻起，与自己的贪婪与恐惧说再见，深刻了解自己的能力与可能性，形
成一套适合自己的操作原则，这样，失败的可以胜利，胜利的继续胜利。

--摘自《2007-09-11 21:38 教你炒股票80：市场没有同情、不信眼泪》
""",

    "47": """
请注意中枢的递归定义的存在性意义，与分型、笔、线段的操作性意义的区别。

--摘自《2007-07-20 08:26 刚起来，下午解不了盘》
""",

    "48": """
大盘无分歧地创新高，才会导致真正的分歧。前天说了，现在最大的分歧就在于真假突破。但无论
真假突破，突破后的调整、回抽、确认等是必然要发生的。站在周线的角度，无非四种：一种是本
周的上影线调整；二是下周的周K线调整。前者是弱的，后者是强的。当然，还有一种更强的，就
是下周继续拉长阳，中间有日的跳水洗盘，再下周才真调整。最强的就是强力夹空，连收N根周阳，
全部调整以日线完成。

--摘自《2007-07-27 08:01 大盘周线上的四种演化分析》
""",

    "49": """
对于散户来说，一旦行情展开，就一定要按照行情自身的规律，喊口号不是操作，股票是用来操作
而不是用来喊口号的。如果大盘能保持基本在前期两高位连线上进行震荡整理，那么就将走强，否
则就要面对假突破后的猛烈清理。

--摘自《2007-07-27 23:09 对不起，刚回，说两句》
""",

    "50": """
市场就是这样的一个生物链，本ID这种第一波进去的，等着4000点上进去的抬，而4000点进去的，
顶住4300点，自然有新一波人进来。所以，现在4000点进来的也进退自如了，当然，如本ID者，
就更自如了，上面已经有了两层保护膜。

--摘自《2007-07-30 15:19 先扬后抑，酝酿震荡》
""",

    "51": """
市场充满了无穷的诱惑与陷阱，对应着人的贪婪与恐惧。单纯停留在技术的层面，最多就是一个交
易机器。

投资市场最终比的是修养与人格及见识，光从技艺上着手，永远只能是匠人，不可能成为真正的高
手。古代有所谓的打禅七，在现代社会，能找到7天来打禅七是极其奢侈的事情了。但每周，有一
个小时，抛开一切束缚，抛开一切人群，独自一个人，在房间里、在高山上、在河流里、在星空下
、在山野的空谷回音中，张开没有眼睛的眼睛、没有耳朵的耳朵、俯视这世界、倾听这世界。其实
，何处不是房间、高山、河流、星空、山野？何处有束缚需要抛开？在资本、政治、淫乱贪婪、恐
惧的血盆大口里，就是自由、解脱的清凉之地。当然，如果没有如此见识，还是先去需要自己的房
间、高山、河流、星空、山野，但最终，依然要在五浊恶世中污之恶之，不如此，无以自由、解脱。

--摘自《2007-01-15 15:50 教你炒股票23：市场与人生》
""",

    "52": """
市场没有什么庄家，有的只是赢家和输家！有的只是各种类型的动物，还有极少数的高明猎手。市场
就是一个围猎的游戏，当你只有一把小弓箭，你可以去打野兔；当你有了屠龙刀，抓几条蛇来玩当然
就没劲了，关键你是否有屠龙刀！

--摘自《2006-06-07 22:41 教你炒股票2：没有庄家，有的只是赢家和输家！》
""",

    "53": """
禅者，即迷非迷、即缠非缠，非悟即悟、非解即解。求解脱者无解脱、不求解脱者也无解脱，因解成
缠、因悟成迷。所谓顿悟者，非顿悟而名顿悟。所谓三关者，非三关而名三关。佛法无多子、禅宗无
多子、乾坤今古无多子，虽如此，此间事犹需一一透脱。所谓透脱者，非透脱而名透脱也。

--摘自《2006-09-28 11:50 缠中说禅：缠非缠、禅非禅，枯木龙吟照大千（序-九）修改版本》
""",

    "54": """
走势反映的是人的贪嗔痴疑慢，如果你能通过走势当下的呈现，而观照其中参与的心理呈现，就等于
看穿了市场参与者的内心。心理，不是虚无飘渺的，最终必然要留下痕迹，也就是市场走势本身。而
一些具有自相似性的结构，就正好是窥测市场心理的科学仪器。

--摘自《2007-09-24 21:31 教你炒股票82：分型结构的心理因素》
""",

    "55": """
本ID理论的哲学本质，就在于人的贪嗔痴疑慢所引发的自相似性以及由此引发走势级别的自组性这
种类生命的现象。走势是有生命的，本ID说“看行情的走势，就如同听一朵花的开放，见一朵花的
芬芳，嗅一朵花的美丽，一切都在当下中灿烂”，这绝对不是孔男人式的矫情比喻，而是科学般的严
谨说明，因为走势确实有着如花一般的生命特征，走势确实在自相似性、自组性中发芽、生长、绽
放、凋败。因此，本ID的理论是一种可发展的理论，可以提供给无数人去不断研究，研究的方向是
什么？就是走势的自相似性、自组性。

--摘自《2007-09-17 22:57 教你炒股票81：图例、更正及分型、走势类型的哲学本质》
""",

    "56": """
为什么要研究分型、走势类型等东西，其哲学基础是什么？这就是人的贪嗔痴疑慢。因为人的贪嗔痴
疑慢都是一样的，只是跟随时间、环境大小不一，所以，就显示出自相似性。而走势是所有人贪嗔痴
疑慢的合力结果，反映在走势中，就使得走势显示出自相似性。

--摘自《2007-09-17 22:57 教你炒股票81：图例、更正及分型、走势类型的哲学本质》
""",

    "57": """
分型、走势类型的本质就是自相似性，同样，走势必完美的本质也就是自相似性。分型，在1分钟级
别是这样的结构，在年线上也是这样的结构，在不同的级别上，级别不同，但结构是一样的，这就是
自相似性。同样，走势类型也一样。正因为走势具有自相似性，所以走势才是可理解的，才是可把握
的，如果没有自相似性，那么走势必然不可理解，无法把握。要把握走势，本质上，就是把握其自相
似性。

--摘自《2007-09-17 22:57 教你炒股票81：图例、更正及分型、走势类型的哲学本质》
""",

    "58": """
世界不是用来解释的，世界是用来改变的，“患”以“不患”的无位次而位次，而不同位次的实践，就是
人对世界的改变，从而才有“人不知”的世界到“人不愠”的世界。

--摘自《2006-11-19 12:12 《论语》详解：给所有曲解孔子的人（32）》
""",

    "59": """
何谓“习相”？就是《论语》开始所说的“学而时习之”。“相”，因“有”患其“患”而相其“相”，而人能“学”
，能“明了”的，只是各种不同位次的“相”，除“相”之外，并没有“相”之后所谓先天、先验之“性”。“相”
而“习”，“学”其“相”，并不是要忽悠出各种的所谓“理论”来，而是要“习”，以“习”习其相。

“习”的根本目的，就是要改变世界，就是“不相”其“相”而显其新“相”，就是与天其时而天与其时、与地其
利而地与其利、与人其和而人与其和。“远”，深远、深奥。真正深远、深奥的是“习”，是实践、是改变，
而不是那些书虫们的哀号和忽悠。

--摘自《2006-11-19 12:12 《论语》详解：给所有曲解孔子的人（32）》
""",

    "60": """
不要预测任何消息的影响，而应该仔细观察市场对消息的反应，即市场走势本身。如感冒之于人的体
质，消息是测试市场体质的，而不是用来预测的。 

--摘自《即缠非缠》微博 2021-11-16
""",

    "61": """
你的一切，不过都是因为各种业力关系交织的结果，除此之外，你的一切什么都不能一切。你什
么都不是，你在业力之网中上下浮沉，你的一切行为、意识、语言等等的一切，也同时构成这业
力之网的分力，你被游戏着也在游戏中。甚至，你装模装样说要打坐，也是被业力所游戏也在游
戏中。

例如，你来本ID这里，听到打坐这词，被本ID的文章所忽悠，然后这个忽悠的力量与你的心理结
构业力产生合力，制造出你希望去打坐的念头，然后这个念头继续忽悠你，在每一时刻的延续中
增强，逐渐产生了更大的让你的身体去打坐的业力，然后你就在这一股业力之中被游戏，你自己也
在游戏之中。如果有点宗教情结分力的，还甚至要到处去当传教士，忽悠出更大的分力来。

--摘自《2007-12-16 13:23 教你打坐19：认识你自己》
""",

    "62": """
本ID是好是坏，是善是恶，不过都是你的心理结构分力等与本ID的文字分力所产生的合力在你的
心中画出的图象而已。

你产生本ID大好人的图象，然后这个图象就构成继续忽悠你的分力；同样，你产生本ID是大坏人
的图象，这个图象也会构成继续忽悠你的分力。只是觉得本ID是大好人，就觉得本ID说的是如何
如何的好；觉得本ID是大坏蛋，就觉得本ID说的都是放狗屁，然后产生各种行为，制造出自己新
的业力，如此而已。

你在心里产生的一切图象，又和本ID有什么关系呢？你自己的一切在你心里产生的一切图象，又
和你有什么关系呢？

你，一无所有。

--摘自《2007-12-16 13:23 教你打坐19：认识你自己》
""",

    "63": """
不仅是股票，这世界游戏的一个基本玩法，就是“上涨动力，来自清洗。”没有清洗，所有人都成功，
所有人都吃香喝辣的，那就不是全球化资本的美丽新世界了。到达顶端的，永远只能是少数人。当
然，股票上涨的动力，更离不开清洗。没有中途下车的，哪里有最后被落井下石的？没有踏空的、
被洗的，哪里有最后被套的、接棒的？

--摘自《2008-01-09 15:12 上涨动力，来自清洗。》
""",

    "64": """
人，总是自己骗自己；人，只能自己骗自己。没有你自己，谁都骗不到你。

--摘自《2008-01-27 10:15 教你打坐22：佛魔最难除》
""",

    "65": """
人，总爱对影自怜的，总是要敝帚自珍的，而人的意识的最大特征之一就是可以制造一个幻象的世界
去满足人的一切自渎。

--摘自《2008-02-03 10:03 教你打坐23：“任”病最缠人》
""",

    "66": """
1. 恐惧和贪婪，都源自对市场的无知。
2. 股票都是废纸，你要的不是任何股票，而是通过股票把血抽出来。
3. 一个坏习惯足以毁掉一切，每次操作后一定要不断总结，逐步提高。
4. 不要有依赖心理，只有自己在实践中成为自己一部分的，才是真实的。

--摘自《2007-01-31 15:13 来这里，首先要洗心革面》
""",

    "67": """
以中长线的心态选择股票，短线全部用纯技术把成本变成负数，这才能永远不败。

--摘自《2007-01-31 15:13 来这里，首先要洗心革面》评论
""",

    "68": """
没有什么是不可以的，但必须知道代价以及能够去承受这代价。
那些又要玩刀又怕被刀杀着的，回家玩豆腐吧。

--摘自《2007-08-31 16:04 刀锋上的行走》
""",

    "69": """
死亡，就是生命真相的一个大揭露。一切在生时抓住的东西，一旦死亡到来，都不管用了，你什
么都抓不住。死亡，赋予生命以意义。你在生命中牵连的一切，在死亡中被意义了。死亡，照亮
了生命。没有死亡，生命没有了意义。

--摘自《2007-09-02 11:00 教你打坐6：于死亡而从容》
""",

    "70": """
莫问为何，接受走势。走势即因，走势亦果。

--摘自《即缠非缠》微博 2022-02-17
""",

    "71": """
股票市场，不是一个单纯的理论问题。虽然在理论上，本ID可以向所有人揭示其买卖点的完备性
，但买卖点不可能自动去买卖，最终的交易是人去完成的，相同的工具，可能在不同的人手下就
有了完全不同的结果，而市场只看结果，任何人，哭着喊着说自己所用的理论是完备的、最好的
都没用，是人使理论，而非理论使人，要让这人使理论达到理论一般的完美，最终只能靠自己在
市场中的修炼了，这就与《论语》有着密切的关系了。修、齐、治、平，同样适用于股票市场的
交易。

--摘自《2007-01-09 15:03 教你炒股票21：缠中说禅买卖点分析的完备性》
""",

    "72": """
站在中线的角度，超短线其实意义并不太大，有能力就玩，没能力就算了。关键是要
抓住大级别的调整，不参与其中，这才是最关键的。

--摘自《2007-01-23 15:13 教你炒股票25：吻，MACD、背弛、中枢》
""",

    "73": """
任何的交易都必须有钱，也就是交易的前提是先有钱，一旦钱是有限期的，那么等于自动设置了一
个停止交易的时限，这样的交易，是所有失败交易中最常见的一种，以前很多人死在透支上，其实就
是这种情况。任何交易的钱，最好是无限期的，如果真有什么限期，也是足够长的，这是投资中极为
关键的一点。一个有限期的钱，唯一可能就是把操作的级别降到足够低，这样才能把这个限期的风险
尽量控制，但这只是一个没有办法的办法，最好别出现。

--摘自《2007-01-30 15:09 教你炒股票26：市场风险如何回避》
""",

    "74": """
走势是怎么出来的？是用钱堆出来的！在这资本的社会里，又有什么比用实在的钱堆出来的更可信？
除了走势，又有什么是更值得相信的？而那些更值得相信的东西，又有哪样不是建筑在金钱之上的？
资本市场就是一个金钱的游戏，除了钱，还是钱。只有钱是唯一值得信任的，而钱在市场上运动的轨
迹，就是走势。这是市场中唯一可以观察与值得观察的东西。

--摘自《2007-01-30 15:09 教你炒股票26：市场风险如何回避》
""",

    "75": """
交易的本质就是投入一笔钱，在若干时间后换成另一笔钱出来，其中的凭证就是交易的品种。本质上
，任何东西都可以是交易品种，所谓股票的价值，不过是引诱你把钱投进来的诱饵。应用本ID理论的
人，绝对要首先认清楚这一点。对于你投入的钱来说，那些能让你在下一时刻变成更多的钱出来的凭
证就是有价值的。

--摘自《2007-01-30 15:09 教你炒股票26：市场风险如何回避》
""",

    "76": """
市场上，对任何的股票都不值得产生感情，没有任何股票可以给你带来收益，能给你带来收益的是你
的智慧和能力，那中把钱在另一个时间变成更多钱的智慧和能力。股票永远是孙子，被股票所转的，
就连孙子都不如了。

--摘自《2007-01-30 15:09 教你炒股票26：市场风险如何回避》
""",

    "77": """
市场的唯一风险就是你投入的钱在后面的时刻不能用相应的凭证换成更多的钱。但任何的凭证，本质
上都是废纸，以0以上的任何价格进行的任何交易都必然包含风险，也就是说，都可能导致投入的钱
在后面的某一时刻不能换回更多的钱，所以，交易的风险永远存在。

--摘自《2007-01-30 15:09 教你炒股票26：市场风险如何回避》
""",

    "78": """
有什么样的可能，使得交易是毫无风险的？唯一的可能，就是你拥有一个负价格的凭证。什么是真正
的高手、永远不败的高手？就是有本事在相应的时期内把任何的凭证变成负价格的人。对于真正的高
手来说，交易什么其实根本不重要，只要市场有波动，就可以把任何的凭证在足够长的时间内变成负
价格。本ID的理论，本质上只探讨一个问题，如何把任何价格的凭证，最终都把其价格在足够长的时
间内变成负数。

--摘自《2007-01-30 15:09 教你炒股票26：市场风险如何回避》
""",

    "79": """
级别的意义，其实只有一个，基本只和买卖量有关，日线级别的买卖量当然比1分钟级别的要多多了。

--摘自《2007-01-30 15:09 教你炒股票26：市场风险如何回避》
""",
}


def print_one():
    k = random.choice(list(texts.keys()))
    print(texts[k].strip())

"""Story ledger for Friday 20 November 2026: the one source for the PNG and SOURCES.md.

kind: lead | card | brief.  tag: REPORTED (named outlets) | CLAIM (one side, unverified) | FORECAST (scheduled or polled).
time: local time as reported ("" when the reports give none). lonlat: map pin for leads and cards.
"""

DATE = "Friday, 20 November 2026"
REGIONS = ["Europe", "Middle East", "Asia", "Africa", "Americas", "Global"]
FIELDS = {"Markets", "War", "Climate", "Diplomacy", "Security", "Weather", "Justice", "Disaster",
          "Politics", "Conflict", "Health", "Aid", "Tech", "Rights", "People", "Business", "Society"}

S = [
    # ---- leads ----
    dict(kind="lead", region="Americas", place="New York", field="Markets", tag="REPORTED", time="16:00 ET close",
         head="AI sell-off pushes Wall Street into correction",
         fact="S&P 500 fell 3.7% to 6,910; Nasdaq lost 5.3% and wiped out its 2026 gain",
         lonlat=(-74.0, 40.7),
         urls=["https://apnews.com/article/wall-street-stocks-dow-nasdaq-c10b797a17c2acf37924d834efebe135",
               "https://www.nbcnews.com/business/markets/anthropic-shares-markets-selloff-nasdaq-rcna610394",
               "https://www.bbc.com/news/articles/c6808ym10vzgo"]),
    dict(kind="lead", region="Europe", place="Kyiv / Poland", field="War", tag="REPORTED", time="overnight; 06:30 CET in Poland",
         head="Russian missiles hit Kyiv, crash in Poland",
         fact="8 killed, 3 Kyiv bridges hit; Warsaw calls 2 missiles and a drone a provocation",
         lonlat=(30.5, 50.45),
         urls=["https://www.aljazeera.com/news/2026/11/20/russia-unleashes-retaliatory-barrage-on-kyiv-bridges",
               "https://www.aa.com.tr/en/eurasia/8-killed-as-ukraine-says-overnight-russian-strikes-damage-key-bridges-in-kyiv/4131687",
               "https://www.theguardian.com/world/2026/nov/20/russian-missiles-drone-poland-attacks-ukraine",
               "https://www.bbc.com/news/articles/cqx2x9dklxnro"]),
    dict(kind="lead", region="Global", place="Antalya, Türkiye", field="Climate", tag="REPORTED", time="Friday evening (UTC+3)",
         head="COP31 climate talks run into overtime",
         fact="Nearly 200 nations deadlocked over a draft that omits fossil fuels",
         lonlat=(30.7, 36.9),
         urls=["https://www.aljazeera.com/news/2026/11/20/fossil-fuel-talks-deadlock-pushes-cop31-climate-summit-into-overtime",
               "https://www.bbc.com/news/articles/c6ly5w40eg07o",
               "https://www.theguardian.com/environment/2026/nov/20/cop31-talks-overtime-fossil-fuels-vanish-from-draft-deal"]),
    # ---- cards ----
    dict(kind="card", region="Europe", place="Brussels", field="Diplomacy", tag="REPORTED", time="Friday (CET)",
         head="EU and UK seal post-Brexit reset deal",
         fact="Food checks scrapped; 100,000 youth visas each way",
         lonlat=(4.35, 50.85),
         urls=["https://apnews.com/article/eu-britain-uk-brexit-summit-brussels-burnham-f265e5e01b5076b9489f7a6c89f831f4",
               "https://www.aljazeera.com/news/2026/11/20/eu-and-uk-seal-reset-deal",
               "https://www.consilium.europa.eu/en/meetings/international-summit/2026/11/20/"]),
    dict(kind="card", region="Europe", place="Tallinn", field="Security", tag="REPORTED", time="12:41 EET",
         head="Estonia to shut Russia road border",
         fact="All 5 crossings close from 1 Dec for six months",
         lonlat=(27.0, 59.0),
         urls=["https://news.err.ee/1610201515/estonia-to-close-land-border-with-russia-from-december-1",
               "https://www.euronews.com/2026/11/20/estonia-to-shut-border-with-russia-over-gru-linked-sabotage-attack",
               "https://www.vm.ee/en/news/foreign-minister-tsahkna-border-closure-russias-hostile-activities-against-estonia-and-europe"]),
    dict(kind="card", region="Asia", place="Odisha, India", field="Weather", tag="REPORTED", time="08:00-11:20 IST",
         head="Cyclone Akvan makes landfall in Odisha",
         fact="372,000 evacuated; no deaths reported",
         lonlat=(84.9, 19.3),
         urls=["https://indianexpress.com/article/india/cyclone-akvan-odisha-gopalpur-landfall-casualties-evacuation-10971128/",
               "https://www.deccanchronicle.com/nation/cyclone-akvan-weakens-after-landfall-near-gopalpur-372-lakh-evacuated-2006339"]),
    dict(kind="card", region="Asia", place="Naypyitaw", field="Justice", tag="REPORTED", time="Friday (MMT)",
         head="Myanmar calls genocide ruling unfair",
         fact="Friday response; spokeswoman cites 9-6 vote",
         lonlat=(96.1, 19.75),
         urls=["https://apnews.com/article/bangladesh-rohingya-myanmar-un-world-court-ruling-c76dcb3f97c1077262f87e0cba01bb78",
               "https://www.channelnewsasia.com/asia/myanmar-icj-genocide-rohingya-not-fair-6568946"]),
    dict(kind="card", region="Americas", place="Junín, Peru", field="Disaster", tag="REPORTED", time="19:09 PET",
         head="Magnitude 6.7 quake shakes Peru's Andes",
         fact="Felt in Lima; no casualties reported",
         lonlat=(-76.0, -11.0),
         urls=["https://apnews.com/article/peru-earthquake-andes-magnitude-67-d9c0a1de6be970d6a5a36993c607f29f",
               "https://andina.pe/ingles/noticia-peru-67magnitude-earthquake-in-junin-shook-homes-buildings-in-lima-and-callao-1100888.aspx"]),
    dict(kind="card", region="Americas", place="Washington", field="Politics", tag="REPORTED", time="afternoon ET",
         head="Trump says Iran's deal offer is unacceptable",
         fact="Said at a White House news conference",
         lonlat=(-77.0, 38.9),
         urls=["https://apnews.com/article/iran-war-trump-diplomacy-attacks-8fd6dcd6dc4a1a77437cedc4567fbee8",
               "https://english.news.cn/20261121/1cfb14c4f62b4554ac986193c1c4d0ed/c.html"]),
    dict(kind="card", region="Middle East", place="Yemen / Saudi", field="Conflict", tag="CLAIM", time="Friday (AST)",
         head="Saudi coalition says it struck Yemen port",
         fact="Riyadh says it downed Houthi drones, missiles",
         lonlat=(42.95, 14.8),
         urls=["https://apnews.com/article/saudi-yemen-war-iran-iraq-november-20-2026-16c39c487a23b53b73c5eabb7f0fd57a",
               "https://www.arabnews.com/saudi-arabia/saudi-arabia-shoots-down-houthi-drones-and-missiles-3013163",
               "https://www.reuters.com/3fec1b0a85a0/world/middle-east/yemens-houthis-threaten-strike-saudi-red-sea-ports-2026-11-20/"]),
    dict(kind="card", region="Africa", place="DR Congo", field="Health", tag="REPORTED", time="WHO update, Friday",
         head="Ebola keeps spreading in Congo, WHO says",
         fact="11,613 confirmed cases and 5,678 deaths",
         lonlat=(30.25, 1.56),
         urls=["https://www.who.int/emergencies/disease-outbreak-news/item/2026-DON630",
               "https://www.semafor.com/article/11/20/2026/ebola-vaccine-trials-launches-amid-security-concerns"]),
    # ---- briefs ----
    dict(kind="brief", region="Europe", place="Copenhagen", field="Security", tag="CLAIM", time="Friday evening (CET)",
         head="Russian attaché expelled over alleged plot on rapper",
         fact="Two gang members arrested; Russia denies it",
         urls=["https://apnews.com/article/denmark-russia-ukraine-intelligence-tensions-poland-plot-03494b78067c9572120deac038addd23",
               "https://kyivindependent.com/denmark-expels-russian-diplomat-over-alleged-assassination-plot-on-ukrainian-rapper-kyivstoner/"]),
    dict(kind="brief", region="Europe", place="Rome", field="Society", tag="REPORTED", time="all day",
         head="Italy general strike as youth protest in 25 countries",
         fact="CGIL strike reached 100+ Italian cities",
         urls=["https://apnews.com/article/italy-europe-protests-strike-workers-students-inflation-8a742daa7242c84d99307c1fcc864f62",
               "https://www.aljazeera.com/news/2026/11/20/protests-held-across-europe-over-wages-services-high-living-costs"]),
    dict(kind="brief", region="Europe", place="Paris", field="Politics", tag="REPORTED", time="morning (CET)",
         head="Ex-PM de Villepin launches 2027 French presidential bid",
         fact="73-year-old polls about 3%",
         urls=["https://apnews.com/article/france-presidential-election-de-villepin-macron-abd1b09867e78f646245f3202821ca35",
               "https://www.straitstimes.com/world/europe/former-french-pm-de-villepin-launches-2027-presidential-bid"]),
    dict(kind="brief", region="Europe", place="Kyiv", field="Rights", tag="REPORTED", time="Friday (EET)",
         head="UNICEF: 1,144 Ukrainian children killed or hurt this year",
         fact="Highest verified toll in almost four years",
         urls=["https://www.unicef.org/press-releases/child-casualties-ukraine-reach-highest-level-almost-four-years-unicef",
               "https://kyivindependent.com/at-least-1-144-children-killed-or-injured-in-ukraine-during-russias-war-this-year-unicef-says/"]),
    dict(kind="brief", region="Middle East", place="Iraq", field="Security", tag="REPORTED", time="Friday (AST)",
         head="Troops enter Kataib Hezbollah stronghold, no clashes",
         fact="First state entry in 12 years",
         urls=["https://www.voanews.com/a/iraqis-cautiously-optimistic-as-government-forces-enter-iran-backed-militia-stronghold/8226152.html",
               "https://www.aljazeera.com/news/2026/11/20/iraqi-forces-deploy-to-jurf-al-sakhar-after-deal-with-iran-backed-group"]),
    dict(kind="brief", region="Middle East", place="Gaza", field="Conflict", tag="REPORTED", time="overnight to evening",
         head="Israeli strikes kill at least 6 in central Gaza",
         fact="Israel says it targeted militants",
         urls=["https://www.arabnews.com/middle-east/gaza-civil-defense-says-israeli-strikes-kill-six-3013219",
               "https://www.aljazeera.com/news/2026/11/20/israeli-drone-attacks-kill-seven-palestinians-in-central-gaza"]),
    dict(kind="brief", region="Asia", place="Taipei", field="Tech", tag="CLAIM", time="Friday (CST)",
         head="Taiwan flags ~2,700 China-linked Threads accounts to Meta",
         fact="Says they target next week's elections",
         urls=["https://www.straitstimes.com/asia/east-asia/taiwan-tells-meta-thousands-of-china-linked-accounts-seek-to-influence-elections",
               "https://www.taipeitimes.com/News/taiwan/archives/2026/11/21/2003868133"]),
    dict(kind="brief", region="Asia", place="Tokyo", field="Diplomacy", tag="FORECAST", time="17:24 JST",
         head="Poll: record 93% of Japanese see China ties as poor",
         fact="Cabinet Office survey, flash results",
         urls=["https://english.kyodonews.net/articles/-/92153",
               "https://www.japantimes.co.jp/news/2026/11/20/japan/politics/japan-china-russia-ties-survey/"]),
    dict(kind="brief", region="Africa", place="South Africa", field="People", tag="REPORTED", time="22:56 SAST",
         head="Ex-deputy president Mlambo-Ngcuka dies at 71",
         fact="Led UN Women 2013-2021",
         urls=["https://apnews.com/article/mlambongcuka-south-africa-deputy-president-obituary-ce72144fd0991768e9cb466daa95dfe5",
               "https://mg.co.za/news/south-africa/2026-11-20-breaking-phumzile-mlambo-ngcuka-has-died/"]),
    dict(kind="brief", region="Americas", place="Buenos Aires", field="Business", tag="REPORTED", time="18:30 ART",
         head="Tesla opens first Argentina store; Milei attends launch",
         fact="Model 3 and Y listed at about $40-50k",
         urls=["https://www.investing.com/news/stock-market-news/tesla-opens-first-argentina-store-deepening-latin-america-push-5042465",
               "https://www.infobae.com/economia/2026/11/20/tesla-se-presento-en-el-pais-los-elogios-de-javier-milei-y-el-confuso-mensaje-de-elon-musk-desde-un-avion/"]),
    dict(kind="brief", region="Global", place="Rome / Geneva", field="Aid", tag="REPORTED", time="Friday (CET)",
         head="UN food agency asks $12.1bn to feed 91m in 2027",
         fact="Fewer than the 110m it aimed to help in 2026",
         urls=["https://www.wfp.org/news/world-food-programme-sets-out-2027-plan-assist-91-million-people-need-food-crisis-looms",
               "https://news.un.org/en/story/2026/11/1168846"]),
    dict(kind="brief", region="Global", place="New York", field="Diplomacy", tag="REPORTED", time="12:00 ET",
         head="UN chief race: 9th straw poll ends with no winner",
         fact="Costa Rica's Grynspan narrowly keeps the lead",
         urls=["https://www.thenationalnews.com/news/2026/11/20/un-secretary-general-race-straw-poll/",
               "https://www.theguardian.com/world/2026/nov/20/uk-france-veto-uae-choice-lana-nusseibeh-next-un-secretary-general"]),
]

# Key numbers: (value, label, source story head) -- every value appears in a ledger fact or its sources.
KEY_NUMBERS = [
    ("-3.7%", "S&P 500 day", "AP: S&P 500 fell 265.44 points, 3.7%, to 6,910.39"),
    ("-5.3%", "Nasdaq day", "AP: Nasdaq fell 1,261.47 points, 5.3%"),
    ("-8.5%", "Anthropic, 1st full day", "CNBC: shares fell 8.5% on Friday"),
    ("8", "killed in Ukraine", "AA/Al Jazeera: at least 8 killed"),
    ("372,000", "evacuated in Odisha", "Deccan Chronicle/Indian Express: 3.72 lakh evacuated"),
    ("$92.57", "Brent settle, +0.6%", "Dow Jones/EnergyNow: Brent +$0.59 to $92.57"),
]

# Selected local times for the timeline: (local label, UTC minutes since 20 Nov 00:00 for ordering, story head).
TIMELINE = [
    ("08:00 IST", 150, "Cyclone Akvan begins landfall"),
    ("06:30 CET", 330, "Russian missile crashes in Poland"),
    ("12:41 EET", 641, "Estonia votes to shut border"),
    ("16:00 ET", 1260, "Wall Street closes in correction"),
    ("19:09 PET", 1449, "M6.7 quake in Peru's Andes"),
]

# Big stories from other days, deliberately left out (SOURCES.md only, never in the image).
DROPPED = [
    ("19 Nov 2026", "Trump-Xi-Putin trilateral meeting and 'Declaration toward Peace' in Shenzhen",
     "https://www.justsecurity.org/165471/early-edition-november-20-2026/"),
    ("19 Nov 2026", "ICJ rules 9-6 that Myanmar committed genocide against the Rohingya (only Myanmar's 20 Nov reaction is used)",
     "https://www.aa.com.tr/en/world/morning-briefing-nov-20-2026/4131638"),
    ("19 Nov 2026", "Anthropic's record IPO debut on Nasdaq (only the 20 Nov fall is used)",
     "https://www.cnbc.com/2026/11/20/anthropic-stock-ai-amd-nvidia.html"),
    ("19 Nov 2026", "Somalia orders UAE ambassador out within 72 hours",
     "https://www.aljazeera.com/news/2026/11/19/somalia-expels-uae-ambassador-accuses-abu-dhabi-of-violating-sovereignty"),
    ("19 Nov 2026", "US Senate rejects Iran war powers resolution 51-48",
     "https://www.democracynow.org/2026/11/20/headlines"),
    ("19 Nov 2026", "Trump fires national cyber director Sean Cairncross",
     "https://english.news.cn/20261120/178477310e5a4b28b8b00f10459154c8/c.html"),
    ("19 Nov 2026", "COP31 'slimmed-down' draft text drops fossil fuels (only Friday's overtime is used)",
     "https://www.democracynow.org/2026/11/20/headlines"),
    ("19 Nov 2026", "St Johns River in Florida breaks 73-year flood record",
     "https://www.floridatoday.com/story/news/local/2026/11/19/st-johns-river-flood-gates-open-to-protect-homes/92857526007/"),
    ("19 Nov 2026", "10,000+ protest outside Japan's Diet against Takaichi policies",
     "https://english.news.cn/20261120/178477310e5a4b28b8b00f10459154c8/c.html"),
    ("18 Nov 2026", "Migrant boat capsizes off Yenne, Senegal",
     "https://apnews.com/article/senegal-migration-migrants-boat-death-yenne-dadc99eceda7ecee1d868ec34f1932e6"),
    ("6 Nov 2026", "At least 34 Orthodox Christians killed in Ethiopia's East Arsi zone",
     "https://www.aa.com.tr/en/africa/gunmen-kill-34-more-orthodox-christians-in-ethiopia-raising-death-toll-to-94/4113812"),
    ("earlier that week", "Ukraine's strikes on the Kerch (Crimea) bridge",
     "https://www.devdiscourse.com/article/international/4009985-reuters-world-news-summary"),
    ("21 Nov 2026 (scheduled)", "BepiColombo enters Mercury orbit",
     "https://www.newscientist.com/article/2599799-the-bepicolombo-spacecraft-is-finally-entering-orbit-around-mercury/"),
    ("20 Nov 2026, retracted", "Malaysia plan to resettle 10,000 Rohingya in Turkey (post deleted the same day)",
     "https://asia.nikkei.com/politics/international-relations/malaysia-says-it-will-resettle-10-000-rohingya-refugees-in-turkey"),
]


def self_check():
    kinds = [s["kind"] for s in S]
    assert kinds.count("lead") == 3 and 8 <= kinds.count("card") <= 12, kinds
    assert 18 <= len(S) <= 24, len(S)
    for s in S:
        assert s["region"] in REGIONS and s["field"] in FIELDS, s["head"]
        assert s["tag"] in ("REPORTED", "CLAIM", "FORECAST"), s["head"]
        assert len(s["urls"]) >= 2 and len({u.split("/")[2] for u in s["urls"]}) >= 2, s["head"]
        assert s["kind"] == "brief" or len(s["head"].split()) <= 8, s["head"]
        assert s["kind"] == "brief" or "lonlat" in s, s["head"]
    assert len({s["region"] for s in S}) >= 5 and len({s["field"] for s in S}) >= 4
    assert [t[1] for t in TIMELINE] == sorted(t[1] for t in TIMELINE)


self_check()

const fullMarketData = [
  {
    "ticker": "AEHL",
    "name": "Antelope Enterprise Holdings Limited",
    "price": 21.45,
    "change": 150.88,
    "type": "gainer"
  },
  {
    "ticker": "BDRX",
    "name": "Biodexa Pharmaceuticals Plc",
    "price": 0.51,
    "change": 45.15,
    "type": "gainer"
  },
  {
    "ticker": "LQDA",
    "name": "Liquidia Corporation",
    "price": 38.23,
    "change": 42.6,
    "type": "gainer"
  },
  {
    "ticker": "RKDA",
    "name": "Arcadia Biosciences, Inc.",
    "price": 0.28,
    "change": 36.82,
    "type": "gainer"
  },
  {
    "ticker": "YFOR",
    "name": "YYForce Inc.",
    "price": 0.64,
    "change": -36.0,
    "type": "loser"
  },
  {
    "ticker": "AGMH",
    "name": "AGM Group Holdings Inc.",
    "price": 0.69,
    "change": 29.55,
    "type": "gainer"
  },
  {
    "ticker": "BMEA",
    "name": "Biomea Fusion, Inc.",
    "price": 0.9,
    "change": -28.57,
    "type": "loser"
  },
  {
    "ticker": "ZTG",
    "name": "Zenta Group Company Limited",
    "price": 0.72,
    "change": 28.34,
    "type": "gainer"
  },
  {
    "ticker": "TCRT",
    "name": "Alaunos Therapeutics, Inc.",
    "price": 3.88,
    "change": 28.05,
    "type": "gainer"
  },
  {
    "ticker": "JBDI",
    "name": "JBDI Holdings Limited",
    "price": 2.69,
    "change": -21.57,
    "type": "loser"
  },
  {
    "ticker": "AMTD",
    "name": "AMTD IDEA Group",
    "price": 0.46,
    "change": 19.84,
    "type": "gainer"
  },
  {
    "ticker": "WVVI",
    "name": "Willamette Valley Vineyards, Inc.",
    "price": 1.74,
    "change": -18.62,
    "type": "loser"
  },
  {
    "ticker": "FBGL",
    "name": "FBS Global Limited",
    "price": 2.86,
    "change": -18.52,
    "type": "loser"
  },
  {
    "ticker": "BHST",
    "name": "BioHarvest Sciences Inc.",
    "price": 1.5,
    "change": -17.57,
    "type": "loser"
  },
  {
    "ticker": "ALXO",
    "name": "ALX Oncology Holdings Inc.",
    "price": 1.14,
    "change": 16.37,
    "type": "gainer"
  },
  {
    "ticker": "HUBC",
    "name": "HUB Cyber Security Ltd.",
    "price": 0.52,
    "change": -15.13,
    "type": "loser"
  },
  {
    "ticker": "TWG",
    "name": "Top Wealth Group Holding Limited",
    "price": 0.1,
    "change": 13.74,
    "type": "gainer"
  },
  {
    "ticker": "AIIO",
    "name": "Robo.ai Inc.",
    "price": 1.0,
    "change": -13.04,
    "type": "loser"
  },
  {
    "ticker": "SCNI",
    "name": "Scinai Immunotherapeutics Ltd.",
    "price": 1.07,
    "change": -13.01,
    "type": "loser"
  },
  {
    "ticker": "EPOW",
    "name": "E-Power Inc.",
    "price": 3.39,
    "change": 12.63,
    "type": "gainer"
  },
  {
    "ticker": "HODO",
    "name": "House of Doge Inc.",
    "price": 0.1,
    "change": 12.19,
    "type": "gainer"
  },
  {
    "ticker": "CNEY",
    "name": "CN Energy Group. Inc.",
    "price": 0.42,
    "change": -12.02,
    "type": "loser"
  },
  {
    "ticker": "EVAX",
    "name": "Evaxion A/S",
    "price": 3.09,
    "change": 11.96,
    "type": "gainer"
  },
  {
    "ticker": "ENVX",
    "name": "Enovix Corporation",
    "price": 2.81,
    "change": 11.95,
    "type": "gainer"
  },
  {
    "ticker": "FEBO",
    "name": "Fenbo Holdings Limited",
    "price": 0.66,
    "change": -10.97,
    "type": "loser"
  },
  {
    "ticker": "AIOK",
    "name": "AI OKTO CORP.",
    "price": 5.99,
    "change": 10.93,
    "type": "gainer"
  },
  {
    "ticker": "TOMZ",
    "name": "TOMI Environmental Solutions, Inc.",
    "price": 1.47,
    "change": -10.81,
    "type": "loser"
  },
  {
    "ticker": "IZM",
    "name": "ICZOOM Group Inc.",
    "price": 1.13,
    "change": -10.32,
    "type": "loser"
  },
  {
    "ticker": "BKYI",
    "name": "BIO-key International, Inc.",
    "price": 3.12,
    "change": 10.25,
    "type": "gainer"
  },
  {
    "ticker": "NWTG",
    "name": "Newton Golf Company, Inc.",
    "price": 0.77,
    "change": -10.06,
    "type": "loser"
  },
  {
    "ticker": "CPOP",
    "name": "Pop Culture Group Co., Ltd",
    "price": 3.46,
    "change": 9.49,
    "type": "gainer"
  },
  {
    "ticker": "FGL",
    "name": "Founder Group Limited",
    "price": 4.5,
    "change": 9.49,
    "type": "gainer"
  },
  {
    "ticker": "NCPL",
    "name": "Netcapital Inc.",
    "price": 1.52,
    "change": 9.35,
    "type": "gainer"
  },
  {
    "ticker": "EUDA",
    "name": "EUDA Health Holdings Limited",
    "price": 15.49,
    "change": -8.93,
    "type": "loser"
  },
  {
    "ticker": "JLHL",
    "name": "Julong Holding Limited",
    "price": 4.69,
    "change": -8.93,
    "type": "loser"
  },
  {
    "ticker": "ENHA",
    "name": "Enhanced Group Inc.",
    "price": 1.35,
    "change": 8.87,
    "type": "gainer"
  },
  {
    "ticker": "HPAI",
    "name": "Helport AI Limited",
    "price": 0.3,
    "change": -8.68,
    "type": "loser"
  },
  {
    "ticker": "SDST",
    "name": "Stardust Power Inc.",
    "price": 0.04,
    "change": -8.48,
    "type": "loser"
  },
  {
    "ticker": "MNDR",
    "name": "Mobile-health Network Solutions",
    "price": 1.34,
    "change": -8.22,
    "type": "loser"
  },
  {
    "ticker": "EZRA",
    "name": "Reliance Global Group, Inc.",
    "price": 2.12,
    "change": -7.83,
    "type": "loser"
  }
];
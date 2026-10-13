const fullMarketData = [
  {
    "ticker": "FCHL",
    "name": "Fitness Champs Holdings Limited",
    "price": 1.84,
    "change": 84.01,
    "type": "gainer"
  },
  {
    "ticker": "DCX",
    "name": "Digital Currency X Technology Inc.",
    "price": 3.1,
    "change": 40.91,
    "type": "gainer"
  },
  {
    "ticker": "SMTK",
    "name": "SmartKem, Inc.",
    "price": 0.74,
    "change": -30.19,
    "type": "loser"
  },
  {
    "ticker": "LNKS",
    "name": "Linkers Industries Limited",
    "price": 1.69,
    "change": -25.55,
    "type": "loser"
  },
  {
    "ticker": "CLWT",
    "name": "Euro Tech Holdings Company Limited",
    "price": 1.67,
    "change": -22.33,
    "type": "loser"
  },
  {
    "ticker": "MNDR",
    "name": "Mobile-health Network Solutions",
    "price": 2.4,
    "change": -20.94,
    "type": "loser"
  },
  {
    "ticker": "MSGY",
    "name": "Masonglory Limited",
    "price": 3.21,
    "change": 18.89,
    "type": "gainer"
  },
  {
    "ticker": "SNDX",
    "name": "Syndax Pharmaceuticals, Inc.",
    "price": 13.75,
    "change": -16.9,
    "type": "loser"
  },
  {
    "ticker": "ZBAO",
    "name": "Zhibao Technology Inc.",
    "price": 2.0,
    "change": -16.67,
    "type": "loser"
  },
  {
    "ticker": "SUGP",
    "name": "SU Group Holdings Limited",
    "price": 2.1,
    "change": 16.02,
    "type": "gainer"
  },
  {
    "ticker": "SHFS",
    "name": "SHF Holdings, Inc.",
    "price": 0.34,
    "change": -15.24,
    "type": "loser"
  },
  {
    "ticker": "ITOC",
    "name": "iTonic Holdings Ltd.",
    "price": 4.12,
    "change": 15.08,
    "type": "gainer"
  },
  {
    "ticker": "KITT",
    "name": "Nauticus Robotics, Inc.",
    "price": 1.55,
    "change": 13.97,
    "type": "gainer"
  },
  {
    "ticker": "SKK",
    "name": "SKK Holdings Limited",
    "price": 5.27,
    "change": -13.32,
    "type": "loser"
  },
  {
    "ticker": "GIXI",
    "name": "Gix Internet Ltd.",
    "price": 4.11,
    "change": -13.02,
    "type": "loser"
  },
  {
    "ticker": "RIBB",
    "name": "Ribbon Acquisition Corp.",
    "price": 8.01,
    "change": 12.82,
    "type": "gainer"
  },
  {
    "ticker": "DKI",
    "name": "Darkiris Inc.",
    "price": 0.13,
    "change": -12.7,
    "type": "loser"
  },
  {
    "ticker": "DAIC",
    "name": "CID HoldCo, Inc.",
    "price": 1.91,
    "change": 12.35,
    "type": "gainer"
  },
  {
    "ticker": "WBUY",
    "name": "Webuy Global Ltd",
    "price": 0.91,
    "change": 12.16,
    "type": "gainer"
  },
  {
    "ticker": "FVN",
    "name": "Future Vision II Acquisition Corp.",
    "price": 8.88,
    "change": 11.98,
    "type": "gainer"
  },
  {
    "ticker": "YMT",
    "name": "Yimutian Inc.",
    "price": 1.0,
    "change": 11.83,
    "type": "gainer"
  },
  {
    "ticker": "JZ",
    "name": "Jianzhi Education Technology Group Company Limited",
    "price": 1.0,
    "change": -11.5,
    "type": "loser"
  },
  {
    "ticker": "AGRZ",
    "name": "Agroz Inc.",
    "price": 4.88,
    "change": 11.42,
    "type": "gainer"
  },
  {
    "ticker": "ZNB",
    "name": "Zeta Network Group",
    "price": 0.9,
    "change": -11.0,
    "type": "loser"
  },
  {
    "ticker": "LOT",
    "name": "Lotus Technology Inc.",
    "price": 0.71,
    "change": 10.44,
    "type": "gainer"
  },
  {
    "ticker": "FUN",
    "name": "Six Flags Entertainment Corporation",
    "price": 10.69,
    "change": -10.34,
    "type": "loser"
  },
  {
    "ticker": "YMAT",
    "name": "J-Star Holding Co., Ltd.",
    "price": 2.61,
    "change": -10.31,
    "type": "loser"
  },
  {
    "ticker": "SXTC",
    "name": "China SXT Pharmaceuticals, Inc.",
    "price": 0.09,
    "change": -10.1,
    "type": "loser"
  },
  {
    "ticker": "OLB",
    "name": "The OLB Group, Inc.",
    "price": 0.59,
    "change": -9.8,
    "type": "loser"
  },
  {
    "ticker": "OWLS",
    "name": "Obook Holdings Inc.",
    "price": 5.83,
    "change": 9.66,
    "type": "gainer"
  },
  {
    "ticker": "CDIO",
    "name": "Cardio Diagnostics Holdings, Inc.",
    "price": 1.95,
    "change": 9.55,
    "type": "gainer"
  },
  {
    "ticker": "FEMY",
    "name": "Femasys Inc.",
    "price": 1.91,
    "change": 9.14,
    "type": "gainer"
  },
  {
    "ticker": "GURE",
    "name": "Gulf Resources, Inc.",
    "price": 3.02,
    "change": -9.04,
    "type": "loser"
  },
  {
    "ticker": "WFF",
    "name": "WF Holding Limited",
    "price": 15.73,
    "change": -8.96,
    "type": "loser"
  },
  {
    "ticker": "TWG",
    "name": "Top Wealth Group Holding Limited",
    "price": 0.07,
    "change": -8.88,
    "type": "loser"
  },
  {
    "ticker": "ANTA",
    "name": "Antalpha Platform Holding Company",
    "price": 2.6,
    "change": 8.79,
    "type": "gainer"
  },
  {
    "ticker": "PHIO",
    "name": "Phio Pharmaceuticals Corp.",
    "price": 1.0,
    "change": 8.36,
    "type": "gainer"
  },
  {
    "ticker": "GSUN",
    "name": "Golden Sun Technology Group Limited",
    "price": 0.22,
    "change": 8.28,
    "type": "gainer"
  },
  {
    "ticker": "POLA",
    "name": "Polar Power, Inc.",
    "price": 1.19,
    "change": 8.18,
    "type": "gainer"
  },
  {
    "ticker": "VIVK",
    "name": "Vivakor, Inc.",
    "price": 2.0,
    "change": -7.83,
    "type": "loser"
  }
];
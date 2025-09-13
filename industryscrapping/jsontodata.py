import json
import csv

# Paste your full JSON string here (from the API response)
raw_json = """
{
    "breadcrumb": [
        {
            "name": "Manufacturing",
            "url": "manufacturing"
        }
    ],
    "countryMapValue": "India",
    "industryPropertiesTitle": "Manufacturing",
    "industryDescription": "The Manufacturing sector comprises establishments engaged in the mechanical, physical, or chemical transformation of materials, substances, or components into new products.  The assembling of component parts of manufactured products is considered manufacturing, except in cases where the activity is appropriately classified in Sector 23, Construction.  Establishments in the Manufacturing sector are often described as plants, factories, or mills and characteristically use power-driven machines and material handling equipment.  However, establishments that transform materials or substances into new products by hand or in the worker's home and those engaged in selling to the general public products made on the same premises from which they are sold, such as bakeries, candy stores, and custom tailors, may also be included in this sector.  Manufacturing establishments may process materials or may contract with other establishments to process their materials for them.  Both types of establishments are included in manufacturing.  The materials, substances, or components transformed by manufacturing establishments are raw materials that are products of agriculture, forestry, fishing, mining, or quarrying as well as products of other manufacturing establishments.  The materials used may be purchased directly from producers, obtained through customary trade channels, or secured without recourse to the market by transferring the product from one establishment to another, under the same ownership.  The new product of a manufacturing establishment may be finished in the sense that it is ready for utilization or consumption, or it may be semi-finished to become an input for an establishment engaged in further manufacturing.  For example, the product of the alumina refinery is the input used in the primary production of aluminum; primary aluminum is the input to an aluminum wire drawing plant; and aluminum wire is the input for a fabricated wire product manufacturing establishment.  The subsectors in the Manufacturing sector generally reflect distinct production processes related to material inputs, production equipment, and employee skills. In the machinery area, where assembling is a key activity, parts and accessories for manufactured products are classified in the industry of the finished manufactured item when they are made for separate sale.  For example, a replacement refrigerator door would be classified with refrigerators and an attachment for a piece of metalworking machinery would be classified with metalworking machinery.  However, components, input from other manufacturing establishments, are classified based on the production function of the component manufacturer.  For example, electronic components are classified in Subsector 334, Computer and Electronic Product Manufacturing, and stampings are classified in Subsector 332, Fabricated Metal Product Manufacturing.  Manufacturing establishments often perform one or more activities that are classified outside the Manufacturing sector of NAICS.  For instance, almost all manufacturing has some captive research and development or administrative operations, such as accounting, payroll, or management.  These captive services are treated the same as captive manufacturing activities.  When the services are provided by separate establishments, they are classified in the NAICS sector where such services are primary, not in manufacturing. ",
    "url": null,
    "candidatesMatchedQuantityIsNullOrZeroString": false,
    "candidatesMatchedQuantity": "8,912",
    "cityStateProvinceCountry": "Kutch,&nbsp;Gujarat,&nbsp;India",
    "industryName": "Manufacturing",
    "candidatesMatchedQuantityInt": 8912,
    "currentPageNumber": 1,
    "pageSize": 50,
    "totalPages": 179,
    "companyInformationCompany": [
        {
            "duns": "3f817e939e417ec74629520ff8350aa7",
            "primaryName": "WELSPUN CORP LIMITED",
            "primaryNameForUrl": "welspun_corp_limited",
            "primaryAddress": {
                "addressCountry": {
                    "isoAlpha2Code": "IN",
                    "countryName": "India",
                    "name": "India"
                },
                "addressLocality": {
                    "name": "Mumbai"
                },
                "addressRegion": {
                    "name": "Maharashtra",
                    "abbreviatedName": "MH"
                },
                "postalCode": "400013",
                "streetAddress": {
                    "line1": "Welspun House, 5th Floor,"
                }
            },
            "isUnincorporatedCompany": false,
            "addressCountryIsoAlphaTwoCode": "IN",
            "addressCountryName": "India",
            "addressLocalityNameFormatted": "Mumbai",
            "addressRegionNameFormatted": "Maharashtra",
            "salesRevenue": "979",
            "companyNameUrl": "welspun_corp_limited.3f817e939e417ec74629520ff8350aa7"
        },
        {
            "duns": "fc5e1e6bcce2d13986afee32fc0eccea",
            "primaryName": "WELSPUN LIVING LIMITED",
            "primaryNameForUrl": "welspun_living_limited",
            "primaryAddress": {
                "addressCountry": {
                    "isoAlpha2Code": "IN",
                    "countryName": "India",
                    "name": "India"
                },
                "addressLocality": {
                    "name": "Mumbai"
                },
                "addressRegion": {
                    "name": "Maharashtra",
                    "abbreviatedName": "MH"
                },
                "postalCode": "400013",
                "streetAddress": {
                    "line1": "Welspun House, S B Marg, Lower Parel"
                }
            },
            "isUnincorporatedCompany": false,
            "addressCountryIsoAlphaTwoCode": "IN",
            "addressCountryName": "India",
            "addressLocalityNameFormatted": "Mumbai",
            "addressRegionNameFormatted": "Maharashtra",
            "salesRevenue": "931.84",
            "companyNameUrl": "welspun_living_limited.fc5e1e6bcce2d13986afee32fc0eccea"
        },
        {
            "duns": "5756b0a7bb510cbce7f8f5c15fb43b01",
            "primaryName": "DORF-KETAL CHEMICALS INDIA PRIVATE LIMITED",
            "primaryNameForUrl": "dorf-ketal_chemicals_india_private_limited",
            "primaryAddress": {
                "addressCountry": {
                    "isoAlpha2Code": "IN",
                    "countryName": "India",
                    "name": "India"
                },
                "addressLocality": {
                    "name": "Mumbai"
                },
                "addressRegion": {
                    "name": "Maharashtra",
                    "abbreviatedName": "MH"
                },
                "postalCode": "400064",
                "streetAddress": {
                    "line1": "1 Dorf Ketal Tower, D Monte Lane,"
                }
            },
            "isUnincorporatedCompany": false,
            "addressCountryIsoAlphaTwoCode": "IN",
            "addressCountryName": "India",
            "addressLocalityNameFormatted": "Mumbai",
            "addressRegionNameFormatted": "Maharashtra",
            "salesRevenue": null,
            "companyNameUrl": "dorf-ketal_chemicals_india_private_limited.5756b0a7bb510cbce7f8f5c15fb43b01"
        },
        {
            "duns": "de3c658e468427a389c1313fe1b3fe07",
            "primaryName": "SNF FLOPAM INDIA PRIVATE LIMITED",
            "primaryNameForUrl": "snf_flopam_india_private_limited",
            "primaryAddress": {
                "addressCountry": {
                    "isoAlpha2Code": "IN",
                    "countryName": "India",
                    "name": "India"
                },
                "addressLocality": {
                    "name": "Kutch"
                },
                "addressRegion": {
                    "name": "Gujarat",
                    "abbreviatedName": "GJ"
                },
                "postalCode": "370201",
                "streetAddress": {
                    "line1": "Survey No. 141 12 N 1421 National Highway 8A East"
                }
            },
            "isUnincorporatedCompany": false,
            "addressCountryIsoAlphaTwoCode": "IN",
            "addressCountryName": "India",
            "addressLocalityNameFormatted": "Kutch",
            "addressRegionNameFormatted": "Gujarat",
            "salesRevenue": null,
            "companyNameUrl": "snf_flopam_india_private_limited.de3c658e468427a389c1313fe1b3fe07"
        },
        {
            "duns": "dcc5471823468fa5a1ca4608929c8a54",
            "primaryName": "VENUS PIPES & TUBES LIMITED",
            "primaryNameForUrl": "venus_pipes__tubes_limited",
            "primaryAddress": {
                "addressCountry": {
                    "isoAlpha2Code": "IN",
                    "countryName": "India",
                    "name": "India"
                },
                "addressLocality": {
                    "name": "Kutch"
                },
                "addressRegion": {
                    "name": "Gujarat",
                    "abbreviatedName": "GJ"
                },
                "postalCode": "370201",
                "streetAddress": {
                    "line1": "Tripada Complex, Plot No 275, Sector 1/A,"
                }
            },
            "isUnincorporatedCompany": false,
            "addressCountryIsoAlphaTwoCode": "IN",
            "addressCountryName": "India",
            "addressLocalityNameFormatted": "Kutch",
            "addressRegionNameFormatted": "Gujarat",
            "salesRevenue": "94.66",
            "companyNameUrl": "venus_pipes__tubes_limited.dcc5471823468fa5a1ca4608929c8a54"
        },
        {
            "duns": "6d7928b74dfcb8563a93ae54ca961201",
            "primaryName": "SHIPRA WOOD PRODUCTS PRIVATE LIMITED",
            "primaryNameForUrl": "shipra_wood_products_private_limited",
            "primaryAddress": {
                "addressCountry": {
                    "isoAlpha2Code": "IN",
                    "countryName": "India",
                    "name": "India"
                },
                "addressLocality": {
                    "name": "Kutch"
                },
                "addressRegion": {
                    "name": "Gujarat",
                    "abbreviatedName": "GJ"
                },
                "postalCode": "370201",
                "streetAddress": {
                    "line1": "N.H.No.8/A"
                }
            },
            "isUnincorporatedCompany": false,
            "addressCountryIsoAlphaTwoCode": "IN",
            "addressCountryName": "India",
            "addressLocalityNameFormatted": "Kutch",
            "addressRegionNameFormatted": "Gujarat",
            "salesRevenue": null,
            "companyNameUrl": "shipra_wood_products_private_limited.6d7928b74dfcb8563a93ae54ca961201"
        },
        {
            "duns": "5e8a509a703cc7a38e6c2bce7aed2a54",
            "primaryName": "AGROCEL INDUSTRIES PRIVATE LIMITED",
            "primaryNameForUrl": "agrocel_industries_private_limited",
            "primaryAddress": {
                "addressCountry": {
                    "isoAlpha2Code": "IN",
                    "countryName": "India",
                    "name": "India"
                },
                "addressLocality": {
                    "name": "Kutch"
                },
                "addressRegion": {
                    "name": "Gujarat",
                    "abbreviatedName": "GJ"
                },
                "postalCode": "370020",
                "streetAddress": {
                    "line1": "Agrocel House, R.s.no. 135/ Paikee 1 / P, Paikee 2 /"
                }
            },
            "isUnincorporatedCompany": false,
            "addressCountryIsoAlphaTwoCode": "IN",
            "addressCountryName": "India",
            "addressLocalityNameFormatted": "Kutch",
            "addressRegionNameFormatted": "Gujarat",
            "salesRevenue": null,
            "companyNameUrl": "agrocel_industries_private_limited.5e8a509a703cc7a38e6c2bce7aed2a54"
        },
        {
            "duns": "1c55befddcbfbb5bd4e40e9b52e90f61",
            "primaryName": "WELSPUN STEEL LIMITED",
            "primaryNameForUrl": "welspun_steel_limited",
            "primaryAddress": {
                "addressCountry": {
                    "isoAlpha2Code": "IN",
                    "countryName": "India",
                    "name": "India"
                },
                "addressLocality": {
                    "name": "Mumbai"
                },
                "addressRegion": {
                    "name": "Maharashtra",
                    "abbreviatedName": "MH"
                },
                "postalCode": "400013",
                "streetAddress": {
                    "line1": "Welspun House, 6th Floor & 7 Floor"
                }
            },
            "isUnincorporatedCompany": false,
            "addressCountryIsoAlphaTwoCode": "IN",
            "addressCountryName": "India",
            "addressLocalityNameFormatted": "Mumbai",
            "addressRegionNameFormatted": "Maharashtra",
            "salesRevenue": null,
            "companyNameUrl": "welspun_steel_limited.1c55befddcbfbb5bd4e40e9b52e90f61"
        },
        {
            "duns": "18ad46fd085afeeab24f44f977701a73",
            "primaryName": "GRG COTSPIN LIMITED",
            "primaryNameForUrl": "grg_cotspin_limited",
            "primaryAddress": {
                "addressCountry": {
                    "isoAlpha2Code": "IN",
                    "countryName": "India",
                    "name": "India"
                },
                "addressLocality": {
                    "name": "Kutch"
                },
                "addressRegion": {
                    "name": "Gujarat",
                    "abbreviatedName": "GJ"
                },
                "postalCode": "370110",
                "streetAddress": {
                    "line1": "Survey No. 536/1"
                }
            },
            "isUnincorporatedCompany": false,
            "addressCountryIsoAlphaTwoCode": "IN",
            "addressCountryName": "India",
            "addressLocalityNameFormatted": "Kutch",
            "addressRegionNameFormatted": "Gujarat",
            "salesRevenue": null,
            "companyNameUrl": "grg_cotspin_limited.18ad46fd085afeeab24f44f977701a73"
        },
        {
            "duns": "6b68a10559fa10cacc734c6742be0851",
            "primaryName": "OLEO ENERGY (INDIA) PRIVATE LIMITED",
            "primaryNameForUrl": "oleo_energy_(india)_private_limited",
            "primaryAddress": {
                "addressCountry": {
                    "isoAlpha2Code": "IN",
                    "countryName": "India",
                    "name": "India"
                },
                "addressLocality": {
                    "name": "Kutch"
                },
                "addressRegion": {
                    "name": "Gujarat",
                    "abbreviatedName": "GJ"
                },
                "postalCode": "370201",
                "streetAddress": {
                    "line1": "RISHABH ARCADE OFFICE NO 05, GROUND FLOOR PLOT NO 83"
                }
            },
            "isUnincorporatedCompany": false,
            "addressCountryIsoAlphaTwoCode": "IN",
            "addressCountryName": "India",
            "addressLocalityNameFormatted": "Kutch",
            "addressRegionNameFormatted": "Gujarat",
            "salesRevenue": null,
            "companyNameUrl": "oleo_energy_(india)_private_limited.6b68a10559fa10cacc734c6742be0851"
        },
        {
            "duns": "8ac7cfe0bcf1a32663a18706381b85ea",
            "primaryName": "AS R MULTIMETALS PRIVATE LIMITED",
            "primaryNameForUrl": "as_r_multimetals_private_limited",
            "primaryAddress": {
                "addressCountry": {
                    "isoAlpha2Code": "IN",
                    "countryName": "India",
                    "name": "India"
                },
                "addressLocality": {
                    "name": "Kutch"
                },
                "addressRegion": {
                    "name": "Gujarat",
                    "abbreviatedName": "GJ"
                },
                "postalCode": "370201",
                "streetAddress": {
                    "line1": "Survey No. 394/2, 398, 399 & 400"
                }
            },
            "isUnincorporatedCompany": false,
            "addressCountryIsoAlphaTwoCode": "IN",
            "addressCountryName": "India",
            "addressLocalityNameFormatted": "Kutch",
            "addressRegionNameFormatted": "Gujarat",
            "salesRevenue": null,
            "companyNameUrl": "as_r_multimetals_private_limited.8ac7cfe0bcf1a32663a18706381b85ea"
        },
        {
            "duns": "cb4dc7dad0233831d434ee2bc9ffeb77",
            "primaryName": "CONSEP ENGINEERING",
            "primaryNameForUrl": "consep_engineering",
            "primaryAddress": {
                "addressCountry": {
                    "isoAlpha2Code": "IN",
                    "countryName": "India",
                    "name": "India"
                },
                "addressLocality": {
                    "name": "Kutch"
                },
                "addressRegion": {
                    "name": "Gujarat",
                    "abbreviatedName": "GJ"
                },
                "postalCode": "370110",
                "streetAddress": {
                    "line1": "PLOT NO 39, NA, REVENUE SURVEY NO 224, BHIMASAR, ANJAR"
                }
            },
            "isUnincorporatedCompany": false,
            "addressCountryIsoAlphaTwoCode": "IN",
            "addressCountryName": "India",
            "addressLocalityNameFormatted": "Kutch",
            "addressRegionNameFormatted": "Gujarat",
            "salesRevenue": null,
            "companyNameUrl": "consep_engineering.cb4dc7dad0233831d434ee2bc9ffeb77"
        },
        {
            "duns": "442002f4031790bf677ad35f4564d797",
            "primaryName": "ORIENTAL CARBON & CHEMICALS LIMITED",
            "primaryNameForUrl": "oriental_carbon__chemicals_limited",
            "primaryAddress": {
                "addressCountry": {
                    "isoAlpha2Code": "IN",
                    "countryName": "India",
                    "name": "India"
                },
                "addressLocality": {
                    "name": "Noida"
                },
                "addressRegion": {
                    "name": "Uttar Pradesh",
                    "abbreviatedName": "UP"
                },
                "postalCode": "201301",
                "streetAddress": {
                    "line1": "14th Floor, Tower-B, World Trade Tower"
                }
            },
            "isUnincorporatedCompany": false,
            "addressCountryIsoAlphaTwoCode": "IN",
            "addressCountryName": "India",
            "addressLocalityNameFormatted": "Noida",
            "addressRegionNameFormatted": "Uttar&nbsp;Pradesh",
            "salesRevenue": "46.52",
            "companyNameUrl": "oriental_carbon__chemicals_limited.442002f4031790bf677ad35f4564d797"
        },
        {
            "duns": "9693be264c6f6ba36cd4e91cbda6e060",
            "primaryName": "SHREE ARIHANT TRADELINKS INDIA PRIVATE LIMITED",
            "primaryNameForUrl": "shree_arihant_tradelinks_india_private_limited",
            "primaryAddress": {
                "addressCountry": {
                    "isoAlpha2Code": "IN",
                    "countryName": "India",
                    "name": "India"
                },
                "addressLocality": {
                    "name": "Kutch"
                },
                "addressRegion": {
                    "name": "Gujarat",
                    "abbreviatedName": "GJ"
                },
                "postalCode": "370201",
                "streetAddress": {
                    "line1": "202, II Floor Aum Corner"
                }
            },
            "isUnincorporatedCompany": false,
            "addressCountryIsoAlphaTwoCode": "IN",
            "addressCountryName": "India",
            "addressLocalityNameFormatted": "Kutch",
            "addressRegionNameFormatted": "Gujarat",
            "salesRevenue": null,
            "companyNameUrl": "shree_arihant_tradelinks_india_private_limited.9693be264c6f6ba36cd4e91cbda6e060"
        },
        {
            "duns": "1e5c65cc06a7cd53b4c0aa762c184f51",
            "primaryName": "ANKUR CHEMFOOD LIMITED",
            "primaryNameForUrl": "ankur_chemfood_limited",
            "primaryAddress": {
                "addressCountry": {
                    "isoAlpha2Code": "IN",
                    "countryName": "India",
                    "name": "India"
                },
                "addressLocality": {
                    "name": "Kutch"
                },
                "addressRegion": {
                    "name": "Gujarat",
                    "abbreviatedName": "GJ"
                },
                "postalCode": "370201",
                "streetAddress": {
                    "line1": "Office No. 1, 1st Floor, Plot No. 258 Ward 12b Gandhidham"
                }
            },
            "isUnincorporatedCompany": false,
            "addressCountryIsoAlphaTwoCode": "IN",
            "addressCountryName": "India",
            "addressLocalityNameFormatted": "Kutch",
            "addressRegionNameFormatted": "Gujarat",
            "salesRevenue": null,
            "companyNameUrl": "ankur_chemfood_limited.1e5c65cc06a7cd53b4c0aa762c184f51"
        },
        {
            "duns": "d8bf20de3d3ec99c07bf91c7aee0feb7",
            "primaryName": "RUDRAKSH DETERGENT AND CHEMICALS PRIVATE LIMITED",
            "primaryNameForUrl": "rudraksh_detergent_and_chemicals_private_limited",
            "primaryAddress": {
                "addressCountry": {
                    "isoAlpha2Code": "IN",
                    "countryName": "India",
                    "name": "India"
                },
                "addressLocality": {
                    "name": "Kutch"
                },
                "addressRegion": {
                    "name": "Gujarat",
                    "abbreviatedName": "GJ"
                },
                "postalCode": "370201",
                "streetAddress": {
                    "line1": "Survey No.157"
                }
            },
            "isUnincorporatedCompany": false,
            "addressCountryIsoAlphaTwoCode": "IN",
            "addressCountryName": "India",
            "addressLocalityNameFormatted": "Kutch",
            "addressRegionNameFormatted": "Gujarat",
            "salesRevenue": null,
            "companyNameUrl": "rudraksh_detergent_and_chemicals_private_limited.d8bf20de3d3ec99c07bf91c7aee0feb7"
        },
        {
            "duns": "287a678e817a79502642f3f194967669",
            "primaryName": "WELSPUN DI PIPES LIMITED",
            "primaryNameForUrl": "welspun_di_pipes_limited",
            "primaryAddress": {
                "addressCountry": {
                    "isoAlpha2Code": "IN",
                    "countryName": "India",
                    "name": "India"
                },
                "addressLocality": {
                    "name": "Mumbai"
                },
                "addressRegion": {
                    "name": "Maharashtra",
                    "abbreviatedName": "MH"
                },
                "postalCode": "400013",
                "streetAddress": {
                    "line1": "5th Floor, Welspun House, Kamala Mills Compound"
                }
            },
            "isUnincorporatedCompany": false,
            "addressCountryIsoAlphaTwoCode": "IN",
            "addressCountryName": "India",
            "addressLocalityNameFormatted": "Mumbai",
            "addressRegionNameFormatted": "Maharashtra",
            "salesRevenue": null,
            "companyNameUrl": "welspun_di_pipes_limited.287a678e817a79502642f3f194967669"
        },
        {
            "duns": "7f6e32cd527e6815815ca3fee55032d7",
            "primaryName": "WELSPUN TRADINGS LIMITED",
            "primaryNameForUrl": "welspun_tradings_limited",
            "primaryAddress": {
                "addressCountry": {
                    "isoAlpha2Code": "IN",
                    "countryName": "India",
                    "name": "India"
                },
                "addressLocality": {
                    "name": "Mumbai"
                },
                "addressRegion": {
                    "name": "Maharashtra",
                    "abbreviatedName": "MH"
                },
                "postalCode": "400013",
                "streetAddress": {
                    "line1": "7th Floor Welspun House"
                }
            },
            "isUnincorporatedCompany": false,
            "addressCountryIsoAlphaTwoCode": "IN",
            "addressCountryName": "India",
            "addressLocalityNameFormatted": "Mumbai",
            "addressRegionNameFormatted": "Maharashtra",
            "salesRevenue": null,
            "companyNameUrl": "welspun_tradings_limited.7f6e32cd527e6815815ca3fee55032d7"
        },
        {
            "duns": "f8b8bc6c6a173e0cfcc58484d4494259",
            "primaryName": "KUTCH DISTRICT CO OP MILK PRODUCERS UNION LTD",
            "primaryNameForUrl": "kutch_district_co_op_milk_producers_union_ltd",
            "primaryAddress": {
                "addressCountry": {
                    "isoAlpha2Code": "IN",
                    "countryName": "India",
                    "name": "India"
                },
                "addressLocality": {
                    "name": "Kutch"
                },
                "addressRegion": {
                    "name": "Gujarat",
                    "abbreviatedName": "GJ"
                },
                "postalCode": "370110",
                "streetAddress": {
                    "line1": "Apmc Premises, Nr Varsaedi Railway Crossing,"
                }
            },
            "isUnincorporatedCompany": false,
            "addressCountryIsoAlphaTwoCode": "IN",
            "addressCountryName": "India",
            "addressLocalityNameFormatted": "Kutch",
            "addressRegionNameFormatted": "Gujarat",
            "salesRevenue": null,
            "companyNameUrl": "kutch_district_co_op_milk_producers_union_ltd.f8b8bc6c6a173e0cfcc58484d4494259"
        },
        {
            "duns": "4ca77494c6ba40bea2a6f922fb713517",
            "primaryName": "BHUJ POLYMERS PRIVATE LIMITED",
            "primaryNameForUrl": "bhuj_polymers_private_limited",
            "primaryAddress": {
                "addressCountry": {
                    "isoAlpha2Code": "IN",
                    "countryName": "India",
                    "name": "India"
                },
                "addressLocality": {
                    "name": "Kutch"
                },
                "addressRegion": {
                    "name": "Gujarat",
                    "abbreviatedName": "GJ"
                },
                "postalCode": "370415",
                "streetAddress": {
                    "line1": "Survey No. 339/1, Paiki 1, Samaghogha, Taluka Mundra,"
                }
            },
            "isUnincorporatedCompany": false,
            "addressCountryIsoAlphaTwoCode": "IN",
            "addressCountryName": "India",
            "addressLocalityNameFormatted": "Kutch",
            "addressRegionNameFormatted": "Gujarat",
            "salesRevenue": null,
            "companyNameUrl": "bhuj_polymers_private_limited.4ca77494c6ba40bea2a6f922fb713517"
        },
        {
            "duns": "b8d5af2fbf8d59093c8ccbfa01d5dc32",
            "primaryName": "RIVERGROW VYAPAAR PRIVATE LIMITED",
            "primaryNameForUrl": "rivergrow_vyapaar_private_limited",
            "primaryAddress": {
                "addressCountry": {
                    "isoAlpha2Code": "IN",
                    "countryName": "India",
                    "name": "India"
                },
                "addressLocality": {
                    "name": "Kutch"
                },
                "addressRegion": {
                    "name": "Gujarat",
                    "abbreviatedName": "GJ"
                },
                "postalCode": "370201",
                "streetAddress": {
                    "line1": "Office No. 207, Plot No. 302"
                }
            },
            "isUnincorporatedCompany": false,
            "addressCountryIsoAlphaTwoCode": "IN",
            "addressCountryName": "India",
            "addressLocalityNameFormatted": "Kutch",
            "addressRegionNameFormatted": "Gujarat",
            "salesRevenue": null,
            "companyNameUrl": "rivergrow_vyapaar_private_limited.b8d5af2fbf8d59093c8ccbfa01d5dc32"
        },
        {
            "duns": "23e545117aa174866f5833102ad8bb00",
            "primaryName": "AHLSTROM FIBERCOMPOSITES INDIA PRIVATE LIMITED",
            "primaryNameForUrl": "ahlstrom_fibercomposites_india_private_limited",
            "primaryAddress": {
                "addressCountry": {
                    "isoAlpha2Code": "IN",
                    "countryName": "India",
                    "name": "India"
                },
                "addressLocality": {
                    "name": "Kutch"
                },
                "addressRegion": {
                    "name": "Gujarat",
                    "abbreviatedName": "GJ"
                },
                "postalCode": "370421",
                "streetAddress": {
                    "line1": "Plot No. 07, Survey No. 141"
                }
            },
            "isUnincorporatedCompany": false,
            "addressCountryIsoAlphaTwoCode": "IN",
            "addressCountryName": "India",
            "addressLocalityNameFormatted": "Kutch",
            "addressRegionNameFormatted": "Gujarat",
            "salesRevenue": null,
            "companyNameUrl": "ahlstrom_fibercomposites_india_private_limited.23e545117aa174866f5833102ad8bb00"
        },
        {
            "duns": "450f79363e8746fa72da2d57233b7065",
            "primaryName": "WOCO TECH POLYMERE KANDLA LIMITED",
            "primaryNameForUrl": "woco_tech_polymere_kandla_limited",
            "primaryAddress": {
                "addressCountry": {
                    "isoAlpha2Code": "IN",
                    "countryName": "India",
                    "name": "India"
                },
                "addressLocality": {
                    "name": "Kutch"
                },
                "addressRegion": {
                    "name": "Gujarat",
                    "abbreviatedName": "GJ"
                },
                "postalCode": "370230",
                "streetAddress": {
                    "line1": "Plot No. 341-344, Sector-IV,"
                }
            },
            "isUnincorporatedCompany": false,
            "addressCountryIsoAlphaTwoCode": "IN",
            "addressCountryName": "India",
            "addressLocalityNameFormatted": "Kutch",
            "addressRegionNameFormatted": "Gujarat",
            "salesRevenue": null,
            "companyNameUrl": "woco_tech_polymere_kandla_limited.450f79363e8746fa72da2d57233b7065"
        },
        {
            "duns": "90412f3d012b777150b9d510f5ad916a",
            "primaryName": "SHREE ASHAPURA ENTERPRISE",
            "primaryNameForUrl": "shree_ashapura_enterprise",
            "primaryAddress": {
                "addressCountry": {
                    "isoAlpha2Code": "IN",
                    "countryName": "India",
                    "name": "India"
                },
                "addressLocality": {
                    "name": "Kutch"
                },
                "addressRegion": {
                    "name": "Gujarat",
                    "abbreviatedName": "GJ"
                },
                "postalCode": "370110",
                "streetAddress": {
                    "line1": "NEAR BUS STATIONVILL. BHORARA"
                }
            },
            "isUnincorporatedCompany": false,
            "addressCountryIsoAlphaTwoCode": "IN",
            "addressCountryName": "India",
            "addressLocalityNameFormatted": "Kutch",
            "addressRegionNameFormatted": "Gujarat",
            "salesRevenue": null,
            "companyNameUrl": "shree_ashapura_enterprise.90412f3d012b777150b9d510f5ad916a"
        },
        {
            "duns": "f4fb400cdb0064979ff9c436874e82e9",
            "primaryName": "K H MITHANI",
            "primaryNameForUrl": "k_h_mithani",
            "primaryAddress": {
                "addressCountry": {
                    "isoAlpha2Code": "IN",
                    "countryName": "India",
                    "name": "India"
                },
                "addressLocality": {
                    "name": "Kutch"
                },
                "addressRegion": {
                    "name": "Gujarat",
                    "abbreviatedName": "GJ"
                },
                "postalCode": "370421",
                "streetAddress": {
                    "line1": "M\\2, Golden Arcade, Dharab, Zero Point, Mundra"
                }
            },
            "isUnincorporatedCompany": false,
            "addressCountryIsoAlphaTwoCode": "IN",
            "addressCountryName": "India",
            "addressLocalityNameFormatted": "Kutch",
            "addressRegionNameFormatted": "Gujarat",
            "salesRevenue": null,
            "companyNameUrl": "k_h_mithani.f4fb400cdb0064979ff9c436874e82e9"
        },
        {
            "duns": "ff3364472713a1cb0c9a09d395505aab",
            "primaryName": "ANJAR TMT STEEL PRIVATE LIMITED",
            "primaryNameForUrl": "anjar_tmt_steel_private_limited",
            "primaryAddress": {
                "addressCountry": {
                    "isoAlpha2Code": "IN",
                    "countryName": "India",
                    "name": "India"
                },
                "addressLocality": {
                    "name": "Kutch"
                },
                "addressRegion": {
                    "name": "Gujarat",
                    "abbreviatedName": "GJ"
                },
                "postalCode": "370110",
                "streetAddress": {
                    "line1": "S. N. 650, Village Versamedi,"
                }
            },
            "isUnincorporatedCompany": false,
            "addressCountryIsoAlphaTwoCode": "IN",
            "addressCountryName": "India",
            "addressLocalityNameFormatted": "Kutch",
            "addressRegionNameFormatted": "Gujarat",
            "salesRevenue": null,
            "companyNameUrl": "anjar_tmt_steel_private_limited.ff3364472713a1cb0c9a09d395505aab"
        },
        {
            "duns": "17e94a2835a13974253f78dca0b9fdfa",
            "primaryName": "AHIR SALT AND ALLIED PRODUCTS PRIVATE LIMITED",
            "primaryNameForUrl": "ahir_salt_and_allied_products_private_limited",
            "primaryAddress": {
                "addressCountry": {
                    "isoAlpha2Code": "IN",
                    "countryName": "India",
                    "name": "India"
                },
                "addressLocality": {
                    "name": "Kutch"
                },
                "addressRegion": {
                    "name": "Gujarat",
                    "abbreviatedName": "GJ"
                },
                "postalCode": "370201",
                "streetAddress": {
                    "line1": "BBZ-S60, Zanda Chowk"
                }
            },
            "isUnincorporatedCompany": false,
            "addressCountryIsoAlphaTwoCode": "IN",
            "addressCountryName": "India",
            "addressLocalityNameFormatted": "Kutch",
            "addressRegionNameFormatted": "Gujarat",
            "salesRevenue": null,
            "companyNameUrl": "ahir_salt_and_allied_products_private_limited.17e94a2835a13974253f78dca0b9fdfa"
        },
        {
            "duns": "14d2489a1ca56b5b3b003a7b41646af3",
            "primaryName": "JAGAT AGRO FOODS PRIVATE LIMITED",
            "primaryNameForUrl": "jagat_agro_foods_private_limited",
            "primaryAddress": {
                "addressCountry": {
                    "isoAlpha2Code": "IN",
                    "countryName": "India",
                    "name": "India"
                },
                "addressLocality": {
                    "name": "Kutch"
                },
                "addressRegion": {
                    "name": "Gujarat",
                    "abbreviatedName": "GJ"
                },
                "postalCode": "370240",
                "streetAddress": {
                    "line1": "P-47, Sec-9, Shop-11 Gim Village, Ta Gandhidham"
                }
            },
            "isUnincorporatedCompany": false,
            "addressCountryIsoAlphaTwoCode": "IN",
            "addressCountryName": "India",
            "addressLocalityNameFormatted": "Kutch",
            "addressRegionNameFormatted": "Gujarat",
            "salesRevenue": null,
            "companyNameUrl": "jagat_agro_foods_private_limited.14d2489a1ca56b5b3b003a7b41646af3"
        },
        {
            "duns": "29d9d13e2044fbc749c24db99cd42ec8",
            "primaryName": "HKC FOODS LLP",
            "primaryNameForUrl": "hkc_foods_llp",
            "primaryAddress": {
                "addressCountry": {
                    "isoAlpha2Code": "IN",
                    "countryName": "India",
                    "name": "India"
                },
                "addressLocality": {
                    "name": "Kutch"
                },
                "addressRegion": {
                    "name": "Gujarat",
                    "abbreviatedName": "GJ"
                },
                "postalCode": "370001",
                "streetAddress": {
                    "line1": "PLOT NO ONE TO SIX-S NO SIX THREE SIX"
                }
            },
            "isUnincorporatedCompany": false,
            "addressCountryIsoAlphaTwoCode": "IN",
            "addressCountryName": "India",
            "addressLocalityNameFormatted": "Kutch",
            "addressRegionNameFormatted": "Gujarat",
            "salesRevenue": null,
            "companyNameUrl": "hkc_foods_llp.29d9d13e2044fbc749c24db99cd42ec8"
        },
        {
            "duns": "c1cc205237d7dae3e22a805f4b52ce11",
            "primaryName": "NAVKAAR ISPAT LIMITED",
            "primaryNameForUrl": "navkaar_ispat_limited",
            "primaryAddress": {
                "addressCountry": {
                    "isoAlpha2Code": "IN",
                    "countryName": "India",
                    "name": "India"
                },
                "addressLocality": {
                    "name": "Mumbai"
                },
                "addressRegion": {
                    "name": "Maharashtra",
                    "abbreviatedName": "MH"
                },
                "postalCode": "400018",
                "streetAddress": {
                    "line1": "3rd Floor, Bokadia Mansion"
                }
            },
            "isUnincorporatedCompany": false,
            "addressCountryIsoAlphaTwoCode": "IN",
            "addressCountryName": "India",
            "addressLocalityNameFormatted": "Mumbai",
            "addressRegionNameFormatted": "Maharashtra",
            "salesRevenue": null,
            "companyNameUrl": "navkaar_ispat_limited.c1cc205237d7dae3e22a805f4b52ce11"
        },
        {
            "duns": "d3bba772cfcf7961f40f2af056a92acb",
            "primaryName": "JALARAM MINERALS",
            "primaryNameForUrl": "jalaram_minerals",
            "primaryAddress": {
                "addressCountry": {
                    "isoAlpha2Code": "IN",
                    "countryName": "India",
                    "name": "India"
                },
                "addressLocality": {
                    "name": "Kutch"
                },
                "addressRegion": {
                    "name": "Gujarat",
                    "abbreviatedName": "GJ"
                },
                "postalCode": "370001",
                "streetAddress": {
                    "line1": "PLOT NO 6"
                }
            },
            "isUnincorporatedCompany": false,
            "addressCountryIsoAlphaTwoCode": "IN",
            "addressCountryName": "India",
            "addressLocalityNameFormatted": "Kutch",
            "addressRegionNameFormatted": "Gujarat",
            "salesRevenue": null,
            "companyNameUrl": "jalaram_minerals.d3bba772cfcf7961f40f2af056a92acb"
        },
        {
            "duns": "41b4b8f646bcaa19e0381ed0934e4a34",
            "primaryName": "SHREE CHEMFOOD PRIVATE LIMITED",
            "primaryNameForUrl": "shree_chemfood_private_limited",
            "primaryAddress": {
                "addressCountry": {
                    "isoAlpha2Code": "IN",
                    "countryName": "India",
                    "name": "India"
                },
                "addressLocality": {
                    "name": "Kutch"
                },
                "addressRegion": {
                    "name": "Gujarat",
                    "abbreviatedName": "GJ"
                },
                "postalCode": "370201",
                "streetAddress": {
                    "line1": "104, Rishi Corner Building, Plot No. 20"
                }
            },
            "isUnincorporatedCompany": false,
            "addressCountryIsoAlphaTwoCode": "IN",
            "addressCountryName": "India",
            "addressLocalityNameFormatted": "Kutch",
            "addressRegionNameFormatted": "Gujarat",
            "salesRevenue": null,
            "companyNameUrl": "shree_chemfood_private_limited.41b4b8f646bcaa19e0381ed0934e4a34"
        },
        {
            "duns": "70626d365e05b4580291d98c61db7850",
            "primaryName": "SHIV ENTERPRISE",
            "primaryNameForUrl": "shiv_enterprise",
            "primaryAddress": {
                "addressCountry": {
                    "isoAlpha2Code": "IN",
                    "countryName": "India",
                    "name": "India"
                },
                "addressLocality": {
                    "name": "Kutch"
                },
                "addressRegion": {
                    "name": "Gujarat",
                    "abbreviatedName": "GJ"
                },
                "postalCode": "370421",
                "streetAddress": {
                    "line1": "PLOT NO. 21, HARSHA NAGAR,BAROI ROAD, NEAR PITRODA FURNITURE,"
                }
            },
            "isUnincorporatedCompany": false,
            "addressCountryIsoAlphaTwoCode": "IN",
            "addressCountryName": "India",
            "addressLocalityNameFormatted": "Kutch",
            "addressRegionNameFormatted": "Gujarat",
            "salesRevenue": null,
            "companyNameUrl": "shiv_enterprise.70626d365e05b4580291d98c61db7850"
        },
        {
            "duns": "f50539ef7cd09bb4cc6eb8488e5690ab",
            "primaryName": "GANESH METCOKE",
            "primaryNameForUrl": "ganesh_metcoke",
            "primaryAddress": {
                "addressCountry": {
                    "isoAlpha2Code": "IN",
                    "countryName": "India",
                    "name": "India"
                },
                "addressLocality": {
                    "name": "Kutch"
                },
                "addressRegion": {
                    "name": "Gujarat",
                    "abbreviatedName": "GJ"
                },
                "postalCode": "370140",
                "streetAddress": {
                    "line1": "Opp Euro Ceramics Limited, Survey No 644/1, Bhachau Sikra Road"
                }
            },
            "isUnincorporatedCompany": false,
            "addressCountryIsoAlphaTwoCode": "IN",
            "addressCountryName": "India",
            "addressLocalityNameFormatted": "Kutch",
            "addressRegionNameFormatted": "Gujarat",
            "salesRevenue": null,
            "companyNameUrl": "ganesh_metcoke.f50539ef7cd09bb4cc6eb8488e5690ab"
        },
        {
            "duns": "d3183fd23615f514ff166086bed30815",
            "primaryName": "RIO CLAYS PRIVATE LIMITED",
            "primaryNameForUrl": "rio_clays_private_limited",
            "primaryAddress": {
                "addressCountry": {
                    "isoAlpha2Code": "IN",
                    "countryName": "India",
                    "name": "India"
                },
                "addressLocality": {
                    "name": "Kutch"
                },
                "addressRegion": {
                    "name": "Gujarat",
                    "abbreviatedName": "GJ"
                },
                "postalCode": "370001",
                "streetAddress": {
                    "line1": "Survey No.-43/p2, Tal.-bhuj, Vadvara"
                }
            },
            "isUnincorporatedCompany": false,
            "addressCountryIsoAlphaTwoCode": "IN",
            "addressCountryName": "India",
            "addressLocalityNameFormatted": "Kutch",
            "addressRegionNameFormatted": "Gujarat",
            "salesRevenue": null,
            "companyNameUrl": "rio_clays_private_limited.d3183fd23615f514ff166086bed30815"
        },
        {
            "duns": "da63dabe32a0cd9a35604db0bb728d7c",
            "primaryName": "PEGASUS PANELS PRIVATE LIMITED",
            "primaryNameForUrl": "pegasus_panels_private_limited",
            "primaryAddress": {
                "addressCountry": {
                    "isoAlpha2Code": "IN",
                    "countryName": "India",
                    "name": "India"
                },
                "addressLocality": {
                    "name": "Kutch"
                },
                "addressRegion": {
                    "name": "Gujarat",
                    "abbreviatedName": "GJ"
                },
                "postalCode": "370140",
                "streetAddress": {
                    "line1": "Survey No. 354, P1 & P2,"
                }
            },
            "isUnincorporatedCompany": false,
            "addressCountryIsoAlphaTwoCode": "IN",
            "addressCountryName": "India",
            "addressLocalityNameFormatted": "Kutch",
            "addressRegionNameFormatted": "Gujarat",
            "salesRevenue": null,
            "companyNameUrl": "pegasus_panels_private_limited.da63dabe32a0cd9a35604db0bb728d7c"
        },
        {
            "duns": "3cee543e865e990d54e540803244754f",
            "primaryName": "SKAPS ADVANCED COMPOSITES PRIVATE LIMITED",
            "primaryNameForUrl": "skaps_advanced_composites_private_limited",
            "primaryAddress": {
                "addressCountry": {
                    "isoAlpha2Code": "IN",
                    "countryName": "India",
                    "name": "India"
                },
                "addressLocality": {
                    "name": "Kutch"
                },
                "addressRegion": {
                    "name": "Gujarat",
                    "abbreviatedName": "GJ"
                },
                "postalCode": "370421",
                "streetAddress": {
                    "line1": "Survey No. 141, (Paiki) Mundra SEZ Textile & Apparel Park,"
                }
            },
            "isUnincorporatedCompany": false,
            "addressCountryIsoAlphaTwoCode": "IN",
            "addressCountryName": "India",
            "addressLocalityNameFormatted": "Kutch",
            "addressRegionNameFormatted": "Gujarat",
            "salesRevenue": null,
            "companyNameUrl": "skaps_advanced_composites_private_limited.3cee543e865e990d54e540803244754f"
        },
        {
            "duns": "6ed9eeff09f886cf0bb57de40e093641",
            "primaryName": "MUSHKAN SHIPPING PRIVATE LIMITED",
            "primaryNameForUrl": "mushkan_shipping_private_limited",
            "primaryAddress": {
                "addressCountry": {
                    "isoAlpha2Code": "IN",
                    "countryName": "India",
                    "name": "India"
                },
                "addressLocality": {
                    "name": "Kutch"
                },
                "addressRegion": {
                    "name": "Gujarat",
                    "abbreviatedName": "GJ"
                },
                "postalCode": "370465",
                "streetAddress": {
                    "line1": "GOVINDGAR MATH AZAD 942 9825227722 MANDVI KUTCH"
                }
            },
            "isUnincorporatedCompany": false,
            "addressCountryIsoAlphaTwoCode": "IN",
            "addressCountryName": "India",
            "addressLocalityNameFormatted": "Kutch",
            "addressRegionNameFormatted": "Gujarat",
            "salesRevenue": null,
            "companyNameUrl": "mushkan_shipping_private_limited.6ed9eeff09f886cf0bb57de40e093641"
        },
        {
            "duns": "0f461ec9915e0548e334ec6ddad46970",
            "primaryName": "JAISU DREDGING AND SHIPPING LIMITED",
            "primaryNameForUrl": "jaisu_dredging_and_shipping_limited",
            "primaryAddress": {
                "addressCountry": {
                    "isoAlpha2Code": "IN",
                    "countryName": "India",
                    "name": "India"
                },
                "addressLocality": {
                    "name": "Kutch"
                },
                "addressRegion": {
                    "name": "Gujarat",
                    "abbreviatedName": "GJ"
                },
                "postalCode": "370205",
                "streetAddress": {
                    "line1": "7, Maitri Society"
                }
            },
            "isUnincorporatedCompany": false,
            "addressCountryIsoAlphaTwoCode": "IN",
            "addressCountryName": "India",
            "addressLocalityNameFormatted": "Kutch",
            "addressRegionNameFormatted": "Gujarat",
            "salesRevenue": null,
            "companyNameUrl": "jaisu_dredging_and_shipping_limited.0f461ec9915e0548e334ec6ddad46970"
        },
        {
            "duns": "6214b1ed12cb351559c0c2efbce4ca36",
            "primaryName": "MURLIDHAR MINERALS",
            "primaryNameForUrl": "murlidhar_minerals",
            "primaryAddress": {
                "addressCountry": {
                    "isoAlpha2Code": "IN",
                    "countryName": "India",
                    "name": "India"
                },
                "addressLocality": {
                    "name": "Kutch"
                },
                "addressRegion": {
                    "name": "Gujarat",
                    "abbreviatedName": "GJ"
                },
                "postalCode": "370020",
                "streetAddress": {
                    "line1": "1, NADAPA"
                }
            },
            "isUnincorporatedCompany": false,
            "addressCountryIsoAlphaTwoCode": "IN",
            "addressCountryName": "India",
            "addressLocalityNameFormatted": "Kutch",
            "addressRegionNameFormatted": "Gujarat",
            "salesRevenue": null,
            "companyNameUrl": "murlidhar_minerals.6214b1ed12cb351559c0c2efbce4ca36"
        },
        {
            "duns": "efcb0cdf7249dad2c741d186e04a8ab8",
            "primaryName": "ANGEL ENTERPRISE",
            "primaryNameForUrl": "angel_enterprise",
            "primaryAddress": {
                "addressCountry": {
                    "isoAlpha2Code": "IN",
                    "countryName": "India",
                    "name": "India"
                },
                "addressLocality": {
                    "name": "Kutch"
                },
                "addressRegion": {
                    "name": "Gujarat",
                    "abbreviatedName": "GJ"
                },
                "postalCode": "370001",
                "streetAddress": {
                    "line1": "GEETA CHAMBERS, 12, BHUJ MADHAPAR HIGHWAY"
                }
            },
            "isUnincorporatedCompany": false,
            "addressCountryIsoAlphaTwoCode": "IN",
            "addressCountryName": "India",
            "addressLocalityNameFormatted": "Kutch",
            "addressRegionNameFormatted": "Gujarat",
            "salesRevenue": null,
            "companyNameUrl": "angel_enterprise.efcb0cdf7249dad2c741d186e04a8ab8"
        },
        {
            "duns": "5074aadb441c4800a28e5f4b06830007",
            "primaryName": "KIRAN MINECHEM INDUSTRY",
            "primaryNameForUrl": "kiran_minechem_industry",
            "primaryAddress": {
                "addressCountry": {
                    "isoAlpha2Code": "IN",
                    "countryName": "India",
                    "name": "India"
                },
                "addressLocality": {
                    "name": "Kutch"
                },
                "addressRegion": {
                    "name": "Gujarat",
                    "abbreviatedName": "GJ"
                },
                "postalCode": "370001",
                "streetAddress": {
                    "line1": "GEETA CHAMBERS, 11, BHUJ MADHAPAR HIGHWAY"
                }
            },
            "isUnincorporatedCompany": false,
            "addressCountryIsoAlphaTwoCode": "IN",
            "addressCountryName": "India",
            "addressLocalityNameFormatted": "Kutch",
            "addressRegionNameFormatted": "Gujarat",
            "salesRevenue": null,
            "companyNameUrl": "kiran_minechem_industry.5074aadb441c4800a28e5f4b06830007"
        },
        {
            "duns": "bfe96607780d9d4e6ca02d4ecfa6e2c1",
            "primaryName": "WISHVAS SALES AGENCY",
            "primaryNameForUrl": "wishvas_sales_agency",
            "primaryAddress": {
                "addressCountry": {
                    "isoAlpha2Code": "IN",
                    "countryName": "India",
                    "name": "India"
                },
                "addressLocality": {
                    "name": "Kutch"
                },
                "addressRegion": {
                    "name": "Gujarat",
                    "abbreviatedName": "GJ"
                },
                "postalCode": "370105",
                "streetAddress": {
                    "line1": "L S No 155, Padhar, Padhar"
                }
            },
            "isUnincorporatedCompany": false,
            "addressCountryIsoAlphaTwoCode": "IN",
            "addressCountryName": "India",
            "addressLocalityNameFormatted": "Kutch",
            "addressRegionNameFormatted": "Gujarat",
            "salesRevenue": null,
            "companyNameUrl": "wishvas_sales_agency.bfe96607780d9d4e6ca02d4ecfa6e2c1"
        },
        {
            "duns": "54dfb40483be3a38077030c5295f0901",
            "primaryName": "KRISHNA JEWELLERS",
            "primaryNameForUrl": "krishna_jewellers",
            "primaryAddress": {
                "addressCountry": {
                    "isoAlpha2Code": "IN",
                    "countryName": "India",
                    "name": "India"
                },
                "addressLocality": {
                    "name": "Kutch"
                },
                "addressRegion": {
                    "name": "Gujarat",
                    "abbreviatedName": "GJ"
                },
                "postalCode": "370001",
                "streetAddress": {
                    "line1": "1, GHEE WALI SHERI, Kachchh, WHITE BUILDING"
                }
            },
            "isUnincorporatedCompany": false,
            "addressCountryIsoAlphaTwoCode": "IN",
            "addressCountryName": "India",
            "addressLocalityNameFormatted": "Kutch",
            "addressRegionNameFormatted": "Gujarat",
            "salesRevenue": null,
            "companyNameUrl": "krishna_jewellers.54dfb40483be3a38077030c5295f0901"
        },
        {
            "duns": "e3c02e6c197d67cb84932d4fc7017899",
            "primaryName": "BH GLOBAL",
            "primaryNameForUrl": "bh_global",
            "primaryAddress": {
                "addressCountry": {
                    "isoAlpha2Code": "IN",
                    "countryName": "India",
                    "name": "India"
                },
                "addressLocality": {
                    "name": "Kutch"
                },
                "addressRegion": {
                    "name": "Gujarat",
                    "abbreviatedName": "GJ"
                },
                "postalCode": "370201",
                "streetAddress": {
                    "line1": "SF 5, SECOND FLOOR, CORPORATE PARK, SECTOR 8 GANDHIDHAM"
                }
            },
            "isUnincorporatedCompany": false,
            "addressCountryIsoAlphaTwoCode": "IN",
            "addressCountryName": "India",
            "addressLocalityNameFormatted": "Kutch",
            "addressRegionNameFormatted": "Gujarat",
            "salesRevenue": null,
            "companyNameUrl": "bh_global.e3c02e6c197d67cb84932d4fc7017899"
        },
        {
            "duns": "ed2475ca9cfbf6bc36f88306b7cc7931",
            "primaryName": "KESARI OIL INDUSTRIES PRIVATE LIMITED",
            "primaryNameForUrl": "kesari_oil_industries_private_limited",
            "primaryAddress": {
                "addressCountry": {
                    "isoAlpha2Code": "IN",
                    "countryName": "India",
                    "name": "India"
                },
                "addressLocality": {
                    "name": "Kutch"
                },
                "addressRegion": {
                    "name": "Gujarat",
                    "abbreviatedName": "GJ"
                },
                "postalCode": "370240",
                "streetAddress": {
                    "line1": "Plot No. 204-205, Gidc Village-mithirohar Mithi Rohar Anjar"
                }
            },
            "isUnincorporatedCompany": false,
            "addressCountryIsoAlphaTwoCode": "IN",
            "addressCountryName": "India",
            "addressLocalityNameFormatted": "Kutch",
            "addressRegionNameFormatted": "Gujarat",
            "salesRevenue": null,
            "companyNameUrl": "kesari_oil_industries_private_limited.ed2475ca9cfbf6bc36f88306b7cc7931"
        },
        {
            "duns": "53112771f279ff3d424214f1b85947e8",
            "primaryName": "SHREE VISHWAS MINERALS",
            "primaryNameForUrl": "shree_vishwas_minerals",
            "primaryAddress": {
                "addressCountry": {
                    "isoAlpha2Code": "IN",
                    "countryName": "India",
                    "name": "India"
                },
                "addressLocality": {
                    "name": "Kutch"
                },
                "addressRegion": {
                    "name": "Gujarat",
                    "abbreviatedName": "GJ"
                },
                "postalCode": "370105",
                "streetAddress": {
                    "line1": "R.S.NO.155/P1, VILLAGE PADHAR, PADHAR"
                }
            },
            "isUnincorporatedCompany": false,
            "addressCountryIsoAlphaTwoCode": "IN",
            "addressCountryName": "India",
            "addressLocalityNameFormatted": "Kutch",
            "addressRegionNameFormatted": "Gujarat",
            "salesRevenue": null,
            "companyNameUrl": "shree_vishwas_minerals.53112771f279ff3d424214f1b85947e8"
        },
        {
            "duns": "de54b1cd2212f0e1277b2aaa07dddeef",
            "primaryName": "SHREE RAM ALUMINA PRODUCTS",
            "primaryNameForUrl": "shree_ram_alumina_products",
            "primaryAddress": {
                "addressCountry": {
                    "isoAlpha2Code": "IN",
                    "countryName": "India",
                    "name": "India"
                },
                "addressLocality": {
                    "name": "Kutch"
                },
                "addressRegion": {
                    "name": "Gujarat",
                    "abbreviatedName": "GJ"
                },
                "postalCode": "370020",
                "streetAddress": {
                    "line1": "C/O SHREE RAM MINERALS"
                }
            },
            "isUnincorporatedCompany": false,
            "addressCountryIsoAlphaTwoCode": "IN",
            "addressCountryName": "India",
            "addressLocalityNameFormatted": "Kutch",
            "addressRegionNameFormatted": "Gujarat",
            "salesRevenue": null,
            "companyNameUrl": "shree_ram_alumina_products.de54b1cd2212f0e1277b2aaa07dddeef"
        },
        {
            "duns": "bfc1f11569ff45a18a0c69638d2790b2",
            "primaryName": "KUSH SYNTHETICS PRIVATE LIMITED",
            "primaryNameForUrl": "kush_synthetics_private_limited",
            "primaryAddress": {
                "addressCountry": {
                    "isoAlpha2Code": "IN",
                    "countryName": "India",
                    "name": "India"
                },
                "addressLocality": {
                    "name": "Kutch"
                },
                "addressRegion": {
                    "name": "Gujarat",
                    "abbreviatedName": "GJ"
                },
                "postalCode": "370140",
                "streetAddress": {
                    "line1": "Survey No. 146, 147, N H 8 A,"
                }
            },
            "isUnincorporatedCompany": false,
            "addressCountryIsoAlphaTwoCode": "IN",
            "addressCountryName": "India",
            "addressLocalityNameFormatted": "Kutch",
            "addressRegionNameFormatted": "Gujarat",
            "salesRevenue": null,
            "companyNameUrl": "kush_synthetics_private_limited.bfc1f11569ff45a18a0c69638d2790b2"
        },
        {
            "duns": "2ed4ed22e42554a362ba64f663656a0e",
            "primaryName": "JAY ECO GREEN FUEL PRIVATE LIMITED",
            "primaryNameForUrl": "jay_eco_green_fuel_private_limited",
            "primaryAddress": {
                "addressCountry": {
                    "isoAlpha2Code": "IN",
                    "countryName": "India",
                    "name": "India"
                },
                "addressLocality": {
                    "name": "Kutch"
                },
                "addressRegion": {
                    "name": "Gujarat",
                    "abbreviatedName": "GJ"
                },
                "postalCode": "370110",
                "streetAddress": {
                    "line1": "Survey No 196, Plot No 1 2 3 4, Modvadar, Anjar"
                }
            },
            "isUnincorporatedCompany": false,
            "addressCountryIsoAlphaTwoCode": "IN",
            "addressCountryName": "India",
            "addressLocalityNameFormatted": "Kutch",
            "addressRegionNameFormatted": "Gujarat",
            "salesRevenue": null,
            "companyNameUrl": "jay_eco_green_fuel_private_limited.2ed4ed22e42554a362ba64f663656a0e"
        }
    ],
    "naicsCodes": [
        "32",
        "33"
    ],
    "firstHit": 1,
    "companyInformationGeos": [],
    "relatedIndustries": {
        "Alumina and Aluminum Production and Processing": "alumina_and_aluminum_production_and_processing",
        "Fruit and Vegetable Preserving and Specialty Food Manufacturing": "fruit_and_vegetable_preserving_and_specialty_food_manufacturing",
        "Resin, Synthetic Rubber, and Artificial and Synthetic Fibers and Filaments Manufacturing": "resin_synthetic_rubber_and_artificial_and_synthetic_fibers_and_filaments_manufacturing",
        "Clay Product and Refractory Manufacturing": "clay_product_and_refractory_manufacturing",
        "Textile and Fabric Finishing and Fabric Coating Mills": "textile_and_fabric_finishing_and_fabric_coating_mills",
        "Iron and Steel Mills and Ferroalloy Manufacturing": "iron_and_steel_mills_and_ferroalloy_manufacturing",
        "Sugar and Confectionery Product Manufacturing": "sugar_and_confectionery_product_manufacturing",
        "Motor Vehicle Body and Trailer Manufacturing": "motor_vehicle_body_and_trailer_manufacturing",
        "Apparel Accessories and Other Apparel Manufacturing": "apparel_accessories_and_other_apparel_manufacturing",
        "Other Chemical Product and Preparation Manufacturing": "other_chemical_product_and_preparation_manufacturing",
        "Pesticide, Fertilizer, and Other Agricultural Chemical Manufacturing": "pesticide_fertilizer_and_other_agricultural_chemical_manufacturing",
        "Electrical Equipment Manufacturing": "electrical_equipment_manufacturing",
        "Communications Equipment Manufacturing": "communications_equipment_manufacturing",
        "Veneer, Plywood, and Engineered Wood Product Manufacturing": "veneer_plywood_and_engineered_wood_product_manufacturing",
        "Lime and Gypsum Product Manufacturing": "lime_and_gypsum_product_manufacturing",
        "Glass and Glass Product Manufacturing": "glass_and_glass_product_manufacturing",
        "Household and Institutional Furniture and Kitchen Cabinet Manufacturing": "household_and_institutional_furniture_and_kitchen_cabinet_manufacturing",
        "Ventilation, Heating, Air-Conditioning, and Commercial Refrigeration Equipment Manufacturing": "ventilation_heating_air-conditioning_and_commercial_refrigeration_equipment_manufacturing",
        "Other Fabricated Metal Product Manufacturing": "other_fabricated_metal_product_manufacturing",
        "Industrial Machinery Manufacturing": "industrial_machinery_manufacturing",
        "Engine, Turbine, and Power Transmission Equipment Manufacturing": "engine_turbine_and_power_transmission_equipment_manufacturing",
        "Semiconductor and Other Electronic Component Manufacturing": "semiconductor_and_other_electronic_component_manufacturing",
        "Fiber, Yarn, and Thread Mills": "fiber_yarn_and_thread_mills",
        "Other Nonmetallic Mineral Product Manufacturing": "other_nonmetallic_mineral_product_manufacturing",
        "Petroleum and Coal Products Manufacturing": "petroleum_and_coal_products_manufacturing",
        "Textile Furnishings Mills": "textile_furnishings_mills",
        "Boiler, Tank, and Shipping Container Manufacturing": "boiler_tank_and_shipping_container_manufacturing",
        "Fabric Mills": "fabric_mills",
        "Household Appliance Manufacturing": "household_appliance_manufacturing",
        "Soap, Cleaning Compound, and Toilet Preparation Manufacturing": "soap_cleaning_compound_and_toilet_preparation_manufacturing",
        "Other Wood Product Manufacturing": "other_wood_product_manufacturing",
        "Sawmills and Wood Preservation": "sawmills_and_wood_preservation",
        "Other Transportation Equipment Manufacturing": "other_transportation_equipment_manufacturing",
        "Railroad Rolling Stock Manufacturing": "railroad_rolling_stock_manufacturing",
        "Paint, Coating, and Adhesive Manufacturing": "paint_coating_and_adhesive_manufacturing",
        "Cement and Concrete Product Manufacturing": "cement_and_concrete_product_manufacturing",
        "Cutlery and Handtool Manufacturing": "cutlery_and_handtool_manufacturing",
        "Audio and Video Equipment Manufacturing": "audio_and_video_equipment_manufacturing",
        "Nonferrous Metal (except Aluminum) Production and Processing": "nonferrous_metal_(except_aluminum)_production_and_processing",
        "Commercial and Service Industry Machinery Manufacturing": "commercial_and_service_industry_machinery_manufacturing",
        "Converted Paper Product Manufacturing": "converted_paper_product_manufacturing",
        "Spring and Wire Product Manufacturing": "spring_and_wire_product_manufacturing",
        "Animal Food Manufacturing": "animal_food_manufacturing",
        "Basic Chemical Manufacturing": "basic_chemical_manufacturing",
        "Other Miscellaneous Manufacturing": "other_miscellaneous_manufacturing",
        "Seafood Product Preparation and Packaging": "seafood_product_preparation_and_packaging",
        "Other General Purpose Machinery Manufacturing": "other_general_purpose_machinery_manufacturing",
        "Motor Vehicle Parts Manufacturing": "motor_vehicle_parts_manufacturing",
        "Ship and Boat Building": "ship_and_boat_building",
        "Pharmaceutical and Medicine Manufacturing": "pharmaceutical_and_medicine_manufacturing",
        "Machine Shops; Turned Product; and Screw, Nut, and Bolt Manufacturing": "machine_shops_turned_product_and_screw_nut_and_bolt_manufacturing",
        "Pulp, Paper, and Paperboard Mills": "pulp_paper_and_paperboard_mills",
        "Coating, Engraving, Heat Treating, and Allied Activities": "coating_engraving_heat_treating_and_allied_activities",
        "Steel Product Manufacturing from Purchased Steel": "steel_product_manufacturing_from_purchased_steel",
        "Other Food Manufacturing": "other_food_manufacturing",
        "Medical Equipment and Supplies Manufacturing": "medical_equipment_and_supplies_manufacturing",
        "Other Furniture Related Product Manufacturing": "other_furniture_related_product_manufacturing",
        "Aerospace Product and Parts Manufacturing": "aerospace_product_and_parts_manufacturing",
        "Electric Lighting Equipment Manufacturing": "electric_lighting_equipment_manufacturing",
        "Footwear Manufacturing": "footwear_manufacturing",
        "Architectural and Structural Metals Manufacturing": "architectural_and_structural_metals_manufacturing",
        "Dairy Product Manufacturing": "dairy_product_manufacturing",
        "Agriculture, Construction, and Mining Machinery Manufacturing": "agriculture_construction_and_mining_machinery_manufacturing",
        "Animal Slaughtering and Processing": "animal_slaughtering_and_processing",
        "Other Leather and Allied Product Manufacturing": "other_leather_and_allied_product_manufacturing",
        "Apparel Knitting Mills": "apparel_knitting_mills",
        "Other Textile Product Mills": "other_textile_product_mills",
        "Hardware Manufacturing": "hardware_manufacturing",
        "Other Electrical Equipment and Component Manufacturing": "other_electrical_equipment_and_component_manufacturing",
        "Beverage Manufacturing": "beverage_manufacturing",
        "Bakeries and Tortilla Manufacturing": "bakeries_and_tortilla_manufacturing",
        "Computer and Peripheral Equipment Manufacturing": "computer_and_peripheral_equipment_manufacturing",
        "Printing and Related Support Activities": "printing_and_related_support_activities",
        "Tobacco Manufacturing": "tobacco_manufacturing",
        "Forging and Stamping": "forging_and_stamping",
        "Leather and Hide Tanning and Finishing": "leather_and_hide_tanning_and_finishing",
        "Motor Vehicle Manufacturing": "motor_vehicle_manufacturing",
        "Rubber Product Manufacturing": "rubber_product_manufacturing",
        "Manufacturing and Reproducing Magnetic and Optical Media": "manufacturing_and_reproducing_magnetic_and_optical_media",
        "Cut and Sew Apparel Manufacturing": "cut_and_sew_apparel_manufacturing",
        "Grain and Oilseed Milling": "grain_and_oilseed_milling",
        "Foundries": "foundries",
        "Plastics Product Manufacturing": "plastics_product_manufacturing",
        "Metalworking Machinery Manufacturing": "metalworking_machinery_manufacturing",
        "Navigational, Measuring, Electromedical, and Control Instruments Manufacturing": "navigational_measuring_electromedical_and_control_instruments_manufacturing",
        "Office Furniture (including Fixtures) Manufacturing": "office_furniture_(including_fixtures)_manufacturing"
    },
    "lastHit": 50
}
"""

def parse_company_info(data):
    parsed_companies = []
    try:
        parsed = json.loads(data)
        hits = parsed.get("hits", {}).get("hits", [])
        for hit in hits:
            source = hit.get("_source", {})
            company_info = {
                "Company Name": source.get("companyname", "N/A"),
                "DUNS": source.get("duns", "N/A"),
                "Address": source.get("addressline", "N/A"),
                "City": source.get("city", "N/A"),
                "State": source.get("state", "N/A"),
                "Postal Code": source.get("postalcode", "N/A"),
                "Country": source.get("countryname", "N/A"),
            }
            parsed_companies.append(company_info)
    except json.JSONDecodeError as e:
        print(f"[ERROR] JSON parsing failed: {e}")
    
    return parsed_companies

def export_to_csv(companies, filename="companies.csv"):
    if not companies:
        print("[INFO] No data to write to CSV.")
        return
    
    fieldnames = companies[0].keys()
    with open(filename, mode="w", newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(companies)
    
    print(f"[SUCCESS] Exported {len(companies)} companies to {filename}")

if __name__ == "__main__":
    companies = parse_company_info(raw_json)
    
    if companies:
        for i, c in enumerate(companies, 1):
            print(f"\nCompany {i}")
            for k, v in c.items():
                print(f"{k}: {v}")
        
        export_to_csv(companies)
    else:
        print("[WARNING] No company data found.")

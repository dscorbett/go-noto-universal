#!/usr/bin/env python3

import os
import sys

import merge_fonts
import merge_noto

all_regions = {
    'GoNotoSouthAsia.ttf': [
        "NotoSans-Regular.ttf",
        "NotoNastaliqUrdu-Regular.ttf",
        "NotoSansBengali-Regular.ttf",
        "NotoSansChakma-Regular.ttf",
        "NotoSansDevanagari-Regular.ttf",
        "NotoSansGujarati-Regular.ttf",
        "NotoSansGunjalaGondi-Regular.ttf",
        "NotoSansGurmukhi-Regular.ttf",
        "NotoSansKannada-Regular.ttf",
        "NotoSansLepcha-Regular.ttf",
        "NotoSansLimbu-Regular.ttf",
        "NotoSansMalayalam-Regular.ttf",
        "NotoSansMasaramGondi-Regular.ttf",
        "NotoSansMeeteiMayek-Regular.ttf",
        "NotoSansMro-Regular.ttf",
        "NotoSansNewa-Regular.ttf",
        "NotoSansOlChiki-Regular.ttf",
        "NotoSansOriya-Regular.ttf",
        "NotoSansSaurashtra-Regular.ttf",
        "NotoSansSinhala-Regular.ttf",
        "NotoSansTamil-Regular.ttf",
        "NotoSansTelugu-Regular.ttf",
        "NotoSansThaana-Regular.ttf",
        "NotoSerifTibetanSubset-Regular.ttf", # Tibetan subset ok
        "NotoSansWancho-Regular.ttf",
        "NotoSansWarangCiti-Regular.ttf",
        # Common for all scripts
        "NotoSansSymbols-Regular.ttf",
        "NotoSansSymbols2-Regular.ttf",
        "NotoSansMath-Regular.ttf",
    ],
    'GoNotoAsiaHistorical.ttf': [
        "NotoSansBhaiksuki-Regular.ttf",
        "NotoSansBrahmi-Regular.ttf",
        "NotoSansGrantha-Regular.ttf",
        "NotoSansKaithi-Regular.ttf",
        "NotoSansKharoshthi-Regular.ttf",
        "NotoSansKhudawadi-Regular.ttf",
        "NotoSansMahajani-Regular.ttf",
        "NotoSansMarchen-Regular.ttf",
        "NotoSansModi-Regular.ttf",
        "NotoSansMultani-Regular.ttf",
        # "NotoSansNandinagari-Regular.ttf", # doesn't exist
        "NotoSansOldSogdian-Regular.ttf",
        "NotoSansOldTurkic-Regular.ttf",
        "NotoSansPhagsPa-Regular.ttf",
        "NotoSansSharada-Regular.ttf",
        "NotoSansSiddham-Regular.ttf",
        "NotoSansSogdian-Regular.ttf",
        "NotoSansSoraSompeng-Regular.ttf",
        "NotoSansSoyombo-Regular.ttf",
        "NotoSansSylotiNagri-Regular.ttf",
        "NotoSansTakri-Regular.ttf",
        "NotoSansTirhuta-Regular.ttf",
        "NotoSansZanabazarSquare-Regular.ttf",
        "NotoSerifAhom-Regular.ttf",
        "NotoSerifDogra-Regular.ttf",
        "NotoSerifKhojki-Regular.ttf",
        # Common for all scripts
        "NotoSansSymbols-Regular.ttf",
        "NotoSansSymbols2-Regular.ttf",
        "NotoSansMath-Regular.ttf",
    ],
    'GoNotoSouthEastAsia.ttf': [
        "NotoSans-Regular.ttf",
        "NotoSansBalinese-Regular.ttf",
        "NotoSansBatak-Regular.ttf",
        "NotoSansBuginese-Regular.ttf",
        "NotoSansBuhid-Regular.ttf",
        "NotoSansCham-Regular.ttf",
        "NotoSansHanifiRohingya-Regular.ttf",
        "NotoSansHanunoo-Regular.ttf",
        "NotoSansJavanese-Regular.ttf",
        "NotoSansKayahLi-Regular.ttf",
        "NotoSansKhmer-Regular.ttf",
        "NotoSansLao-Regular.ttf",
        # "NotoSansMakasar-Regular.ttf", # doesn't exist
        "NotoSansMyanmar-Regular.ttf",
        "NotoSansNewTaiLue-Regular.ttf",
        "NotoSansPahawhHmong-Regular.ttf",
        "NotoSansPauCinHau-Regular.ttf",
        "NotoSansRejang-Regular.ttf",
        "NotoSansSundanese-Regular.ttf",
        "NotoSansTagalog-Regular.ttf",
        "NotoSansTagbanwa-Regular.ttf",
        "NotoSansTaiLe-Regular.ttf",
        "NotoSansTaiTham-Regular.ttf",
        "NotoSansTaiViet-Regular.ttf",
        "NotoSansThai-Regular.ttf",
        # Common for all scripts
        "NotoSansSymbols-Regular.ttf",
        "NotoSansSymbols2-Regular.ttf",
        "NotoSansMath-Regular.ttf",
    ],
    'GoNotoEuropeAmericas.ttf': [
        "NotoSans-Regular.ttf",
        "NotoSansArmenian-Regular.ttf",
        "NotoSansCanadianAboriginal-Regular.ttf",
        "NotoSansCarian-Regular.ttf",
        "NotoSansCaucasianAlbanian-Regular.ttf",
        "NotoSansCherokee-Regular.ttf",
        "NotoSansCoptic-Regular.ttf",
        "NotoSansCypriot-Regular.ttf",
        "NotoSansDeseret-Regular.ttf",
        "NotoSansGeorgian-Regular.ttf",
        "NotoSansGlagolitic-Regular.ttf",
        "NotoSansOsage-Regular.ttf",
        # TODO: Add Chapter 8 scripts
        # Common for all scripts
        "NotoSansSymbols-Regular.ttf",
        "NotoSansSymbols2-Regular.ttf",
        "NotoSansMath-Regular.ttf",
    ],
    'GoNotoAfricaMiddleEast.ttf': [
        "NotoSans-Regular.ttf",
        "NotoNaskhArabic-Regular.ttf", # or "NotoSansArabic-Regular.ttf"
        "NotoSansAdlam-Regular.ttf",
        "NotoSansAvestan-Regular.ttf",
        "NotoSansBamum-Regular.ttf",
        "NotoSansBassaVah-Regular.ttf",
        "NotoSansCuneiform-Regular.ttf",
        "NotoSansHebrew-Regular.ttf",
        "NotoSansSyriac-Regular.ttf",
        "NotoSansSamaritan-Regular.ttf",
        "NotoSansMandaic-Regular.ttf",
        "NotoSerifYezidi-Regular.ttf",
        # TODO: Add Chapter 10 scripts
        # Common for all scripts
        "NotoSansSymbols-Regular.ttf",
        "NotoSansSymbols2-Regular.ttf",
        "NotoSansMath-Regular.ttf",
    ],
    'GoNotoEastAsia.ttf': [
        "NotoSans-Regular.ttf",
        "NotoSansMarchen-Regular.ttf",
        # "NotoSansMongolian-Regular.ttf", # not working
        "NotoSansOldSogdian-Regular.ttf",
        "NotoSansOldTurkic-Regular.ttf",
        "NotoSansPhagsPa-Regular.ttf",
        "NotoSansSogdian-Regular.ttf",
        "NotoSansSoyombo-Regular.ttf",
        "NotoSansZanabazarSquare-Regular.ttf",
        "NotoSerifTibetanSubset-Regular.ttf",
        "NotoSansYi-Regular.ttf",
        # "NotoSansNushu-Regular.ttf", # not working
        "NotoSansLisu-Regular.ttf",
        "NotoSansMiao-Regular.ttf",
        # "NotoSerifTangut-Regular.ttf", # not working
        # Common for all scripts
        "NotoSansSymbols-Regular.ttf",
        "NotoSansSymbols2-Regular.ttf",
        "NotoSansMath-Regular.ttf",
    ],
}

def download_fonts(directory="./"):
    """Download all the fonts in the @c files list"""
    from urllib.request import urlretrieve
    from time import sleep
    url_base = "https://github.com/googlefonts/noto-fonts/raw/main/hinted/ttf/%s/%s"
    for ttf in merge_fonts.files:
        outfile = os.path.join(directory, ttf)
        if os.path.exists(outfile): continue
        url = url_base % (ttf.split('-')[0], ttf)
        print("Fetching %s" % url)
        try:
            urlretrieve(url, outfile)
        except:
            print("Could not retrieve %s. Please check if it exists", ttf)
        sleep(0.5)

def edit_font_info(fontname):
    from fontTools import ttLib
    import re
    print("editing font info %s" % fontname)
    name_without_spaces = fontname.split('.')[0]
    name_with_spaces = ' '.join(re.split('(?=[A-Z])', name_without_spaces)).strip()
    font = ttLib.TTFont(fontname)
    names = font['name'].names
    for i in range(len(names)):
        print(i, names[i].toStr())

    encoding = names[0].getEncoding()
    names[0].string += "; Copyright 2021 Satish B.; SIL Open Font License v1.1".encode(encoding)
    names[1].string = name_with_spaces.encode(encoding)
    names[3].string = names[3].toStr().replace('NotoSans', name_without_spaces).encode(encoding)
    names[4].string = (name_with_spaces + ' ' + names[2].toStr()).encode(encoding)
    names[6].string = (name_without_spaces + '-' + names[2].toStr()).encode(encoding)
    font.save(fontname)
    font.close()

# append new entries from # https://docs.microsoft.com/en-gb/typography/opentype/spec/scripttags
merge_noto.SCRIPT_TO_OPENTYPE_SCRIPT_TAG['TaiLe'] = 'tale'
merge_noto.SCRIPT_TO_OPENTYPE_SCRIPT_TAG['Multani'] = 'mult'
merge_noto.SCRIPT_TO_OPENTYPE_SCRIPT_TAG['SoraSompeng'] = 'sora'
merge_noto.SCRIPT_TO_OPENTYPE_SCRIPT_TAG['NewTaiLue'] = 'talu'
merge_noto.SCRIPT_TO_OPENTYPE_SCRIPT_TAG['TaiViet'] = 'tavt'
merge_noto.SCRIPT_TO_OPENTYPE_SCRIPT_TAG['Rejang'] = 'rjng'
merge_noto.SCRIPT_TO_OPENTYPE_SCRIPT_TAG['Tagalog'] = 'tglg'
merge_noto.SCRIPT_TO_OPENTYPE_SCRIPT_TAG['Tagbanwa'] = 'tagb'
merge_noto.SCRIPT_TO_OPENTYPE_SCRIPT_TAG['Thaana'] = 'thaa'
merge_noto.SCRIPT_TO_OPENTYPE_SCRIPT_TAG['Mro'] = 'mroo'
merge_noto.SCRIPT_TO_OPENTYPE_SCRIPT_TAG['PahawhHmong'] = "hmng"
merge_noto.SCRIPT_TO_OPENTYPE_SCRIPT_TAG['Bamum'] = "bamu"
merge_noto.SCRIPT_TO_OPENTYPE_SCRIPT_TAG['NotoSerifYezidi'] = "yezi"
merge_noto.SCRIPT_TO_OPENTYPE_SCRIPT_TAG['Nushul'] = "nshu"

if __name__ == "__main__":
    merge_fonts.files = all_regions[sys.argv[2]]
    download_fonts(sys.argv[4])
    merge_fonts.main()

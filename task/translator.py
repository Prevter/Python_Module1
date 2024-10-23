from googletrans import Translator as GoogleTranslator

LANGS = {
    "Afrikaans": "af", "Albanian": "sq",
    "Amharic": "am", "Arabic": "ar",
    "Armenian": "hy", "Assamese": "as",
    "Aymara": "ay", "Azerbaijani": "az",
    "Bambara": "bm", "Basque": "eu",
    "Belarusian": "be", "Bengali": "bn",
    "Bhojpuri": "bho", "Bosnian": "bs",
    "Bulgarian": "bg", "Catalan": "ca",
    "Cebuano": "ceb", "Chinese (Simplified)": "zh-CN",
    "Chinese (Traditional)": "zh-TW", "Corsican": "co",
    "Croatian": "hr", "Czech": "cs",
    "Danish": "da", "Dhivehi": "dv",
    "Dogri": "doi", "Dutch": "nl",
    "English": "en", "Esperanto": "eo",
    "Estonian": "et", "Ewe": "ee",
    "Filipino": "fil", "Finnish": "fi",
    "French": "fr", "Frisian": "fy",
    "Galician": "gl", "Georgian": "ka",
    "German": "de", "Greek": "el",
    "Guarani": "gn", "Gujarati": "gu",
    "Haitian Creole": "ht", "Hausa": "ha",
    "Hawaiian": "haw", "Hebrew": "he or iw",
    "Hindi": "hi", "Hmong": "hmn",
    "Hungarian": "hu", "Icelandic": "is",
    "Igbo": "ig", "Ilocano": "ilo",
    "Indonesian": "id", "Irish": "ga",
    "Italian": "it", "Japanese": "ja",
    "Javanese": "jv or jw", "Kannada": "kn",
    "Kazakh": "kk", "Khmer": "km",
    "Kinyarwanda": "rw", "Konkani": "gom",
    "Korean": "ko", "Krio": "kri",
    "Kurdish": "ku", "Kyrgyz": "ky",
    "Lao": "lo", "Latin": "la",
    "Latvian": "lv", "Lingala": "ln",
    "Lithuanian": "lt", "Luganda": "lg",
    "Luxembourgish": "lb", "Macedonian": "mk",
    "Maithili": "mai", "Malagasy": "mg",
    "Malay": "ms", "Malayalam": "ml",
    "Maltese": "mt", "Maori": "mi",
    "Marathi": "mr", "Meiteilon": "mni-Mtei",
    "Mizo": "lus", "Mongolian": "mn",
    "Myanmar": "my", "Nepali": "ne",
    "Norwegian": "no", "Nyanja": "ny",
    "Oromo": "om", "Pashto": "ps",
    "Persian": "fa", "Polish": "pl",
    "Portuguese": "pt", "Punjabi": "pa",
    "Quechua": "qu", "Romanian": "ro",
    "Russian": "ru", "Samoan": "sm",
    "Sanskrit": "sa", "Scots Gaelic": "gd",
    "Sepedi": "nso", "Serbian": "sr",
    "Sesotho": "st", "Shona": "sn",
    "Sindhi": "sd", "Sinhala": "si",
    "Slovak": "sk", "Slovenian": "sl",
    "Somali": "so", "Spanish": "es",
    "Sundanese": "su", "Swahili": "sw",
    "Swedish": "sv", "Tagalog": "tl",
    "Tajik": "tg", "Tamil": "ta",
    "Tatar": "tt", "Telugu": "te",
    "Thai": "th", "Tigrinya": "ti",
    "Tsonga": "ts", "Turkish": "tr",
    "Turkmen": "tk", "Twi": "ak",
    "Ukrainian": "uk", "Urdu": "ur",
    "Uyghur": "ug", "Uzbek": "uz",
    "Vietnamese": "vi", "Welsh": "cy",
    "Xhosa": "xh", "Yiddish": "yi",
    "Yoruba": "yo", "Zulu": "zu",
}

class Translator:
    def __init__(self, locale, name):
        self.locale = locale
        self.translator = GoogleTranslator()
        self.name = self.translate(name)

    @staticmethod
    def get(locale) -> 'Translator':
        if locale in LANGS:
            return Translator(LANGS[locale], locale)
        for lang, code in LANGS.items():
            if code.lower() == locale.lower():
                return Translator(code, lang)
        return None

    def translate(self, str) -> str:
        return self.translator.translate(str, dest=self.locale).text

import matplotlib.font_manager
from matplotlib.font_manager import FontProperties, FontManager, FontEntry, \
    ttfFontProperty
from matplotlib import ft2font, rcParams
import os

_fonts_directory = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                "fonts"))

_boomslang_fonts = [os.path.join(_fonts_directory, x) for x in
                    os.listdir(_fonts_directory) if x[-3:] == "ttf"]

# If you drop fonts into the fonts/ directory, you can change the default fonts
# used here:
default_fonts = {
    "serif" : ["Tinos"],
    "sans-serif" : ["Arimo"],
    "monospace" : ["Lekton"]
}

for family, font_names in default_fonts.items():
    rcParams["font.%s" % (family)] = font_names

class BoomslangFontManager(FontManager):
    """
    This class is designed to mimic matplotlib's default FontManager, but to
    provide Boomslang-specific fonts in response to all requests
    """
    def __init__(self, size=None, weight='normal'):
        # Since FontManager is an old-style class, we have to initialize it the
        # old-fashioned way
        FontManager.__init__(self, size, weight)

        # This font manager should only consider using Boomslang-blessed fonts
        self.ttflist = map(lambda x: ttfFontProperty(ft2font.FT2Font(x)),
                           _boomslang_fonts)

        self.defaultFamily['ttf'] = "Arimo"

    def findfont(self, prop, fontext='ttf', directory=None,
                 fallback_to_default=True, rebuild_if_missing=True):
        return FontManager.findfont(
            self, prop, fontext=fontext, directory=directory,
            fallback_to_default=fallback_to_default,
            rebuild_if_missing=rebuild_if_missing)

def useBoomslangFonts():
    matplotlib.font_manager.fontManager = BoomslangFontManager()

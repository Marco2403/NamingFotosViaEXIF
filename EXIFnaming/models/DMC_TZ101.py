from collections import OrderedDict
from EXIFnaming.models.ModelBase import ModelBase


class DMC_TZ101(ModelBase):
    TagNames = OrderedDict()

    TagNames['AF'] = ["AF Area Mode", "AF Assist Lamp", "Focus Mode", "Macro Mode", "Metering Mode"]
    TagNames['Mode'] = ["Advanced Scene Mode", "Advanced Scene Type", "Color Effect", "Contrast Mode", "HDR",
                        "Photo Style", "Scene Capture Type", "Scene Mode", "Scene Type", "Self Timer",
                        "Sensitivity Type", "Shooting Mode", "Shutter Type", "Sweep Panorama Direction",
                        "Sweep Panorama Field Of View", "Timer Recording"]
    TagNames['Series'] = ["Bracket Settings", "Burst Mode", "Burst Speed", "Sequence Number"]
    TagNames['Series'] += ["Dependent Image 1 Entry Number", "Dependent Image 2 Entry Number", "Number Of Images"]
    TagNames['Exposure'] = ["Exposure Compensation", "Exposure Mode", "Exposure Program", "Exposure Time"]
    TagNames['Flash'] = ["Flash", "Flash Bias", "Flash Curtain", "Flash Fired"]
    TagNames['Zoom'] = ["Field Of View", "Focal Length In 35mm Format", "F Number", "Hyperfocal Distance"]
    TagNames['Qual'] = ["ISO", "Light Source", "Light Value", "Long Exposure Noise Reduction", "Program ISO",
                        "Gain Control", "White Balance"]
    TagNames['Time'] = ["Date/Time Original", "Sub Sec Time Original"]
    TagNames['Rec'] = ["Audio", "Megapixels", "Video Frame Rate", "Image Quality"]
    TagNames['Rot'] = ["Orientation", "Rotation", "Camera Orientation", "Roll Angle", "Pitch Angle"]

    KreativeShort = OrderedDict()
    KreativeShort['Expressive'] = "EXPS"
    KreativeShort['Retro'] = "RETR"
    KreativeShort['Old Days'] = "OLD"
    KreativeShort['High Key'] = "HKEY"
    KreativeShort['Low Key'] = "LKEY"
    KreativeShort['Sepia'] = "SEPI"
    KreativeShort['Monochrome'] = "MONO"
    KreativeShort['Dynamic Monochrome'] = "D.MONO"
    KreativeShort['Rough Monochrome'] = "R.MONO"
    KreativeShort['Silky Monochrome'] = "S.MONO"
    KreativeShort['Impressive Art'] = "IART"
    KreativeShort['High Dynamic'] = "HDYN"
    KreativeShort['Cross Process'] = "XPRO"
    KreativeShort['Toy Effect'] = "TOY "
    KreativeShort['Toy Pop'] = "TOYP"
    KreativeShort['Bleach Bypass'] = "BLEA"
    KreativeShort['Miniature'] = "MINI"
    KreativeShort['Soft'] = "SOFT"
    KreativeShort['Fantasy'] = "FAN "
    KreativeShort['Star'] = "STAR"
    KreativeShort['Color Select'] = "CLR"
    KreativeShort['Sunshine'] = "SUN"

    SceneShort = OrderedDict()
    SceneShort['Clear Portrait'] = "POR1"
    SceneShort['Silky Skin'] = "POR2"
    SceneShort['Backlit Softness'] = "POR3"
    SceneShort['Clear in Backlight'] = "POR4"
    SceneShort['Relaxing Tone'] = "POR5"
    SceneShort['Sweet Child\'s Face'] = "POR6"
    SceneShort['Distinct Scenery'] = "LAN1"
    SceneShort['Bright Blue Sky'] = "LAN2"
    SceneShort['Romantic Sunset Glow'] = "SUN1"
    SceneShort['Vivid Sunset Glow'] = "SUN2"
    SceneShort['Glistening Water'] = "GLIT1"
    SceneShort['Clear Nightscape'] = "NIGHT1"
    SceneShort['Cool Night Sky'] = "NIGHT2"
    SceneShort['Warm Glowing Nightscape'] = "NIGHT3"
    SceneShort['Artistic Nightscape'] = "NIGHT4"
    SceneShort['Glittering Illuminations'] = "GLIT2"
    SceneShort['Handheld Night Shot'] = "NIGHT5"
    SceneShort['Clear Night Portrait'] = "NIGHT6"
    SceneShort['Soft Image of a Flower'] = "SOFT1"
    SceneShort['Appetizing Food'] = "SOFT2"
    SceneShort['Cute Desert'] = "SOFT3"
    SceneShort['Freeze Animal Motion'] = "FAST1"
    SceneShort['Clear Sports Shot'] = "FAST2"
    SceneShort['Monochrome'] = "SMONO"
    SceneShort['Panorama'] = "PANO"

    unknownTags = OrderedDict()
    unknownTags[("AF Area Mode", "Unknown (0 49)")] = "49-area"
    unknownTags[("AF Area Mode", "Unknown (240 0) ")] = "Tracking"
    unknownTags[("Contrast Mode", "Unknown (0x3)")] = "3"
    unknownTags[("Contrast Mode", "Unknown (0x5)")] = "5"
    unknownTags[("Contrast Mode", "Unknown (0x8)")] = "8"
    unknownTags[("Advanced Scene Mode", "Unknown (54 1)")] = "HS"
    unknownTags[("Advanced Scene Mode", "Unknown (60 7)")] = "4K"
    unknownTags[("Advanced Scene Mode", "Unknown (0 7)")] = "4K"
    unknownTags[("Scene Mode", "Unknown (60)")] = "4K"
    unknownTags[("Scene Mode", "Unknown (54)")] = "HS"


    def __init__(self, Tagdict: OrderedDict, i: int):
        super().__init__(Tagdict, i)

    def is_4KBurst(self):
        return self.check_entry("Image Quality", "4k Movie") and self.check_entry("Video Frame Rate", "29.97")

    def is_4KFilm(self):
        return self.check_entry("Image Quality", "4k Movie")

    def is_HighSpeed(self):
        return self.check_entry("Image Quality", "Full HD Movie") and self.check_entry("Advanced Scene Mode", "HS")

    def is_FullHD(self):
        return self.check_entry("Image Quality", "Full HD Movie") and self.check_entry("Advanced Scene Mode", "Off")

    def is_series(self):
        return self.check_entry("Burst Mode", "On")

    def is_Bracket(self):
        return self.has("Bracket Settings") and not self.check_entry("Bracket Settings", "No Bracket")

    def is_stopmotion(self):
        return self.check_entry("Timer Recording", "Stop-motion Animation")

    def is_timelapse(self):
        return self.check_entry("Timer Recording", "Time Lapse")

    def is_4K(self):
        return self.check_entry("Image Quality", '8.2')

    def is_creative(self):
        return self.check_entry("Scene Mode", "Creative Control") or self.check_entry("Scene Mode", "Digital Filter")

    def is_scene(self):
        return self.has("Scene Mode") and not self.check_entry("Scene Mode", "Off") and self.is_printable_scene()

    def is_HDR(self):
        return self.has("HDR") and not self.check_entry("HDR", "Off")

    def is_sun(self):
        return self.check_entry("Scene Mode", "Sun1") or self.check_entry("Scene Mode", "Sun2")

    def get_scene_abbr_dict(self) -> OrderedDict:
        return DMC_TZ101.SceneShort

    def get_creative_abbr_dict(self) -> OrderedDict:
        return DMC_TZ101.KreativeShort

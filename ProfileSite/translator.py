
import request
from googletrans import Translator
from django.shortcuts import render
def ranslat(request):

    ranslator = Translator()
    translatorProfile = {
        'FullName': (ranslator.translate("Full Name", dest=request.LANGUAGE_CODE).text),
        'Section': (ranslator.translate("Section", dest=request.LANGUAGE_CODE).text),
        'State':   (ranslator.translate("State", dest=request.LANGUAGE_CODE).text),
        'SpecialtyType': ranslator.translate("Specialty Type", dest=request.LANGUAGE_CODE).text,
        'Specialty': ranslator.translate("Specialty", dest=request.LANGUAGE_CODE).text,
        'description': ranslator.translate("Description", dest=request.LANGUAGE_CODE).text,

        'age':ranslator.translate("Full Name", dest=request.LANGUAGE_CODE).text,

        'DateOfBirth': ranslator.translate("Full Name", dest=request.LANGUAGE_CODE).text,
        'gender': ranslator.translate("Full Name", dest=request.LANGUAGE_CODE).text,
        'Phone': ranslator.translate("Full Name", dest=request.LANGUAGE_CODE).text,
        'Profile_Art': ranslator.translate("Full Name", dest=request.LANGUAGE_CODE).text,
        'Profile_Icon': ranslator.translate("Full Name", dest=request.LANGUAGE_CODE).text,

        'address': ranslator.translate("Address", dest=request.LANGUAGE_CODE).text,
        'Stage': ranslator.translate("Full Name", dest=request.LANGUAGE_CODE).text,
        'user': ranslator.translate("Full Name", dest=request.LANGUAGE_CODE).text,
        'slug': ranslator.translate("Full Name", dest=request.LANGUAGE_CODE).text,
        'subcribers': ranslator.translate("Full Name", dest=request.LANGUAGE_CODE).text,
        'follower': ranslator.translate("Full Name", dest=request.LANGUAGE_CODE).text,
        'following': ranslator.translate("Full Name", dest=request.LANGUAGE_CODE).text,
        'emaiAddress': ranslator.translate("Full Name", dest=request.LANGUAGE_CODE).text,
        'date_joined': ranslator.translate("Full Name", dest=request.LANGUAGE_CODE).text,
        'last_login': ranslator.translate("Full Name", dest=request.LANGUAGE_CODE).text,
        'is_active': ranslator.translate("Full Name", dest=request.LANGUAGE_CODE).text,
        'is_subcriber': ranslator.translate("Full Name", dest=request.LANGUAGE_CODE).text,
        'is_supersubcriber': ranslator.translate("Full Name", dest=request.LANGUAGE_CODE).text,
        'is_admin': ranslator.translate("Full Name", dest=request.LANGUAGE_CODE).text,
        'is_staff': ranslator.translate("Full Name", dest=request.LANGUAGE_CODE).text,
        'is_star': ranslator.translate("Full Name", dest=request.LANGUAGE_CODE).text,
        'Facebook': ranslator.translate("Full Name", dest=request.LANGUAGE_CODE).text,
        'Instagram': ranslator.translate("Full Name", dest=request.LANGUAGE_CODE).text,
        'Twitter': ranslator.translate("Full Name", dest=request.LANGUAGE_CODE).text,
        'Snapchat': ranslator.translate("Full Name", dest=request.LANGUAGE_CODE).text,
        'YouTube': ranslator.translate("Full Name", dest=request.LANGUAGE_CODE).text,
        'Skype': ranslator.translate("Full Name", dest=request.LANGUAGE_CODE).text,
        'Zoom': ranslator.translate("Full Name", dest=request.LANGUAGE_CODE).text,



        }
    return translatorProfile








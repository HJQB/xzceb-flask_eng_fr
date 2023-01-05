"""Module for translating text from English to French and vice versa."""

# pylint: disable=invalid-name

import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os

authenticator = IAMAuthenticator('1ECyG_b4BGroIJj9V-n82RJo75XidtQwZ5QJKIEZLjsX')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.eu-de.language-translator.watson.cloud.ibm.com/instances/50d7c653-9ec5-4d60-8c90-2b8aa2b5bd1b')

def englishToFrench(englishText):
    """Translate the given text from English to French.

    Args:
        englishText: The text to translate, in English.

    Returns:
        frenchText: The translated text, in French.
    """
    translation = language_translator.translate(
        text=englishText,
        model_id='en-fr'
    ).get_result()
    frenchText = translation['translations'][0]['translation']
    return frenchText

def frenchToEnglish(frenchText):
    """Translate the given text from French to English.

    Args:
        frenchText: The text to translate, in French.

    Returns:
        englishText: The translated text, in English.
    """
    translation = language_translator.translate(
        text=frenchText,
        model_id='fr-en'
    ).get_result()
    englishText = translation['translations'][0]['translation']
    return englishText

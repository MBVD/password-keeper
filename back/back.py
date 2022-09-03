import eel
import pandas as pd
import pyperclip
import json
from logutils import logger
import config as cfg

@eel.expose
def get_element (name):
    try:
        df = pd.read_csv(cfg.CSV_FILE)
        element_dict = df.loc[df["name"] == name.replace(' ', '')]["key"].to_dict()
        # df.loc[df["name"] == name]["call"] += 1 #фича для рейтинга
        key = list(element_dict.keys())[0]
        element = element_dict[key]
        pyperclip.copy(element)
        logger.info(element)
        return element
    except Exception as e:
        if type(e) is IndexError:
            logger.info(None)
            return None
        logger.info(str(e))
        return None

@eel.expose
def save_element(name, key):
    d_frame = pd.read_csv(cfg.CSV_FILE)   
    if get_element(name):
        return False
    d_frame.loc[len(d_frame), d_frame.columns] = name, key, 0
    d_frame.to_csv(cfg.CSV_FILE,index=False)
    logger.info("Успешно сохранили Сервис: {name}".format(name = name))
    return True

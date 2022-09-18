import eel
import pandas as pd
import pyperclip
import json
from logutils import logger
import config as cfg


@eel.expose
def get_element(name):
    try:
        df = pd.read_csv(cfg.CSV_FILE)
        element_dict = df.loc[df["name"] == name.replace(' ', '')]["key"].to_dict()
        # df.loc[df["name"] == name]["call"] += 1 #фича для рейтинга
        key = list(element_dict.keys())[0]
        element = element_dict[key]
        pyperclip.copy(element)
        logger.info("Пароль " + element + " индекс - " + str(key))
        return element, key
    except Exception as e:
        if type(e) is IndexError:
            logger.info(None)
            return None, None
        logger.info(str(e))
        return None, None


@eel.expose
def save_element(name, key):
    d_frame = pd.read_csv(cfg.CSV_FILE)
    element, key1 = get_element(name)
    if element is None:
        d_frame.loc[len(d_frame), d_frame.columns] = name, key, 0
        d_frame.to_csv(cfg.CSV_FILE, index=False)
        logger.info("Успешно сохранили Сервис: {name}".format(name=name))
        return True
    return False


@eel.expose
def delete_element(name):
    d_frame = pd.read_csv(cfg.CSV_FILE)
    element, key = get_element(name)
    if key is None:
        logger.info("Невозможно удалить элемент {name}".format(name=name))
        return False
    else:
        d_frame = d_frame.drop([key])
        logger.info("Удален Элемент - {service} с паролем - {element}".format(element=element, service=name))
        d_frame.to_csv(cfg.CSV_FILE, index=False)
        return True

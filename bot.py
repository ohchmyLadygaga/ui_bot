"""
@Author     : shiying (github: LYshiying)
@Contact    : Twitter: @shiying_ui | QQ: 839778960
@Version    : 1.0.0
@EditTime   : 2021/10/7 7:48pm(Editor: shiying)
@Desc       : 尝试使用文件头信息判断版本以提醒用户使用git pull进行更新
"""
import os
import sys
from loguru import logger

import nonebot

import config
from src.Services import init_bot


def switch_modules(modules_list):
    for module_name in modules_list:
        nonebot.load_plugin(f"src.plugins.{module_name}")
    return


def log(debug_mode: bool = False):
    logger.remove()
    logger.add(
        sys.stderr,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <lvl>{level}</lvl> | <lvl>{message}</lvl>",
        level="DEBUG" if debug_mode else "INFO",
        colorize=True,
    )
    logger.add(
        "./log/uilog.log",
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <lvl>{level}</lvl> | <lvl>{message}</lvl>",
        rotation="00:00",
        retention="5 days",
        diagnose=False,
        level="DEBUG" if debug_mode else "INFO",
    )


if __name__ == "__main__":

    os.makedirs(config.res, exist_ok=True)

    log(config.DEBUG)
    nonebot.init(config)
    init_bot()

    nonebot.run()

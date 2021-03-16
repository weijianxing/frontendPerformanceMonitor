#-*- coding: utf-8 -*-
# ------ wuage.com testing team ---------
# __author__ : jianxing.wei@wuage.com

import asyncio

loop = asyncio.get_event_loop()


async def helloa():
    print('Hello')
    await asyncio.sleep(3)
    print('World!')


if __name__ == '__main__':
    loop.run(helloa())
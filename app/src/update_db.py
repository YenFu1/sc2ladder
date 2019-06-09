import asyncio

from django.conf import settings

from app.models import Player
from app.src.fetch import get_all_ladder_responses_for_region
from app.src.parse import parse_ladder

NA_REGION = 'us'
EU_REGION = 'eu'
KR_TW_REGION = 'kr'
CN_REGION = 'cn'


def update_all_for_region(region):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    future = asyncio.ensure_future(get_all_ladder_responses_for_region(region))
    ladder_list = loop.run_until_complete(future)
    for ladder in ladder_list:
        ladder = parse_ladder(ladder, region)
        Player.players.bulk_create(ladder, batch_size=settings.DB_BATCH_SIZE, ignore_conflicts=True)
        Player.players.bulk_update(ladder, ['mmr', 'wins', 'losses', 'clan', 'rank', 'modified_at'],
                                   batch_size=settings.DB_BATCH_SIZE)
    loop.close()


def update_all():
    print('updating NA region')
    update_all_for_region(NA_REGION)
    print('updating EU region')
    update_all_for_region(EU_REGION)
    print('updating KR region')
    update_all_for_region(KR_TW_REGION)

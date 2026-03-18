from sqlalchemy import select
from database.models import User 



async def get_user(session, telegram_id: int):
    result = await session.execute(
        select(User).where(User.telegram_id == telegram_id)
    )
    return result.scalar_one_or_none()



async def create_user(session, telegram_id: int):
    user = User(telegram_id=telegram_id)
    session.add(user)
    await session.commit()
    return user 



async def subscribe_user(session, telegram_id: int):
    user = await get_user(session, telegram_id)

    if user:
        user.subscribed = True 
        await session.commit()


async def unsubscribe_user(session, telegram_id: int):
    user = await get_user(session, telegram_id)

    if user:
        user.subscribed = False
        await session.commit()



async def get_subscribed_users(session):
    result = await session.execute(
        select(User).where(User.subscribed == True)
    )
    return result.scalars().all()
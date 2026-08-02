from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import ProcessedEvent


async def is_processed(
    db: AsyncSession,
    event_id: int,
) -> bool:

    result = await db.execute(
        select(ProcessedEvent).where(
            ProcessedEvent.event_id == event_id
        )
    )

    return result.scalar_one_or_none() is not None


async def mark_processed(
    db: AsyncSession,
    event_id: int,
):

    processed = ProcessedEvent(
        event_id=event_id
    )

    db.add(processed)

    await db.commit()
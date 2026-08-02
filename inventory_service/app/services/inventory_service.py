from sqlalchemy.ext.asyncio import AsyncSession
from app.core.logger import logger

from app.repositories.inventory_repository import (
    get_product,
    update_stock,
)

from app.repositories.processed_event_repository import (
    is_processed,
    mark_processed,
)

from app.events.publisher import publish_event


async def process_order(
    db: AsyncSession,
    order: dict,
):
    # Event ID <- Order ID
    event_id = order["id"]


    # Idempotency Check
    if await is_processed(db, event_id):
        logger.info(f"Event {event_id} already processed. Skipping...")
        return

    # Product Check
    product = await get_product(
        db,
        order["product_name"],
    )

    if product is None:

        logger.warning("Product Not Found")

        await publish_event(
            "order.rejected",
            {
                **order,
                "reason": "Product Not Found",
            },
        )

        await mark_processed(
            db,
            event_id,
        )

        return

    # Stock Check
    if product.stock < order["quantity"]:

        logger.warning("Insufficient Stock")

        await publish_event(
            "order.rejected",
            {
                **order,
                "reason": "Insufficient Stock",
            },
        )

        await mark_processed(
            db,
            event_id,
        )

        return

    # Update Stock
    await update_stock(
        db,
        product,
        order["quantity"],
    )

    logger.info(f"Stock Updated -> {product.stock}")

    # Publish Confirmed Event
    await publish_event(
        "order.confirmed",
        {
            **order,
            "status": "CONFIRMED",
        },
    )

    # Mark Event Processed
    await mark_processed(
        db,
        event_id,
    )
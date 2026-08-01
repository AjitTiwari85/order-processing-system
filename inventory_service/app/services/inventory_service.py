from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.inventory_repository import (
    get_product,
    update_stock,
)

from app.events.publisher import publish_event


async def process_order(
    db: AsyncSession,
    order: dict,
):

    product = await get_product(
        db,
        order["product_name"],
    )

    if product is None:

        print("Product Not Found")

        await publish_event(

            "order.rejected",

            {
                **order,
                "reason": "Product Not Found",
            },
        )

        return

    if product.stock < order["quantity"]:

        print("Insufficient Stock")

        await publish_event(

            "order.rejected",

            {
                **order,
                "reason": "Insufficient Stock",
            },
        )

        return

    await update_stock(

        db,

        product,

        order["quantity"],
    )

    print(
        f"Stock Updated -> {product.stock}"
    )

    await publish_event(

        "order.confirmed",

        {
            **order,
            "status": "CONFIRMED",
        },
    )
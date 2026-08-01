from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.inventory_repository import (
    get_product,
    update_stock,
)


async def process_order(
    db: AsyncSession,
    order: dict,
):

    product = await get_product(
        db,
        order["product_name"],
    )

    if product is None:

        print("❌ Product Not Found")

        return False

    if product.stock < order["quantity"]:

        print("❌ Stock Not Available")

        return False

    await update_stock(
        db,
        product,
        order["quantity"],
    )

    print(
        f"✅ Stock Updated : {product.product_name} -> {product.stock}"
    )

    return True
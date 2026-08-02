import asyncio

from app.core.logger import logger


async def send_confirmation_email(message: dict):

    logger.info("Order confirmation email process started.")
    logger.info(f"Order Details: {message}")

    print("=" * 50)
    print("ORDER CONFIRMED")
    print(message)
    print("=" * 50)

    logger.info("Sending confirmation email...")

    await asyncio.sleep(2)

    logger.info("Confirmation email sent successfully.")


async def send_rejection_email(message: dict):

    logger.warning("Order rejected.")
    logger.warning(f"Order Details: {message}")

    print("=" * 50)
    print("ORDER REJECTED")
    print(message)
    print("=" * 50)

    logger.info("Sending rejection email...")

    await asyncio.sleep(2)

    logger.info("Rejection email sent successfully.")
import asyncio


async def send_confirmation_email(message: dict):

    print("\n")
    print("=" * 50)
    print("ORDER CONFIRMED")
    print(message)

    print("Sending Email...")

    await asyncio.sleep(2)

    print("Email Sent Successfully")
    print("=" * 50)


async def send_rejection_email(message: dict):

    print("\n")
    print("=" * 50)
    print("ORDER REJECTED")
    print(message)

    print("Sending Email...")

    await asyncio.sleep(2)

    print("Email Sent Successfully")

    print("=" * 50)
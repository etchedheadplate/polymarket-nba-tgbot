from src.bot.schedule.text import ScheduleRange
from src.config import settings
from src.queue import RabbitMQConnection, RabbitMQProducer


async def get_games_schedule(schedule_range: ScheduleRange):
    connection = RabbitMQConnection()
    producer = RabbitMQProducer(connection)

    await producer.send_message(
        exchange_name=settings.EXCHANGE_NAME,
        routing_key=settings.RK_ORACLE_QUERY,
        message={"schedule_range": schedule_range.value},
    )

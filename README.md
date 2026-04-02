This Telegram bot provides access to [Polymarket NBA Reports](https://github.com/etchedheadplate/polymarket-nba-report) and [Polymarket NBA Oracle](https://github.com/etchedheadplate/polymarket-nba-oracle) database.

## Demo

![demo](media/demo.gif)

## Usage

The system is built around a RabbitMQ-based task processing model. A consumer subscribes to task queues, executes incoming tasks, and publishes results back to response queues.

Start Telegram bot with RabbitMQ consumer:

```bash
python -m main
```

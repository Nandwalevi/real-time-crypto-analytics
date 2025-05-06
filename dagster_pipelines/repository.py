from dagster import repository, ScheduleDefinition
from dagster_pipelines.crypto_pipeline import crypto_ingestion_job

@repository
def crypto_analytics_repo():
    return [
        crypto_ingestion_job,
        ScheduleDefinition(
            job=crypto_ingestion_job,
            cron_schedule="*/5 * * * *",  # Runs every 5 minutes
            name="crypto_ingestion_schedule"
        )
    ]